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
        ComputeBestGradient.resize(576, 697)
        self.gridLayout = QtGui.QGridLayout(ComputeBestGradient)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(ComputeBestGradient)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.modelBox = QtGui.QComboBox(ComputeBestGradient)
        self.modelBox.setObjectName(_fromUtf8("modelBox"))
        self.horizontalLayout.addWidget(self.modelBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ComputeBestGradient)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(ComputeBestGradient)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.tr_min = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.tr_min.setDecimals(2)
        self.tr_min.setMinimum(0.0)
        self.tr_min.setMaximum(999999999.0)
        self.tr_min.setProperty("value", 2.0)
        self.tr_min.setObjectName(_fromUtf8("tr_min"))
        self.horizontalLayout_5.addWidget(self.tr_min)
        self.label_5 = QtGui.QLabel(ComputeBestGradient)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.tr_max = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.tr_max.setDecimals(2)
        self.tr_max.setMaximum(999999999.0)
        self.tr_max.setProperty("value", 10.0)
        self.tr_max.setObjectName(_fromUtf8("tr_max"))
        self.horizontalLayout_5.addWidget(self.tr_max)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.calculateButton = QtGui.QPushButton(ComputeBestGradient)
        self.calculateButton.setMaximumSize(QtCore.QSize(110, 32))
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))
        self.horizontalLayout_3.addWidget(self.calculateButton)
        spacerItem1 = QtGui.QSpacerItem(796, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_20 = QtGui.QLabel(ComputeBestGradient)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_4.addWidget(self.label_20)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_21 = QtGui.QLabel(ComputeBestGradient)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_7.addWidget(self.label_21)
        self.doubleSpinBox_10 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_10.setReadOnly(True)
        self.doubleSpinBox_10.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(368, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_16 = QtGui.QLabel(ComputeBestGradient)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_6.setReadOnly(True)
        self.doubleSpinBox_6.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_6)
        self.label_17 = QtGui.QLabel(ComputeBestGradient)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_7.setReadOnly(True)
        self.doubleSpinBox_7.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_7)
        self.label_18 = QtGui.QLabel(ComputeBestGradient)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_6.addWidget(self.label_18)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_8.setReadOnly(True)
        self.doubleSpinBox_8.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_8)
        self.label_19 = QtGui.QLabel(ComputeBestGradient)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_6.addWidget(self.label_19)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(ComputeBestGradient)
        self.doubleSpinBox_9.setReadOnly(True)
        self.doubleSpinBox_9.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_9)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 4)
        self.plotterBox = QtGui.QGroupBox(ComputeBestGradient)
        self.plotterBox.setMinimumSize(QtCore.QSize(551, 311))
        self.plotterBox.setObjectName(_fromUtf8("plotterBox"))
        self.gridLayout.addWidget(self.plotterBox, 5, 0, 1, 4)
        spacerItem3 = QtGui.QSpacerItem(932, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 3)
        self.closeButton = QtGui.QPushButton(ComputeBestGradient)
        self.closeButton.setMaximumSize(QtCore.QSize(110, 32))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 6, 3, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(368, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 7, 1, 1, 3)
        self.closeButton.raise_()
        self.plotterBox.raise_()

        self.retranslateUi(ComputeBestGradient)
        QtCore.QMetaObject.connectSlotsByName(ComputeBestGradient)

    def retranslateUi(self, ComputeBestGradient):
        ComputeBestGradient.setWindowTitle(_translate("ComputeBestGradient", "Automatic elution windows stretching", None))
        self.label_4.setText(_translate("ComputeBestGradient", "Select model", None))
        self.label.setText(_translate("ComputeBestGradient", "Peak window", None))
        self.label_3.setText(_translate("ComputeBestGradient", "<html><head/><body><p>t<span style=\" vertical-align:sub;\">R</span> min</p></body></html>", None))
        self.label_5.setText(_translate("ComputeBestGradient", "<html><head/><body><p>t<span style=\" vertical-align:sub;\">R</span> max</p></body></html>", None))
        self.calculateButton.setText(_translate("ComputeBestGradient", "Calculate", None))
        self.label_20.setText(_translate("ComputeBestGradient", "Best conditions:", None))
        self.label_21.setText(_translate("ComputeBestGradient", "Gradient Resolution", None))
        self.label_16.setText(_translate("ComputeBestGradient", "Gradient Start:", None))
        self.label_17.setText(_translate("ComputeBestGradient", "Gradient Stop:", None))
        self.label_18.setText(_translate("ComputeBestGradient", "Time Gradient:", None))
        self.label_19.setText(_translate("ComputeBestGradient", "Flow rate:", None))
        self.plotterBox.setTitle(_translate("ComputeBestGradient", "Selectivity map", None))
        self.closeButton.setText(_translate("ComputeBestGradient", "Close", None))

