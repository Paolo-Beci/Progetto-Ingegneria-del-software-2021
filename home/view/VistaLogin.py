from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from listadelpersonale.controller.ControllerListaDelPersonale import ControllerListaDelPersonale


class VistaLogin(QWidget):
    def __init__(self):
        super(VistaLogin, self).__init__()
        self.controller = ControllerListaDelPersonale()
        self.corretto = False
        self.setObjectName("MainWindow")
        self.resize(760, 439)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)

        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 3, 2, 1, 1)

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 5, 2, 1, 1)

        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.gridLayout.addWidget(self.pushButton_login, 7, 3, 1, 1)
        self.pushButton_login.clicked.connect(self.login)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.pushButton_annulla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.gridLayout.addWidget(self.pushButton_annulla, 7, 1, 1, 1)
        self.pushButton_annulla.clicked.connect(self.show_back)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        # dimensionamento interaccia
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = (self.screenRect.height()) / 2.5
        width = (self.screenRect.width()) / 2.5
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login amministratore"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.pushButton_annulla.setText(_translate("MainWindow", "Annulla"))
        self.label.setText(_translate("MainWindow", "Login amministratore"))

    def login(self):
        self.username_inserito = self.lineEdit_username.text()
        self.password_inserito = self.lineEdit_password.text()

        for utente in self.controller.get_lista_del_personale():
            if str(utente.username) == str(self.username_inserito):
                if str(utente.password) == str(self.password_inserito):
                    self.corretto = True
                    self.close()
                    break
            else:
                self.popup_errore()
                self.corretto = True
                break

    def get_status(self):
        return self.corretto

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito un username o password errati! \n\nRiprova con altri dati")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def show_back(self):
        self.close()