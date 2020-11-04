# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Scrapping.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import io
import glob


class Scrapping(object):
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
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(360, 20, 380, 141))
        #self.listView.setObjectName("listView")
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButtonElMundo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonElMundo.setGeometry(QtCore.QRect(230, 70, 93, 28))
        self.pushButtonElMundo.setObjectName("pushButtonElMundo")
        self.pushButtonElMundo.clicked.connect(self.pushButtonElMundoExecute)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(44, 80, 151, 20))
        self.label.setObjectName("label")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(360, 190, 380, 141))
        #self.listView_2.setObjectName("listView_2")
        self.listView.setObjectName(_fromUtf8("listView2"))
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(360, 360, 380, 141))
        #self.listView_3.setObjectName("listView_3")
        self.listView.setObjectName(_fromUtf8("listView3"))
        self.pushButton_elpais = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_elpais.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.pushButton_elpais.setObjectName("pushButton_elpais")
        self.pushButton_elpais.clicked.connect(self.pushButtonElPaisExecute)
        self.pushButton_20mins = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20mins.setGeometry(QtCore.QRect(230, 410, 93, 28))
        self.pushButton_20mins.setObjectName("pushButton_20mins")
        self.pushButton_20mins.clicked.connect(self.pushButton20MinutosExecute)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 410, 151, 20))
        self.label_3.setObjectName("label_3")
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
        self.pushButtonElMundo.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Scrapping El Mundo"))
        self.pushButton_elpais.setText(_translate("MainWindow", "Aceptar"))
        self.pushButton_20mins.setText(_translate("MainWindow", "Aceptar"))
        self.label_2.setText(_translate("MainWindow", "Scrapping El Pais"))
        self.label_3.setText(_translate("MainWindow", "Scrapping 20 minutos"))
        
        
    def cargarNoticiaElMundo(self,url,periodico,seccion,n):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print("parseando "+url)
        articulo = soup.find("div", {"class":"ue-l-article__body ue-c-article__body"})
        titulo = soup.find("h1")
        entradilla=soup.find("p", {"class":"ue-c-article__standfirst"})
        fecha=soup.find("time")
        if articulo is not None:
            articulo=articulo.findAll('p', class_=lambda x: x != 'ue-c-article__trust-container')
        if articulo is None or entradilla is None or titulo is None or fecha is None:
            print("Error parseando\n")
            return False
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,fecha["datetime"][:10],n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text() + "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True

    def cargarNoticiaElPais(self,url,periodico,seccion,n):
        dmeses ={"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}
        print("parseando "+url)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error parseando\n")
            return False
        articulo = soup.find("div", {"class":"articulo-cuerpo"})
        if articulo is None:
            articulo= soup.find("div",{"class":"article_body"})
        titulo = soup.find("h1")
        entradilla=soup.find("h2")
        if entradilla is None:
            entradilla=soup.find("div",{"class":"articulo-introduccion"})
        fecha=soup.find("a", {"class":"a_ti"})
        if not fecha is None:
            datos=fecha.get_text().split(" - ")
            if len(datos)==3:
                fechatext=datos[1].strip()
            else:
                fechatext=datos[0].strip()
            datosfecha=fechatext.split(" ")[:3]
            cadenafecha="%s-%02d-%s"%(datosfecha[2],dmeses[datosfecha[1]],datosfecha[0])
        else:
            fecha=soup.find("time")
            if fecha is not None:
                cadenafecha=fecha["datetime"][:10]
        if articulo is None or entradilla is None or titulo is None or fecha is None:
            print("Error parseando\n")
            return False
        articulo=articulo.findAll('p')
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,cadenafecha,n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text() + "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True
    
    def cargarNoticia20minutos(self,url,periodico,seccion,n):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error parseando\n")
            return False
        print("parseando "+url)
        articulo = soup.find("div", {"class":"article-text"})
        titulo = soup.find("h1")
        entradilla=soup.find("div", {"id":"m35-34-36"})
        if entradilla is None:
            entradilla=soup.find("div",{"id":"m96-95-97"})
        fecha=soup.find("span", {"class":"article-date"})
        if not fecha is None:
            datos=fecha.get_text().split(" - ")
            fechatext=datos[0].strip()
            datosfecha=fechatext.split(".")[:3]
            cadenafecha="%s-%s-%s"%(datosfecha[2],datosfecha[1],datosfecha[0])
        if articulo is None or entradilla is None or titulo is None or fecha is None:
            print("Error parseando\n")
            return False
        articulo=articulo.findAll('p')
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,cadenafecha,n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text().strip() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text().strip() + "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True
    
       
    def cargarListanoticiasElMundo(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("a",{"class":"ue-c-cover-content__link"})
        n=1;
        for l in links:
            if self.cargarNoticiaElMundo(l["href"],periodico,seccion,n):
                n=n+1
                
                
    def cargarListanoticiasElPais(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("h2",{"class":"headline"})
        n=1;
        for l in links:
            url="http://www.elpais.com" + l.find("a")["href"]
            if self.cargarNoticiaElPais(url,periodico,seccion,n):
                n=n+1
                
                
    def cargarListanoticias20minutos(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("div",{"class":"media-content"})
        n=1;
        for l in links:
            url=l.find("a")["href"]
            if self.cargarNoticia20minutos(url,periodico,seccion,n):
                n=n+1
                
    def pushButtonElMundoExecute(self):
        self.cargarListanoticiasElMundo("https://www.elmundo.es/ciencia-y-salud/salud.html","ElMundo","Salud")
        self.cargarListanoticiasElMundo('https://www.elmundo.es/tecnologia.html','ElMundo','Tecnologia')
        self.cargarListanoticiasElMundo("https://www.elmundo.es/ciencia-y-salud/ciencia.html","ElMundo","Ciencia")
        lista=glob.glob("ElMundo/Salud/*.txt")
        lista2=glob.glob("ElMundo/Tecnologia/*.txt")
        lista3=glob.glob("ElMundo/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        
    def pushButtonElPaisExecute(self):
        self.cargarListanoticiasElPais("https://elpais.com/noticias/sanidad-publica/","ElPais","Salud")
        self.cargarListanoticiasElPais("https://elpais.com/tecnologia/","ElPais","Tecnologia")
        self.cargarListanoticiasElPais("https://elpais.com/ciencia/","ElPais","Ciencia")
        lista=glob.glob("ElPais/Salud/*.txt")
        lista2=glob.glob("ElPais/Tecnologia/*.txt")
        lista3=glob.glob("ElPais/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        
    def pushButton20MinutosExecute(self):
        self.cargarListanoticias20minutos("https://www.20minutos.es/salud/","20Minutos","Salud")
        self.cargarListanoticias20minutos("https://www.20minutos.es/tecnologia/","20Minutos","Tecnologia")
        self.cargarListanoticias20minutos("https://www.20minutos.es/ciencia/","20Minutos","Ciencia")
        lista=glob.glob("20Minutos/Salud/*.txt")
        lista2=glob.glob("20Minutos/Tecnologia/*.txt")
        lista3=glob.glob("20Minutos/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView_3.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Scrapping()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

