
import requests
from bs4 import BeautifulSoup 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAbstractItemView
from PyQt5.QtWidgets import QTableWidgetItem

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Movies')
        self.table_products = QtWidgets.QTableWidget(self)
        self.table_products.setGeometry(QtCore.QRect(10, 30, 801, 591))
        self.table_products.setObjectName("table_products")
        self.table_products.setColumnCount(0)
        self.table_products.setRowCount(0)

        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=250)

        self.table_products.setRowCount(len(list))
        self.table_products.setColumnCount(3)
        self.table_products.setHorizontalHeaderLabels(('Title','Year','Rating'))
        self.table_products.setColumnWidth(0,200) # birinci sutun kalınlıgı
        self.table_products.setColumnWidth(1,200) # ikinci sutun kalınlıgı
        self.table_products.setColumnWidth(2,200) # ikinci sutun kalınlıgı

        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=250)
        i =0
        row=0
        for tr in list:
            i +=1
            title = tr.find("td",{ "class": "titleColumn"}).find("a").text
            year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
            rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
            self.table_products.setItem(row,0,QTableWidgetItem(str(title)))
            self.table_products.setItem(row,1,QTableWidgetItem(str(year)))
            self.table_products.setItem(row,2,QTableWidgetItem(str(rating)))
            row +=1
        self.table_products.setSelectionBehavior(QAbstractItemView.SelectRows) # satır satır seçer
        self.table_products.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #seçilemez yaptık
            
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle('IMDB')
        self.resize(1008, 607)
        self.x = AnotherWindow()
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(130, 90, 701, 191))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 20, 611, 161))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(640, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "IMDB MOST POPULAR TOP 250 MOVIES"))
        self.pushButton.setText(_translate("MainWindow", "BRING"))
        self.pushButton.clicked.connect(self.getir)
        

    def getir(self):
        self.x.show()

def app():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
app()
