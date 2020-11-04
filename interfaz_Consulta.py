# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Consulta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import similitudes as sim
import glob
import analisis_Lexico as al

class Consulta(object):
    def setupUi(self, MainWindow):
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 55, 41))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 40, 291, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.comprobarboton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 55, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 130, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.consultarPalabras)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 220, 311, 281))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView.doubleClicked.connect(self.cargarNoticia)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 190, 121, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(410, 220, 321, 281))
        self.textEdit_2.setObjectName("textEdit_2")
        #self.textEdit_2.setEnabled(False)
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
        self.label.setText(_translate("MainWindow", "Consulta:"))
        self.label_2.setText(_translate("MainWindow", "TOP-N"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox.setItemText(3, _translate("MainWindow", "25"))
        self.comboBox.setItemText(4, _translate("MainWindow", "50"))
        self.label_3.setText(_translate("MainWindow", "Filtrar:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ElMundo"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ElPais"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "20Minutos"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.label_4.setText(_translate("MainWindow", "Ranking:"))
        self.label_5.setText(_translate("MainWindow", "Texto de la noticia:"))
        
    def comprobarboton(self):
        if(self.textEdit.toPlainText()!=''):
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


    def consultarPalabras(self):
        listapalabras=self.textEdit.toPlainText().split()
        listapalabras=al.preprocess(listapalabras).split()
        freqconsulta=sim.frecuencias(listapalabras,list(set(listapalabras)))#set es conjunto para eliminar repetidos
        listanoticias=self.obtenerListaNoticiasSeleccionada()
        dicnoticias={}
        for noticia in listanoticias:
            palabrasfichero=sim.ficheroListaPalabras(noticia)
            palabrasfichero=al.preprocess(palabrasfichero).split()
            freqnoticia=sim.frecuencias(palabrasfichero,listapalabras)
            dicnoticias[noticia]=int(sim.similitud(freqconsulta,freqnoticia)*100)
        ranking=int(self.comboBox.currentText())
        ordenado=sim.ordenarsimilitudes(dicnoticias)[:ranking]#menos para cogerlo de ultimas a primeras y : hasta el final
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for (noticia,similitud) in ordenado:
            try:
                item = QtGui.QStandardItem(noticia+" - SIM "+str(similitud)+"%")
                model.appendRow(item)
            except:
                pass
    def obtenerListaNoticiasSeleccionada(self):
        seleccion=str(self.comboBox_2.currentText())
        print("seleccion:",seleccion)
        listanoticias=[]
        if seleccion=='Todos'or seleccion=='ElPais':
            listanoticias+=self.getnoticias('ElPais')
        if seleccion=='Todos'or seleccion=='ElMundo':
            listanoticias+=self.getnoticias('ElMundo')
        if seleccion=='Todos'or seleccion=='20Minutos':
            listanoticias+=self.getnoticias('20Minutos')
        return listanoticias
    
    
    def getnoticias(self,carpeta):
        lista=glob.glob(carpeta+"/Salud/*.txt")
        lista+=glob.glob(carpeta+"/Tecnologia/*.txt")
        lista+=glob.glob(carpeta+"/Ciencia/*.txt")
        return lista
            
    def cargarNoticia(self):
        noticia = self.listView.selectedIndexes()
        for data in noticia:
            dato=data.data()
            print(dato)
        dato1=dato.split(" - SIM ")[0]
        file = open(dato1, encoding="utf8")
        self.textEdit_2.setText(file.read())
        #item=str(self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked))
        
      

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Consulta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

