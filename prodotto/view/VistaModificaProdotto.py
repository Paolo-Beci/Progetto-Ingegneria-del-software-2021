from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

"""
    MODIFICA DEI PARAMETRI DEL PRODOTTO
    prende in input un prodotto e ne permette di modificare i campi (visualizzandone i vecchi?)
"""


class VistaModificaProdotto(QWidget):
    def __init__(self, controller, update_ui, parent=None):
        super(VistaModificaProdotto, self).__init__(parent)
        self.controller = controller
        self.update_ui = update_ui
        self.setObjectName("MainWindow")
        self.resize(1071, 715)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_marca = QtWidgets.QLabel(self.centralwidget)
        self.label_marca.setObjectName("label_marca")
        self.gridLayout.addWidget(self.label_marca, 7, 3, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        # BOTTONI FONDO FINESTRA
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        # annulla
        self.pushButton_annulla = QtWidgets.QPushButton(self.widget)
        self.pushButton_annulla.setObjectName("pushButton_annulla")
        self.horizontalLayout.addWidget(self.pushButton_annulla)
        # SALVA
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_salva = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_salva.setFont(font)
        self.pushButton_salva.setObjectName("pushButton_salva")
        self.horizontalLayout.addWidget(self.pushButton_salva)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        # GRID CENTRALE
        self.gridLayout.addWidget(self.widget, 25, 1, 1, 5)
        # SCONTO
        self.label_sconto = QtWidgets.QLabel(self.centralwidget)
        self.label_sconto.setObjectName("label_sconto")
        self.gridLayout.addWidget(self.label_sconto, 22, 5, 1, 1)

        self.lineEdit_sconto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sconto.setObjectName("lineEdit_sconto")
        self.gridLayout.addWidget(self.lineEdit_sconto, 23, 5, 1, 1)
        # QUANTITA
        self.label_quantita = QtWidgets.QLabel(self.centralwidget)
        self.label_quantita.setObjectName("label_quantita")
        self.gridLayout.addWidget(self.label_quantita, 16, 5, 1, 1)

        self.lineEdit_quantita = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_quantita.setObjectName("lineEdit_quantita")
        self.gridLayout.addWidget(self.lineEdit_quantita, 17, 5, 1, 1)
        # TAGLIA
        self.label_taglia = QtWidgets.QLabel(self.centralwidget)
        self.label_taglia.setObjectName("label_taglia")
        self.gridLayout.addWidget(self.label_taglia, 16, 3, 1, 1)

        self.comboBox_taglia = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_taglia.setObjectName("comboBox_taglia")
        self.gridLayout.addWidget(self.comboBox_taglia, 17, 3, 1, 1)
        # GENERE
        self.label_genere = QtWidgets.QLabel(self.centralwidget)
        self.label_genere.setObjectName("label_genere")
        self.gridLayout.addWidget(self.label_genere, 12, 3, 1, 1)

        self.comboBox_genere = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_genere.setObjectName("comboBox_genere")
        self.gridLayout.addWidget(self.comboBox_genere, 14, 3, 1, 1)
        # DATA ORDINE
        self.label_data_ordine = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_data_ordine.setFont(font)     #    <-----------------------
        self.label_data_ordine.setObjectName("label_data_ordine")
        self.gridLayout.addWidget(self.label_data_ordine, 0, 5, 1, 1)

        self.dateEdit_data_ordine = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_data_ordine.setObjectName("dateEdit_data_ordine")
        self.gridLayout.addWidget(self.dateEdit_data_ordine, 1, 5, 1, 1)
        # CODICE FORNITORE
        self.label_cod_fornitore = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cod_fornitore.setFont(font)
        self.label_cod_fornitore.setObjectName("label_cod_fornitore")
        self.gridLayout.addWidget(self.label_cod_fornitore, 0, 3, 1, 1)

        self.lineEdit_cod_fornitore = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_fornitore.setObjectName("lineEdit_cod_fornitore")
        self.gridLayout.addWidget(self.lineEdit_cod_fornitore, 1, 3, 1, 1)
        # CODICE FATTURA
        self.lineEdit_cod_fattura = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_fattura.setObjectName("lineEdit_cod_fattura")
        self.gridLayout.addWidget(self.lineEdit_cod_fattura, 1, 1, 1, 1)

        self.label_cod_fattura = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_cod_fattura.setFont(font)
        self.label_cod_fattura.setTextFormat(QtCore.Qt.AutoText)
        self.label_cod_fattura.setObjectName("label_cod_fattura")
        self.gridLayout.addWidget(self.label_cod_fattura, 0, 1, 1, 1)
        # CODICE PRODOTTO
        self.label_cod_prodotto = QtWidgets.QLabel(self.centralwidget)
        self.label_cod_prodotto.setObjectName("label_cod_prodotto")
        self.gridLayout.addWidget(self.label_cod_prodotto, 7, 1, 1, 1)

        self.lineEdit_cod_prodotto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cod_prodotto.setObjectName("lineEdit_cod_prodotto")
        self.gridLayout.addWidget(self.lineEdit_cod_prodotto, 8, 1, 1, 1)
        # COLORE
        self.label_colore = QtWidgets.QLabel(self.centralwidget)
        self.label_colore.setObjectName("label_colore")
        self.gridLayout.addWidget(self.label_colore, 16, 1, 1, 1)

        self.lineEdit_colore = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_colore.setObjectName("lineEdit_colore")
        self.gridLayout.addWidget(self.lineEdit_colore, 17, 1, 1, 1)
        # MATERIALE
        self.label_materiale = QtWidgets.QLabel(self.centralwidget)
        self.label_materiale.setObjectName("label_materiale")
        self.gridLayout.addWidget(self.label_materiale, 12, 5, 1, 1)

        self.lineEdit_materiale = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_materiale.setObjectName("lineEdit_materiale")
        self.gridLayout.addWidget(self.lineEdit_materiale, 14, 5, 1, 1)
        # TIPO
        self.label_tipo = QtWidgets.QLabel(self.centralwidget)
        self.label_tipo.setObjectName("label_tipo")
        self.gridLayout.addWidget(self.label_tipo, 12, 1, 1, 1)

        self.comboBox_tipo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tipo.setCurrentText("")
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.gridLayout.addWidget(self.comboBox_tipo, 14, 1, 1, 1)
        # PREZZO ACQUISTO
        self.lineEdit_prezzo_acquisto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prezzo_acquisto.setObjectName("lineEdit_prezzo_acquisto")
        self.gridLayout.addWidget(self.lineEdit_prezzo_acquisto, 20, 1, 1, 1)

        self.label_prezzo_acquisto = QtWidgets.QLabel(self.centralwidget)
        self.label_prezzo_acquisto.setObjectName("label_prezzo_acquisto")
        self.gridLayout.addWidget(self.label_prezzo_acquisto, 19, 1, 1, 1)
        # NOME
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 7, 5, 1, 1)

        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 8, 5, 1, 1)
        # STATO
        self.comboBox_stato = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stato.setObjectName("comboBox_stato")
        self.gridLayout.addWidget(self.comboBox_stato, 23, 1, 1, 1)

        self.label_stato = QtWidgets.QLabel(self.centralwidget)
        self.label_stato.setObjectName("label_stato")
        self.gridLayout.addWidget(self.label_stato, 22, 1, 1, 1)
        # SCONTO CONSIGLIATO
        self.label_sconto_consigliato = QtWidgets.QLabel(self.centralwidget)
        self.label_sconto_consigliato.setObjectName("label_sconto_consigliato")
        self.gridLayout.addWidget(self.label_sconto_consigliato, 22, 3, 1, 1)

        self.lineEdit_sconto_consigliato = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sconto_consigliato.setObjectName("lineEdit_sconto_consigliato")
        self.gridLayout.addWidget(self.lineEdit_sconto_consigliato, 23, 3, 1, 1)
        # STAGIONE
        self.label_stagione = QtWidgets.QLabel(self.centralwidget)
        self.label_stagione.setObjectName("label_stagione")
        self.gridLayout.addWidget(self.label_stagione, 19, 5, 1, 1)

        self.comboBox_stagione = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stagione.setObjectName("comboBox_stagione")
        self.gridLayout.addWidget(self.comboBox_stagione, 20, 5, 1, 1)
        # MARCA
        self.lineEdit_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_marca.setObjectName("lineEdit_marca")
        self.gridLayout.addWidget(self.lineEdit_marca, 8, 3, 1, 1)
        # PREZZO VENDITA
        self.label_prezzo_vendita = QtWidgets.QLabel(self.centralwidget)
        self.label_prezzo_vendita.setObjectName("label_prezzo_vendita")
        self.gridLayout.addWidget(self.label_prezzo_vendita, 19, 3, 1, 1)

        self.lineEdit_prezzo_vendita = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prezzo_vendita.setObjectName("lineEdit_prezzo_vendita")
        self.gridLayout.addWidget(self.lineEdit_prezzo_vendita, 20, 3, 1, 1)

        # SPACER
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 24, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 9, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 15, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 21, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 18, 1, 1, 1)
        #self.setCentralWidget(self.centralwidget)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1071, 715))  # settata in finestra

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modifica prodotto"))
        self.label_marca.setText(_translate("MainWindow", "Marca"))
        self.lineEdit_marca.setText(_translate("Form", str(self.controller.get_marca())))
        self.label_sconto.setText(_translate("MainWindow", "Sconto"))
        self.lineEdit_sconto.setText(_translate("Form", str(self.controller.get_sconto())))
        self.label_taglia.setText(_translate("MainWindow", "Taglia"))
        #self.lineEdit_taglia.setText(_translate("Form", str(self.controller.get_taglia())))
        self.label_genere.setText(_translate("MainWindow", "Genere"))
        #self.lineEdit_genere.setText(_translate("Form", self.controller.get_genere()))
        self.label_data_ordine.setText(_translate("MainWindow", "Data ordine"))
        #self.lineEdit_data_ordine.setText(_translate("Form", self.controller.get_data_ordine()))
        self.label_cod_fornitore.setText(_translate("MainWindow", "Codice fornitore"))
        self.lineEdit_cod_fornitore.setText(_translate("Form", str(self.controller.get_cod_fornitore())))
        self.label_cod_prodotto.setText(_translate("MainWindow", "Codice prodotto"))
        self.lineEdit_cod_prodotto.setText(_translate("Form", str(self.controller.get_cod_prodotto())))
        self.label_colore.setText(_translate("MainWindow", "Colore"))
        self.lineEdit_colore.setText(_translate("Form", str(self.controller.get_colore())))
        self.label_materiale.setText(_translate("MainWindow", "Materiale"))
        self.lineEdit_materiale.setText(_translate("Form", str(self.controller.get_materiale())))
        self.label_tipo.setText(_translate("MainWindow", "Tipo"))
        #self.lineEdit_tipo.setText(_translate("Form", self.controller.get_tipo()))
        self.label_prezzo_acquisto.setText(_translate("MainWindow", "Prezzo di acquisto"))
        self.lineEdit_prezzo_acquisto.setText(_translate("Form", str(self.controller.get_prezzo_acquisto())))
        self.label_nome.setText(_translate("MainWindow", "Nome"))
        self.lineEdit_nome.setText(_translate("Form",str(self.controller.get_nome())))
        self.label_sconto_consigliato.setText(_translate("MainWindow", "Sconto consigliato"))
        self.lineEdit_sconto_consigliato.setText(_translate("Form", str(self.controller.get_sconto_consigliato())))
        self.label_cod_fattura.setText(_translate("MainWindow", "Codice fattura"))
        self.lineEdit_cod_fattura.setText(_translate("Form", str(self.controller.get_cod_fattura())))
        self.label_prezzo_vendita.setText(_translate("MainWindow", "Prezzo di vendita"))
        self.lineEdit_prezzo_vendita.setText(_translate("Form", str(self.controller.get_prezzo_vendita())))
        self.label_stagione.setText(_translate("MainWindow", "Stagione"))
        #self.lineEdit_stagione.setText(_translate("Form", self.controller.get_stagione()))
        self.label_quantita.setText(_translate("MainWindow", "Quantità"))
        self.lineEdit_quantita.setText(_translate("Form", str(self.controller.get_quantita())))
        self.label_stato.setText(_translate("MainWindow", "Stato"))
        #self.lineEdit_stato.setText(_translate("Form", self.controller.get_stato()))
        self.pushButton_annulla.setText(_translate("MainWindow", "Annulla"))
        self.pushButton_salva.setText(_translate("MainWindow", "Salva"))

    """
            Eventi trigger click dei bottoni
    """

    def salva_modifiche_click(self):
        # prendo il testo che l'utente inserisce in ciascuna lineEdit
        partita_iva = self.lineEdit_9.text()
        indirizzo = self.lineEdit_10.text()
        telefono = self.lineEdit_11.text()
        email = self.lineEdit_12.text()
        data_affiliazione = self.lineEdit_13.text()
        rappresentante = self.lineEdit_14.text()
        nome = self.lineEdit_15.text()
        codice = self.lineEdit_16.text()
        stato = str(self.comboBox_2.currentText())

        # modifico gli attributi del fornitore in base al testo inserito
        self.controller.set_nome_fornitore(nome)
        self.controller.set_telefono(telefono)
        self.controller.set_indirizzo(indirizzo)
        self.controller.set_partita_iva(partita_iva)
        self.controller.set_email(email)
        self.controller.set_rappresentante(rappresentante)
        self.controller.set_data_affiliazione(data_affiliazione)
        self.controller.set_cod_fornitore(codice)
        self.controller.set_stato(stato)

        # campo1 = self.lineEdit_9.text()
        # self.controller.set_nome_fornitore(campo1)
        self.update_ui()
        self.close()

    def annulla_click(self):
        self.close()
