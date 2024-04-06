# Blender Learning Notes
## 1. Why is an obj file looks like this ??
```
# Blender 3.6.4
# www.blender.org
mtllib model.mtl
g IHMC_Mug.001_IHMC_Mug.001
v 0.042483 -0.040067 -0.020203
v 0.041987 -0.039238 -0.021304
v 0.043409 -0.039516 -0.017608
v 0.042640 -0.038237 -0.019553
v 0.043221 -0.041066 -0.018310
v 0.043434 -0.038309 -0.017005
v 0.043150 -0.036963 -0.017630
v 0.042871 -0.036951 -0.018445
v 0.041724 -0.037497 -0.021864
v 0.042218 -0.041832 -0.021123
v 0.042747 -0.041106 -0.019586
v 0.043391 -0.035778 -0.016467 
```

This is a OBJ file format, which is a standard 3D image format used by different 3D image editing programs, including Blender. The OBJ format is a plain text file format and represents three-dimensional geometry alone. Here's what each line and value in your snippet represents:

- `# Blender 3.6.4`: This is a comment (anything following a `#` is a comment). It indicates the version of Blender used to export this file.

- `# www.blender.org`: Another comment, usually showing the source of the software used.

- `mtllib model.mtl`: This line refers to an external .mtl file (material library file) associated with this OBJ file. The MTL file contains definitions for materials applied to the model. `model.mtl` is the filename of this associated material definitions file.

- `g IHMC_Mug.001_IHMC_Mug.001`: This defines a group, which in OBJ files is a way to organize the model's geometry. Everything following this line until the next group definition (or the end of the file) is part of this group. "IHMC_Mug.001_IHMC_Mug.001" is the name of the group.

- `v`: Lines beginning with `v` are vertex definitions. Each `v` is followed by three coordinate values representing the X, Y, and Z coordinates of a vertex in the model's space. For example:
   - `v 0.042483 -0.040067 -0.020203` defines a vertex located at X = 0.042483, Y = -0.040067, Z = -0.020203.
   - Each subsequent `v` line defines another vertex in the 3D space of the model.

Vertices (`v`) are the fundamental pieces in the geometry of the model, defining the points in 3D space that are connected to form the model's surfaces. The list of `v` values essentially maps out all the corners and distinctive points of the 3D model in its geometric mesh.

## 2. What does map_Kd normal and map_ao image files mentioned in mtl files in blender ?  
- map_Kd refers to the diffuse texture map of the material. The "Kd" stands for "diffuse reflectivity." This map defines the base color of the material, which is affected by direct light. It's essentially the texture that gives the object its primary color and detail under direct light, making it one of the most commonly used texture maps in 3D modeling.

- normal specifies the normal map of the material. Normal maps are used to simulate fine surface details without actually increasing the complexity (and therefore the number of polygons) of the model. They affect how light bounces off the surface, creating the illusion of depth and detail on textures. This can include bumps, dents, and other surface textures that are too small to be modeled efficiently with geometry.

- map_ao stands for Ambient Occlusion map. Ambient Occlusion (AO) maps simulate how light radiates in real life, especially in creases, holes, and surfaces that are close together. It's a shading method that adds depth to scenes by darkening crevices, holes, and surfaces that are close to each other. The AO map doesn't affect the model's geometry; instead, it makes the lighting appear more natural by emphasizing the natural shadows that would occur in those tight spaces.

Each of these maps contributes to the final appearance of the 3D model by influencing its color, the way it interacts with light, and the apparent complexity of its surface. When used together in a 3D program like Blender, they can create highly realistic textures and surfaces on 3D models.
