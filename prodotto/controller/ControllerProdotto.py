class ControllerProdotto:
    def __init__(self, prodotto) -> object:
        self.model = prodotto

    def somma_prodotti(self): pass

    def modifica_prodotto(self): pass

    def elimina_prodotto(self): pass

    # GET di servizio

    def get_codice_fattura(self):
        return self.model.codice_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    def get_materiale(self):
        return self.model.materiale

    def get_colore(self):
        return self.model.colore

    def get_taglia(self):
        return self.model.taglia

    def get_quantita(self):
        return self.model.quantita

    def get_prezzo(self):
        return self.model.prezzo

    def get_stato(self):
        return self.model.stato

    def get_stagione(self):
        return self.model.stagione
