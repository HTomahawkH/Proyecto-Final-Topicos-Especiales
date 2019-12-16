# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu(object):

    def Ventana_datos(self):
        from proyectof.datos import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def Ventana_comportamiento(self):
        from proyectof.poblacion import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def Ventana_estadofase(self):
        from proyectof.Diagramafase import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(299, 465)
        self.label = QtWidgets.QLabel(menu)
        self.label.setGeometry(QtCore.QRect(120, 20, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(menu)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 251, 71))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(menu)
        self.groupBox.setGeometry(QtCore.QRect(30, 140, 221, 181))
        self.groupBox.setObjectName("groupBox")
        self.comportamiento = QtWidgets.QPushButton(self.groupBox)
        self.comportamiento.setGeometry(QtCore.QRect(30, 30, 171, 61))
        self.comportamiento.setObjectName("comportamiento")

        self.comportamiento.clicked.connect(self.Ventana_comportamiento)

        self.diagrama = QtWidgets.QPushButton(self.groupBox)
        self.diagrama.setGeometry(QtCore.QRect(30, 100, 171, 61))
        self.diagrama.setObjectName("diagrama")

        self.diagrama.clicked.connect(self.Ventana_estadofase)

        self.groupBox_2 = QtWidgets.QGroupBox(menu)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 330, 221, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.ingresa_dato = QtWidgets.QPushButton(self.groupBox_2)
        self.ingresa_dato.setGeometry(QtCore.QRect(30, 30, 171, 61))
        self.ingresa_dato.setObjectName("ingresa_dato")

        self.ingresa_dato.clicked.connect(self.Ventana_datos)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Menú"))
        self.label.setText(_translate("menu", "Menú"))
        self.label_2.setText(_translate("menu", "Objetivo:\n"
"Este programa busca resolver un sistema de \n"
"Lotka-Volterra."))
        self.groupBox.setTitle(_translate("menu", "¿Qué es?"))
        self.comportamiento.setText(_translate("menu", "Comportamiento de Poblaciones"))
        self.diagrama.setText(_translate("menu", "Diagrama de Estado-Fase"))
        self.groupBox_2.setTitle(_translate("menu", "Crear un Diagrama"))
        self.ingresa_dato.setText(_translate("menu", "Ingresar Datos"))



