import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMenuBar, QMenu, QAction, QPushButton, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class MyWindow(QMainWindow):
    win = None

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        self.win = uic.loadUi("calculadora.ui", self)
        self.connect_actions()

    def connect_actions(self):
        self.win.pushButton_clear.clicked.connect(self.clear_input)
        self.win.buttonGroup_numeros.buttonClicked.connect(self.append_number)
        self.win.pushButton_result.clicked.connect(self.calcular)

    def calcular(self):
        result = eval(self.win.input.toPlainText())
        self.win.input.setPlainText(str(result))

    def append_number(self, button):
        text = button.text()
        input_text = self.win.input.toPlainText()
        self.win.input.setPlainText( input_text + text)

    def clear_input(self):
        self.win.input.setPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
