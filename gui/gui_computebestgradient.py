# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'computebestgradient.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ComputeBestGradient(object):
    def setupUi(self, ComputeBestGradient):
        ComputeBestGradient.setObjectName(_fromUtf8("ComputeBestGradient"))
        ComputeBestGradient.resize(1037, 683)
        self.gridLayout_2 = QtGui.QGridLayout(ComputeBestGradient)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(ComputeBestGradient)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.modelBox = QtGui.QComboBox(ComputeBestGradient)
        self.modelBox.setObjectName(_fromUtf8("modelBox"))
        self.horizontalLayout.addWidget(self.modelBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ComputeBestGradient)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.flowMinSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.flowMinSpinBox.setDecimals(3)
        self.flowMinSpinBox.setMinimum(0.0)
        self.flowMinSpinBox.setProperty("value", 0.2)
        self.flowMinSpinBox.setObjectName(_fromUtf8("flowMinSpinBox"))
        self.gridLayout.addWidget(self.flowMinSpinBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ComputeBestGradient)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.flowMaxSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.flowMaxSpinBox.setDecimals(3)
        self.flowMaxSpinBox.setProperty("value", 0.5)
        self.flowMaxSpinBox.setObjectName(_fromUtf8("flowMaxSpinBox"))
        self.gridLayout.addWidget(self.flowMaxSpinBox, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(ComputeBestGradient)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.GStartMinSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.GStartMinSpinBox.setProperty("value", 5.0)
        self.GStartMinSpinBox.setObjectName(_fromUtf8("GStartMinSpinBox"))
        self.gridLayout.addWidget(self.GStartMinSpinBox, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ComputeBestGradient)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.GSartMaxSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.GSartMaxSpinBox.setProperty("value", 20.0)
        self.GSartMaxSpinBox.setObjectName(_fromUtf8("GSartMaxSpinBox"))
        self.gridLayout.addWidget(self.GSartMaxSpinBox, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(ComputeBestGradient)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.GStoptMinSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.GStoptMinSpinBox.setProperty("value", 40.0)
        self.GStoptMinSpinBox.setObjectName(_fromUtf8("GStoptMinSpinBox"))
        self.gridLayout.addWidget(self.GStoptMinSpinBox, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ComputeBestGradient)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.GStopMaxSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.GStopMaxSpinBox.setProperty("value", 95.0)
        self.GStopMaxSpinBox.setObjectName(_fromUtf8("GStopMaxSpinBox"))
        self.gridLayout.addWidget(self.GStopMaxSpinBox, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(ComputeBestGradient)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.timeMinSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.timeMinSpinBox.setMinimum(1.0)
        self.timeMinSpinBox.setProperty("value", 2.0)
        self.timeMinSpinBox.setObjectName(_fromUtf8("timeMinSpinBox"))
        self.gridLayout.addWidget(self.timeMinSpinBox, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(ComputeBestGradient)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.timeMaxSpinBox = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.timeMaxSpinBox.setMaximum(200.0)
        self.timeMaxSpinBox.setProperty("value", 20.0)
        self.timeMaxSpinBox.setObjectName(_fromUtf8("timeMaxSpinBox"))
        self.gridLayout.addWidget(self.timeMaxSpinBox, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.calculateButton = QtGui.QPushButton(ComputeBestGradient)
        self.calculateButton.setMaximumSize(QtCore.QSize(110, 32))
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.horizontalLayout_3.addWidget(self.calculateButton)
        spacerItem = QtGui.QSpacerItem(796, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        self.plotterBox = QtGui.QGroupBox(ComputeBestGradient)
        self.plotterBox.setMinimumSize(QtCore.QSize(551, 311))
        self.plotterBox.setObjectName(_fromUtf8("plotterBox"))
        self.gridLayout_2.addWidget(self.plotterBox, 3, 0, 1, 3)
        self.label_10 = QtGui.QLabel(ComputeBestGradient)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_15 = QtGui.QLabel(ComputeBestGradient)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_4.addWidget(self.label_15)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_5.setReadOnly(True)
        self.doubleSpinBox_5.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(647, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_11 = QtGui.QLabel(ComputeBestGradient)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.doubleSpinBox_1 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_1.setReadOnly(True)
        self.doubleSpinBox_1.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_1.setObjectName(_fromUtf8("doubleSpinBox_1"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_1)
        self.label_12 = QtGui.QLabel(ComputeBestGradient)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_2.setReadOnly(True)
        self.doubleSpinBox_2.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.label_13 = QtGui.QLabel(ComputeBestGradient)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_2.addWidget(self.label_13)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_3.setReadOnly(True)
        self.doubleSpinBox_3.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_3)
        self.label_14 = QtGui.QLabel(ComputeBestGradient)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_2.addWidget(self.label_14)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_4.setReadOnly(True)
        self.doubleSpinBox_4.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(932, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 7, 0, 1, 2)
        self.closeButton = QtGui.QPushButton(ComputeBestGradient)
        self.closeButton.setMaximumSize(QtCore.QSize(110, 32))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout_2.addWidget(self.closeButton, 7, 2, 1, 1)
        self.closeButton.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.GSartMaxSpinBox.raise_()
        self.GStartMinSpinBox.raise_()
        self.plotterBox.raise_()
        self.calculateButton.raise_()
        self.timeMinSpinBox.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.timeMaxSpinBox.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.doubleSpinBox_1.raise_()
        self.doubleSpinBox_2.raise_()
        self.doubleSpinBox_3.raise_()
        self.doubleSpinBox_4.raise_()
        self.doubleSpinBox_5.raise_()
        self.label_15.raise_()

        self.retranslateUi(ComputeBestGradient)
        QtCore.QMetaObject.connectSlotsByName(ComputeBestGradient)

    def retranslateUi(self, ComputeBestGradient):
        ComputeBestGradient.setWindowTitle(_translate("ComputeBestGradient", "Compute best gradient conditions", None))
        self.label_4.setText(_translate("ComputeBestGradient", "Select model", None))
        self.label.setText(_translate("ComputeBestGradient", "Flow min", None))
        self.label_2.setText(_translate("ComputeBestGradient", "Flow max", None))
        self.label_3.setText(_translate("ComputeBestGradient", "Gradient Start min", None))
        self.label_7.setText(_translate("ComputeBestGradient", "Gradient Start max", None))
        self.label_5.setText(_translate("ComputeBestGradient", "Gradient Stop min", None))
        self.label_6.setText(_translate("ComputeBestGradient", "Gradient Gradient Stop max", None))
        self.label_8.setText(_translate("ComputeBestGradient", "Time min", None))
        self.label_9.setText(_translate("ComputeBestGradient", "Time max", None))
        self.calculateButton.setText(_translate("ComputeBestGradient", "Calculate", None))
        self.plotterBox.setTitle(_translate("ComputeBestGradient", "Optimization View", None))
        self.label_10.setText(_translate("ComputeBestGradient", "Best conditions:", None))
        self.label_15.setText(_translate("ComputeBestGradient", "Gradient Steepness", None))
        self.label_11.setText(_translate("ComputeBestGradient", "Gradient Start:", None))
        self.label_12.setText(_translate("ComputeBestGradient", "Gradient Stop:", None))
        self.label_13.setText(_translate("ComputeBestGradient", "Time Gradient:", None))
        self.label_14.setText(_translate("ComputeBestGradient", "Flow rate:", None))
        self.closeButton.setText(_translate("ComputeBestGradient", "Close", None))

