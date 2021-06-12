from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

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
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_form_entry("cod_fattura", "Codice fattura")
        self.get_form_entry("cod_fornitore", "Codice fornitore")
        self.get_form_entry("stagione", "Stagione")
        self.get_form_entry("stato", "Stato")
        self.get_form_entry("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
        self.get_form_entry("data_arrivo_prevista", "data arrivo prevista")
        self.get_form_entry("data_arrivo_effettiva", "data arrivo effettiva")
        self.get_form_entry("importo_totale", "importo totale")
        self.get_form_entry("calzature_totali", "calzature totali")



        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_ordine)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Inserisci ordine")

    def get_form_entry(self, nome, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.info[nome] = current_text_edit
        self.v_layout.addWidget(current_text_edit)

    def inserisci_ordine(self):
        cod_fattura = self.info["cod_fattura"].text()
        cod_fornitore = self.info["cod_fornitore"].text()
        stagione = self.info["stagione"].text()
        stato = self.info["stato"].text()
        data_ordine = self.info["data_ordine"].text()
        data_arrivo_prevista= self.info["data_arrivo_prevista"].text()
        data_arrivo_effettiva= self.info["data_arrivo_effettiva"].text()
        importo_totale = self.info["importo_totale"].text()
        calzature_totali = self.info["calzature_totali"].text()



        for value in self.info.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return
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
