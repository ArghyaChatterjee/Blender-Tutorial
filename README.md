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

