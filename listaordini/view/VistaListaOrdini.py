from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QTableWidgetItem
import time

import home.view.VistaHome
from listaordini.controller.ControllerListaOrdini import ControllerListaOrdini
from listaordini.view.VistaInserisciOrdine import VistaInserisciOrdine
from ordine.controller.ControllerOrdine import ControllerOrdine
from ordine.view.VistaOrdine import VistaOrdine
from listaordini.view.VistaInserisciOrdine import VistaInserisciOrdine

class VistaListaOrdini(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)

        self.controller= ControllerListaOrdini()
        ###############################
        self.in_arrivo = False
        self.in_negozio = False
        self.lista_ordini = self.controller.get_lista_ordini()
        #self.lista_dinamica = self.controller.get_lista_dinamica()
        self.lista_dinamica = self.lista_ordini[:]
        #############################

        self.setObjectName("Form")
        self.resize(1121, 576)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_apri = QtWidgets.QPushButton(self)
        self.pushButton_apri.setObjectName("pushButton_apri")
        self.pushButton_apri.clicked.connect(self.show_ordine)
        self.verticalLayout_2.addWidget(self.pushButton_apri)
        self.pushButton_nuovo = QtWidgets.QPushButton(self)
        self.pushButton_nuovo.setObjectName("pushButton_nuovo")
        self.pushButton_nuovo.clicked.connect(self.show_inserici_ordine)
        self.verticalLayout_2.addWidget(self.pushButton_nuovo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.lineEdit_cerca = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_cerca.sizePolicy().hasHeightForWidth())
        self.lineEdit_cerca.setSizePolicy(sizePolicy)
        self.lineEdit_cerca.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_cerca.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_cerca.setFont(font)
        self.lineEdit_cerca.setClearButtonEnabled(False)
        self.lineEdit_cerca.setObjectName("lineEdit_cerca")
        self.lineEdit_cerca.setPlaceholderText("Cerca per codice")
        self.lineEdit_cerca.returnPressed.connect(self.filter_cerca)
        self.gridLayout.addWidget(self.lineEdit_cerca, 2, 6, 1, 1)
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 0))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        self.label_logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_logo, 1, 4, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 3, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.pushButton_indietro.clicked.connect(self.close)
        self.gridLayout.addWidget(self.pushButton_indietro, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 7, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)

        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 6)

        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.pushButton_stato1 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        self.pushButton_stato1.setFont(font)
        self.pushButton_stato1.setObjectName("pushButton_stato1")
        self.pushButton_stato1.clicked.connect(self.filter_in_arrivo)
        self.gridLayout_3.addWidget(self.pushButton_stato1, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 2, 1, 1)
        self.pushButton_stato2 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_stato2.setFont(font)
        self.pushButton_stato2.setObjectName("pushButton_stato2")
        self.pushButton_stato2.clicked.connect(self.filter_in_negozio)
        self.gridLayout_3.addWidget(self.pushButton_stato2, 0, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 4, 1, 1)
        self.pushButton_all = QtWidgets.QPushButton(self)
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_all.clicked.connect(self.filter_all)
        self.gridLayout_3.addWidget(self.pushButton_all, 0, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 1, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 7)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 5, 3, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        self.setWindowTitle("Area del personale")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_apri.setText(_translate("Form", "Apri"))
        self.pushButton_nuovo.setText(_translate("Form", "Nuovo"))
        self.pushButton_indietro.setText(_translate("Form", "<-  Indietro"))
        self.pushButton_stato1.setText(_translate("Form", "In arrivo"))
        self.pushButton_stato2.setText(_translate("Form", "In negozio"))
        self.pushButton_all.setText(_translate("Form", "All"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice fattura"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Codice fornitore"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stato"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Data arrivo prevista"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Data arrivo effettiva"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Calzature totali"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Importo totale"))

        row = 0
        self.tableWidget.setColumnCount(7)
        if self.in_arrivo or self.in_negozio:
            self.filter()
        self.tableWidget.setRowCount(len(self.lista_dinamica))
        for ordine in self.lista_dinamica:
            item = QTableWidgetItem(str(ordine.cod_fattura))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            item = QTableWidgetItem(str(ordine.cod_fornitore))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(ordine.stato))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(ordine.data_arrivo_prevista))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(ordine.data_arrivo_effettiva))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(ordine.calzature_totali)))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(ordine.importo_totale)+" €"))

            row = row + 1
        ###############################

    def show_ordine(self):
        if len(self.tableWidget.selectedIndexes()) > 0:
            selected = self.tableWidget.selectedIndexes()[0].row()
            ordine_selezionato = self.lista_dinamica[selected]
            self.vista_ordine = VistaOrdine(ordine_selezionato, self.controller.elimina_ordine_by_codice, self.retranslateUi, self.controller, self.lista_dinamica)
            self.vista_ordine.showMaximized()
            time.sleep(0.3)
            self.close()

    def show_inserici_ordine(self):
        self.vista_inserisci_ordine = VistaInserisciOrdine(self.controller, self.retranslateUi, self.lista_dinamica)
        self.vista_inserisci_ordine.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def filter_in_arrivo(self):
        self.in_arrivo = True
        self.in_negozio = False
        self.lista_ordini = self.controller.get_lista_ordini()
        self.lista_dinamica = self.lista_ordini[:]
        self.filter()
        self.retranslateUi()

    def filter_in_negozio(self):
        self.in_arrivo= False
        self.in_negozio= True
        self.lista_ordini = self.controller.get_lista_ordini()
        self.lista_dinamica = self.lista_ordini[:]
        self.filter()
        self.retranslateUi()

    def filter_all(self):
        self.in_arrivo = False
        self.in_negozio = False
        self.lista_ordini = self.controller.get_lista_ordini()
        self.lista_dinamica = self.lista_ordini[:]
        self.filter()
        self.retranslateUi()

    def filter_cerca(self):
        self.lista_ordini = self.controller.get_lista_ordini()
        self.lista_dinamica = self.lista_ordini[:]
        codice= self.lineEdit_cerca.text()
        codice.capitalize()
        elementi_da_rimuovere = []
        for ordine in self.lista_dinamica:
            if not (codice in str(ordine.cod_fattura)):
                elementi_da_rimuovere.append(ordine)
        for ordine in elementi_da_rimuovere:
            if ordine in self.lista_dinamica:
                self.lista_dinamica.remove(ordine)
        self.retranslateUi()

    def filter(self):
        elementi_da_rimuovere = []

        if self.in_arrivo:
            for ordine in self.lista_dinamica:
                if str(ordine.stato) != "In arrivo":
                    elementi_da_rimuovere.append(ordine)
            for ordine in elementi_da_rimuovere:
                if ordine in self.lista_dinamica:
                    self.lista_dinamica.remove(ordine)
            return

        if self.in_negozio:
            for ordine in self.lista_dinamica:
                if str(ordine.stato)!= "In negozio":
                    elementi_da_rimuovere.append(ordine)
            for ordine in elementi_da_rimuovere:
                if ordine in self.lista_dinamica:
                    self.lista_dinamica.remove(ordine)
            return
        else:
            self.lista_ordini= self.controller.get_lista_ordini()
            self.lista_dinamica= self.lista_ordini[:]
            return
