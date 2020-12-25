#version 330
in vec3 newColor;
in vec2 newTexture;
in vec3 fragNormal;

out vec4 outColor;
uniform sampler2D samplerTexture;

void main()
{
    vec3 ambientLightIntensity = vec3(0.3f, 0.2f, 0.4f);
    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    vec3 sunLightDirection = normalize(vec3(0.0f, 3.0f, 3.0f));
    
    
    vec4 texel = texture(samplerTexture, newTexture);
    if (texel.r < 0.8)
        discard;
    
    vec3 lightIntensity = ambientLightIntensity + sunLightIntensity * max(dot(fragNormal, sunLightDirection), 0.0f);
    
    outColor = vec4(texel.rgb * lightIntensity, texel.a);
}