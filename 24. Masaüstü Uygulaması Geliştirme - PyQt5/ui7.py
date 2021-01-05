import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Paint(QWidget):       # Paint => QWidget'ten türetilecek
    def __init__(self, color):
        super(Paint, self).__init__()
        self.setAutoFillBackground(True)      # Oluşturulan Widget arka planını otomatik boyar

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):  # MainWindow => QMainWindow'dan türetilecek
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)

        # Vertical ve Horizontal Layout Oluşturma
        """
        hlayout = QtWidgets.QHBoxLayout(self)  # Horizontal layout
        hlayout.addWidget(Paint("red"))
        hlayout.addWidget(Paint("blue"))
        hlayout.addWidget(Paint("green"))
        hlayout.addWidget(Paint("orange"))
        hlayout.addWidget(Paint("yellow"))


        vlayout = QtWidgets.QVBoxLayout(self)    # Vertical layout oluşturmai
        vlayout.addLayout(hlayout)
        vlayout.addWidget(Paint("red"))
        vlayout.addWidget(Paint("blue"))
        vlayout.addWidget(Paint("green"))
        """
        # Grid Layout Oluşturma
        glayout = QtWidgets.QGridLayout(self)
        glayout.addWidget(Paint('red'),0,0)     # Grid rengi, satır, sütun
        glayout.addWidget(Paint('blue'),1,0)
        glayout.addWidget(Paint('green'),0,2)
        glayout.addWidget(Paint('orange'),3,1)


        widget = QWidget()
        widget.setLayout(glayout)
        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()