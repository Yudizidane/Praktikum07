from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 321)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 301, 21))
        self.label.setObjectName("label")
        self.NameEdit = QtWidgets.QLineEdit(Form)
        self.NameEdit.setGeometry(QtCore.QRect(50, 70, 371, 20))
        self.NameEdit.setObjectName("NameEdit")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.Exit.setObjectName("Exit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(140, 100, 211, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Hallo = QtWidgets.QPushButton(self.widget)
        self.Hallo.setObjectName("Hallo")
        self.horizontalLayout.addWidget(self.Hallo)
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        self.Clear.clicked.connect(self.NameEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Masukkan Nama Anda :</span></p></body></html>"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.Hallo.setText(_translate("Form", "Hallo"))
        self.Clear.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
