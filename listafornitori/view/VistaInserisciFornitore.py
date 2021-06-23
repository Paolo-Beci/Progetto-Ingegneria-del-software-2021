import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox, \
    QGroupBox, QScrollArea, QFormLayout

from fornitore.model.Fornitore import Fornitore


class VistaInserisciFornitore(QWidget):
    def __init__(self, controller, update_ui, lista_dinamica):
        super(VistaInserisciFornitore, self).__init__()
        self.controller = controller
        self.update_ui = update_ui
        self.lista_dinamica= lista_dinamica

        # boolean che permette di eseguire due eventi diversi in caso di chiusura della finestra
        self.end1 = False

        ############################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        self.setStyleSheet("background-color: white;")

        # Inserimento icona
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_mini.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.v_layout = QVBoxLayout()
        self.formLayout= QFormLayout()
        self.groupBox= QGroupBox()

        #oggetto: "campo", "valore"
        self.qlines = {}
        self.add_info_text("nome", "Nome")
        self.add_info_text("indirizzo", "Indirizzo")
        self.add_info_text("partita_iva", "Partita iva")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("sito_web", "Sito web")
        self.add_info_text("rappresentante", "Rappresentante")
        self.label_data_affiliazione= QLabel("Data affiliazione")
        self.formLayout.addWidget(self.label_data_affiliazione)
        self.dateEdit_data_affiliazione= QtWidgets.QDateEdit(self)
        self.formLayout.addWidget(self.dateEdit_data_affiliazione)
        self.add_info_text("codice_fornitore", "Codice Fornitore")
        self.label_stato = QLabel("Stato")
        self.formLayout.addWidget(self.label_stato)
        self.combo_box_stato= QtWidgets.QComboBox(self)
        self.combo_box_stato.addItem("Standard")
        self.combo_box_stato.addItem("Premium")
        self.combo_box_stato.setCurrentIndex(0)
        self.formLayout.addWidget(self.combo_box_stato)
        self.groupBox.setLayout(self.formLayout)
        scroll= QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumSize(250, 600)
        scroll.setWidget(self.groupBox)
        self.v_layout.addWidget(scroll)
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_fornitore)
        self.v_layout.addWidget(btn_ok)
        btn_ok.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")

        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserisci fornitore")

    def add_info_text(self, nome, label):
        self.formLayout.addRow(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.formLayout.addRow(current_text)

    def inserisci_fornitore(self):
        self.end1 = True
        # Controllo inserimento di tutti i campi
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        # Controllo fornitore già esistente
        for fornitore in self.controller.get_lista_fornitori():
            if fornitore.partita_iva == self.qlines["partita_iva"].text() or fornitore.cod_fornitore==self.qlines["codice_fornitore"].text():
                QMessageBox.critical(self, 'Errore', 'Fornitore già presente in lista!', QMessageBox.Ok, QMessageBox.Ok)
                return

        gg= str(self.dateEdit_data_affiliazione.date().day())
        mm= str(self.dateEdit_data_affiliazione.date().month())
        aaaa= str(self.dateEdit_data_affiliazione.date().year())
        data_affiliazione= gg + "/" + mm + "/" + aaaa
        if str(self.combo_box_stato.currentText()) == "Standard":
            stato= "S"
        else:
            stato= "P"

        fornitore= Fornitore(
             self.qlines["codice_fornitore"].text(),
             self.qlines["nome"].text(),
             self.qlines["indirizzo"].text(),
             self.qlines["telefono"].text(),
             self.qlines["partita_iva"].text(),
             self.qlines["sito_web"].text(),
             self.qlines["rappresentante"].text(),
             data_affiliazione,
             stato)

        self.controller.inserisci_fornitore(fornitore)
        self.lista_dinamica.append(fornitore)
        self.update_ui()
        self.close()
        self.end1 = False

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
