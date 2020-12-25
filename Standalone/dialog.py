# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math
from mc_simulation import MCSimulation as mc
from myOpenGLWidget import MyOpenGLWidget
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from numpy import array
import scipy.stats as st

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 866)
        MainWindow.setMinimumSize(QtCore.QSize(983, 866))
        MainWindow.setMaximumSize(QtCore.QSize(983, 866))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_variableFloorLoad = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_variableFloorLoad.setFont(font)
        self.label_variableFloorLoad.setObjectName("label_variableFloorLoad")
        self.gridLayout.addWidget(self.label_variableFloorLoad, 21, 0, 1, 1)
        self.label_material = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_material.setFont(font)
        self.label_material.setObjectName("label_material")
        self.gridLayout.addWidget(self.label_material, 1, 0, 1, 2)
        self.label_mode = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_mode.setFont(font)
        self.label_mode.setObjectName("label_mode")
        self.gridLayout.addWidget(self.label_mode, 31, 3, 1, 1)
        self.horizontalSlider_mode = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_mode.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_mode.setObjectName("horizontalSlider_mode")
        self.gridLayout.addWidget(self.horizontalSlider_mode, 32, 3, 1, 1)
        self.horizontalSlider_upperBound = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_upperBound.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_upperBound.setObjectName("horizontalSlider_upperBound")
        self.gridLayout.addWidget(self.horizontalSlider_upperBound, 32, 2, 1, 1)
        self.label_UpperBound_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_UpperBound_value.setFont(font)
        self.label_UpperBound_value.setObjectName("label_UpperBound_value")
        self.gridLayout.addWidget(self.label_UpperBound_value, 34, 2, 1, 1)
        self.label_mode_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_mode_2.setFont(font)
        self.label_mode_2.setObjectName("label_mode_2")
        self.gridLayout.addWidget(self.label_mode_2, 34, 3, 1, 1)
        self.label_geometry = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_geometry.setFont(font)
        self.label_geometry.setObjectName("label_geometry")
        self.gridLayout.addWidget(self.label_geometry, 3, 0, 1, 2)
        self.comboBox_material = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_material.setFont(font)
        self.comboBox_material.setObjectName("comboBox_material")
        self.gridLayout.addWidget(self.comboBox_material, 1, 2, 1, 1)
        self.label_secondarySpan_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_secondarySpan_value.setFont(font)
        self.label_secondarySpan_value.setObjectName("label_secondarySpan_value")
        self.gridLayout.addWidget(self.label_secondarySpan_value, 8, 2, 1, 1)
        self.horizontalSlider_secondarySpan = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_secondarySpan.setMinimum(500)
        self.horizontalSlider_secondarySpan.setMaximum(1200)
        self.horizontalSlider_secondarySpan.setSingleStep(10)
        self.horizontalSlider_secondarySpan.setPageStep(100)
        self.horizontalSlider_secondarySpan.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_secondarySpan.setObjectName("horizontalSlider_secondarySpan")
        self.gridLayout.addWidget(self.horizontalSlider_secondarySpan, 7, 2, 1, 1)
        self.label_NoStoreys = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NoStoreys.setFont(font)
        self.label_NoStoreys.setObjectName("label_NoStoreys")
        self.gridLayout.addWidget(self.label_NoStoreys, 12, 3, 1, 1)
        self.label_noSecondarySpan_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_noSecondarySpan_value.setFont(font)
        self.label_noSecondarySpan_value.setObjectName("label_noSecondarySpan_value")
        self.gridLayout.addWidget(self.label_noSecondarySpan_value, 15, 2, 1, 1)
        self.horizontalSlider_NoSecondarySpans = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_NoSecondarySpans.setMinimum(100)
        self.horizontalSlider_NoSecondarySpans.setMaximum(1300)
        self.horizontalSlider_NoSecondarySpans.setSingleStep(100)
        self.horizontalSlider_NoSecondarySpans.setPageStep(100)
        self.horizontalSlider_NoSecondarySpans.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_NoSecondarySpans.setObjectName("horizontalSlider_NoSecondarySpans")
        self.gridLayout.addWidget(self.horizontalSlider_NoSecondarySpans, 14, 2, 1, 1)
        self.label_interstoreyHeight = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_interstoreyHeight.setFont(font)
        self.label_interstoreyHeight.setObjectName("label_interstoreyHeight")
        self.gridLayout.addWidget(self.label_interstoreyHeight, 5, 3, 1, 1)
        self.label_secondarySpan = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_secondarySpan.setFont(font)
        self.label_secondarySpan.setObjectName("label_secondarySpan")
        self.gridLayout.addWidget(self.label_secondarySpan, 5, 2, 1, 1)
        self.horizontalSlider_interstoreyHeight = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_interstoreyHeight.setMinimum(350)
        self.horizontalSlider_interstoreyHeight.setMaximum(400)
        self.horizontalSlider_interstoreyHeight.setSingleStep(10)
        self.horizontalSlider_interstoreyHeight.setPageStep(100)
        self.horizontalSlider_interstoreyHeight.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_interstoreyHeight.setObjectName("horizontalSlider_interstoreyHeight")
        self.gridLayout.addWidget(self.horizontalSlider_interstoreyHeight, 7, 3, 1, 1)
        self.label_interstoreyHeight_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_interstoreyHeight_value.setFont(font)
        self.label_interstoreyHeight_value.setObjectName("label_interstoreyHeight_value")
        self.gridLayout.addWidget(self.label_interstoreyHeight_value, 8, 3, 1, 1)
        self.horizontalSlider_noStoreys = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_noStoreys.setMinimum(100)
        self.horizontalSlider_noStoreys.setMaximum(1000)
        self.horizontalSlider_noStoreys.setSingleStep(100)
        self.horizontalSlider_noStoreys.setPageStep(100)
        self.horizontalSlider_noStoreys.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_noStoreys.setObjectName("horizontalSlider_noStoreys")
        self.gridLayout.addWidget(self.horizontalSlider_noStoreys, 14, 3, 1, 1)
        self.label_NoStoreys_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NoStoreys_value.setFont(font)
        self.label_NoStoreys_value.setObjectName("label_NoStoreys_value")
        self.gridLayout.addWidget(self.label_NoStoreys_value, 15, 3, 1, 1)
        self.label_noPrimarySpan = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_noPrimarySpan.setFont(font)
        self.label_noPrimarySpan.setObjectName("label_noPrimarySpan")
        self.gridLayout.addWidget(self.label_noPrimarySpan, 12, 0, 1, 2)
        self.label_noSecondarySpan = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_noSecondarySpan.setFont(font)
        self.label_noSecondarySpan.setObjectName("label_noSecondarySpan")
        self.gridLayout.addWidget(self.label_noSecondarySpan, 12, 2, 1, 1)
        self.label_loads = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_loads.setFont(font)
        self.label_loads.setObjectName("label_loads")
        self.gridLayout.addWidget(self.label_loads, 20, 0, 1, 1)
        self.horizontalSlider_variableFloorLoad = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_variableFloorLoad.setMinimum(100)
        self.horizontalSlider_variableFloorLoad.setMaximum(500)
        self.horizontalSlider_variableFloorLoad.setSingleStep(10)
        self.horizontalSlider_variableFloorLoad.setPageStep(100)
        self.horizontalSlider_variableFloorLoad.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_variableFloorLoad.setObjectName("horizontalSlider_variableFloorLoad")
        self.gridLayout.addWidget(self.horizontalSlider_variableFloorLoad, 23, 0, 1, 1)
        self.label_primarySpan_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_primarySpan_value.setFont(font)
        self.label_primarySpan_value.setObjectName("label_primarySpan_value")
        self.gridLayout.addWidget(self.label_primarySpan_value, 8, 0, 1, 1)
        self.horizontalSlider_finishesCeiling = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_finishesCeiling.setMaximum(175)
        self.horizontalSlider_finishesCeiling.setSingleStep(25)
        self.horizontalSlider_finishesCeiling.setPageStep(100)
        self.horizontalSlider_finishesCeiling.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_finishesCeiling.setObjectName("horizontalSlider_finishesCeiling")
        self.gridLayout.addWidget(self.horizontalSlider_finishesCeiling, 23, 2, 1, 1)
        self.label_lowerBound = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lowerBound.setFont(font)
        self.label_lowerBound.setObjectName("label_lowerBound")
        self.gridLayout.addWidget(self.label_lowerBound, 31, 0, 1, 1)
        self.label_UpperBound = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_UpperBound.setFont(font)
        self.label_UpperBound.setObjectName("label_UpperBound")
        self.gridLayout.addWidget(self.label_UpperBound, 31, 2, 1, 1)
        self.label_envelopeWallsLoad_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_envelopeWallsLoad_2.setFont(font)
        self.label_envelopeWallsLoad_2.setObjectName("label_envelopeWallsLoad_2")
        self.gridLayout.addWidget(self.label_envelopeWallsLoad_2, 25, 3, 1, 1)
        self.horizontalSlider_lowerBound = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_lowerBound.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_lowerBound.setObjectName("horizontalSlider_lowerBound")
        self.gridLayout.addWidget(self.horizontalSlider_lowerBound, 32, 0, 2, 2)
        self.label_variableFloorLoad_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_variableFloorLoad_value.setFont(font)
        self.label_variableFloorLoad_value.setObjectName("label_variableFloorLoad_value")
        self.gridLayout.addWidget(self.label_variableFloorLoad_value, 25, 2, 1, 1)
        self.horizontalSlider_envelopeWallsLoad = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_envelopeWallsLoad.setMinimum(100)
        self.horizontalSlider_envelopeWallsLoad.setMaximum(500)
        self.horizontalSlider_envelopeWallsLoad.setSingleStep(10)
        self.horizontalSlider_envelopeWallsLoad.setPageStep(100)
        self.horizontalSlider_envelopeWallsLoad.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_envelopeWallsLoad.setObjectName("horizontalSlider_envelopeWallsLoad")
        self.gridLayout.addWidget(self.horizontalSlider_envelopeWallsLoad, 23, 3, 1, 1)
        self.label_finishesCeiling_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_finishesCeiling_value.setFont(font)
        self.label_finishesCeiling_value.setObjectName("label_finishesCeiling_value")
        self.gridLayout.addWidget(self.label_finishesCeiling_value, 25, 0, 1, 1)
        self.label_beetle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_beetle.setFont(font)
        self.label_beetle.setObjectName("label_beetle")
        self.gridLayout.addWidget(self.label_beetle, 0, 0, 1, 3)
        self.label_primarySpan = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_primarySpan.setFont(font)
        self.label_primarySpan.setObjectName("label_primarySpan")
        self.gridLayout.addWidget(self.label_primarySpan, 5, 0, 1, 1)
        self.horizontalSlider_primarySpan = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_primarySpan.setMinimum(500)
        self.horizontalSlider_primarySpan.setMaximum(900)
        self.horizontalSlider_primarySpan.setSingleStep(9)
        self.horizontalSlider_primarySpan.setPageStep(100)
        self.horizontalSlider_primarySpan.setSliderPosition(500)
        self.horizontalSlider_primarySpan.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_primarySpan.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_primarySpan.setTickInterval(10)
        self.horizontalSlider_primarySpan.setObjectName("horizontalSlider_primarySpan")
        self.gridLayout.addWidget(self.horizontalSlider_primarySpan, 7, 0, 1, 1)
        self.horizontalSlider_noPrimarySpan = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_noPrimarySpan.setMinimum(200)
        self.horizontalSlider_noPrimarySpan.setMaximum(2100)
        self.horizontalSlider_noPrimarySpan.setSingleStep(100)
        self.horizontalSlider_noPrimarySpan.setPageStep(100)
        self.horizontalSlider_noPrimarySpan.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_noPrimarySpan.setObjectName("horizontalSlider_noPrimarySpan")
        self.gridLayout.addWidget(self.horizontalSlider_noPrimarySpan, 14, 0, 1, 1)
        self.label_lowerBound_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lowerBound_value.setFont(font)
        self.label_lowerBound_value.setObjectName("label_lowerBound_value")
        self.gridLayout.addWidget(self.label_lowerBound_value, 34, 0, 1, 1)
        self.label_noPrimarySpan_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_noPrimarySpan_value.setFont(font)
        self.label_noPrimarySpan_value.setObjectName("label_noPrimarySpan_value")
        self.gridLayout.addWidget(self.label_noPrimarySpan_value, 15, 0, 1, 1)
        self.label_finishesCeiling = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_finishesCeiling.setFont(font)
        self.label_finishesCeiling.setObjectName("label_finishesCeiling")
        self.gridLayout.addWidget(self.label_finishesCeiling, 21, 2, 2, 1)
        self.comboBox_distribution = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_distribution.setFont(font)
        self.comboBox_distribution.setObjectName("comboBox_distribution")
        self.gridLayout.addWidget(self.comboBox_distribution, 29, 1, 1, 2)
        self.label_distribution = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_distribution.setFont(font)
        self.label_distribution.setObjectName("label_distribution")
        self.gridLayout.addWidget(self.label_distribution, 29, 0, 1, 1)
        self.label_ecc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_ecc.setFont(font)
        self.label_ecc.setObjectName("label_ecc")
        self.gridLayout.addWidget(self.label_ecc, 27, 0, 1, 5)
        self.label_envelopeWallsLoad = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_envelopeWallsLoad.setFont(font)
        self.label_envelopeWallsLoad.setObjectName("label_envelopeWallsLoad")
        self.gridLayout.addWidget(self.label_envelopeWallsLoad, 21, 3, 1, 1)
        self.openGLWidget = MyOpenGLWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(36)
        sizePolicy.setVerticalStretch(36)
        sizePolicy.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout.addWidget(self.openGLWidget, 1, 4, 18, 6)
        self.label_explanation = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_explanation.setFont(font)
        self.label_explanation.setObjectName("label_explanation")
        self.gridLayout.addWidget(self.label_explanation, 20, 4, 1, 1)
        self.pushButton_reset_pos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset_pos.setObjectName("pushButton_reset_pos")
        self.gridLayout.addWidget(self.pushButton_reset_pos, 20, 7, 1, 1)
        self.pushButton_render = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_render.setObjectName("pushButton_render")
        self.gridLayout.addWidget(self.pushButton_render, 20, 5, 1, 2)
        self.label_histogram = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_histogram.setFont(font)
        self.label_histogram.setObjectName("label_histogram")
        self.gridLayout.addWidget(self.label_histogram, 21, 4, 1, 1)
        self.pushButton_histogram = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_histogram.setObjectName("pushButton_histogram")
        self.gridLayout.addWidget(self.pushButton_histogram, 34, 4, 1, 1)
        self.label_building = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_building.setFont(font)
        self.label_building.setObjectName("label_building")
        self.gridLayout.addWidget(self.label_building, 0, 4, 1, 2)
        self.plotWidget = MplWidget(self.centralwidget)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout.addWidget(self.plotWidget, 22, 4, 11, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # EVERYTHING AFTER THIS IS NOT DESIGNER GENERATED
        # The scale for sliders is increased 100x fold, this is because sliders only
        # take in Integer values. When reading or displaying the value remember to divide by 100
        
        # Buttons
        self.pushButton_histogram.clicked.connect(self.generateHistograms)
        self.pushButton_render.clicked.connect(self.generateBuilding)
        self.pushButton_reset_pos.clicked.connect(self.resetCamera)
        
        # Dropdown boxes
        self.comboBox_material.addItems(["Steel", "Reinforced Concrete", "Glulam"])
        self.comboBox_distribution.addItems(["Uniform", "Gaussian", "Triangular"])
        
        # Set the default values for everything
        self.horizontalSlider_lowerBound.setMinimum(10)
        self.horizontalSlider_lowerBound.setMaximum(500)
        self.horizontalSlider_upperBound.setMinimum(10)
        self.horizontalSlider_upperBound.setMaximum(500)
        self.horizontalSlider_mode.setMinimum(10)
        self.horizontalSlider_mode.setMaximum(500)
        self.valueChangePrimarySpan()
        self.valueChangeSecondarySpan()
        self.valueChangeInterStoreyHeight()
        self.valueChangeNoOfPrimarySpans()
        self.valueChangeNoOfSecondarySpans()
        self.valueChangeNoOfStoreys()
        self.valueChangeVariableFloorLoad()
        self.valueChangeFinishesCeiling()
        self.valueChangeEnvelopeWallsLoad()
        self.valueChangeLowerBound()
        self.valueChangeUpperBound()
        self.valueChangeMode()
        self.valueChangeDistribution()

        
        
        # Horizontal sliders
        self.horizontalSlider_primarySpan.valueChanged.connect(self.valueChangePrimarySpan)
        self.horizontalSlider_secondarySpan.valueChanged.connect(self.valueChangeSecondarySpan)
        self.horizontalSlider_interstoreyHeight.valueChanged.connect(self.valueChangeInterStoreyHeight)
        self.horizontalSlider_noPrimarySpan.valueChanged.connect(self.valueChangeNoOfPrimarySpans)
        self.horizontalSlider_NoSecondarySpans.valueChanged.connect(self.valueChangeNoOfSecondarySpans)
        self.horizontalSlider_noStoreys.valueChanged.connect(self.valueChangeNoOfStoreys)
        self.horizontalSlider_variableFloorLoad.valueChanged.connect(self.valueChangeVariableFloorLoad)
        self.horizontalSlider_finishesCeiling.valueChanged.connect(self.valueChangeFinishesCeiling)
        self.horizontalSlider_envelopeWallsLoad.valueChanged.connect(self.valueChangeEnvelopeWallsLoad)
        self.horizontalSlider_lowerBound.valueChanged.connect(self.valueChangeLowerBound)
        self.horizontalSlider_upperBound.valueChanged.connect(self.valueChangeUpperBound)
        self.horizontalSlider_mode.valueChanged.connect(self.valueChangeMode)
        
        # Drop down
        self.comboBox_distribution.currentTextChanged.connect(self.valueChangeDistribution)
        
    def resetCamera(self):
        self.openGLWidget.resetCamera()
        self.openGLWidget.update()
        

    def generateBuilding(self):
        self.openGLWidget.changeBuilding(self.valueChangePrimarySpan(), self.valueChangeSecondarySpan(), \
                                         self.valueChangeInterStoreyHeight(), self.valueChangeNoOfPrimarySpans(), \
                                         self.valueChangeNoOfSecondarySpans(), self.valueChangeNoOfStoreys())
            
        self.openGLWidget.update()
        
    def generateHistograms(self):
        area = self.valueChangePrimarySpan() * self.valueChangeSecondarySpan() \
        * self.valueChangeNoOfPrimarySpans() * self.valueChangeNoOfSecondarySpans()
        
        aspect_ratio = self.valueChangePrimarySpan() * self.valueChangeNoOfPrimarySpans() \
        / (self.valueChangeSecondarySpan() * self.valueChangeNoOfSecondarySpans())
        
        inputs = [area, aspect_ratio, self.valueChangePrimarySpan(), self.valueChangeSecondarySpan(), \
                  self.valueChangeNoOfPrimarySpans(), self.valueChangeNoOfSecondarySpans(), \
                  self.valueChangeNoOfStoreys(), self.valueChangeInterStoreyHeight(), \
                  self.valueChangeFinishesCeiling(), self.valueChangeVariableFloorLoad(), \
                  self.valueChangeEnvelopeWallsLoad()]
            
        # Generate the results based on desired models
        material = str(self.comboBox_material.currentText())
        distribution = str(self.comboBox_distribution.currentText())
        lower = self.valueChangeLowerBound()
        upper = self.valueChangeUpperBound()
        mode = self.valueChangeMode()
        
        if (distribution == "Uniform" and upper <= lower):
            self.warningMessage("Ensure that the upper bound is greater than the lower bound.")
            return
        if (distribution == "Triangular" and (mode < lower or mode > upper)):
            self.warningMessage("Ensure that the mode is between the upper and lower bound")
            return
        
        # Run Monte Carlo
        mcs = mc(inputs, material, distribution, lower, upper, mode)
        finalList = mcs.getList()
        
        
        # Create Graph
        self.plotWidget.canvas.ax.clear()
        self.plotWidget.canvas.ax.hist(finalList, density=True, bins=30, label="Data")
        self.plotWidget.canvas.ax.set_ylabel('Probability')
        self.plotWidget.canvas.draw()
        
        
        
    def warningMessage(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        msg.setText(message)
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    
    def valueChangeDistribution(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.comboBox_distribution.currentText()
        if (value == "Uniform"):
            self.label_lowerBound.setText(_translate("MainWindow", "Lower Bound"))
            self.label_UpperBound.setText(_translate("MainWindow", "Upper Bound"))
            self.label_mode.hide()
            self.horizontalSlider_mode.hide()
            self.label_mode_2.hide()
            try: self.horizontalSlider_lowerBound.valueChanged.disconnect(self.boundariesChangeLower)
            except Exception: pass
            self.horizontalSlider_upperBound.setMaximum(500)
        elif (value == "Gaussian"):
            self.label_lowerBound.setText(_translate("MainWindow", "Mean"))
            self.label_UpperBound.setText(_translate("MainWindow", "Standard Deviation"))
            self.label_mode.hide()
            self.horizontalSlider_mode.hide()
            self.label_mode_2.hide()
            self.horizontalSlider_lowerBound.valueChanged.connect(self.boundariesChangeLower)
            self.boundariesChangeLower()
        else:
            self.label_lowerBound.setText(_translate("MainWindow", "Lower Bound"))
            self.label_UpperBound.setText(_translate("MainWindow", "Upper Bound"))
            self.label_mode.show()
            self.label_mode.setText(_translate("MainWindow", "Mode"))
            self.horizontalSlider_mode.show()
            self.label_mode_2.show()
            try: self.horizontalSlider_lowerBound.valueChanged.disconnect(self.boundariesChangeLower)
            except Exception: pass
            self.horizontalSlider_upperBound.setMaximum(500)
            
    def boundariesChangeLower(self):
        newMaximum = self.horizontalSlider_lowerBound.value()
        newMaximum = self.roundDown(newMaximum / 3, 10)
        self.horizontalSlider_upperBound.setMaximum(newMaximum)
    
    def valueChangePrimarySpan(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_primarySpan.value()
        value = self.valueCalc(value, 10.0)
        self.label_primarySpan_value.setText(_translate("MainWindow", str(value)))
        return value
    
    def valueChangeSecondarySpan(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_secondarySpan.value()
        value = self.valueCalc(value, 10.0)
        self.label_secondarySpan_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeInterStoreyHeight(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_interstoreyHeight.value()
        value = self.valueCalc(value, 10.0)
        self.label_interstoreyHeight_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeNoOfPrimarySpans(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_noPrimarySpan.value()
        value = self.valueCalc(value, 100.0)
        self.label_noPrimarySpan_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeNoOfSecondarySpans(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_NoSecondarySpans.value()
        value = self.valueCalc(value, 100.0)
        self.label_noSecondarySpan_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeNoOfStoreys(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_noStoreys.value()
        value = self.valueCalc(value, 100.0)
        self.label_NoStoreys_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeVariableFloorLoad(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_variableFloorLoad.value()
        value = self.valueCalc(value, 100.0)
        self.label_variableFloorLoad_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeFinishesCeiling(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_finishesCeiling.value()
        value = self.valueCalc(value, 25.0)
        self.label_finishesCeiling_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeEnvelopeWallsLoad(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_envelopeWallsLoad.value()
        value = self.valueCalc(value, 100.0)
        self.label_envelopeWallsLoad_2.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeLowerBound(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_lowerBound.value()
        value = self.valueCalc(value, 10.0)
        self.label_lowerBound_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeUpperBound(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_upperBound.value()
        value = self.valueCalc(value, 10.0)
        self.label_UpperBound_value.setText(_translate("MainWindow", str(value)))
        return value
        
    def valueChangeMode(self):
        _translate = QtCore.QCoreApplication.translate
        value = self.horizontalSlider_mode.value()
        value = self.valueCalc(value, 10.0)
        self.label_mode_2.setText(_translate("MainWindow", str(value)))
        return value
        
        
    def valueCalc(self, value, roundTo):
        if (value % roundTo != 0):
            value = self.roundUp(value, roundTo)
        if (roundTo == 100):
            return int(value / 100)
        else:
            return value / 100
    
    def roundUp(self, x, roundTo):
        return int(math.ceil(x / roundTo)) * roundTo
    
    def roundDown(self, x, roundTo):
        return int(math.floor(x / roundTo)) * roundTo
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beetle"))
        self.label_variableFloorLoad.setText(_translate("MainWindow", "Variable Floor Load"))
        self.label_material.setText(_translate("MainWindow", "MATERIAL"))
        self.label_mode.setText(_translate("MainWindow", "Mode"))
        self.label_UpperBound_value.setText(_translate("MainWindow", "Value"))
        self.label_mode_2.setText(_translate("MainWindow", "Value"))
        self.label_geometry.setText(_translate("MainWindow", "GEOMETRY"))
        self.label_secondarySpan_value.setText(_translate("MainWindow", "Value"))
        self.label_NoStoreys.setText(_translate("MainWindow", "No. of Storeys"))
        self.label_noSecondarySpan_value.setText(_translate("MainWindow", "Value"))
        self.label_interstoreyHeight.setText(_translate("MainWindow", "Inter-storey Height [m]"))
        self.label_secondarySpan.setText(_translate("MainWindow", "Secondary Span [m]"))
        self.label_interstoreyHeight_value.setText(_translate("MainWindow", "Value"))
        self.label_NoStoreys_value.setText(_translate("MainWindow", "Value"))
        self.label_noPrimarySpan.setText(_translate("MainWindow", "No. of Primary Spans"))
        self.label_noSecondarySpan.setText(_translate("MainWindow", "No. of Secondary Spans"))
        self.label_loads.setText(_translate("MainWindow", "LOADS"))
        self.label_primarySpan_value.setText(_translate("MainWindow", "Value"))
        self.label_lowerBound.setText(_translate("MainWindow", "Lower Bound"))
        self.label_UpperBound.setText(_translate("MainWindow", "Upper Bound"))
        self.label_envelopeWallsLoad_2.setText(_translate("MainWindow", "Value"))
        self.label_variableFloorLoad_value.setText(_translate("MainWindow", "Value"))
        self.label_finishesCeiling_value.setText(_translate("MainWindow", "Value"))
        self.label_beetle.setText(_translate("MainWindow", "BEETLE"))
        self.label_primarySpan.setText(_translate("MainWindow", "Primary Span [m]"))
        self.label_lowerBound_value.setText(_translate("MainWindow", "Value"))
        self.label_noPrimarySpan_value.setText(_translate("MainWindow", "Value"))
        self.label_finishesCeiling.setText(_translate("MainWindow", "Finishes, Ceiling,\n"
"Services And Partitions\n"
"Load"))
        self.label_distribution.setText(_translate("MainWindow", "Distribution"))
        self.label_ecc.setText(_translate("MainWindow", "EMBODIED CARBON COEFFICIENT"))
        self.label_envelopeWallsLoad.setText(_translate("MainWindow", "Envelope Walls Load"))
        self.label_explanation.setText(_translate("MainWindow", "Move camera by pressing\n"
" left, right, and middle\n"
"mouse buttons."))
        self.pushButton_reset_pos.setText(_translate("MainWindow", "Reset Position"))
        self.pushButton_render.setText(_translate("MainWindow", "3D Render"))
        self.label_histogram.setText(_translate("MainWindow", "HISTOGRAM"))
        self.pushButton_histogram.setText(_translate("MainWindow", "Generate Histogram"))
        self.label_building.setText(_translate("MainWindow", "BUILDING VISUALISATION"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

