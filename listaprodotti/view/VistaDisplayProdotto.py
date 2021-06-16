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
    def __init__(self, prodotto):
        super(VistaDisplayProdotto, self).__init__()

        self.prodotto= prodotto

        self.setObjectName("Form")
        self.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_foto = QtWidgets.QLabel(self)
        self.label_foto.setScaledContents(False)
        self.label_foto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_foto.setObjectName("label_foto")
        self.gridLayout.addWidget(self.label_foto, 0, 0, 1, 2)
        self.label_marca = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_marca.sizePolicy().hasHeightForWidth())
        self.label_marca.setSizePolicy(sizePolicy)
        self.label_marca.setMinimumSize(QtCore.QSize(0, 30))
        self.label_marca.setObjectName("label_marca")
        self.gridLayout.addWidget(self.label_marca, 1, 1, 1, 1)
        self.pushButton_dettagli = QtWidgets.QPushButton(self)
        self.pushButton_dettagli.setObjectName("pushButton_dettagli")
        self.pushButton_dettagli.clicked.connect(self.dettagli_click)
        self.gridLayout.addWidget(self.pushButton_dettagli, 4, 0, 1, 2)
        self.label_nome = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy)
        self.label_nome.setMinimumSize(QtCore.QSize(0, 30))
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.label_prezzo_vendita = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prezzo_vendita.sizePolicy().hasHeightForWidth())
        self.label_prezzo_vendita.setSizePolicy(sizePolicy)
        self.label_prezzo_vendita.setMinimumSize(QtCore.QSize(0, 30))
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.gridLayout.addWidget(self.label_prezzo_vendita, 2, 0, 1, 2)
        self.label_taglia = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_taglia.sizePolicy().hasHeightForWidth())
        self.label_taglia.setSizePolicy(sizePolicy)
        self.label_taglia.setMinimumSize(QtCore.QSize(0, 30))
        self.label_taglia.setObjectName("label_taglia")
        self.gridLayout.addWidget(self.label_taglia, 3, 0, 1, 1)
        self.label_quantita = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_quantita.sizePolicy().hasHeightForWidth())
        self.label_quantita.setSizePolicy(sizePolicy)
        self.label_quantita.setMinimumSize(QtCore.QSize(0, 30))
        self.label_quantita.setObjectName("label_quantita")
        self.gridLayout.addWidget(self.label_quantita, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_foto.setText(_translate("Form", "Foto"))
        self.label_marca.setText(_translate("Form", self.prodotto.marca))
        self.pushButton_dettagli.setText(_translate("Form", "Dettagli"))
        self.label_nome.setText(_translate("Form", self.prodotto.nome))
        self.label_prezzo_vendita.setText(_translate("Form", "Prezzo vendita"))
        self.label_taglia.setText(_translate("Form", "Taglia"))
        self.label_quantita.setText(_translate("Form", "Quantita"))

    def dettagli_click(self):
        self.vista_prodotto= VistaProdotto(self.prodotto, None)
        self.vista_prodotto.showMaximized()