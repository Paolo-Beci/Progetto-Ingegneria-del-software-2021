from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.model.Prodotto import Prodotto

"""
DA FARE
# implementare i controlli di correttezza dell'inserimento (crasha)
# fare interfaccia
"""
class VistaInserisciProdotto(QWidget):
    def __init__(self, controller, update_ui):
        # callback ??
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.update_ui = update_ui
        # self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("cod_fattura", "Codice fattura")
        self.get_form_entry("cod_fornitore", "Codice fornitore")
        self.get_form_entry("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
        self.get_form_entry("cod_prodotto", "Codice del prodotto")
        self.get_form_entry("marca", "Marca")
        self.get_form_entry("nome", "Nome")
        self.get_form_entry("tipo", "Tipo")
        self.get_form_entry("genere", "Genere")
        self.get_form_entry("materiale", "Materiale")
        self.get_form_entry("colore", "Colore")
        self.get_form_entry("taglia", "Taglia")
        self.get_form_entry("quantita", "Quantità")
        self.get_form_entry("prezzo_acquisto", "Prezzo di acquisto")
        self.get_form_entry("prezzo_vendita", "Prezzo di vendita")
        self.get_form_entry("stagione", "Stagione")
        self.get_form_entry("stato", "Stato")
        self.get_form_entry("sconto_consigliato", "Sconto consigliato")
        self.get_form_entry("sconto", "Sconto")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_prodotto)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserisci prodotto")

    def get_form_entry(self, nome, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.info[nome] = current_text_edit
        self.v_layout.addWidget(current_text_edit)

    def inserisci_prodotto(self):

        cod_fattura = self.info["Codice fattura"].text()
        cod_fornitore = self.info["Codice fornitore"].text()
        data_ordine = self.info["Data dell'ordine (dd/mm/AAAA)"].text()
        cod_prodotto = self.info["Codice del prodotto"].text()
        nome = self.info["Marca"].text()
        marca = self.info["Nome"].text()
        tipo = self.info["Tipo"].text()
        genere = self.info["Genere"].text()
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

        for value in self.info.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
            # I CONTROLLI DANNO PROBLEMI DI CRASH
            #if taglia > 50:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci una taglia valida',
            #                          QMessageBox.Ok, QMessageBox.Ok)
            #    return
            #if sconto > 100 or sconto_consigliato > 100:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci uno sconto valido',
            #                         QMessageBox.Ok, QMessageBox.Ok)
            #    return
            #if sconto.isnumeric() or sconto_consigliato.isnumeric():
            #    return
            #else:
            #    QMessageBox.critical(self, 'Errore', 'Per favore, inserisci uno sconto numerico',
            #                         QMessageBox.Ok, QMessageBox.Ok)
            #    return

        self.controller.inserisci_prodotto(Prodotto(cod_fattura, cod_fornitore, data_ordine, cod_prodotto,
                                                    marca, nome, tipo, genere, materiale, colore, taglia, quantita,
                                                    prezzo_acquisto, prezzo_vendita, stagione, stato,
                                                    sconto_consigliato, sconto, "",))
        # self.callback()
        self.update_ui()
        self.close()
