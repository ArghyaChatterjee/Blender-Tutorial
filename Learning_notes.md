# Blender Learning Notes
1. What does 
2. What does map_Kd normal and map_ao image files mentioned in mtl files in blender ?  
- map_Kd refers to the diffuse texture map of the material. The "Kd" stands for "diffuse reflectivity." This map defines the base color of the material, which is affected by direct light. It's essentially the texture that gives the object its primary color and detail under direct light, making it one of the most commonly used texture maps in 3D modeling.

- normal specifies the normal map of the material. Normal maps are used to simulate fine surface details without actually increasing the complexity (and therefore the number of polygons) of the model. They affect how light bounces off the surface, creating the illusion of depth and detail on textures. This can include bumps, dents, and other surface textures that are too small to be modeled efficiently with geometry.

- map_ao stands for Ambient Occlusion map. Ambient Occlusion (AO) maps simulate how light radiates in real life, especially in creases, holes, and surfaces that are close together. It's a shading method that adds depth to scenes by darkening crevices, holes, and surfaces that are close to each other. The AO map doesn't affect the model's geometry; instead, it makes the lighting appear more natural by emphasizing the natural shadows that would occur in those tight spaces.

Each of these maps contributes to the final appearance of the 3D model by influencing its color, the way it interacts with light, and the apparent complexity of its surface. When used together in a 3D program like Blender, they can create highly realistic textures and surfaces on 3D models.
