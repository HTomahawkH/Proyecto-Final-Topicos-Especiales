# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presentacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from proyectof.datos import Ui_Form

class Ui_presentacion(object):

    def openWindow(self):
        from proyectof.menu import Ui_menu
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.window)
        presentacion.hide()
        self.window.show()

    def setupUi(self, presentacion):
        presentacion.setObjectName("presentacion")
        presentacion.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        presentacion.setFont(font)
        presentacion.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(presentacion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 50, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 140, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 200, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 410, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 500, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 310, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 20, 131, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("logo1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 30, 131, 111))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("logo2.gif"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.entra_menu = QtWidgets.QPushButton(self.centralwidget)
        self.entra_menu.setGeometry(QtCore.QRect(660, 500, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entra_menu.setFont(font)
        self.entra_menu.setObjectName("entra_menu")

        self.entra_menu.clicked.connect(self.openWindow)

        presentacion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(presentacion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        presentacion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(presentacion)
        self.statusbar.setObjectName("statusbar")
        presentacion.setStatusBar(self.statusbar)

        self.retranslateUi(presentacion)
        QtCore.QMetaObject.connectSlotsByName(presentacion)

    def retranslateUi(self, presentacion):
        _translate = QtCore.QCoreApplication.translate
        presentacion.setWindowTitle(_translate("presentacion", "Presentación"))
        self.label.setText(_translate("presentacion", "Universidad Tecnológica de Panamá"))
        self.label_2.setText(_translate("presentacion", "Facultad de Ingeniería en Sistemas Y Computación"))
        self.label_3.setText(_translate("presentacion", "Licenciatura Ingeniería en Sistemas Y Computación"))
        self.label_4.setText(_translate("presentacion", "Tópicos Especiales I"))
        self.label_5.setText(_translate("presentacion", "Proyecto Final"))
        self.label_6.setText(_translate("presentacion", "Pablo Vives      8-919-2174\n"
"Manuel Tuñon   8-928–1124\n"
"Aris Guerra       8-922-1799"))
        self.label_7.setText(_translate("presentacion", "19/12/2019"))
        self.label_8.setText(_translate("presentacion", "Javier Sánchez Galán"))
        self.entra_menu.setText(_translate("presentacion", "Entrar al Menú"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    presentacion = QtWidgets.QMainWindow()
    ui = Ui_presentacion()
    ui.setupUi(presentacion)
    presentacion.show()
    sys.exit(app.exec_())
