from listaordini.model.ListaOrdini import ListaOrdini


class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def somma_prodotti(self): pass

    def modifica_prodotto_by_codice(self, cod_prodotto, new_value):
        self.model.ListaProdotti.modifica_prodotto(cod_prodotto, new_value)

    def elimina_prodotto(self, cod_prodotto): pass

    def get_prodotto(self, index):
        return self.model.get_prodotto(index)

    # ----------------GET------------------

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        return self.model.data_ordine

    def get_data_arrivo_prevista(self):
        return self.model.data_arrivo_prevista

    def get_data_arrivo_effettiva(self):
        return self.model.data_arrivo_effettiva

    def get_stagione(self):
        return self.model.stagione

    def get_stato(self):
        return self.model.stato
    def get_importo_totale(self):
        return self.model.importo_totale
    def get_calzature_totali(self):
        return self.model.calzature_totali



    # ----------------SET------------------

    def set_cod_fattura(self, cod_prodotto, new_cod_fattura):
        self.modifica_prodotto_by_codice(cod_prodotto, new_cod_fattura)

    def set_cod_fornitore(self, cod_prodotto, new_cod_fornitore):
        self.modifica_prodotto_by_codice(cod_prodotto, new_cod_fornitore)

    def set_data_ordine(self, cod_prodotto, new_data_ordine):
        self.modifica_prodotto_by_codice(cod_prodotto, new_data_ordine)

    def set_calzature_totali(self):
        return self.model.calzature_totali

    def set_stagione(self):
        return self.model.stagione

    def set_stato(self):
        return self.model.stato

    def set_data_vendita(self):
        return self.model.data_vendita

