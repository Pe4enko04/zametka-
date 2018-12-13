import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QInputDialog

import untitled as design
class ExamleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.Add.clicked.connect(self.click0)
        self.list = []
        self.listView = []
        self.screen.itemClicked.connect(self.item_click)
        findAction = QAction(QIcon('e.png'),'&Find',self)
        findAction.triggered.connect(self.search)
        self.menu.addAction(findAction)
    def click0(self):
        if not self.text.toPlainText()=='' and not self.text2.toPlainText()=='':
            by = {'text':self.text.toPlainText(), 'date':self.text2.toPlainText()}
            self.list.append(by)
            self.listView.append(str(by))
            self.screen.clear()
            self.screen.insertItems(0,self.listView)
            self.text.setText('')
            self.text2.setText('')

    def item_click(self, item):
        print(str(item.text()))
        self.list.pop(self.listView.index(str(item.text())))
        self.listView.remove(str(item.text()))
        self.screen.clear()
        self.screen.insertItems(0,self.listView)

    def search(self):
        text,ok = QInputDialog.getText(self,'ПОИСК','Элемент')
        if ok:
            print(str(text))



app=QtWidgets.QApplication(sys.argv)
window=ExamleApp()
window.show()
app.exec_()