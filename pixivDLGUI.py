
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import QBasicTimer
import pixivpy3
from time import sleep

import pixivui

def imageDlFromUserId(user_id, path, username, password, score=700):
    papi = pixivpy3.PixivAPI()
    papi.login(username, password)

    res = papi.users(user_id)
    work_num = res['response'][0]['stats']['works']
    json_result = papi.users_works(user_id, per_page=work_num)

    aapi = pixivpy3.AppPixivAPI()
    for work in json_result["response"]:

        sleep(1)

        if work['stats']['score'] < score:
            continue

        #もし一つの記事に複数枚あるならそれを全部取得
        if work['is_manga']:
            for i in range(work['page_count']):
                url = work["image_urls"]['large'][0:-5] + str(i) + work["image_urls"]['large'][-4:]
                print("\r"+url)
                aapi.download(url, path)

        else:
            url = work["image_urls"]['large']
            print("\r"+url)
            aapi.download(url, path)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = pixivui.Ui_PixivDownloader()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.download)
        self.timer = QBasicTimer()
        self.step = 0

    def download(self):
            username = self.ui.lineEdit.text()
            password = self.ui.lineEdit_2.text()
            directory = self.ui.lineEdit_3.text()
            user_id = int( self.ui.lineEdit_4.text() )
            self.api = pixivpy3.PixivAPI()
            self.api.login(username, password)
            res = self.api.users(user_id)
            work_num = res['response'][0]['stats']['works']
            json_result = self.api.users_works(user_id, per_page=work_num)
            self.work_list = json_result["response"]


import sys
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
