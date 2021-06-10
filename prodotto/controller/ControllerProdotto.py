import datetime

from listaprodotti.model.ListaProdotti import ListaProdotti
import time


class ControllerProdotto:
    def __init__(self, prodotto) -> object:
        self.model = prodotto

    def somma_prodotti(self): pass

    def modifica_prodotto_by_codice(self, cod_prodotto, new_value):
        self.model.ListaProdotti.modifica_prodotto(cod_prodotto, new_value)

    def get_prodotto(self, index):
        return self.model.get_prodotto(index)

    def get_dimensione_lista(self):
        return self.model.get_dimensione_lista()

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

    def set_venduto(self):
        # Da controllare con più quantità
        self.model.stato = "Venduto"
        i = datetime.datetime.now()
        self.model.data_vendita = str("%s/%s/%s" % (i.day, i.month, i.year))

    def set_cod_fattura(self, cod_fattura):
        self.model.cod_fattura = cod_fattura

    def set_cod_fornitore(self, cod_fornitore):
        self.model.cod_fornitore = cod_fornitore

    def set_data_ordine(self, data_ordine):
        self.model.data_ordine = data_ordine

    def set_cod_prodotto(self, cod_prodotto):
        self.model.cod_prodotto = cod_prodotto

    def set_genere(self, genere):
        self.model.genere = genere

    def set_tipo(self, tipo):
        self.model.tipo = tipo

    def set_marca(self, marca):
        self.model.marca = marca

    def set_nome(self, nome):
        self.model.nome = nome

    def set_materiale(self, materiale):
        self.model.materiale = materiale

    def set_colore(self, colore):
        self.model.colore = colore

    def set_taglia(self, taglia):
        self.model.taglia = taglia

    def set_quantita(self, quantita):
        self.model.quantita = quantita

    def set_prezzo_acquisto(self, prezzo_acquisto):
        self.model.prezzo_acquisto = prezzo_acquisto

    def set_prezzo_vendita(self, prezzo_vendita):
        self.model.prezzo_vendita = prezzo_vendita

    def set_stagione(self, stagione):
        self.model.stagione = stagione

    def set_stato(self, stato):
        self.model.stato = stato

    def set_data_vendita(self, data_vendita):
        self.model.data_vendita = data_vendita

    def set_sconto_consigliato(self, sconto_consigliato):
        self.model.sconto_consigliato = sconto_consigliato

    def set_sconto(self, sconto):
        self.model.sconto = sconto
