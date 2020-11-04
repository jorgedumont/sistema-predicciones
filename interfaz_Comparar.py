# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Comparar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import similitudes as sim
import glob
import analisis_Lexico as al

class Comparar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 140, 681, 121))
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 55, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 440, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 490, 55, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 490, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 400, 61, 16) )
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 460, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.consultarPalabras)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 590, 681, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 560, 121, 16))
        self.label_9.setObjectName("label_9")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(410, 20, 371, 101))
        self.listView.setObjectName("listView")
        self.listView.doubleClicked.connect(self.cargarNoticia1)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(370, 430, 381, 111))
        self.listView_2.setObjectName("listView_2")
        self.listView_2.doubleClicked.connect(self.cargarNoticia2)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 70, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 70, 101, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 70, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cargarNoticias)
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
        self.label.setText(_translate("MainWindow", "Seleccionar noticia de referencia:"))
        self.label_2.setText(_translate("MainWindow", "Medio:"))
        self.label_3.setText(_translate("MainWindow", "Categoria:"))
        self.label_4.setText(_translate("MainWindow", "Noticias:"))
        self.label_5.setText(_translate("MainWindow", "Preview:"))
        self.label_6.setText(_translate("MainWindow", "TOP-N"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox.setItemText(3, _translate("MainWindow", "25"))
        self.comboBox.setItemText(4, _translate("MainWindow", "50"))
        self.label_7.setText(_translate("MainWindow", "Filtrar:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ElMundo"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ElPais"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "20Minutos"))
        self.label_8.setText(_translate("MainWindow", "Ranking:"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.label_9.setText(_translate("MainWindow", "Texto de la noticia:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "ElMundo"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "ElPais"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "20Minutos"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Salud"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Tecnologia"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Ciencia"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar"))
        

        
    def cargarNoticia(self,dato,textedit):
        file = open(dato, encoding="utf8")
        textedit.setText(file.read())   
        
    def cargarNoticia1(self):
        noticia = self.listView.selectedIndexes()
        dato=noticia[0].data()
        self.cargarNoticia(dato,self.textEdit)
                
    def cargarNoticia2(self):
        noticia = self.listView_2.selectedIndexes()
        dato=noticia[0].data()
        dato1=dato.split(" - SIM ")[0]
        self.cargarNoticia(dato1,self.textEdit_2)

    def cargarNoticias(self):
        listanoticias=self.obtenerListaNoticiasSeleccionada()
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in listanoticias:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
       
            
    def consultarPalabras(self):
        noticia = self.listView.selectedIndexes()
        noticiareferencia=noticia[0].data()
        listapalabras=sim.ficheroListaPalabras(noticiareferencia)
        listapalabras=al.preprocess(listapalabras).split()
        conjuntopalabras=list(set(listapalabras))
        freqconsulta=sim.frecuencias(listapalabras,conjuntopalabras)
        print("freqconsulta:",freqconsulta)
        listanoticias=self.obtenerListaNoticiasSeleccionada2(str(self.comboBox_2.currentText()))
        dicnoticias={}
        for noticia in listanoticias:
            palabrasfichero=sim.ficheroListaPalabras(noticia)
            palabrasfichero=al.preprocess(palabrasfichero).split()
            freqnoticia=sim.frecuencias(palabrasfichero,conjuntopalabras)
            print("fre1noticia:",freqnoticia,"titulo:", noticia)
            dicnoticias[noticia]=int(sim.similitud(freqconsulta,freqnoticia)*100)
        ranking=int(self.comboBox.currentText())
        ordenado=sim.ordenarsimilitudes(dicnoticias)[:ranking]#menos para cogerlo de ultimas a primeras y : hasta el final
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        for (noticia,similitud) in ordenado:
            item = QtGui.QStandardItem(noticia+" - SIM "+str(similitud)+"%")
            model.appendRow(item)
            
            
            

    def obtenerListaNoticiasSeleccionada2(self,seleccion="Todos"): #por defecto es Todos al no ser que le pases una seleccion
        listanoticias=[]
        if seleccion=='Todos'or seleccion=='ElPais':
            listanoticias+=self.getnoticias2('ElPais')
        if seleccion=='Todos'or seleccion=='ElMundo':
            listanoticias+=self.getnoticias2('ElMundo')
        if seleccion=='Todos'or seleccion=='20Minutos':
            listanoticias+=self.getnoticias2('20Minutos')
        return listanoticias
    
    
    def getnoticias2(self,carpeta):
        lista=glob.glob(carpeta+"\\Salud\\*.txt")
        lista+=glob.glob(carpeta+"\\Tecnologia\\*.txt")
        lista+=glob.glob(carpeta+"\\Ciencia\\*.txt")
        return lista


    def obtenerListaNoticiasSeleccionada(self):
        seleccion=str(self.comboBox_3.currentText())
        categoria=str(self.comboBox_4.currentText())
        print("seleccion:",seleccion,"categoria:",categoria)
        listanoticias=[]
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Salud':
            listanoticias+=self.getnoticias('ElPais','Salud')
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('ElPais','Tecnologia')
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('ElPais','Ciencia')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Salud':
            listanoticias+=self.getnoticias('ElMundo','Salud')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('ElMundo','Tecnologia')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('ElMundo','Ciencia')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Salud':
            listanoticias+=self.getnoticias('20Minutos','Salud')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('20Minutos','Tecnologia')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('20Minutos','Ciencia')
        return listanoticias
    
    
    
    def getnoticias(self,medio,categoria):
        lista=glob.glob(medio+'\\'+categoria+"/*.txt")
        lista+=glob.glob(medio+'\\'+categoria+"/*.txt")
        lista+=glob.glob(medio+'\\'+categoria+"/*.txt")
        return lista       
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Comparar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())