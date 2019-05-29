import sys

from DesignGui_2 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class MainForm(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Hallo.clicked.connect(self.halloClicked)

    def halloClicked(self):
        QMessageBox.information(self, 'Demo Qt Designer',
             'Hallo %s, apa kabar?' % self.ui.NameEdit.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
