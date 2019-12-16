# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poblacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 476)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 511, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("diagramaconejo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 561, 91))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Diagrama de Población"))
        self.label.setText(_translate("Form", "Diagramas de Población"))
        self.label_3.setText(_translate("Form", "Las ecuaciones de Lotka-Volterra\n"
"describen un sistema depredador-presa y es uno de los ejemplos de sistemas dinámicos más famosos. De hecho,\n"
"sobre este sistema existen muchas generalizaciones y aplicaciones fuera de la biología. Este tipo de sistemas,\n"
"generalmente se introducen en el curso de Ingeniería de Sistemas Dinámicos o Simulación, en carreras de Computación.\n"
))


