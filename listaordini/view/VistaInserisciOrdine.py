import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QApplication

from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from ordine.model.Ordine import Ordine


class VistaInserisciOrdine(QWidget):
    def __init__(self, controller_lista_ordini, controller_lista_prodotti, update_ui, lista_dinamica):
        super(VistaInserisciOrdine, self).__init__()

        self.controller_lista_ordini = controller_lista_ordini
        self.controller_lista_prodotti= controller_lista_prodotti
        self.update_ui = update_ui
        self.lista_dinamica_ordini= lista_dinamica # Lista contenente gli ordini

        # Lista: E' un sottoinsieme di lista_prodotti, le modifiche fatte su questa lista influenzeranno
        # lista_prodotti solo dopo aver chiamato inserisci_ordine ed aver quindi salvato.
        self.lista_prodotti_ordine= []

        # boolean che permette di eseguire due eventi diversi in caso di chiusura della finestra
        self.end1 = False

        ############################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''

        # Come prendere le dimensioni dello schermo
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.setObjectName("Form")
        self.resize(962, 780)
        self.setStyleSheet("background-color: white;")

        # Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 28, 0, 1, 7)
        self.pushButton_rimuovi = QtWidgets.QPushButton(self)
        self.pushButton_rimuovi.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_rimuovi.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_rimuovi.setObjectName("pushButton_rimuovi")
        self.pushButton_rimuovi.clicked.connect(self.rimuovi_prodotto)
        self.gridLayout.addWidget(self.pushButton_rimuovi, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 27, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_salva = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_salva.sizePolicy().hasHeightForWidth())
        
        self.pushButton_salva.setSizePolicy(sizePolicy)
        self.pushButton_salva.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_salva.setObjectName("pushButton_salva")
        self.pushButton_salva.clicked.connect(self.inserisci_ordine)
        self.horizontalLayout.addWidget(self.pushButton_salva)
        self.pushButton_salva.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_annulla = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_annulla.sizePolicy().hasHeightForWidth())
        self.pushButton_annulla.setSizePolicy(sizePolicy)
        self.pushButton_annulla.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.pushButton_annulla.clicked.connect(self.close)
        self.horizontalLayout.addWidget(self.pushButton_annulla)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 33, 0, 1, 7)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 5, 1, 1)
        self.pushButton_inserisci = QtWidgets.QPushButton(self)
        self.pushButton_inserisci.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_inserisci.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_inserisci.setObjectName("pushButton_inserisci")
        self.pushButton_inserisci.clicked.connect(self.show_inserisci_prodotto)
        self.gridLayout.addWidget(self.pushButton_inserisci, 1, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setMinimumSize(QtCore.QSize(710, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
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

        self.tableWidget.setColumnWidth(0, self.width/7.72)
        self.tableWidget.setColumnWidth(1, self.width/7.72)
        self.tableWidget.setColumnWidth(2, self.width/7.72)
        self.tableWidget.setColumnWidth(3, self.width/7.72)
        self.tableWidget.setColumnWidth(4, self.width/7.72)
        self.tableWidget.setColumnWidth(5, self.width/7.72)
        self.gridLayout.addWidget(self.tableWidget, 2, 2, 26, 5)
        self.label_cod_fattura = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cod_fattura.sizePolicy().hasHeightForWidth())
        self.label_cod_fattura.setSizePolicy(sizePolicy)
        self.label_cod_fattura.setMinimumSize(QtCore.QSize(200, 20))
        self.label_cod_fattura.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_cod_fattura.setObjectName("label_cod_fattura")
        self.gridLayout.addWidget(self.label_cod_fattura, 1, 0, 1, 1)
        self.lineEdit_cod_fattura = QtWidgets.QLineEdit(self)
        self.lineEdit_cod_fattura.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_cod_fattura.setObjectName("lineEdit_cod_fattura")
        self.gridLayout.addWidget(self.lineEdit_cod_fattura, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 3, 0, 1, 1)
        self.label_cod_fornitore = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cod_fornitore.sizePolicy().hasHeightForWidth())
        self.label_cod_fornitore.setSizePolicy(sizePolicy)
        self.label_cod_fornitore.setMinimumSize(QtCore.QSize(0, 20))
        self.label_cod_fornitore.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_cod_fornitore.setObjectName("label_cod_fornitore")
        self.gridLayout.addWidget(self.label_cod_fornitore, 4, 0, 1, 1)
        self.lineEdit_cod_fornitore = QtWidgets.QLineEdit(self)
        self.lineEdit_cod_fornitore.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_cod_fornitore.setObjectName("lineEdit_cod_fornitore")
        self.gridLayout.addWidget(self.lineEdit_cod_fornitore, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 6, 0, 1, 1)
        self.label_stagione = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stagione.sizePolicy().hasHeightForWidth())
        self.label_stagione.setSizePolicy(sizePolicy)
        self.label_stagione.setMinimumSize(QtCore.QSize(0, 20))
        self.label_stagione.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_stagione.setObjectName("label_stagione")
        self.gridLayout.addWidget(self.label_stagione, 7, 0, 1, 1)
        self.comboBox_stagione = QtWidgets.QComboBox(self)
        self.comboBox_stagione.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_stagione.setObjectName("comboBox_stagione")
        self.comboBox_stagione.addItem("")
        self.comboBox_stagione.addItem("")
        self.gridLayout.addWidget(self.comboBox_stagione, 8, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 9, 0, 1, 1)
        self.label_stato = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stato.sizePolicy().hasHeightForWidth())
        self.label_stato.setSizePolicy(sizePolicy)
        self.label_stato.setMinimumSize(QtCore.QSize(0, 20))
        self.label_stato.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_stato.setObjectName("label_stato")
        self.gridLayout.addWidget(self.label_stato, 10, 0, 1, 1)
        self.comboBox_stato = QtWidgets.QComboBox(self)
        self.comboBox_stato.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_stato.setObjectName("comboBox_stato")
        self.comboBox_stato.addItem("")
        self.comboBox_stato.addItem("")
        self.gridLayout.addWidget(self.comboBox_stato, 11, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem12, 12, 0, 1, 1)
        self.label_data_ordine = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_ordine.sizePolicy().hasHeightForWidth())
        self.label_data_ordine.setSizePolicy(sizePolicy)
        self.label_data_ordine.setMinimumSize(QtCore.QSize(0, 20))
        self.label_data_ordine.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_data_ordine.setObjectName("label_data_ordine")
        self.gridLayout.addWidget(self.label_data_ordine, 13, 0, 1, 1)
        self.dateEdit_ordine = QtWidgets.QDateEdit(self)
        self.dateEdit_ordine.setMaximumSize(QtCore.QSize(250, 16777215))
        self.dateEdit_ordine.setObjectName("dateEdit_ordine")
        self.gridLayout.addWidget(self.dateEdit_ordine, 14, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem13, 15, 0, 1, 1)
        self.label_data_arrivo_prevista = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_arrivo_prevista.sizePolicy().hasHeightForWidth())
        self.label_data_arrivo_prevista.setSizePolicy(sizePolicy)
        self.label_data_arrivo_prevista.setMinimumSize(QtCore.QSize(0, 20))
        self.label_data_arrivo_prevista.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_data_arrivo_prevista.setObjectName("label_data_arrivo_prevista")
        self.gridLayout.addWidget(self.label_data_arrivo_prevista, 16, 0, 1, 1)
        self.dateEdit_arrivo_prevista = QtWidgets.QDateEdit(self)
        self.dateEdit_arrivo_prevista.setMaximumSize(QtCore.QSize(250, 16777215))
        self.dateEdit_arrivo_prevista.setObjectName("dateEdit_arrivo_prevista")
        self.gridLayout.addWidget(self.dateEdit_arrivo_prevista, 17, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem14, 18, 0, 1, 1)
        self.label_data_arrivo_effettiva = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_arrivo_effettiva.sizePolicy().hasHeightForWidth())
        self.label_data_arrivo_effettiva.setSizePolicy(sizePolicy)
        self.label_data_arrivo_effettiva.setMinimumSize(QtCore.QSize(0, 20))
        self.label_data_arrivo_effettiva.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_data_arrivo_effettiva.setObjectName("label_data_arrivo_effettiva")
        self.gridLayout.addWidget(self.label_data_arrivo_effettiva, 19, 0, 1, 1)
        self.dateEdit_arrivo_effettiva = QtWidgets.QDateEdit(self)
        self.dateEdit_arrivo_effettiva.setMaximumSize(QtCore.QSize(250, 16777215))
        self.dateEdit_arrivo_effettiva.setObjectName("dateEdit_arrivo_effettiva")
        self.gridLayout.addWidget(self.dateEdit_arrivo_effettiva, 20, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem15, 21, 0, 1, 1)
        self.label_importo_totale = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_importo_totale.sizePolicy().hasHeightForWidth())
        self.label_importo_totale.setSizePolicy(sizePolicy)
        self.label_importo_totale.setMinimumSize(QtCore.QSize(0, 20))
        self.label_importo_totale.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_importo_totale.setObjectName("label_importo_totale")
        self.gridLayout.addWidget(self.label_importo_totale, 22, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem16, 24, 0, 1, 1)
        self.label_calzature_totali = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_calzature_totali.sizePolicy().hasHeightForWidth())
        self.label_calzature_totali.setSizePolicy(sizePolicy)
        self.label_calzature_totali.setMinimumSize(QtCore.QSize(0, 20))
        self.label_calzature_totali.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_calzature_totali.setObjectName("label_calzature_totali")
        self.gridLayout.addWidget(self.label_calzature_totali, 25, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Inserisci ordine")

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #imposto il testo degli oggetti dell'interfaccia
        self.label_10.setText(_translate("Form", "Lista prodotti ordine:"))
        self.pushButton_rimuovi.setText(_translate("Form", "Rimuovi prodotto"))
        self.pushButton_salva.setText(_translate("Form", "Salva"))
        self.pushButton_annulla.setText(_translate("Form", "Annulla"))
        self.pushButton_inserisci.setText(_translate("Form", "Inserisci prodotto"))

        #imposto le colonne della tabella
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

        # inserisco gli elementi in tabella
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

        # I campi importo_totale e calzature_totali dipendono dai campi quantita e prezzo di acquisto in lista_prodotti_ordine
        importo_totale = 0
        calzature_totali = 0
        for prodotto in self.lista_prodotti_ordine:
            importo_totale = importo_totale + int(prodotto.prezzo_acquisto)
            calzature_totali = calzature_totali + int(prodotto.quantita)

        self.label_cod_fattura.setText(_translate("Form", "Codice fattura"))
        self.label_cod_fornitore.setText(_translate("Form", "Codice fornitore"))
        self.label_stagione.setText(_translate("Form", "Stagione"))
        self.comboBox_stagione.setItemText(0, _translate("Form", "Primavera / Estate"))
        self.comboBox_stagione.setItemText(1, _translate("Form", "Autunno / Inverno"))
        self.label_stato.setText(_translate("Form", "Stato"))
        self.comboBox_stato.setItemText(0, _translate("Form", "In arrivo"))
        self.comboBox_stato.setItemText(1, _translate("Form", "In negozio"))
        self.label_data_ordine.setText(_translate("Form", "Data ordine"))
        self.label_data_arrivo_prevista.setText(_translate("Form", "Data arrivo prevista"))
        self.label_data_arrivo_effettiva.setText(_translate("Form", "Data arrivo effettiva"))
        self.label_importo_totale.setText(_translate("Form", "Importo totale: {}".format(str(importo_totale))))
        self.label_calzature_totali.setText(_translate("Form", "Calzature totali: {}".format(str(calzature_totali))))
        #######################################

    def show_inserisci_prodotto(self):
        inserimento_da_ordine= True

        # in VistaInserisciProdotto alcuni dati per istanziare il prodotto vengono presi dall'ordine in questione (perchè se chiamiamo vistaInserisciprodotto da VistaOrdine ci serve che sia così)
        # Per questo motivo gli passo un ordine fittizio, tanto i suoi attributi verranno sovrascritti successivamente!
        ordine_fittizio= Ordine(0000, 0000, None, None, None, None, None, None, None)

        self.vista_inserisci_prodotto= VistaInserisciProdotto(self.controller_lista_prodotti, self.retranslateUi, inserimento_da_ordine, self.lista_prodotti_ordine, None, ordine_fittizio)
        self.vista_inserisci_prodotto.show()

    def rimuovi_prodotto(self):
        if len(self.tableWidget.selectedIndexes()) > 0:
            selected = self.tableWidget.selectedIndexes()[0].row()
            prodotto_selezionato = self.lista_prodotti_ordine[selected]
            self.lista_prodotti_ordine.remove(prodotto_selezionato)
            self.retranslateUi()

    def inserisci_ordine(self):
        self.end1= True
        # Controllo inserimento di tutti i campi
        if self.lineEdit_cod_fornitore.text() == "" or self.lineEdit_cod_fattura.text() == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return
        # Controllo inserimento di almeno un prodotto
        if len(self.lista_prodotti_ordine)==0:
            QMessageBox.critical(self, 'Errore', "L'ordine non contiene alcun prodotto.",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        # Controllo se l'ordine che si vuole inserire è già presente in lista.
        for ordine in self.lista_dinamica_ordini:
            if str(ordine.cod_fattura) == self.lineEdit_cod_fattura.text() and str(ordine.cod_fornitore)== self.lineEdit_cod_fornitore.text():
                reply = QMessageBox.question(self, 'Attenzione', "L'ordine è già presente in lista, sovrasciverlo?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()
                    for prodotto in self.lista_prodotti_ordine:
                        if prodotto in lista_prodotti:
                            lista_prodotti.remove(prodotto)

                    self.controller_lista_prodotti.save_data_specialized(lista_prodotti)
                    self.controller_lista_prodotti.refresh_data()
                    self.controller_lista_ordini.elimina_ordine_by_codice(ordine.cod_fattura, self.lista_dinamica_ordini)
                    self.update_ui()
                    self.close()

                else:
                    return

        # prendo i dati inseriti nelle lineEdit
        cod_fattura = self.lineEdit_cod_fattura.text()
        cod_fornitore = self.lineEdit_cod_fornitore.text()
        if str(self.comboBox_stagione.currentText()) == "Primavera / Estate":
            stagione= "P/E"
        else:
            stagione= "A/I"

        stato = self.comboBox_stato.currentText()

        gg = str(self.dateEdit_ordine.date().day())
        mm = str(self.dateEdit_ordine.date().month())
        aaaa = str(self.dateEdit_ordine.date().year())
        # ho bisogno di due formattazioni diverse, una per i prodotti e una per gli ordini
        data_ordine1 = aaaa + "-" + mm + "-" + gg
        data_ordine2= gg + "/" + mm + "/" + aaaa

        gg_p = str(self.dateEdit_arrivo_prevista.date().day())
        mm_p = str(self.dateEdit_arrivo_prevista.date().month())
        aaaa_p = str(self.dateEdit_arrivo_prevista.date().year())
        data_arrivo_prevista = aaaa_p + "-" + mm_p + "-" + gg_p

        gg_e = str(self.dateEdit_arrivo_effettiva.date().day())
        mm_e = str(self.dateEdit_arrivo_effettiva.date().month())
        aaaa_e = str(self.dateEdit_arrivo_effettiva.date().year())
        data_arrivo_effettiva = aaaa_e + "-" + mm_e + "-" + gg_e

        # I campi importo_totale e calzature_totali dipendono dai campi quantita e prezzo di acquisto in lista_prodotti_ordine
        importo_totale = 0
        calzature_totali = 0

        for prodotto in self.lista_prodotti_ordine:
            importo_totale= importo_totale + int(prodotto.prezzo_acquisto)
            calzature_totali= calzature_totali + int(prodotto.quantita)

        # istanzio l'ordine
        ordine= Ordine(cod_fattura, cod_fornitore, stagione, stato,
                      data_ordine1, data_arrivo_prevista, data_arrivo_effettiva,
                      importo_totale, calzature_totali)

        self.controller_lista_ordini.inserisci_ordine(ordine)
        self.lista_dinamica_ordini.append(ordine)

        # sovrascrivo i campi dei prodotti con quelli dell'ordine (parametri globali)
        for prodotto in self.lista_prodotti_ordine:
            prodotto.cod_fattura= cod_fattura
            prodotto.cod_fornitore= cod_fornitore
            prodotto.stagione= stagione
            prodotto.stato= stato
            prodotto.data_ordine= data_ordine2

        lista_prodotti= self.controller_lista_prodotti.get_lista_prodotti()

        # elimino tutti gli eventuali prodotti con il cod_fattura in questione e inserisco quelli in lista_prodotti_ordine
        prodotti_da_eliminare=[]
        for prodotto in lista_prodotti:
            if prodotto.cod_fattura == cod_fattura:
                prodotti_da_eliminare.append(prodotto)
        for prodotto in prodotti_da_eliminare:
            lista_prodotti.remove(prodotto)

        for prodotto in self.lista_prodotti_ordine:
            lista_prodotti.append(prodotto)

        self.update_ui()

        self.close()
        self.end1=False

    def closeEvent(self, event):
        if self.end1==False:
            reply = QMessageBox.question(self, 'Annullare?',
                                         'Sicuro di voler annullare? Tutte le modifiche andranno perse.',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if not type(event) == bool:
                    event.accept()
                else:
                    sys.exit()
            else:
                if not type(event) == bool:
                    event.ignore()

