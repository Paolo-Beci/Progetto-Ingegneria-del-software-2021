import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox

from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from listaprodotti.view.VistaDisplayProdotto import VistaDisplayProdotto

"""
    VISTA CHE FACILITA IL PROCESSO DI VENDITA DI UN PRODOTTO (shortcut)
"""


class VistaVendita(QWidget):
    def __init__(self, parent=None):
        super(VistaVendita, self).__init__(parent)
        self.controller = ControllerListaProdotti()
        self.prodotto_trovato = None
        self.flag = False

        self.resize(902, 475)
        self.setObjectName("Form")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cerca = QtWidgets.QLineEdit(self.widget)
        self.cerca.setObjectName("cerca")
        self.gridLayout_3.addWidget(self.cerca, 1, 2, 1, 1)
        self.cerca.setStyleSheet("QLineEdit {\n"
                                 "   border-width: 2px;\n"
                                 "   border-radius: 10px;\n"
                                 "   border: 2px solid gray;\n"
                                 "   font: 12px;\n"
                                 "   padding: 6px;\n"
                                 "}")
        self.cerca.returnPressed.connect(self.cerca_prodotto)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 5, 1, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self.widget)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.png'))
        self.pushButton_indietro.setIcon(icon)
        self.pushButton_indietro.setIconSize(QSize(50, 50))
        self.gridLayout_3.addWidget(self.pushButton_indietro, 0, 0, 1, 1)
        self.pushButton_indietro.setStyleSheet("QPushButton {\n"
                                    "   background-color:white;\n"
                                    "   border-width: 2px;\n"
                                    "   border-radius: 10px;\n"
                                    "   padding: 6px;\n"
                                    "}")
        self.pushButton_indietro.clicked.connect(self.close)
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setObjectName("logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini3.png')
        self.logo.setPixmap(pixmap)
        self.gridLayout_3.addWidget(self.logo, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 3, 1, 1)
        self.taglia = QtWidgets.QComboBox(self.widget)
        self.taglia.setObjectName("taglia")
        for count in range(16, 49):
            self.taglia.addItem(str(count))
        self.gridLayout_3.addWidget(self.taglia, 0, 2, 1, 1)
        self.taglia.setStyleSheet("QComboBox {\n"
                                 "   background-color:rgb(26, 108, 218);\n"
                                 "   border-width: 2px;\n"
                                 "   font: 12px;\n"
                                 "   padding: 3px;\n"
                                 "   color: white;\n"
                                 "}")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # container VistDisplayProdotto
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.setStyleSheet("QPushButton {\n""   background-color: rgb(228, 107, 41);\n""   border-width: 2px;\n""   border-radius:bold 15px;\n""   font: bold 12px;\n""   padding: 10px;\n""   color: white;\n""}")
        self.pushButton.clicked.connect(self.vendi)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        for i in reversed(range(self.gridLayout_3.count())):
            self.gridLayout_3.itemAt(i).widget().setParent(None)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Vendi prodotto"))
        self.pushButton.setText(_translate("MainWindow", "VENDI"))
        self.cerca.setPlaceholderText(_translate("MainWindow", "Inserisci codice e premi invio"))
        self.taglia.setItemText(0, _translate("MainWindow", "Taglia"))
        if self.flag:
            self.vista_prodotto_da_vendere = VistaDisplayProdotto(self.prodotto_trovato, self.retranslateUi, self.controller, None)
            self.widget_vendita = self.vista_prodotto_da_vendere
            self.gridLayout_3.addWidget(self.widget_vendita, 0, 0, 1, 1)

    def cerca_prodotto(self):
        cod_prodotto_cerca = str(self.cerca.text())
        cod_prodotto = cod_prodotto_cerca.capitalize()
        if self.taglia.currentText()!="Taglia":
            for prodotto in self.controller.get_lista_prodotti():
                if str(prodotto.cod_prodotto) == str(cod_prodotto) and int(prodotto.taglia) == int(self.taglia.currentText()) and str(prodotto.stato) == "In negozio":
                    self.prodotto_trovato = prodotto
                    self.flag = True
        else:
            return
        #print(self.prodotto_trovato)
        if self.prodotto_trovato is None:
            self.popup_errore()

        self.retranslateUi()

    def vendi(self):
        if self.flag:
            self.prodotto_trovato.stato = "Venduto"
            data_odierna = datetime.datetime.now()
            self.prodotto_trovato.data_vendita = str("%s/%s/%s" % (data_odierna.day, data_odierna.month, data_odierna.year))
            self.popup_venduto()

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Codice prodotto già venduto oppure non presente nel database! \n\n"
            "Prova con un formato codice del tipo: S03 o con una nuova taglia")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def popup_venduto(self):
        msg = QMessageBox()
        msg.setWindowTitle("VENDUTO")
        msg.setText(
            "Hai venduto il prodotto inserito! \n\n"
            "Puoi verificare il suo stato nella sezione prodotti")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def closeEvent(self, event):
        self.controller.save_data()
