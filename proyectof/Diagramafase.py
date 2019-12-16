# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Diagramafase.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 477)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(20, 70, 461, 121))
        self.label_18.setObjectName("label_18")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 461, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Focal_stability.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Diagrama de Fase"))
        self.label.setText(_translate("Form", "Espacio Fásico o Diagrama de Fases"))
        self.label_18.setText(_translate("Form", "\n"
"En mecánica clásica, el espacio fásico, espacio de fases o diagrama de fases es una \n"
"construcción matemática que permite representar el conjunto de posiciones y momentos \n"
"conjugados de un sistema de partículas. Técnicamente, el espacio de fases es una variedad \n"
"diferenciable de dimensión par, tal que las coordenadas de cada punto representan tanto \n"
"las posiciones generalizadas como sus momentos conjugados correspondientes. Es decir, cada \n"
"punto del espacio fásico representa un estado del sistema físico. Ese estado físico vendrá \n"
"caracterizado por la posición de cada una de las partículas y sus respectivos momentos.\n"
"\n"
""))

