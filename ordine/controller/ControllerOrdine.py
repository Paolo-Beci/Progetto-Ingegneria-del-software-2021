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

    def get_cod_prodotto(self):
        return self.model.cod_prodotto

    def get_genere(self):
        return self.model.genere

    def get_tipo(self):
        return self.model.tipo

    def get_marca(self):
        return self.model.marca

    def get_nome(self):
        return self.model.nome

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

    # ----------------SET------------------

    def set_cod_fattura(self, cod_prodotto, new_cod_fattura):
        self.modifica_prodotto_by_codice(cod_prodotto, new_cod_fattura)

    def set_cod_fornitore(self, cod_prodotto, new_cod_fornitore):
        self.modifica_prodotto_by_codice(cod_prodotto, new_cod_fornitore)

    def set_data_ordine(self, cod_prodotto, new_data_ordine):
        self.modifica_prodotto_by_codice(cod_prodotto, new_data_ordine)

    def set_cod_prodotto(self):
        return self.model.cod_prodotto

    def set_genere(self):
        return self.model.genere

    def set_tipo(self):
        return self.model.tipo

    def set_marca(self):
        return self.model.marca

    def set_nome(self):
        return self.model.nome

    def set_materiale(self):
        return self.model.materiale

    def set_colore(self):
        return self.model.colore

    def set_taglia(self):
        return self.model.taglia

    def set_quantita(self):
        return self.model.quantita

    def set_prezzo_acquisto(self):
        return self.model.prezzo_acquisto

    def set_prezzo_vendita(self):
        return self.model.prezzo_vendita

    def set_stagione(self):
        return self.model.stagione

    def set_stato(self):
        return self.model.stato

    def set_data_vendita(self):
        return self.model.data_vendita

    def set_sconto_consigliato(self):
        return self.model.sconto_consigliato

    def set_sconto(self):
        return self.model.sconto
