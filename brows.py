import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("http://google.com"))
		self.setCentralWidget(self.browser)
		self.show()

		self.setWindowTitle("AbJ Brow")
		self.setWindowIcon(QIcon(os.path.join("brow-icon", "x.jpg")))

		exitActIcon = QIcon(os.path.join("brow-icon", "x.jpg"))
		exitAct = QAction(exitActIcon, "Exit", self)
		exitAct.setShortcut("Ctrl+Q")
		exitAct.triggered.connect(qApp.quit)

		self.toolbar = self.addToolBar("Exit")
		self.toolbar.addAction(exitAct)
		self.toolbar.setIconSize(QSize(24, 24))

		navbar = QToolBar("Tool")
		self.addToolBar(navbar)


		back_btn = QAction("Bac", self)
		back_btn.triggered.connect(self.browser.back)
		navbar.addAction(back_btn)
		back_btn.setText("Go Backward")
		back_btn.setIconText("Bac")

		forward_btn = QAction("For", self)
		forward_btn.triggered.connect(self.browser.forward)
		navbar.addAction(forward_btn)
		forward_btn.setText("Go Forward")
		forward_btn.setIconText("For")

		reload_btn = QAction("Rel", self)
		reload_btn.triggered.connect(self.browser.reload)
		navbar.addAction(reload_btn)
		reload_btn.setText("Reload This Page")
		reload_btn.setIconText("Rel")

		home_btn = QAction("Hom", self)
		home_btn.triggered.connect(self.navigate_home)
		home_btn.setText("To AbJ Home")
		home_btn.setIconText("Hom")
		navbar.addAction(home_btn)

		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar)

		self.browser.urlChanged.connect(self.update_url)

	def navigate_home(self):
		self.browser.setUrl(QUrl("https://abj-port.herokuapp.com/"))

	def navigate_to_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))

	def update_url(self, q):
		self.url_bar.setText(q.toString())

app = QApplication(sys.argv)

app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

QApplication.setApplicationName("Browser")
window = MainWindow()
app.exec_()
