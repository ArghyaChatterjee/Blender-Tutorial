import bpy
import bmesh
import math
import mathutils
from mathutils import Vector
from mathutils.kdtree import KDTree


# -----------------------------
# User settings
# -----------------------------
TOLERANCE = 0.002   # meters if your mesh is in meters. Increase if mesh is noisy.
SAMPLE_LIMIT = 5000 # reduce for faster testing
FULL_ROTATION_STEPS = 24  # tests every 15 degrees


def get_mesh_vertices_local(obj):
    """Return mesh vertices in the object's local coordinate frame."""
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval = obj.evaluated_get(depsgraph)
    mesh = obj_eval.to_mesh()

    verts = [v.co.copy() for v in mesh.vertices]

    obj_eval.to_mesh_clear()

    if len(verts) > SAMPLE_LIMIT:
        step = max(1, len(verts) // SAMPLE_LIMIT)
        verts = verts[::step]

    return verts


def build_kdtree(points):
    tree = KDTree(len(points))
    for i, p in enumerate(points):
        tree.insert(p, i)
    tree.balance()
    return tree


def max_nearest_distance(rotated_points, tree):
    max_dist = 0.0
    mean_dist = 0.0

    for p in rotated_points:
        _, _, dist = tree.find(p)
        max_dist = max(max_dist, dist)
        mean_dist += dist

    mean_dist /= len(rotated_points)
    return max_dist, mean_dist


def rotate_points(points, axis, angle_rad):
    if axis == "x":
        rot = mathutils.Matrix.Rotation(angle_rad, 4, "X")
    elif axis == "y":
        rot = mathutils.Matrix.Rotation(angle_rad, 4, "Y")
    elif axis == "z":
        rot = mathutils.Matrix.Rotation(angle_rad, 4, "Z")
    else:
        raise ValueError("axis must be x, y, or z")

    return [rot @ p for p in points]


def test_rotation_symmetry(points, tree, axis, angle_rad, tolerance):
    rotated = rotate_points(points, axis, angle_rad)
    max_dist, mean_dist = max_nearest_distance(rotated, tree)

    return max_dist < tolerance, max_dist, mean_dist


def detect_symmetry(obj):
    points = get_mesh_vertices_local(obj)

    # Center mesh around local origin for symmetry testing.
    # This is important if the mesh origin is slightly offset.
    centroid = sum(points, Vector()) / len(points)
    points = [p - centroid for p in points]

    tree = build_kdtree(points)

    results = {}

    for axis in ["x", "y", "z"]:
        # Test 180 degree symmetry
        is_180, max_180, mean_180 = test_rotation_symmetry(
            points, tree, axis, math.radians(180), TOLERANCE
        )

        # Test full rotational symmetry
        full_ok = True
        worst_full = 0.0
        mean_full_total = 0.0

        for i in range(1, FULL_ROTATION_STEPS):
            angle = 2.0 * math.pi * i / FULL_ROTATION_STEPS
            ok, max_dist, mean_dist = test_rotation_symmetry(
                points, tree, axis, angle, TOLERANCE
            )

            worst_full = max(worst_full, max_dist)
            mean_full_total += mean_dist

            if not ok:
                full_ok = False

        mean_full = mean_full_total / (FULL_ROTATION_STEPS - 1)

        results[axis] = {
            "180": is_180,
            "180_max_error": max_180,
            "180_mean_error": mean_180,
            "full": full_ok,
            "full_max_error": worst_full,
            "full_mean_error": mean_full,
        }

    return results


# -----------------------------
# Main
# -----------------------------
obj = bpy.context.object

if obj is None or obj.type != "MESH":
    raise RuntimeError("Please select one mesh object.")

results = detect_symmetry(obj)

print("\n==============================")
print(f"Symmetry result for: {obj.name}")
print("==============================")

foundationpose_axes = []

for axis, r in results.items():
    print(f"\nAxis: {axis.upper()}")
    print(f"  180 symmetry: {r['180']} | max error: {r['180_max_error']:.6f}, mean error: {r['180_mean_error']:.6f}")
    print(f"  full symmetry: {r['full']} | max error: {r['full_max_error']:.6f}, mean error: {r['full_mean_error']:.6f}")

    if r["full"]:
        foundationpose_axes.append(f"{axis}_full")
    elif r["180"]:
        foundationpose_axes.append(f"{axis}_180")

print("\nFoundationPose suggestion:")
if foundationpose_axes:
    print(f'"symmetry_axes": {foundationpose_axes}')
else:
    print("# No clear rotational symmetry detected")
