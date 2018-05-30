# 界面与逻辑分离
# 用来写事件响应 导入界面文件的类
from PyQt5.QtWidgets import QApplication,QMainWindow
from MainView import MainUIView
import sys

class MainLogic(QMainWindow,MainUIView):
    def __init__(self):
        super(MainLogic, self).__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.hello)

    def hello(self):
        print("hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainLogic()
    MainWindow.show()
    sys.exit(app.exec_())

