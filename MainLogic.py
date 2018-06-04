# 界面与逻辑分离
# 用来写事件响应 导入界面文件的类
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QStandardItemModel, QStandardItem
# from PyQt5.QtCore import QString
from MainView import MainUIView
from movie1 import MovieSpider
import sys


class MainLogic(QMainWindow, MainUIView):
    def __init__(self):
        super(MainLogic, self).__init__()
        self.search_key = "http://www.chapaofan.com/search/"
        self.setupUi(self)
        self.group2.hide()
        self.BtnSearching.clicked.connect(self.Seraching)
        # 不能编辑
        # self.tableLinks.setEditTriggers(QTableWidget.NoEditTriggers)
        # 整行选中的方式
        # self.tableLinks.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 使列完全填充并平分
        # self.tableLinks.verticalHeader.setResizeMode(QHeaderView.Stretch)

    def Seraching(self):
        spider = MovieSpider()
        movie_name = self.lineEditInput.text()
        # 双击事件
        self.tableLinks.itemDoubleClicked.connect(self.itemDoubleClicked)
        try:
            html = spider.get_html(self.search_key + movie_name)
            results = spider.get_urls(html)
            self.SetTableData(results)

        except Exception as e:
 3

print("[Error]", str(e))


    def itemDoubleClicked(self):
        spider = MovieSpider()
        cur_item = self.tableLinks.currentItem()
        # 获取链接格的文本
        url = self.tableLinks.item(cur_item.row(), 1).text()
        try:
            links = spider.get_download(url)
            self.SetTableData(links)
        except Exception as e:
            print("[Error]", str(e))



        # def test(self):
        #     print("test")

if __name__ == '__main__':
    # 所有的PyQt5应用必须创建一个应用（Application）对象。
    # sys.argv参数是一个来自命令行的参数列表。
    app = QApplication(sys.argv)
    MainWindow = MainLogic()
    MainWindow.show()
    # 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
    # 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # 方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
    sys.exit(app.exec_())

