import time
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets, QtGui

from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.view.VistaModificaOrdine import VistaModificaOrdine
from prodotto.view.VistaProdotto import VistaProdotto


class VistaOrdine(QWidget):
    def __init__(self, ordine, elimina_ordine_by_codice, update_ui, controller_lista_ordini, controller_lista_prodotti, parent=None):
        super(VistaOrdine, self).__init__(parent)
        self.ordine_selezionato = ordine

        self.controller_ordine = ControllerOrdine(ordine)
        self.controller_lista_ordini= controller_lista_ordini
        self.controller_lista_prodotti= controller_lista_prodotti

        self.elimina_ordine_by_codice = elimina_ordine_by_codice
        self.update_ui = update_ui

        self.lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
        self.lista_prodotti_ordine= []

        #######################################

        self.setObjectName("Form")
        self.resize(882, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self)
        self.pushButton_indietro.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_indietro.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.pushButton_indietro.clicked.connect(self.close)
        self.gridLayout.addWidget(self.pushButton_indietro, 1, 4, 1, 1)
        self.pushButton_apri = QtWidgets.QPushButton(self)
        self.pushButton_apri.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_apri.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_apri.setObjectName("pushButton_apri")
        self.pushButton_apri.clicked.connect(self.show_prodotto)
        self.gridLayout.addWidget(self.pushButton_apri, 1, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_modifica = QtWidgets.QPushButton(self)
        self.pushButton_modifica.setObjectName("pushButton_modifica")
        self.pushButton_modifica.clicked.connect(self.show_modifica_ordine)
        self.horizontalLayout.addWidget(self.pushButton_modifica)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_elimina = QtWidgets.QPushButton(self)
        self.pushButton_elimina.setObjectName("pushButton_elimina")
        self.horizontalLayout.addWidget(self.pushButton_elimina)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setMinimumSize(QtCore.QSize(630, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 180)
        self.tableWidget.setColumnWidth(5, 180)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 9, 5)
        self.label_11 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 11, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 7)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Visualizza ordine")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Marca"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Quantità"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Taglia"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Prezzo d\'acquisto"))

        # riempie la lista_prodotti_ordine
        self.filter()

        row = 0
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(self.lista_prodotti_ordine))

        for prodotto in self.lista_prodotti_ordine:

            item = QTableWidgetItem(str(prodotto.cod_prodotto))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(prodotto.marca))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto.tipo))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(prodotto.quantita)))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(prodotto.taglia)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(prodotto.prezzo_acquisto) + " €"))

            row = row + 1

        self.label_5.setText(_translate("Form", "Data ordine: {}".format(self.controller_ordine.get_data_ordine())))
        self.label_8.setText(_translate("Form", "Importo totale: {}".format(str(self.controller_ordine.get_importo_totale()) + " €")))
        self.pushButton_indietro.setText(_translate("Form", "<- Indietro"))
        self.pushButton_apri.setText(_translate("Form", "Apri"))
        self.label_2.setText(_translate("Form", "Stato: {}".format(self.controller_ordine.get_stato())))
        self.label_10.setText(_translate("Form", "Lista prodotti ordine:"))
        self.label.setText(_translate("Form", "Codice fattura: {}".format(self.controller_ordine.get_cod_fattura())))
        self.pushButton_modifica.setText(_translate("Form", "Modifica"))
        self.pushButton_elimina.setText(_translate("Form", "Elimina"))
        self.label_6.setText(_translate("Form", "Data arrivo prevista: {}".format(self.controller_ordine.get_data_arrivo_prevista())))
        self.label_9.setText(_translate("Form", "Calzature totali: {}".format(str(self.controller_ordine.get_calzature_totali()))))
        self.label_3.setText(_translate("Form", "Stagione: {}".format(self.controller_ordine.get_stagione())))
        self.label_7.setText(_translate("Form", "Data arrivo effettiva: {}".format(self.controller_ordine.get_data_arrivo_effettiva())))
        self.label_4.setText(_translate("Form", "Codice fornitore: {}".format(self.controller_ordine.get_cod_fornitore())))
        self.label_11.setText(_translate("Form", "Dati ordine:"))

        #######################################

    # prendo da lista_prodotti solo quei prodotti relativi a ordine_selezionato
    def filter(self):
        for prodotto in self.lista_prodotti:
            if prodotto.cod_fattura == self.controller_ordine.get_cod_fattura():
                self.lista_prodotti_ordine.append(prodotto)

    def show_prodotto(self):
        if len(self.tableWidget.selectedIndexes()) > 0:
            selected = self.tableWidget.selectedIndexes()[0].row()
            prodotto_selezionato = self.lista_prodotti_ordine[selected]
            self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.retranslateUi)
            self.vista_prodotto.showMaximized()
            time.sleep(0.3)

    def elimina_ordine_click(self):
        self.controller_lista_ordini.elimina_ordine_by_codice(self.controller_ordine.get_cod_fattura())
        #self.elimina_ordine_by_codice(self.controller_ordine.get_cod_fattura())
        self.update_ui()
        self.close()

    def show_modifica_ordine(self):
        self.vista_modifica_ordine= VistaModificaOrdine(self.ordine_selezionato, self.controller_ordine, self.retranslateUi, self.lista_prodotti_ordine)
        self.vista_modifica_ordine.showMaximized()
        #self.update_ui()
        #self.close()

