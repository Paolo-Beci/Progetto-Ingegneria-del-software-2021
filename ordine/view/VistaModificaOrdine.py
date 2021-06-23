import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QMessageBox


class VistaModificaOrdine(QWidget):
    def __init__(self, ordine, controller, update_ui, lista_prodotti_ordine, lista_dinamica_ordini, parent=None):
        super(VistaModificaOrdine, self).__init__(parent)
        self.controller = controller
        self.update_ui_ordine = update_ui
        self.ordine_selezionato = ordine
        self.lista_prodotti_ordine = lista_prodotti_ordine
        self.lista_prodotti_ordine_dinamica = self.lista_prodotti_ordine[:]
        self.lista_dinamica_ordini= lista_dinamica_ordini

        self.new_lista_fornitori = self.lista_dinamica_ordini[:]
        # affinche non ci siano problemi con il controllo in save_data() (controllo sull'inserimento di un ordine con stesso codice)
        # ho bisogno di una lista che non contenga il fornitore che sto modificando
        self.new_lista_fornitori.remove(self.ordine_selezionato)

        # boolean che permette di eseguire due eventi diversi in casi di chiusura
        self.end1 = False

        ############################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        # Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.resize(600, 400)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 5, 1, 1)
        self.pushButton.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        self.pushButton_2.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.label_7 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 5, 1, 1)
        self.dateEdit_3 = QtWidgets.QDateEdit(self)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.gridLayout.addWidget(self.dateEdit_3, 8, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 4, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 5, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 11, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Modifica ordine")

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.clicked.connect(self.save_data_click)
        self.pushButton_2.clicked.connect(self.close)
        self.label.setText(_translate("MainWindow", "Codice fornitore:"))
        self.pushButton.setText(_translate("MainWindow", "Salva modifiche"))
        self.pushButton_2.setText(_translate("MainWindow", "Annulla"))
        self.label_7.setText(_translate("MainWindow", "Data arrivo effettiva"))
        self.label_5.setText(_translate("MainWindow", "Data ordine:"))
        self.label_6.setText(_translate("MainWindow", "Data arrivo prevista:"))
        self.label_3.setText(_translate("MainWindow", "Stagione:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "In negozio"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "In arrivo"))
        self.label_4.setText(_translate("MainWindow", "Stato:"))
        self.label_2.setText(_translate("MainWindow", "Codice fattura:"))

        self.comboBox.setItemText(0, _translate("MainWindow", "Primavera / Estate"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Autunno / Inverno"))
        if self.controller.get_stagione() == "P/E":
            index = self.comboBox.findText("Primavera / Estate", QtCore.Qt.MatchFixedString)
        else:
            index = self.comboBox.findText("Autunno / Inverno", QtCore.Qt.MatchFixedString)
        self.comboBox.setCurrentIndex(index)

        if self.controller.get_stato() == "In arrivo":
            index = self.comboBox_2.findText("In arrivo", QtCore.Qt.MatchFixedString)
        else:
            index = self.comboBox_2.findText("In negozio", QtCore.Qt.MatchFixedString)
        self.comboBox_2.setCurrentIndex(index)

        data_ordine = self.controller.get_data_ordine()
        data_ordine_split = data_ordine.split("-")
        self.dateEdit.setDate(QDate(int(data_ordine_split[0]), int(data_ordine_split[1]), int(data_ordine_split[2])))

        data_arrivo_prevista = self.controller.get_data_arrivo_prevista()
        data_arrivo_prevista_split = data_arrivo_prevista.split("-")
        self.dateEdit_2.setDate(QDate(int(data_arrivo_prevista_split[0]), int(data_arrivo_prevista_split[1]),
                                int(data_arrivo_prevista_split[2])))

        data_arrivo_effettiva = self.controller.get_data_arrivo_effettiva()
        data_arrivo_effettiva_split = data_arrivo_effettiva.split("-")
        self.dateEdit_3.setDate(QDate(int(data_arrivo_effettiva_split[0]), int(data_arrivo_effettiva_split[1]),
                                int(data_arrivo_effettiva_split[2])))

        self.lineEdit.setText(_translate("MainWindow", str(self.controller.get_cod_fattura())))
        self.lineEdit_2.setText(_translate("MainWindow", str(self.controller.get_cod_fornitore())))

    def save_data_click(self):
        self.end1= True
        # Controllo ordine già esistente
        for ordine in self.new_lista_fornitori:
            if str(ordine.cod_fattura) == self.lineEdit.text():
                QMessageBox.critical(self, 'Errore', 'Ordine già esistente.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

        # prendo il testo che l'utente inserisce in ciascuna lineEdit
        cod_fattura = self.lineEdit.text()
        cod_fornitore = self.lineEdit_2.text()
        if str(self.comboBox.currentText()) == "Primavera / Estate":
            stagione = "P/E"
        else:
            stagione = "A/I"
        stato = str(self.comboBox_2.currentText())

        aaaa = self.dateEdit.date().year()
        mm = self.dateEdit.date().month()
        gg = self.dateEdit.date().day()
        data_ordine = str(aaaa) + "-" + str(mm) + "-" + str(gg)
        data_ordine_2 = str(gg) + "/" + str(mm) + "/" + str(aaaa)

        aaaa = self.dateEdit_2.date().year()
        mm = self.dateEdit_2.date().month()
        gg = self.dateEdit_2.date().day()
        data_arrivo_prevista = str(aaaa) + "-" + str(mm) + "-" + str(gg)

        aaaa = self.dateEdit_3.date().year()
        mm = self.dateEdit_3.date().month()
        gg = self.dateEdit_3.date().day()
        data_arrivo_effettiva = str(aaaa) + "-" + str(mm) + "-" + str(gg)

        # imposto i campi dell'ordine
        self.controller.set_cod_fornitore(cod_fornitore)
        self.controller.set_cod_fattura(cod_fattura)
        self.controller.set_stagione(stagione)
        self.controller.set_stato(stato)
        self.controller.set_data_ordine(data_ordine)
        self.controller.set_data_arrivo_prevista(data_arrivo_prevista)
        self.controller.set_data_arrivo_effettiva(data_arrivo_effettiva)

        # imposto i campi dell'ordine (parametri globali) a tutti i prodotti in lista_prodotti_ordine
        if len(self.lista_prodotti_ordine) != 0:
            for prodotto in self.lista_prodotti_ordine:
                prodotto.cod_fattura = cod_fattura
                prodotto.cod_fornitore = cod_fornitore
                prodotto.stato = stato
                prodotto.stagione = stagione
                prodotto.data_ordine = data_ordine_2

        self.update_ui_ordine()
        self.close()
        self.end1= False

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

