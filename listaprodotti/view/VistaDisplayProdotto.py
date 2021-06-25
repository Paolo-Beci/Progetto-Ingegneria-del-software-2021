import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from prodotto.view.VistaProdotto import VistaProdotto

"""
    DISPLAY DEL SINGOLO PRODOTTO IN VistaListaProdotti
        Contiene le informazioni necessarie per costruire l'interfaccia di ogni singola tile di VistaListaProdotti
"""


class VistaDisplayProdotto(QWidget):
    def __init__(self, prodotto, update_ui, controller, lista_prodotti):
        super(VistaDisplayProdotto, self).__init__()
        self.update_ui = update_ui
        self.prodotto = prodotto
        self.controller = controller
        self.lista_prodotti_filtrata = lista_prodotti

        # FONT
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        font.setWeight(75)

        '''
            Costruzione parte statica dell'interfaccia  
        '''
        self.setObjectName("Form")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_foto = QtWidgets.QLabel(self)
        self.label_foto.setScaledContents(False)
        self.label_foto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_foto.setObjectName("label_foto")
        if os.path.isfile('listaprodotti/data/images/' + str(prodotto.cod_prodotto) + '.jpg'):
            pixmap = QPixmap('listaprodotti/data/images/' + str(prodotto.cod_prodotto) + '.jpg')
        else:
            pixmap = QPixmap('listaprodotti/data/images/noimage.jpg')
        self.label_foto.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_foto, 0, 0, 1, 2)
        self.label_marca = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_marca.sizePolicy().hasHeightForWidth())
        self.label_marca.setSizePolicy(sizePolicy)
        self.label_marca.setMinimumSize(QtCore.QSize(0, 30))
        self.label_marca.setObjectName("label_marca")
        self.label_marca.setFont(font)
        self.gridLayout.addWidget(self.label_marca, 1, 1, 1, 1)
        self.pushButton_dettagli = QtWidgets.QPushButton(self)
        self.pushButton_dettagli.setObjectName("pushButton_dettagli")
        self.pushButton_dettagli.setStyleSheet("QPushButton {\n"
                                            "   background-color:rgb(26, 108, 218);\n"
                                            "   border-width: 2px;\n"
                                            "   border-radius: 10px;\n"
                                            "   font: bold 12px;\n"
                                            "   padding: 6px;\n"
                                            "   color: white;\n"
                                            "}")
        self.pushButton_dettagli.clicked.connect(self.show_prodotto)
        self.gridLayout.addWidget(self.pushButton_dettagli, 4, 0, 1, 2)
        self.label_nome = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome.sizePolicy().hasHeightForWidth())
        self.label_nome.setSizePolicy(sizePolicy)
        self.label_nome.setMinimumSize(QtCore.QSize(0, 30))
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setFont(font)
        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.label_prezzo_vendita = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prezzo_vendita.sizePolicy().hasHeightForWidth())
        self.label_prezzo_vendita.setSizePolicy(sizePolicy)
        self.label_prezzo_vendita.setMinimumSize(QtCore.QSize(0, 30))
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.label_prezzo_vendita.setFont(font)
        self.gridLayout.addWidget(self.label_prezzo_vendita, 3, 0, 1, 2)
        self.label_taglia = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_taglia.sizePolicy().hasHeightForWidth())
        self.label_taglia.setSizePolicy(sizePolicy)
        self.label_taglia.setMinimumSize(QtCore.QSize(0, 30))
        self.label_taglia.setObjectName("label_taglia")
        self.label_taglia.setFont(font)
        self.gridLayout.addWidget(self.label_taglia, 2, 0, 1, 1)
        self.label_quantita = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_quantita.sizePolicy().hasHeightForWidth())
        self.label_quantita.setSizePolicy(sizePolicy)
        self.label_quantita.setMinimumSize(QtCore.QSize(0, 30))
        self.label_quantita.setObjectName("label_quantita")
        self.label_quantita.setFont(font)
        self.gridLayout.addWidget(self.label_quantita, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
       Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_marca.setText(_translate("Form", "Marca: " + str(self.prodotto.marca)))
        self.pushButton_dettagli.setText(_translate("Form", "Dettagli"))
        if str(self.prodotto.nome) == "None":
            self.label_nome.setText(_translate("Form", "Nome: Nessuno"))
        else:
            self.label_nome.setText(_translate("Form", "Nome: " + str(self.prodotto.nome)))
        self.label_prezzo_vendita.setText(_translate("Form", "Prezzo: " + str(self.prodotto.prezzo_vendita) + " €"))
        self.label_taglia.setText(_translate("Form", "Taglia: " + str(self.prodotto.taglia)))
        self.label_quantita.setText(_translate("Form", "Quantità: " + str(self.prodotto.quantita)))

    def show_prodotto(self):
        self.vista_prodotto = VistaProdotto(self.prodotto, self.update_ui, self.controller, self.lista_prodotti_filtrata)
        self.vista_prodotto.showMaximized()
