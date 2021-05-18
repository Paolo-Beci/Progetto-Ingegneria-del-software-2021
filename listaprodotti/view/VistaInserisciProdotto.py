from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.model.Prodotto import Prodotto

# DA FARE
# far funzionare il fottutissimo inserimento che da exit code...e crasha
# implementare i controlli di correttezza dell'inserimento
# fare interfaccia
class VistaInserisciProdotto(QWidget):
    def __init__(self, controller):
        # callback ??
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        # self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Codice fattura")
        self.get_form_entry("Codice fornitore")
        self.get_form_entry("Data dell'ordine (dd/mm/AAAA)")
        self.get_form_entry("Codice del prodotto")
        self.get_form_entry("Genere")
        self.get_form_entry("Marca")
        self.get_form_entry("Materiale")
        self.get_form_entry("Colore")
        self.get_form_entry("Taglia")
        self.get_form_entry("Quantità")
        self.get_form_entry("Prezzo di acquisto")
        self.get_form_entry("Prezzo di vendita")
        self.get_form_entry("Stagione")
        self.get_form_entry("Stato")
        self.get_form_entry("Sconto consigliato")
        self.get_form_entry("Sconto")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_prodotto)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserisci prodotto")

    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def inserisci_prodotto(self):
        cod_fattura = self.info["Codice fattura"].text()
        cod_fornitore = self.info["Codice fornitore"].text()
        data_ordine = self.info["Data dell'ordine (dd/mm/AAAA)"].text()
        cod_prodotto = self.info["Codice del prodotto"].text()
        genere = self.info["Genere"].text()
        marca = self.info["Marca"].text()
        materiale = self.info["Materiale"].text()
        colore = self.info["Colore"].text()
        taglia = self.info["Taglia"].text()
        quantita = self.info["Quantità"].text()
        prezzo_acquisto = self.info["Prezzo di acquisto"].text()
        prezzo_vendita = self.info["Prezzo di vendita"].text()
        stagione = self.info["Stagione"].text()
        stato = self.info["Stato"].text()
        sconto_consigliato = self.info["Sconto consigliato"].text()
        sconto = self.info["Sconto"].text()
        if cod_fattura == "" or data_ordine == "" or cod_prodotto == "" or cod_fornitore == "" or genere == "" or marca =="" \
                or materiale == "" or colore == "" or taglia == "" or quantita == "" or prezzo_acquisto == "" or prezzo_vendita == "" \
                or stagione == "" or stato == "" or sconto_consigliato == "" or sconto == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.inserisci_prodotto(Prodotto(cod_fattura, cod_fornitore, data_ordine, cod_prodotto,
                                                       genere, marca, materiale, colore, taglia, quantita, prezzo_acquisto,
                                                       prezzo_vendita, stagione, stato, sconto_consigliato, sconto))
            #self.callback()
            self.close()
