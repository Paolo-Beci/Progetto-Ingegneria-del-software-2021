import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QMessageBox

class VistaModificaFornitore(QWidget):
    def __init__(self, fornitore, controller, controller_lista, update_ui_fornitore, parent=None):
        super(VistaModificaFornitore, self).__init__(parent)
        self.controller= controller
        self.controller_lista= controller_lista
        self.update_ui_fornitore= update_ui_fornitore
        self.fornitore_selezionato= fornitore

        lista= self.controller_lista.get_lista_fornitori()
        self.new_lista_fornitori= lista[:]
        # affinche non ci siano problemi con il controllo in save_data() (controllo sull'inserimento di un fornitore con stesso codice)
        # ho bisogno di una lista che non contenga il fornitore che sto modificando
        self.new_lista_fornitori.remove(self.fornitore_selezionato)

        # boolean che permette di eseguire due eventi diversi in casi di chiusura
        self.end1 = False

        ###################################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        # Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.setWindowTitle("Modifica fornitore")
        self.setObjectName("Form")
        self.resize(579, 427)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)

        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(205, 360, 160, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.update_ui_fornitore()

        #Tasto SALVA
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_3.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.pushButton_3.setDefault(True)
        self.pushButton_3.clicked.connect(self.save_data)
        #Tasto ANNULLA
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_4.setStyleSheet("QPushButton {\n" "   background-color:white;\n" "   border-width: 2px;\n""   border-radius: 10px;\n""   border: 2px solid gray;\n""   font: bold 12px;\n""   padding: 6px;\n""}")
        self.pushButton_4.clicked.connect(self.close)

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 491, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 11, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 5, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 12, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 12, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 9, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 9, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 8, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 3, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 8, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 11, 1, 1, 1)

        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 2, 0, 1, 1)

        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 7, 3, 1, 1)

        self.dateEdit_1= QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.gridLayout_2.addWidget(self.dateEdit_1, 12, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 3, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 4, 3, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 9, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 7, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 11, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem16, 6, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem17, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 11, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 11, 5, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modifica fornitore"))
        self.pushButton_3.setText(_translate("Form", "Salva"))
        self.pushButton_4.setText(_translate("Form", "Annulla"))

        self.lineEdit_11.setText(_translate("Form", str(self.controller.get_telefono())))
        self.label_7.setText(_translate("Form", "Data affiliazione"))
        self.lineEdit_16.setText(_translate("Form", str(self.controller.get_cod_fornitore())))
        self.label_5.setText(_translate("Form", "Sito web"))
        self.label_2.setText(_translate("Form", "Indirizzo"))

        self.comboBox_2.setItemText(0, _translate("Form", "Standard"))
        self.comboBox_2.setItemText(1, _translate("Form", "Premium"))
        #faccio in modo che il valore di default della combobox corrisponda allo stato attuale del fornitore
        if self.controller.get_stato()=="Standard":
            index= self.comboBox_2.findText("Standard", QtCore.Qt.MatchFixedString)
        else:
            index= self.comboBox_2.findText("Premium", QtCore.Qt.MatchFixedString)
        self.comboBox_2.setCurrentIndex(index)

        self.label.setText(_translate("Form", "Nome"))
        self.label_3.setText(_translate("Form", "Partita iva"))
        self.label_4.setText(_translate("Form", "Telefono"))
        self.lineEdit_9.setText(_translate("Form", str(self.controller.get_partita_iva())))
        self.lineEdit_15.setText(_translate("Form", str(self.controller.get_nome())))
        self.lineEdit_12.setText(_translate("Form", str(self.controller.get_sito_web())))

        data= self.controller.get_data_affiliazione()
        data_split= data.split("/")
        self.dateEdit_1.setDate(QDate(int(data_split[2]), int(data_split[1]), int(data_split[0])))

        self.lineEdit_10.setText(_translate("Form", str(self.controller.get_indirizzo())))
        self.label_6.setText(_translate("Form", "Rappresentante"))
        self.lineEdit_14.setText(_translate("Form", str(self.controller.get_rappresentante())))
        self.label_8.setText(_translate("Form", "Codice"))
        self.label_9.setText(_translate("Form", "Stato"))

    def save_data(self):
        self.end1 = True
        # Controllo fornitore già esistente
        for fornitore in self.new_lista_fornitori:
            if str(fornitore.cod_fornitore) == self.lineEdit_16.text() or fornitore.partita_iva == self.lineEdit_9.text():
                QMessageBox.critical(self, 'Errore', 'Fornitore già presente in lista!', QMessageBox.Ok, QMessageBox.Ok)
                return
        # prendo il testo che l'utente inserisce in ciascuna lineEdit
        partita_iva = self.lineEdit_9.text()
        codice = self.lineEdit_16.text()
        indirizzo = self.lineEdit_10.text()
        telefono = self.lineEdit_11.text()
        sito_web = self.lineEdit_12.text()
        aaaa = str(self.dateEdit_1.date().year())
        mm = str(self.dateEdit_1.date().month())
        gg= str(self.dateEdit_1.date().day())
        data_affiliazione = gg + "/" + mm + "/" + aaaa

        rappresentante = self.lineEdit_14.text()
        nome = self.lineEdit_15.text()
        stato = str(self.comboBox_2.currentText())

        #modifico gli attributi del fornitore in base al testo inserito
        self.controller.set_cod_fornitore = codice
        self.controller.set_nome(nome)
        self.controller.set_telefono(telefono)
        self.controller.set_indirizzo(indirizzo)
        self.controller.set_partita_iva(partita_iva)
        self.controller.set_sito_web(sito_web)
        self.controller.set_rappresentante(rappresentante)
        self.controller.set_data_affiliazione(data_affiliazione)
        self.controller.set_stato(stato)
        self.controller.set_partita_iva(partita_iva)

        self.update_ui_fornitore()
        self.close()
        self.end1 =False

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