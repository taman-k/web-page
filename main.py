import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget( self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.Url_bar)

    def navigate_home(self):
        self.browser.setUrl((QUrl('http://google.com')))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName('my cool browser')
window = MainWindow()
app.exec_()
