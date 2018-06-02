import sys
from PyQt5.QtWidgets import *


class TableWidget(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)

        self.setWindowTitle('TableWidget')
        self.table = QTableWidget(5,7)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['SUN','MON','TUE','WED',
                                              'THU','FIR','SAT'])
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                cnt = '(%d,%d)'% (i,j)
                newItem = QTableWidgetItem(cnt)
                self.table.setItem(i,j,newItem)
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
tb = TableWidget()
tb.show()
app.exec_()