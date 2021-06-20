from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from prodotto.controller.ControllerProdotto import ControllerProdotto


class VistaVendiProdotto(QWidget):
    def __init__(self, prodotto, parent=None):
        super(VistaVendiProdotto, self).__init__(parent)
        self.controller = ControllerProdotto(prodotto)
        self.prodotto = prodotto
        # self.controller.set_venduto()

        self.setObjectName("Form")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.taglia_quantita = QtWidgets.QLabel(self)
        self.taglia_quantita.setAlignment(QtCore.Qt.AlignCenter)
        self.taglia_quantita.setObjectName("taglia_nome")
        self.gridLayout.addWidget(self.taglia_quantita, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.prezzo = QtWidgets.QLabel(self)
        self.prezzo.setAlignment(QtCore.Qt.AlignCenter)
        self.prezzo.setObjectName("prezzo")
        self.gridLayout.addWidget(self.prezzo, 3, 1, 1, 1)
        self.pushButton_vendi = QtWidgets.QPushButton(self)
        self.pushButton_vendi.setObjectName("pushButton_vendi")
        self.gridLayout.addWidget(self.pushButton_vendi, 5, 1, 1, 1)
        self.marca_nome = QtWidgets.QLabel(self)
        self.marca_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.marca_nome.setObjectName("marca_nome")
        self.gridLayout.addWidget(self.marca_nome, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.immagine = QtWidgets.QLabel(self)
        self.immagine.setAlignment(QtCore.Qt.AlignCenter)
        self.immagine.setObjectName("immagine")
        self.gridLayout.addWidget(self.immagine, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.marca_nome.setText(_translate("MainWindow", "Nome: " + str(self.prodotto.nome))
                                + " - Marca: " + str(self.prodotto.marca))
        self.taglia_quantita.setText(_translate("MainWindow", "Taglia: " + str(self.prodotto.taglia)
                                                + " - Quantita: " + str(self.prodotto.quantita)))
        self.prezzo.setText(_translate("MainWindow", "Prezzo: " + str(self.prodotto.prezzo_vendita)) + " €")
        self.pushButton_vendi.setText(_translate("MainWindow", "VENDI"))

        if self.prodotto is None:
            pixmap = QPixmap('listaprodotti/data/images/' + str(self.prodotto.cod_prodotto) + '.jpg')
        else:
            pixmap = QPixmap('listaprodotti/data/images/noimage.jpg')
        self.immagine.setPixmap(pixmap)

