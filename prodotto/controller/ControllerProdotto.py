class ControllerProdotto:
    def __init__(self, prodotto) -> object:
        self.model = prodotto

    def somma_prodotti(self): pass

    def modifica_prodotto(self, cod_prodotto): pass

    def elimina_prodotto(self, cod_prodotto): pass

    def get_prodotto(self, index):
        return self.model.get_prodotto(index)

    # GET di servizio

    def get_cod_fattura(self):
        return self.model.codice_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    # def genere(self):
    #    return self.model.genere

    def get_materiale(self):
        return self.model.materiale

    def get_colore(self):
        return self.model.colore

    def get_taglia(self):
        return self.model.taglia

    def get_quantita(self):
        return self.model.quantita

    def get_prezzo_acquisto(self):
        return self.model.prezzo_acquisto

    def get_prezzo_vendita(self):
        return self.model.prezzo_vendita

    def get_stagione(self):
        return self.model.stagione

    def get_stato(self):
        return self.model.stato

    def get_data_vendita(self):
        return self.model.data_vendita

    def get_sconto_consigliato(self):
        return self.model.sconto_consigliato

    def get_sconto(self):
        return self.model.sconto

    def get_cod_immagine(self):
        return self.model.cod_immagine
