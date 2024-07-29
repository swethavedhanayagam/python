import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QWidget,QAction,QMenuBar,QDialog
class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("second Window")
        self.setGeometry(200,200,300,200)
        layout=QVBoxLayout()
        label=QLabel("this is the second window",self)
        layout.addWidget(label)
        self.setLayout(layout)
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyQt Example")
        self.setGeometry(100,100,400,300)
        self.central_widget=QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout=QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.label=QLabel("hello,pyQt!",self)
        self.button=QPushButton("click me",self)
        self.layout.addWidget(self.button)
        self.init_menu()
    def init_menu(self):
        menubar=self.menuBar()
        file_menu=menubar.addMenu("file")
        exit_action=QAction("exit",self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        view_menu=menubar.addMenu("view")
        second_Window_action=QAction("open second window",self)
        second_Window_action.triggered.connect(self.open_second_window)
        view_menu.addAction(second_Window_action)
    def open_second_window(self):
        self.second_window=SecondWindow()
        self.second_window.exec_()
app=QApplication(sys.argv)
window=MyWindow()
window.show()
sys.exit(app.exec_())