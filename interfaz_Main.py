    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from interfaz_Scrapping import Scrapping
from interfaz_Consulta import Consulta
from interfaz_Comparar import Comparar


class Principal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Scrapping = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Scrapping.setGeometry(QtCore.QRect(290, 120, 93, 28))
        self.pushButton_Scrapping.setObjectName("pushButton_Scrapping")
        self.pushButton_Scrapping.clicked.connect(self.abrirScrapping)
        self.pushButton_Busqueda = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Busqueda.setGeometry(QtCore.QRect(290, 230, 93, 28))
        self.pushButton_Busqueda.setObjectName("pushButton_Busqueda")
        self.pushButton_Busqueda.clicked.connect(self.abrirConsulta)
        self.pushButton_Comparacion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Comparacion.setGeometry(QtCore.QRect(290, 340, 93, 28))
        self.pushButton_Comparacion.setObjectName("pushButton_Comparacion")
        self.pushButton_Comparacion.clicked.connect(self.abrirComparar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Scrapping.setText(_translate("MainWindow", "Scrapping"))
        self.pushButton_Busqueda.setText(_translate("MainWindow", "Busqueda"))
        self.pushButton_Comparacion.setText(_translate("MainWindow", "Comparacion"))
        
    def abrirScrapping (self):
            self.ventana=QtWidgets.QMainWindow()
            self.ui=Scrapping()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
        
    def abrirConsulta(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Consulta()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def abrirComparar (self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Comparar()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
    
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Principal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

