from OpenGL.GL import *
import OpenGL.GL.shaders


def loadShader(shader_file):
    shader_source = ""
    with open(shader_file) as f:
        shader_source = f.read()
    f.close()
    return str.encode(shader_source)

def compileShader(vs, fs):
    vert_shader = loadShader(vs)
    frag_shader = loadShader(fs)
    
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vert_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER))
    return shader
     