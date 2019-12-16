# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from scipy.integrate import odeint

class Ui_Form(object):

    def Calculadiagrama(self):
        plt.close('all')
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_3.text())
        c = int(self.lineEdit_4.text())
        d = int(self.lineEdit_5.text())

        def dP_dt(P, t):
            return [P[0] * (a - b * P[1]), -P[1] * (c - d * P[0])]

        ts = np.linspace(int(self.lineEdit_6.text()),int(self.lineEdit_7.text()),int(self.lineEdit_8.text()))
        P0 = [float(self.lineEdit_9.text()),float(self.lineEdit_10.text())]
        Ps = odeint(dP_dt, P0, ts)
        prey = Ps[:, 0]
        predators = Ps[:, 1]

        plt2.subplot(1, 1, 1)
        plt2.plot(prey, predators, "b.")
        plt2.xlabel("Monos")
        plt2.ylabel("Jaguares")
        plt2.title("Diagrama de Espacio de Fase");
        plt2.show()

    def Calculacomportamiento(self):
        plt.close('all')
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_3.text())
        c = int(self.lineEdit_4.text())
        d = int(self.lineEdit_5.text())

        def dP_dt(P, t):
            return [P[0] * (a - b * P[1]), -P[1] * (c - d * P[0])]

        ts = np.linspace(int(self.lineEdit_6.text()),int(self.lineEdit_7.text()),int(self.lineEdit_8.text()))
        P0 = [float(self.lineEdit_9.text()),float(self.lineEdit_10.text())]
        Ps = odeint(dP_dt, P0, ts)
        prey = Ps[:, 0]
        predators = Ps[:, 1]

        plt.subplot(1, 1, 1)
        plt.plot(ts, prey, "r-", label="Monos")
        plt.plot(ts, predators, "b-", label="Jaguares")
        plt.xlabel("Tiempo (meses)")
        plt.ylabel("Población")
        plt.legend();
        plt.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(639, 581)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 591, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 271, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 411, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 311, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 221, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(460, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 50, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(460, 80, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 110, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 591, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 231, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(460, 20, 113, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(460, 50, 113, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(460, 80, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 410, 591, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 131, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 141, 41))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(460, 20, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(460, 60, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(260, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 341, 41))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(490, 70, 131, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("ecuaciondepre.PNG"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(370, 70, 121, 51))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("ecuacionpresa.PNG"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.comportamiento = QtWidgets.QPushButton(Form)
        self.comportamiento.setGeometry(QtCore.QRect(70, 510, 171, 61))
        self.comportamiento.setObjectName("comportamiento")

        self.comportamiento.clicked.connect(self.Calculacomportamiento)


        self.diagrama = QtWidgets.QPushButton(Form)
        self.diagrama.setGeometry(QtCore.QRect(350, 510, 171, 61))
        self.diagrama.setObjectName("diagrama")

        self.diagrama.clicked.connect(self.Calculadiagrama)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Datos"))
        self.groupBox.setTitle(_translate("Form", "Valores"))
        self.label_4.setText(_translate("Form", "D: Crecimiento de la Poblacion de Depredadores"))
        self.label_3.setText(_translate("Form", "C: Tasa de pérdida de los depredadores debido a la muerte natural o emigración"))
        self.label_2.setText(_translate("Form", "B: Tasa de interacción entre ambas, depredadores y presas"))
        self.label.setText(_translate("Form", "A: Crecimiento (Exponencial) de la presa"))
        self.lineEdit.setPlaceholderText(_translate("Form", "1"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "1"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "1"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "1"))
        self.groupBox_2.setTitle(_translate("Form", "Gráfica"))
        self.label_5.setText(_translate("Form", "Tiempo en el que empieza (meses)"))
        self.label_6.setText(_translate("Form", "Tiempo en el que termina (meses)"))
        self.label_7.setText(_translate("Form", "Cantidad de puntos o integración numérica"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "0"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "12"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "100"))
        self.groupBox_3.setTitle(_translate("Form", "Valores Iniciales"))
        self.label_8.setText(_translate("Form", "Población inicial Presa"))
        self.label_9.setText(_translate("Form", "Población inicial Depredador"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "1.5"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "1.0"))
        self.label_10.setText(_translate("Form", "Ingreso de Datos"))
        self.label_11.setText(_translate("Form", "Ingrese los siguientes datos para las siguientes ecuaciones:"))
        self.comportamiento.setText(_translate("Form", "Mostrar\n"
"Comportamiento de Poblaciones"))
        self.diagrama.setText(_translate("Form", "Mostrar\n"
"Diagrama de Estado Fase"))


