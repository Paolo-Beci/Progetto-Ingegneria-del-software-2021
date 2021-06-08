import os
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from prodotto.view.VistaProdotto import VistaProdotto
from listaprodotti.controller.ControllerListaProdotti import ControllerListaProdotti

"""
    DISPLAY DEL SINGOLO PRODOTTO IN VistaListaProdotti
"""


class VistaDisplayProdotto(QWidget):
    def __init__(self, prodotto, retranslateUi, widget, r, c, grid_layout):
        super(VistaDisplayProdotto, self).__init__()
        self.prodotto = prodotto
        self.retranslate_ui = retranslateUi
        self.widget = widget
        self.righe = r
        self.colonne = c
        self.gridLayout_2 = grid_layout
        self.controller = ControllerListaProdotti()

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)

        self.display_prodotto = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_prodotto.sizePolicy().hasHeightForWidth())
        self.display_prodotto.setSizePolicy(sizePolicy)
        self.display_prodotto.setMinimumSize(QtCore.QSize(200, 400))
        self.display_prodotto.setObjectName("display_prodotto")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.display_prodotto)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.immagine = QtWidgets.QLabel(self.display_prodotto)
        self.immagine.setObjectName("immagine")
        self.immagine.setAlignment(QtCore.Qt.AlignCenter)
        if os.path.isfile('listaprodotti/data/images/' + str(prodotto.cod_prodotto) + '.jpg'):
            pixmap = QPixmap('listaprodotti/data/images/' + str(prodotto.cod_prodotto) + '.jpg')
        else:
            pixmap = QPixmap('listaprodotti/data/images/noimage.jpg')
        self.immagine.setPixmap(pixmap)
        self.verticalLayout_2.addWidget(self.immagine, QtCore.Qt.AlignHCenter)
        self.nome_marca = QtWidgets.QLabel(self.display_prodotto)
        self.nome_marca.setObjectName("nome_marca")
        self.nome_marca.setFont(font)
        self.nome_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_marca.setText(str(prodotto.nome) + " - " + str(prodotto.marca))
        self.verticalLayout_2.addWidget(self.nome_marca)
        self.prezzo = QtWidgets.QLabel(self.display_prodotto)
        self.prezzo.setObjectName("prezzo")
        self.prezzo.setFont(font)
        self.prezzo.setAlignment(QtCore.Qt.AlignCenter)
        self.prezzo.setText(str(prodotto.prezzo_vendita) + " €")
        self.verticalLayout_2.addWidget(self.prezzo)

        self.taglia_quantita = QtWidgets.QLabel(self.display_prodotto)
        self.taglia_quantita.setObjectName("taglia_quantita")
        self.taglia_quantita.setFont(font)
        self.taglia_quantita.setAlignment(QtCore.Qt.AlignCenter)
        self.taglia_quantita.setText("Taglia: " + str(prodotto.taglia) + " - Qt.: " + str(prodotto.quantita))
        self.verticalLayout_2.addWidget(self.taglia_quantita)

        self.dettagli_button = QtWidgets.QPushButton(self.widget)
        self.dettagli_button.setObjectName("dettagli")
        self.dettagli_button.setText("Dettagli")
        self.verticalLayout_2.addWidget(self.dettagli_button, 1)
        self.dettagli_button.clicked.connect(self.show_prodotto)

        self.gridLayout_2.addWidget(self.display_prodotto, self.righe, self.colonne, 1, 1)

    def show_prodotto(self):
        self.vista_prodotto = VistaProdotto(self.prodotto, self.retranslate_ui)
        self.vista_prodotto.showMaximized()
        time.sleep(0.3)
        self.close()
