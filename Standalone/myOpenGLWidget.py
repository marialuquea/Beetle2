import sys
import math

from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QOpenGLWidget, QSlider,
                             QWidget)

import OpenGL.GL as gl
from OpenGL.GL import *
import shaderLoader
import numpy
from pyrr import matrix44, Vector3, Matrix44
import textureLoader
from generateCuboid import createCuboid
from camera import Camera
from math import sin, cos
import time

class MyOpenGLWidget (QOpenGLWidget):

    def __init__(self, parent=None):
        super(QOpenGLWidget, self).__init__(parent)
        self.lastPos = QPoint()

        self.colourWhite = QColor.fromCmykF(0.0, 0.0, 0.0, 0.0)
        self.colourRed = QColor.fromCmykF(0.0, 0.8, 0.8, 0.0)
        self.trigger = False
        self.x = None
        self.y = None
        self.z = None
        self.X = None
        self.Y = None
        self.Z = None


    def initializeGL(self, x=1, y=1, z=1, X=1, Y=1, Z=1, firstTime=True):
        self.setClearColor(self.colourWhite)
        self.createBuilding(x, y, z, X, Y, Z, firstTime)
        gl.glEnable(gl.GL_DEPTH_TEST)
        if (firstTime):
            self.cam = Camera()
        self.update()
        
    def changeBuilding(self, x, y, z, X, Y, Z):
        self.trigger = True
        self.x = x
        self.y = y
        self.z = z
        self.X = X
        self.Y = Y
        self.Z = Z

    def paintGL(self):
        
        if (self.trigger):
            self.trigger = False
            self.initializeGL(self.x, self.y, self.z, self.X, self.Y, self.Z, False)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        view = self.cam.get_view_matrix()
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, view)
        glDrawElementsInstanced(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None, self.len_of_instance_array)
        glBindTexture(GL_TEXTURE_2D, self.frame)
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, self.model)
        glUniformMatrix4fv(self.light_loc, 1, GL_FALSE, self.model)
        
        

    def resetCamera(self):
        self.cam.resetCamera()

    def mousePressEvent(self, event):
        self.lastPos = event.pos()
        

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.cam.process_mouse_movement(dx, -dy)
            self.update()
        elif event.buttons() & Qt.RightButton:
            self.cam.process_keyboard("FORWARD", -dy * 0.2)
            self.update()
        elif event.buttons() & Qt.MidButton:
            self.cam.process_keyboard("LEFT", -dx * 0.2)
            self.cam.process_keyboard("UP", -dy * 0.2)
            self.update()
            

        self.lastPos = event.pos()
        
    def createBuilding(self, xs, ys, zs, Xs, Ys, Zs, firstTime):
        # xs - primary span
        # ys - secondary span
        # zs - inter-storey height
        # Xs - no. of primary spans
        # Ys - no. of secondary spans
        # Zs - no. of storeys
        # Create the cube object and specify its lengths
        cube = numpy.array(createCuboid(xs, ys, zs), dtype = numpy.float32)
    
        # Specify the indices to make the cube two points will repeat themselves in order to creater one side
        self.indices = [ 0,  1,  2,  2,  3,  0,
                    4,  5,  6,  6,  7,  4,
                    8,  9, 10, 10, 11,  8,
                   12, 13, 14, 14, 15, 12,
                   16, 17, 18, 18, 19, 16,
                   20, 21, 22, 22, 23, 20]
    
        # Converting to specific type because openGL is very specific about what type it takes in
        self.indices = numpy.array(self.indices, dtype= numpy.uint32)
        
        shader = shaderLoader.compileShader("shaders/vert.vs", "shaders/frag.fs")
        
        # Vertex Buffer Objest takes in our cube indices
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, cube.itemsize * len(cube), cube, GL_STATIC_DRAW)
    
        # Element BUffer Array
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.itemsize * len(self.indices), self.indices, GL_STATIC_DRAW)
    
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
        
        for z in numpy.arange(0, ys * Ys, ys):
            for y in numpy.arange(0, zs * Zs, zs):
                for x in numpy.arange(0, xs * Xs, xs):
                    translation = Vector3([0.0, 0.0, 0.0])
                    translation.x = x + offset
                    translation.y = y + offset
                    translation.z = z + offset
                    instance_array.append(translation)
             
        self.len_of_instance_array = len(instance_array)
        instance_array = numpy.array(instance_array, numpy.float32).flatten()
        
        instanceVBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, instanceVBO)
        glBufferData(GL_ARRAY_BUFFER, instance_array.itemsize * len(instance_array), instance_array, GL_STATIC_DRAW)
    
        glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(4)
        glVertexAttribDivisor(4, 1)
        
        if (firstTime):
            self.frame = textureLoader.load_texture("../images/frame.jpg")
        
            glUseProgram(shader)
        
    
            
            self.projection = matrix44.create_perspective_projection_matrix(45.0, 361 / 341, 0.1, 1000.0)
            self.model = matrix44.create_from_translation(Vector3([0.0, 0.0, 0.0]))
        
            self.view_loc = glGetUniformLocation(shader, "view")
            self.proj_loc = glGetUniformLocation(shader, "projection")
            self.model_loc = glGetUniformLocation(shader, "model")
            self.light_loc = glGetUniformLocation(shader, "light")
        
            glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, self.projection)
        



    def setClearColor(self, c):
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    def setColor(self, c):
        gl.glColor4f(c.redF(), c.greenF(), c.blueF(), c.alphaF())