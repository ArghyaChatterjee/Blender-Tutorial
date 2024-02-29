# Blender-Tutorial
This repository is all about learning Blender as part of my PhD.

1. Make the geometric center to the bounding box center: https://blender.stackexchange.com/questions/260528/how-do-i-set-the-origin-to-the-center-of-the-bounding-box
2. Generate texture for an object in Blender:

### Using Blender’s Texture Paint Mode:
Blender itself has texture painting capabilities that allow you to directly paint onto your 3D models.

**Steps:**
- In Blender, switch to Texture Paint workspace.
- Prepare your model with a proper UV map.
- In the toolshelf, you can select different brushes and colors to paint directly onto your model or its UV layout.
- You can also use stencils, masks, and layers to create more complex textures.
- Save the texture from Blender to your computer when finished.

### Additional Tips:
- When creating textures, keep in mind how they will be used: consider factors like lighting, scale, and the material properties of the object you're texturing.
- For game assets or other performance-sensitive applications, be mindful of the texture size and format to balance quality and performance.
- Experiment with different techniques and tools to find what works best for your specific needs and style.

3. Add a Texture file in blender mesh:
Adding a texture file, such as a PNG, to a mesh in Blender involves several steps, typically involving UV mapping the mesh and then applying the texture via a material. Here’s a step-by-step guide to help you through the process:

### Step 1: Prepare Your Mesh
1. Open your Blender project and select the mesh you want to texture.
2. Switch to Edit Mode (`Tab` key).
3. UV unwrap your mesh (if not already done). You can do this by selecting all vertices (`A` key), then pressing `U` and selecting a unwrap method, like "Smart UV Project" or "Unwrap" for more standard objects. Adjust the unwrap parameters as needed.

### Step 2: Create and Assign a Material
1. Switch back to Object Mode (`Tab` key).
2. Go to the Properties panel, find the Material Properties tab (the little red ball icon).
3. Click on the "New" button to create a new material.
4. Name your material as needed.

### Step 3: Add Texture to the Material
1. In the same Material Properties tab, scroll down to the Base Color section under the Surface panel.
2. Next to the Base Color label, you'll see a white circle (color field) with a dot on the side. Click on the dot to open the menu, and select “Image Texture” from the options.
3. A new menu will appear allowing you to open an image file. Click "Open" and navigate to your PNG texture file, then select it and click “Open Image” to apply it to the material.

### Step 4: Map the Texture
1. Make sure the UV map is selected correctly under the Image Texture settings, which should typically default to the correct map if you've just unwrapped your mesh.
2. If necessary, go back to the UV Editing workspace to adjust the placement of your UV map to ensure the texture aligns correctly on your mesh.

### Step 5: Check and Adjust
1. Go to the Layout workspace to view your model with the applied texture. You might need to switch the viewport shading to "Material Preview" or "Rendered" mode to see the texture. You can switch between these modes by clicking the sphere icons on the top-right of the 3D Viewport or by pressing `Z` and moving the mouse to the preferred mode.
2. If the texture isn't appearing correctly, make sure the texture coordinates in the shader are set to "UV" and that your UV map properly covers the texture space. You might need to return to the UV Editing workspace for adjustments. 

Remember you need to generate your texture first in order to add that to the material. Follow step 2 to generate the texture inside blender.

4. How to cut a mesh in blender:

Cutting a mesh in Blender can be done using several techniques, depending on the type of cut you want to make. Here are some common methods:

### Knife Tool:
The Knife tool lets you make freeform cuts across your mesh.

1. Select your mesh by clicking on it in Object Mode, then switch to Edit Mode by pressing `Tab`.
2. Select the Knife Tool from the toolshelf or press `K`. This activates the Knife.
3. Click on your mesh where you want the cut to start, and move your mouse to draw the cut across the mesh. Click again where you want the cut to end.
4. Press `Enter` to confirm the cut.

You can make the cut straight by holding the `Ctrl` key while drawing the line. The Knife tool also supports cutting through the entire mesh by pressing the `Z` key while the tool is active.

### Bisect Tool:
The Bisect tool cuts through a mesh along a straight plane.

1. In Edit Mode, select all vertices of the mesh you want to cut by pressing `A`.
2. Go to the Mesh menu, choose Bisect.
3. Click and drag across your mesh to define the plane of the cut. You can adjust the plane by moving the mouse, and confirm by clicking.
4. In the Operator panel (bottom left), you can adjust the exact position and orientation of the bisecting plane and choose whether to fill the cut and clear inner or outer vertices.

### Boolean Modifier:
The Boolean modifier allows you to use another object to cut your mesh.

1. Create the object you want to use as a cutting tool (it can be any shape).
2. Position this object so that it intersects with the mesh you want to cut.
3. Select your target mesh, go to the Modifiers tab (wrench icon), and add a Boolean modifier.
4. Set the Operation to 'Difference'.
5. For the Object field in the modifier, select the mesh you're using to cut.
6. Apply the modifier to execute the cut. You might need to hide or delete the cutting object afterward.

### Loop Cut:
For adding control loops or making systematic cuts along the surface.

1. In Edit Mode, press `Ctrl + R`. You'll see a purple loop appear on your mesh.
2. Move your mouse to position the loop where you want the cut. Scroll the mouse wheel to increase the number of cuts.
3. Click to set the location of the loop cut, then move the mouse to slide the cut along its potential path, and click again to finalize its position.

Each of these methods has its own best use cases, and the right one to use will depend on the specifics of what you're trying to achieve with your mesh in Blender.

5. How to create a sphere in blender?
Creating a sphere in Blender is a straightforward process. Here's how you can do it:

**Start a New Blender Project**: Open Blender and start a new project.

**Delete the Default Cube** (if present): In the 3D Viewport, you might see a default cube when you start a new project. To delete this, make sure it is selected (it should be highlighted in orange if it is), then press the `Delete` key or `X` key and confirm the deletion.

**Add a Sphere**:
    - Press `Shift + A` to open the Add menu in the 3D Viewport. This brings up a list of mesh objects you can add.
    - Navigate to `Mesh > UV Sphere` to add a standard UV sphere. Alternatively, you can choose `Mesh > Ico Sphere` for a sphere made of triangles instead of quads.

**Adjust Sphere Settings** (Optional):
    - Immediately after adding the sphere, you can adjust its properties in the bottom left corner of the 3D Viewport. If you don't see the options, click on the small arrow or press `F9` to expand the menu.
    - Here, you can change the number of segments and rings for a UV Sphere, or subdivisions for an Ico Sphere. Increasing these values will increase the sphere's detail and smoothness but also the number of vertices.

**Position the Sphere** (If Needed):
    - With the sphere selected, you can move it by pressing `G` (grab), then moving your mouse. You can also constrain the movement to an axis by pressing `X`, `Y`, or `Z` after pressing `G`.
    - Scale the sphere by pressing `S` and moving your mouse. Again, you can constrain scaling to an axis by pressing `X`, `Y`, or `Z` after pressing `S`.
    - Rotate the sphere by pressing `R` and moving your mouse. Constrain rotation to an axis by pressing `X`, `Y`, or `Z` after pressing `R`.

**Edit the Sphere** (If Required):
    - To modify the sphere further, switch to Edit Mode by pressing `Tab` or selecting Edit Mode from the mode dropdown menu in the top left corner of the 3D Viewport.
    - In Edit Mode, you can select vertices, edges, or faces to move, scale, extrude, or otherwise modify the shape of your sphere.

**Apply Object Transformations** (Optional):
    - If you've significantly moved, rotated, or scaled your sphere, you might want to apply these transformations to reset the object's origin. With the sphere selected, press `Ctrl + A` and choose the transformations you want to apply (Location, Rotation, Scale).

By following these steps, you should now have a sphere in your Blender scene which you can continue to edit, texture, and use within your project as needed.
