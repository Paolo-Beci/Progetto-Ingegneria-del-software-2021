import datetime

"""
    CONTROLLER DEL PRODOTTO
    Contiene i get e set essenziali per gestire il flusso di dati relativo ai prodotti
"""


class ControllerProdotto:
    def __init__(self, prodotto):
        self.model = prodotto

    # ----------------GET------------------

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    def get_genere(self):
        if self.model.genere == "U":
            return "Uomo"
        elif self.model.genere == "D":
            return "Donna"
        elif self.model.genere == "BO":
            return "Bambino"
        elif self.model.genere == "BA":
            return "Bambina"

    def get_nome(self):
        return self.model.nome

    def get_stagione(self):
        return self.model.stagione

    def get_stato(self):
        return self.model.stato

    # ----------------SET------------------

    def set_cod_fattura(self, cod_fattura):
        self.model.cod_fattura = cod_fattura

    def set_cod_fornitore(self, cod_fornitore):
        self.model.cod_fornitore = cod_fornitore

    def set_data_ordine(self, data_ordine):
        self.model.data_ordine = data_ordine

    def set_nome(self, nome):
        self.model.nome = nome

    def set_stagione(self, stagione):
        self.model.stagione = stagione

    def set_stato(self, stato):
        self.model.stato = stato


