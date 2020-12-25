#version 330
in layout(location = 0) vec3 position;
in layout(location = 1) vec3 color;
in layout(location = 2) vec2 textureCoords;
in layout(location = 3) vec3 vertNormal;
in layout(location = 4) vec3 offset;
uniform mat4 transform;
    
uniform mat4 view;
uniform mat4 projection;
uniform mat4 model;
uniform mat4 light;

out vec3 newColor;
out vec2 newTexture;
out vec3 fragNormal;
void main()
{
    vec3 final_pos = vec3(position.x + offset.x, position.y + offset.y, position.z + offset.z);
    gl_Position = projection * view * model * vec4(final_pos, 1.0f);
    newColor = color;
    newTexture = textureCoords;
    fragNormal = (light * vec4(vertNormal, 0.0f)).xyz;
}