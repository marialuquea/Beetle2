import glfw
from OpenGL.GL import *
import shaderLoader
import numpy
from pyrr import matrix44, Vector3, Matrix44
import textureLoader
from generateCuboid import createCuboid
from camera import Camera
from math import sin, cos

def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    
keys = [False] * 1024
# Camera related stuff
cam = Camera()
lastX, lastY = 600, 600
first_mouse = True

def key_callback(window, key, scancode, action, mode):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)
        
    if key >= 0 and key < 1024:
        if action == glfw.PRESS:
            keys[key] = True
        elif action == glfw.RELEASE:
            keys[key] = False
            
def do_movement():
    if keys[glfw.KEY_W]:
        cam.process_keyboard("FORWARD", 0.05)
    if keys[glfw.KEY_S]:
        cam.process_keyboard("BACKWARD", 0.05)
    if keys[glfw.KEY_A]:
        cam.process_keyboard("LEFT", 0.05)
    if keys[glfw.KEY_D]:
        cam.process_keyboard("RIGHT", 0.05)
    if keys[glfw.KEY_E]:
        cam.process_keyboard("UP", 0.05)
    if keys[glfw.KEY_Q]:
        cam.process_keyboard("DOWN", 0.05)


def mouse_callback(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)

def main():
    
    # Initialization of GLFW
    if not glfw.init():
        return
    
    # Specify window size and create the window
    w_width, w_height = 1200, 1200
    window = glfw.create_window(w_width, w_height, "Building Visualiztion", None, None)
    
    # If you couldn't create the window return
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glfw.set_window_size_callback(window, window_resize)
    glfw.set_key_callback(window, key_callback)
    glfw.set_cursor_pos_callback(window, mouse_callback)
    # Disable the mouse
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    # Create the cube object and specify its lengths
    cube = numpy.array(createCuboid(1, 1, 1), dtype = numpy.float32)

    # Specify the indices to make the cube two points will repeat themselves in order to creater one side
    indices = [ 0,  1,  2,  2,  3,  0,
                4,  5,  6,  6,  7,  4,
                8,  9, 10, 10, 11,  8,
               12, 13, 14, 14, 15, 12,
               16, 17, 18, 18, 19, 16,
               20, 21, 22, 22, 23, 20]

    # Converting to specific type because openGL is very specific about what type it takes in
    indices = numpy.array(indices, dtype= numpy.uint32)
    
    shader = shaderLoader.compileShader("shaders/vert.vs", "shaders/frag.fs")
    
    # Vertex Buffer Objest takes in our cube indices
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, cube.itemsize * len(cube), cube, GL_STATIC_DRAW)

    # Element BUffer Array
    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.itemsize * len(indices), indices, GL_STATIC_DRAW)

    #position
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    #color
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(12))
    glEnableVertexAttribArray(1)
    #texture
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(24))
    glEnableVertexAttribArray(2)
    #normal
    glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(32))
    glEnableVertexAttribArray(3)
    #instances
    instance_array = []
    offset = 0
    
    for z in numpy.arange(0, 6, 1):
        for y in numpy.arange(0, 8, 1):
            for x in numpy.arange(0, 20, 2):
                translation = Vector3([0.0, 0.0, 0.0])
                translation.x = x + offset
                translation.y = y + offset
                translation.z = z + offset
                instance_array.append(translation)
         
    len_of_instance_array = len(instance_array)
    instance_array = numpy.array(instance_array, numpy.float32).flatten()
    
    instanceVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO)
    glBufferData(GL_ARRAY_BUFFER, instance_array.itemsize * len(instance_array), instance_array, GL_STATIC_DRAW)

    glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    glEnableVertexAttribArray(4)
    glVertexAttribDivisor(4, 1)

    lydia = textureLoader.load_texture("../images/lydia.jpg")
    bernardino = textureLoader.load_texture("../images/bernardino.jpg")
    emma = textureLoader.load_texture("../images/emma.jpg")
    francesco = textureLoader.load_texture("../images/francesco.jpg")
    frame = textureLoader.load_texture("../images/frame.jpg")

    glUseProgram(shader)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


    projection = matrix44.create_perspective_projection_matrix(45.0, w_width / w_height, 0.1, 1000.0)
    model = matrix44.create_from_translation(Vector3([0.0, 0.0, 0.0]))

    view_loc = glGetUniformLocation(shader, "view")
    proj_loc = glGetUniformLocation(shader, "projection")
    model_loc = glGetUniformLocation(shader, "model")
    light_loc = glGetUniformLocation(shader, "light")
    
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    
    triggerOnce = True
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        do_movement()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        
        view = cam.get_view_matrix()
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
            
        glDrawElementsInstanced(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None, len_of_instance_array)
        glBindTexture(GL_TEXTURE_2D, frame)
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glUniformMatrix4fv(light_loc, 1, GL_FALSE, model)

        glfw.swap_buffers(window)
        if (glfw.get_time() > 10.0 and triggerOnce):
            print("Triggered")
            triggerOnce = False
            # Create the cube object and specify its lengths
            cube = numpy.array(createCuboid(4, 1, 1), dtype = numpy.float32)
        
            # Specify the indices to make the cube two points will repeat themselves in order to creater one side
            indices = [ 0,  1,  2,  2,  3,  0,
                        4,  5,  6,  6,  7,  4,
                        8,  9, 10, 10, 11,  8,
                       12, 13, 14, 14, 15, 12,
                       16, 17, 18, 18, 19, 16,
                       20, 21, 22, 22, 23, 20]
        
            # Converting to specific type because openGL is very specific about what type it takes in
            indices = numpy.array(indices, dtype= numpy.uint32)
            
            shader = shaderLoader.compileShader("shaders/vert.vs", "shaders/frag.fs")
            
            # Vertex Buffer Objest takes in our cube indices
            VBO = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, VBO)
            glBufferData(GL_ARRAY_BUFFER, cube.itemsize * len(cube), cube, GL_STATIC_DRAW)
        
            # Element BUffer Array
            EBO = glGenBuffers(1)
            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.itemsize * len(indices), indices, GL_STATIC_DRAW)
        
            #position
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(0))
            glEnableVertexAttribArray(0)
            #color
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(12))
            glEnableVertexAttribArray(1)
            #texture
            glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(24))
            glEnableVertexAttribArray(2)
            #normal
            glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 11, ctypes.c_void_p(32))
            glEnableVertexAttribArray(3)
            #instances
            instance_array = []
            offset = 0
            
            for z in numpy.arange(0, 6, 1):
                for y in numpy.arange(0, 8, 1):
                    for x in numpy.arange(0, 20, 2):
                        translation = Vector3([0.0, 0.0, 0.0])
                        translation.x = x + offset
                        translation.y = y + offset
                        translation.z = z + offset
                        instance_array.append(translation)
                 
            len_of_instance_array = len(instance_array)
            instance_array = numpy.array(instance_array, numpy.float32).flatten()
            
            instanceVBO = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, instanceVBO)
            glBufferData(GL_ARRAY_BUFFER, instance_array.itemsize * len(instance_array), instance_array, GL_STATIC_DRAW)
        
            glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
            glEnableVertexAttribArray(4)
            glVertexAttribDivisor(4, 1)
        
            lydia = textureLoader.load_texture("../images/lydia.jpg")
            bernardino = textureLoader.load_texture("../images/bernardino.jpg")
            emma = textureLoader.load_texture("../images/emma.jpg")
            francesco = textureLoader.load_texture("../images/francesco.jpg")
            frame = textureLoader.load_texture("../images/frame.jpg")
        
            glUseProgram(shader)
        
            glClearColor(1.0, 1.0, 1.0, 1.0)
            glEnable(GL_DEPTH_TEST)
            # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        
        
            projection = matrix44.create_perspective_projection_matrix(45.0, w_width / w_height, 0.1, 1000.0)
            model = matrix44.create_from_translation(Vector3([0.0, 0.0, 0.0]))
        
            view_loc = glGetUniformLocation(shader, "view")
            proj_loc = glGetUniformLocation(shader, "projection")
            model_loc = glGetUniformLocation(shader, "model")
            light_loc = glGetUniformLocation(shader, "light")
            
            glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
        

    glfw.terminate()

if __name__ == "__main__":
    main()