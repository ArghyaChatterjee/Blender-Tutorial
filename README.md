# All About Blender (Tutorial)
This is a tutorial repository for working with meshes in Blender.

#### 1. How to grab and change an object position?
Answer:
With the object selected, press G to grab and move it. Press `X`, `Y`, or `Z` after pressing `G` to constrain the movement to an axis.

#### 2. How to change an object rotation?
Answer:
With the object selected, go to the preset viewpoint to constrain the rotation to an axis by pressing `X`, `Y`, or `Z` after pressing `R`.

#### 3. How to apply transform/set a translation, rotation, and scale to default (0, 0, 0) of an object in blender?
Answer:
Make the Transform --> Select the object --> ctrl + A --> Apply the Transform operation as needed (Translation/Rotation/Scale)

#### 4. How can an object dimension / 2 points distance be measured in blender?
Answer:
https://docs.blender.org/manual/en/2.83/editors/3dview/toolbar/measure.html

#### 5. How to make the geometric centroid to the bounding box centroid (volumetric)?
Answer:
Object Mode --> Object --> Set Origin --> Origin to Center of Mass (surface)/ Origin to Center of Mass (volume)

#### 6. How to make the Bounding Box Volume as the center of the object volume (0, 0, 0)?
Answer:

https://blender.stackexchange.com/questions/260528/how-do-i-set-the-origin-to-the-center-of-the-bounding-box

Object Mode --> select the object --> Square icon with dot (in the top middle beside magnet icon) --> Transform Pivot Point --> Bounding Box Center

Select the object --> right click --> set origin --> set origin to geometry

If you want to do it more precisely, set the pivot point to Bounding Box Center; move the 3D cursor to the object (Shortcut Shift+S+2) and use the right click menu to set Origin to 3D Cursor.

#### 7. How to generate texture for an object in Blender ?
Answer:
- Using Blender’s Texture Paint Mode:
Blender itself has texture painting capabilities that allow you to directly paint onto your 3D models.

- Steps:
  - In Blender, switch to Texture Paint workspace.
  - Prepare your model with a proper UV map.
  - In the toolshelf, you can select different brushes and colors to paint directly onto your model or its UV layout.
  - You can also use stencils, masks, and layers to create more complex textures.
  - Save the texture from Blender to your computer when finished.

-  Additional Tips:
    - When creating textures, keep in mind how they will be used: consider factors like lighting, scale, and the material properties of the object you're texturing.
    - For game assets or other performance-sensitive applications, be mindful of the texture size and format to balance quality and performance.
    - Experiment with different techniques and tools to find what works best for your specific needs and style.

#### 8. How to add a Texture file in blender mesh ?
Answer:
Adding a texture file, such as a PNG, to a mesh in Blender involves several steps, typically involving UV mapping the mesh and then applying the texture via a material. Here’s a step-by-step guide to help you through the process:

- Prepare Your Mesh
  - Open your Blender project and select the mesh you want to texture.
  - Switch to Edit Mode (`Tab` key).
  - UV unwrap your mesh (if not already done). You can do this by selecting all vertices (`A` key), then pressing `U` and selecting a unwrap method, like "Smart UV Project" or "Unwrap" for more standard objects. Adjust the unwrap parameters as needed.

- Create and Assign a Material
  - Switch back to Object Mode (`Tab` key).
  - Go to the Properties panel, find the Material Properties tab (the little red ball icon).
  - Click on the "New" button to create a new material.
  - Name your material as needed.

- Add Texture to the Material
  - In the same Material Properties tab, scroll down to the Base Color section under the Surface panel.
  - Next to the Base Color label, you'll see a white circle (color field) with a dot on the side. Click on the dot to open the menu, and select “Image Texture” from the options.
  - A new menu will appear allowing you to open an image file. Click "Open" and navigate to your PNG texture file, then select it and click “Open Image” to apply it to the material.

- Map the Texture
  - Make sure the UV map is selected correctly under the Image Texture settings, which should typically default to the correct map if you've just unwrapped your mesh.
  - If necessary, go back to the UV Editing workspace to adjust the placement of your UV map to ensure the texture aligns correctly on your mesh.

- Check and Adjust
  - Go to the Layout workspace to view your model with the applied texture. You might need to switch the viewport shading to "Material Preview" or "Rendered" mode to see the texture. You    can switch between these modes by clicking the sphere icons on the top-right of the 3D Viewport or by pressing `Z` and moving the mouse to the preferred mode.
  - If the texture isn't appearing correctly, make sure the texture coordinates in the shader are set to "UV" and that your UV map properly covers the texture space. You might need to       return to the UV Editing workspace for adjustments. 

Remember you need to generate your texture first in order to add that to the material. Follow step 2 to generate the texture inside blender.

#### 9. How to cut a mesh in blender ?
Answer:
Cutting a mesh in Blender can be done using several techniques, depending on the type of cut you want to make. Here are some common methods:

- Knife Tool:
The Knife tool lets you make freeform cuts across your mesh.

  - Select your mesh by clicking on it in Object Mode, then switch to Edit Mode by pressing `Tab`.
  - Select the Knife Tool from the toolshelf or press `K`. This activates the Knife.
  - Click on your mesh where you want the cut to start, and move your mouse to draw the cut across the mesh. Click again where you want the cut to end.
  - Press `Enter` to confirm the cut.

You can make the cut straight by holding the `Ctrl` key while drawing the line. The Knife tool also supports cutting through the entire mesh by pressing the `Z` key while the tool is active.

- Bisect Tool:
The Bisect tool cuts through a mesh along a straight plane.

  - In Edit Mode, select all vertices of the mesh you want to cut by pressing `A`.
  - Go to the Mesh menu, choose Bisect.
  - Click and drag across your mesh to define the plane of the cut. You can adjust the plane by moving the mouse, and confirm by clicking.
  - In the Operator panel (bottom left), you can adjust the exact position and orientation of the bisecting plane and choose whether to fill the cut and clear inner or outer vertices.

- Boolean Modifier:
The Boolean modifier allows you to use another object to cut your mesh.

  - Create the object you want to use as a cutting tool (it can be any shape).
  - Position this object so that it intersects with the mesh you want to cut.
  - Select your target mesh, go to the Modifiers tab (wrench icon), and add a Boolean modifier.
  - Set the Operation to 'Difference'.
  - For the Object field in the modifier, select the mesh you're using to cut.
  - Apply the modifier to execute the cut. You might need to hide or delete the cutting object afterward.

- Loop Cut:
For adding control loops or making systematic cuts along the surface.

  - In Edit Mode, press `Ctrl + R`. You'll see a purple loop appear on your mesh.
  - Move your mouse to position the loop where you want the cut. Scroll the mouse wheel to increase the number of cuts.
  - Click to set the location of the loop cut, then move the mouse to slide the cut along its potential path, and click again to finalize its position.

Each of these methods has its own best use cases, and the right one to use will depend on the specifics of what you're trying to achieve with your mesh in Blender.

#### 10. How to create a sphere in blender?
Answer:
Creating a sphere in Blender is a straightforward process. Here's how you can do it:

- Start a New Blender Project: Open Blender and start a new project.

- Delete the Default Cube (if present): In the 3D Viewport, you might see a default cube when you start a new project. To delete this, make sure it is selected (it should be highlighted in orange if it is), then press the `Delete` key or `X` key and confirm the deletion.

- Add a Sphere:
    - Press `Shift + A` to open the Add menu in the 3D Viewport. This brings up a list of mesh objects you can add.
    - Navigate to `Mesh > UV Sphere` to add a standard UV sphere. Alternatively, you can choose `Mesh > Ico Sphere` for a sphere made of triangles instead of quads.

- Adjust Sphere Settings (Optional):
    - Immediately after adding the sphere, you can adjust its properties in the bottom left corner of the 3D Viewport. If you don't see the options, click on the small arrow or press `F9` to expand the menu.
    - Here, you can change the number of segments and rings for a UV Sphere, or subdivisions for an Ico Sphere. Increasing these values will increase the sphere's detail and smoothness but also the number of vertices.

- Position the Sphere (If Needed):
    - With the sphere selected, you can move it by pressing `G` (grab), then moving your mouse. You can also constrain the movement to an axis by pressing `X`, `Y`, or `Z` after pressing `G`.
    - Scale the sphere by pressing `S` and moving your mouse. Again, you can constrain scaling to an axis by pressing `X`, `Y`, or `Z` after pressing `S`.
    - Rotate the sphere by pressing `R` and moving your mouse. Constrain rotation to an axis by pressing `X`, `Y`, or `Z` after pressing `R`.

- Edit the Sphere (If Required):
    - To modify the sphere further, switch to Edit Mode by pressing `Tab` or selecting Edit Mode from the mode dropdown menu in the top left corner of the 3D Viewport.
    - In Edit Mode, you can select vertices, edges, or faces to move, scale, extrude, or otherwise modify the shape of your sphere.

- Apply Object Transformations (Optional):
    - If you've significantly moved, rotated, or scaled your sphere, you might want to apply these transformations to reset the object's origin. With the sphere selected, press `Ctrl + A` and choose the transformations you want to apply (Location, Rotation, Scale).

By following these steps, you should now have a sphere in your Blender scene which you can continue to edit, texture, and use within your project as needed.

#### 11. How to create a plane in blender which is in the middle of 2 surfaces ? Basically drawing a plane in the middle of 2 surfaces of that 1 object.
Answer:
Creating a plane exactly in the middle of two surfaces of a single object involves a few steps, especially if those surfaces are not parallel. I'll guide you through a method to achieve this:

- Select the Two Faces
  - In Blender, select your object and enter Edit Mode (`Tab`).
  - Select the two faces between which you want to place a plane. You can select faces by clicking on them while in Face Select mode (`3` on the keyboard if using Blender's default   keymap, or click the face icon in the top corner of the 3D Viewport).

- Create the Midpoint Edges
  - With the two faces selected, right-click to open the context menu and choose `Subdivide`. This will add vertices and edges dividing each face into smaller faces.
  - Select the new edge loop created at the center of each of the original faces (these are the closest edges to the midpoint of your original faces).

- Create the Plane
  - Use `Shift + S` and choose "Cursor to Selected" with the new central edges selected. This will place the 3D cursor exactly in the middle between these two edges.
  - Now, go back to Object Mode (`Tab`), press `Shift + A` and add a new Plane.
  - The plane will be created at the location of the 3D cursor, which is now in the middle between the two faces. However, it might not be oriented correctly according to your surfaces.

- Align the Plane
  - To align the plane, you might need to rotate and resize it manually. In Edit Mode, you can use the `Rotate` (`R`) and `Scale` (`S`) commands to align the plane with the midpoint of the two surfaces.
  - Alternatively, if you want the plane to align precisely with the orientation of one of the original faces, you could:
   - Select one face of your object and enter Edit Mode.
   - Press `Shift + Numpad 7`. This will align the view to the selected face.
   - Go back to Object Mode, select the plane, and in Edit Mode, rotate and scale the plane to fit exactly between the two original faces based on your view.

- Fine-tuning
  - Adjust the plane's position and orientation as needed to ensure it sits exactly in the middle of the two surfaces. You may need to switch between different views and use snapping (`Shift + Tab`) to align things precisely.
  - Remember, if the two faces are not parallel, determining the "middle" can be more conceptual than geometric. You might decide based on the visual midpoint or other criteria relevant to your model.

This method requires some manual adjustments because Blender doesn't have a direct feature for creating a plane exactly between two non-parallel surfaces. The exactness of the placement will depend on the initial position of the 3D cursor and your adjustments to the plane's orientation and size.

#### 12. How to add vertex and edge in blender:
Answer:
https://www.youtube.com/watch?v=YVGWy3qNeOE

#### 13. How to Duplicate a mesh ?
Answer:
Duplicating a mesh in Blender is a straightforward process. Here's how you can do it:

- Duplicating in Object Mode:

  - Select the Mesh: In the 3D Viewport, select the mesh object you wish to duplicate by clicking on it. Ensure you are in Object Mode (you can switch to Object Mode by pressing `Tab` or by selecting it from the mode dropdown in the top left corner of the viewport).

  - Duplicate the Mesh: Press `Shift + D` to duplicate the selected object. Once you press these keys, the duplicate will “stick” to your mouse cursor.

  - Place the Duplicate: Move the mouse to position the duplicate wherever you want. You can also snap it to a specific location or along an axis by moving the mouse and then clicking to confirm the position. If you want to constrain the movement to a specific axis, you can press `X`, `Y`, or `Z` after pressing `Shift + D` and then move the mouse.

  - Confirm the Placement: Left-click to confirm the placement of the duplicate. If you want to cancel the operation after pressing `Shift + D`, press `Esc` or right-click before placing the object.

- Duplicating in Edit Mode (for part of a mesh):

  - Enter Edit Mode: Select the mesh and press `Tab` to switch to Edit Mode.
  - Select Part of the Mesh: In Edit Mode, select the vertices, edges, or faces you want to duplicate. You can select them using Box Select (`B`), Circle Select (`C`), or Lasso Select   (`Ctrl + LMB drag`), among other methods.
  - Duplicate the Selection: Press `Shift + D` after making your selection. The selected parts will be duplicated and will follow your mouse cursor.
  - Place the Duplicate: Move the mouse to position the duplicated geometry. Just like in Object Mode, you can constrain this movement to an axis by pressing `X`, `Y`, or `Z`.
  - Confirm the Placement: Left-click to confirm the placement. If you change your mind, press `Esc` or right-click before placing.

- Additional Tips:

  - After duplicating an object in Object Mode, the duplicate will have the same properties as the original, including materials and modifiers.
  - If you duplicate part of a mesh in Edit Mode, the new geometry remains part of the same object.
  - To create a new separate object from duplicated geometry in Edit Mode, press `P` and choose "Selection" after duplicating. This will make the selected geometry a new separate object.
  - Remember to switch back to Object Mode (`Tab`) if you want to transform or edit the duplicated objects independently.

By following these steps, you can easily duplicate any mesh or part of a mesh in Blender.

#### 14. How to change the background of the 3D viewport in Blender ?
Answer:
Edit --> Preferences --> Themes --> 3D Viewport --> Theme Space --> Gradiant Colors --> Background Type --> Gradiant High (Make it White) --> Save preferences with 3 horizontal lines on the left bottom panel.

#### 15. How to hide 3D cursor, Axes, Floor, Origin point in Blender 3D viewport ?
Answer:
- Find the Overlays: At the top of the 3D viewport, look for the 'Overlays' dropdown menu. This is typically represented by two circles overlapping each other. It's located near the center of the viewport's header, next to the viewport shading options.
- Access the Overlays Menu: Click on the 'Overlays' dropdown to open the overlay options.
- Hide the 3D Cursor: Within the Overlays menu, find the option for the "3D Cursor" and uncheck it. This action will hide the 3D cursor from the viewport.

#### 16. How to show bounding box, individual axis and wire frame mesh and other properties of objects visible in object mode ?
Answer:
On the right pane --> Object (object properties) --> turn on the options as necessary.

#### 17. How to render point cloud in blender ?
Answer:
- Point Cloud Visualizer - Blender [[video]](https://www.youtube.com/watch?v=eXct_7k779Q)
- Render Point Clouds in Blender with Cycles [[video]](https://www.youtube.com/watch?v=kwpj7ZUtnac)
- 3D Point Clouds in Blender: Starter Guide [[video]](https://www.youtube.com/watch?v=DCkFhHNeSc0)
- Download Pointcloud Assets [[sketchfab]](https://sketchfab.com/thevoidescaperoom/collections/point-cloud-b57ab4e8887b45d6b31cc8a5bec3b1f4)





