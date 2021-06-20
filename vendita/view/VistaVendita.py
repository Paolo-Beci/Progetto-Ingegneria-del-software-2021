from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti
from vendita.view.VistaVendiProdotto import VistaVendiProdotto

"""
    VISTA CHE FACILITA IL PROCESSO DI VENDITA DI UN PRODOTTO (shortcut)
"""


class VistaVendita(QWidget):
    def __init__(self, parent=None):
        super(VistaVendita, self).__init__(parent)
        self.controller = ControllerListaProdotti()
        self.prodotto_trovato = []

        self.resize(902, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        # Cerca prodotto
        self.cerca = QtWidgets.QLineEdit(self.widget)
        self.cerca.setObjectName("cerca")
        self.gridLayout.addWidget(self.cerca, 0, 2, 1, 1)
        self.cerca.returnPressed.connect(self.cerca_prodotto)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        # indietro
        self.pushButton_indietro = QtWidgets.QPushButton(self.widget)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.gridLayout.addWidget(self.pushButton_indietro, 0, 0, 1, 1)
        self.pushButton_indietro.clicked.connect(self.show_home)
        # LOGO
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setObjectName("logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini3.png')
        self.logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.logo, 0, 4, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        # Taglia
        self.taglia = QtWidgets.QComboBox(self.widget)
        self.taglia.setObjectName("taglia")
        for count in range(16, 49):
            self.taglia.addItem(str(count))
        self.gridLayout.addWidget(self.taglia, 1, 2, 1, 1)

        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # Immagine
        self.immagine = QtWidgets.QLabel(self.widget_2)
        self.immagine.setAlignment(QtCore.Qt.AlignCenter)
        self.immagine.setObjectName("immagine")

        self.verticalLayout_2.addWidget(self.immagine)
        # label marca e nome
        self.marca_nome = QtWidgets.QLabel(self.widget_2)
        self.marca_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.marca_nome.setObjectName("marca_nome")
        self.verticalLayout_2.addWidget(self.marca_nome)
        # label taglia e quantita
        self.taglia_quantita = QtWidgets.QLabel(self.widget_2)
        self.taglia_quantita.setAlignment(QtCore.Qt.AlignCenter)
        self.taglia_quantita.setObjectName("taglia_quantita")
        self.verticalLayout_2.addWidget(self.taglia_quantita)
        # label prezzo
        self.prezzo = QtWidgets.QLabel(self.widget_2)
        self.prezzo.setAlignment(QtCore.Qt.AlignCenter)
        self.prezzo.setObjectName("prezzo")
        self.verticalLayout_2.addWidget(self.prezzo)

        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
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
        # pushButton vendita
        self.pushButton_vendi = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_vendi.setObjectName("pushButton_vendi")
        self.horizontalLayout.addWidget(self.pushButton_vendi)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget_3)
        # dimensionamento interaccia
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = (self.screenRect.height()) / 2.25
        width = (self.screenRect.width()) / 2.15
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, width, height))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Area vendita"))
        self.cerca.setPlaceholderText(_translate("MainWindow", "Cerca per codice prodotto"))
        self.pushButton_indietro.setText(_translate("MainWindow", "< Indietro"))
        self.taglia.setItemText(0, _translate("MainWindow", "Taglia"))
        self.marca_nome.setText(_translate("MainWindow", "Nome: " + str(self.controller.get_nome_prodotto_by_code(self.cerca.text()))
                                           + " - Marca: " + str(self.controller.get_marca_prodotto_by_code(self.cerca.text()))))
        self.taglia_quantita.setText(_translate("MainWindow", "Taglia: " + str(self.taglia.currentText())
                                                + " - Quantita: " + str(self.controller.get_quantita_prodotto_by_code(self.cerca.text()))))
        self.prezzo.setText(_translate("MainWindow", "Prezzo: " + str(self.controller.get_prezzo_prodotto_by_code(self.cerca.text()))) + " €")
        self.pushButton_vendi.setText(_translate("MainWindow", "VENDI"))

        if len(self.prodotto_trovato) != 0:
            pixmap = QPixmap('listaprodotti/data/images/' + str(self.cerca.text()) + '.jpg')
        else:
            pixmap = QPixmap('listaprodotti/data/images/noimage.jpg')
        self.immagine.setPixmap(pixmap)

    def show_home(self):
        self.close()

    def cerca_prodotto(self):
        cod_prodotto = str(self.cerca.text())
        cod_prodotto.capitalize()
        print(str(self.cerca.text()))
        for prodotto in self.controller.get_lista_prodotti():
            if prodotto.cod_prodotto == cod_prodotto and prodotto.taglia == int(self.taglia.currentText()):
                self.prodotto_trovato.append(prodotto)
        if len(self.prodotto_trovato) == 0:
            self.popup_errore()

    def vendi_prodotto(self):
        VistaVendiProdotto(self.controller.get_prodotto_by_code(str(self.cerca.text())))

    def popup_errore(self):
        msg = QMessageBox()
        msg.setWindowTitle("ATTENZIONE")
        msg.setText(
            "Hai inserito un codice prodotto non valido oppure non hai inserito la taglia! \n\nProva con un formato codice del tipo: S03")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()

    def closeEvent(self, event):
        self.controller.save_data()
