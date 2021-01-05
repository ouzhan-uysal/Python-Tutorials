# pip install pyqt5
# pip install pyqt5-tools   => Tasarımla yapacağımız araç: Designer.exeimport sys
"""
VS Code üzerinden Yüklediklerim:
1. Kite Autocomplete for Python
2. Magic Python
3. Pylance
4. Django
5. Kite indir.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Window")
    win.setGeometry(600, 300, 640, 480)        # Parametreler: Konum X, Konum Y, Genişlik, Yükseklik
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my tooltip")        # İmleci üzerine getirdiğinde çıkan yazı

    win.show()
    sys.exit(app.exec_())    # Penceredeki X ikonuna tıklanınca pencereyi sonlandıracak komut


window()