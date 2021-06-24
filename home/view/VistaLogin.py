from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox


class VistaLogin(QWidget):
    def __init__(self, controller, update_ui):
        super(VistaLogin, self).__init__()
        self.controller = controller
        self.update_ui = update_ui

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        # ICONA
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.setObjectName("Form")
        self.resize(500, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_login = QtWidgets.QPushButton(self)
        self.pushButton_login.setObjectName("pushButton_login")
        self.gridLayout.addWidget(self.pushButton_login, 8, 2, 1, 1)
        self.pushButton_login.setStyleSheet("QPushButton {\n""   background-color: green;\n""   border-width: 2px;\n""min-width: 80px;\n""border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.pushButton_login.clicked.connect(self.login)
        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_password, 5, 1, 1, 1)
        self.lineEdit_password.returnPressed.connect(self.login)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.pushButton_annulla = QtWidgets.QPushButton(self)
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.gridLayout.addWidget(self.pushButton_annulla, 8, 0, 1, 1)
        self.pushButton_annulla.setStyleSheet("QPushButton {\n" "   background-color:white;\n" "   border-width: 2px;\n""   border-radius: 10px;\n""   border: 2px solid gray;\n""   font: bold 12px;\n""   padding: 6px;\n""}")
        self.pushButton_annulla.clicked.connect(self.close)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 9, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
            Costruzione parte dinamica dell'interfaccia  
        '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Login"))
        self.pushButton_login.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Username"))
        self.pushButton_annulla.setText(_translate("Form", "Annulla"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label.setText(_translate("Form", "Login amministratore"))

    # Metodo: verifica effettivamente se l'username e la password inserite sono valide
    def login(self):
        username_inserito = self.lineEdit_username.text()
        password_inserito = self.lineEdit_password.text()

        self.controller.refresh_data()

        for utente in self.controller.get_lista_del_personale():
            if str(utente.username) == str(username_inserito):
                if str(utente.password) == str(password_inserito):
                    self.controller.set_status(True)
                    break

        if self.controller.get_status():
            self.close()
        else:
            self.popup_errore()

    # Metodo: consente la visualizzazione di un messaggio di errore nel caso l'utente inserisca un username o una password errata
    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito un username o password errati! \n\nRiprova con altri dati")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    # Metodo: consente di eseguire una determinata azione alla chiusura dell'interfaccia
    def closeEvent(self, event):
        self.update_ui()
