from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QTableWidgetItem

from listaprodotti.view.VistaInserisciProdotto import VistaInserisciProdotto
from ordine.model.Ordine import Ordine

"""
DA FARE
# implementare i controlli di correttezza dell'inserimento (crasha)
# fare interfaccia
"""


class VistaInserisciOrdine(QWidget):
    def __init__(self, controller, update_ui, lista_dinamica):
        super(VistaInserisciOrdine, self).__init__()
        self.controller = controller
        self.update_ui = update_ui
        self.lista_dinamica= lista_dinamica

        #######################################
        self.setObjectName("Form")
        self.resize(962, 780)
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
        self.pushButton_apri = QtWidgets.QPushButton(self)
        self.pushButton_apri.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_apri.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_apri.setObjectName("pushButton_apri")
        #self.pushButton_apri.clicked.connect()
        self.gridLayout.addWidget(self.pushButton_apri, 1, 4, 1, 1)
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
        self.horizontalLayout.addWidget(self.pushButton_annulla)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 33, 0, 1, 7)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 5, 1, 1)
        self.pushButton_nuovo = QtWidgets.QPushButton(self)
        self.pushButton_nuovo.setMinimumSize(QtCore.QSize(130, 0))
        self.pushButton_nuovo.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_nuovo.setObjectName("pushButton_nuovo")
        self.pushButton_nuovo.clicked.connect(self.inserisci_prodotto)
        self.gridLayout.addWidget(self.pushButton_nuovo, 1, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setMinimumSize(QtCore.QSize(710, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
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
        self.lineEdit_importo_totale = QtWidgets.QLineEdit(self)
        self.lineEdit_importo_totale.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_importo_totale.setObjectName("lineEdit_importo_totale")
        self.gridLayout.addWidget(self.lineEdit_importo_totale, 23, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem16, 24, 0, 1, 1)
        self.label_calzature_totalli = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_calzature_totalli.sizePolicy().hasHeightForWidth())
        self.label_calzature_totalli.setSizePolicy(sizePolicy)
        self.label_calzature_totalli.setMinimumSize(QtCore.QSize(0, 20))
        self.label_calzature_totalli.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_calzature_totalli.setObjectName("label_calzature_totalli")
        self.gridLayout.addWidget(self.label_calzature_totalli, 25, 0, 1, 1)
        self.lineEdit_calzature_totali = QtWidgets.QLineEdit(self)
        self.lineEdit_calzature_totali.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_calzature_totali.setObjectName("lineEdit_calzature_totali")
        self.gridLayout.addWidget(self.lineEdit_calzature_totali, 26, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Inserisci ordine")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_10.setText(_translate("Form", "Lista prodotti ordine:"))
        self.pushButton_apri.setText(_translate("Form", "Apri"))
        self.pushButton_salva.setText(_translate("Form", "Salva"))
        self.pushButton_annulla.setText(_translate("Form", "Annulla"))
        self.pushButton_nuovo.setText(_translate("Form", "Inserisci prodotto"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice prodotto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Marca"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Genere"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Taglia"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Prezzo d\'acquisto"))

        row = 0
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(self.lista_dinamica))
        for prodotto in self.lista_dinamica:
            item = QTableWidgetItem(str(utente.cod_utente))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(utente.nome))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(utente.cognome))
            if utente.ruolo == "A":
                ruolo = "Amministratore"
            else:
                ruolo = "Dipendente"

            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(ruolo))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(utente.telefono)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(utente.data_scadenza_contratto))

            row = row + 1

        self.label_cod_fattura.setText(_translate("Form", "Codice fattura"))
        #self.lineEdit_cod_fattura.setText(_translate("Form", self.controller.get_cod_fattura()))
        self.label_cod_fornitore.setText(_translate("Form", "Codice fornitore"))
        #self.lineEdit_cod_fornitore.setText(_translate("Form", self.controller.get_cod_fornitore()))
        self.label_stagione.setText(_translate("Form", "Stagione"))
        self.comboBox_stagione.setItemText(0, _translate("Form", "Primaverile/Estiva"))
        self.label_stato.setText(_translate("Form", "Stato"))
        self.comboBox_stato.setItemText(0, _translate("Form", "In arrivo"))
        self.comboBox_stato.setItemText(1, _translate("Form", "In negozio"))
        self.label_data_ordine.setText(_translate("Form", "Data ordine"))
        self.label_data_arrivo_prevista.setText(_translate("Form", "Data arrivo prevista"))
        self.label_data_arrivo_effettiva.setText(_translate("Form", "Data arrivo effettiva"))
        self.label_importo_totale.setText(_translate("Form", "Importo totale"))
        #self.lineEdit_importo_totale.setText(_translate("Form", "c"))
        self.label_calzature_totalli.setText(_translate("Form", "Calzature totali"))
        #self.lineEdit_calzature_totali.setText(_translate("Form", "d"))
        #######################################
    #     self.info = {}
    #
    #     self.v_layout = QVBoxLayout()
    #
    #     self.get_form_entry("cod_fattura", "Codice fattura")
    #     self.get_form_entry("cod_fornitore", "Codice fornitore")
    #     self.get_form_entry("stagione", "Stagione")
    #     self.get_form_entry("stato", "Stato")
    #     self.get_form_entry("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
    #     self.get_form_entry("data_arrivo_prevista", "data arrivo prevista")
    #     self.get_form_entry("data_arrivo_effettiva", "data arrivo effettiva")
    #     self.get_form_entry("importo_totale", "importo totale")
    #     self.get_form_entry("calzature_totali", "calzature totali")
    #
    #
    #
    #     self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    #
    #     btn_ok = QPushButton("OK")
    #     btn_ok.clicked.connect(self.inserisci_ordine)
    #     self.v_layout.addWidget(btn_ok)
    #
    #     self.setLayout(self.v_layout)
    #     self.setWindowTitle("Inserisci ordine")
    #
    # def get_form_entry(self, nome, tipo):
    #     self.v_layout.addWidget(QLabel(tipo))
    #     current_text_edit = QLineEdit(self)
    #     self.info[nome] = current_text_edit
    #     self.v_layout.addWidget(current_text_edit)

    def inserisci_ordine(self):
        cod_fattura = self.lineEdit_cod_fattura.text()
        cod_fornitore = self.lineEdit_cod_fornitore.text()
        if str(self.comboBox_stagione.currentText()) == "Primaverile/Estiva":
            stagione= "P/E"
        else:
            stagione= "A/I"

        stato = self.comboBox_stato.currentText()

        gg = str(self.dateEdit_ordine.date().day())
        mm = str(self.dateEdit_ordine.date().month())
        aaaa = str(self.dateEdit_ordine.date().year())
        data_ordine = gg + "/" + mm + "/" + aaaa

        gg_p = str(self.dateEdit_arrivo_prevista.date().day())
        mm_p = str(self.dateEdit_arrivo_prevista.date().month())
        aaaa_p = str(self.dateEdit_arrivo_prevista.date().year())
        data_arrivo_prevista = gg_p + "/" + mm_p + "/" + aaaa_p

        gg_e = str(self.dateEdit_arrivo_effettiva.date().day())
        mm_e = str(self.dateEdit_arrivo_effettiva.date().month())
        aaaa_e = str(self.dateEdit_arrivo_effettiva.date().year())
        data_arrivo_effettiva = gg_e + "/" + mm_e + "/" + aaaa_e

        importo_totale = self.lineEdit_importo_totale.text()
        calzature_totali = self.lineEdit_calzature_totali.text()

        # for value in self.info.values():
        #     if value.text() == "":
        #         QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
        #                              QMessageBox.Ok, QMessageBox.Ok)
        #         return
            # I CONTROLLI DANNO PROBLEMI DI CRASH
            # if taglia > 50:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci una taglia valida',
            #                          QMessageBox.Ok, QMessageBox.Ok)
            #    return
            # if sconto > 100 or sconto_consigliato > 100:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci uno sconto valido',
            #                         QMessageBox.Ok, QMessageBox.Ok)
            #    return
            # if sconto.isnumeric() or sconto_consigliato.isnumeric():
            #    return
            # else:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci uno sconto numerico',
            #                         QMessageBox.Ok, QMessageBox.Ok)
            #    return

        ordine= Ordine(cod_fattura, cod_fornitore, stagione, stato,
                      data_ordine, data_arrivo_prevista, data_arrivo_effettiva,
                      importo_totale, calzature_totali)

        self.controller.inserisci_ordine(ordine)
        self.lista_dinamica.append(ordine)
        self.update_ui()
        self.close()

    def inserisci_prodotto(self):
        var= True
        vista_inserisci_prodotto= VistaInserisciProdotto()
        vista_inserisci_prodotto.showMaximized()
