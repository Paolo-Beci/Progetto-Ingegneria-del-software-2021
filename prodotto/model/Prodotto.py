# model del Prodotto
class Prodotto:

    def __init__(self, cod_fattura, cod_fornitore, data_ordine, cod_prodotto, materiale,
                 colore, taglia, quantita, prezzo_di_acquisto, prezzo_di_vendita,  stato, stagione, data_di_vendita):
        super(Prodotto, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.data_ordine = data_ordine  # str
        self.cod_prodotto = cod_prodotto  # int
        self.materiale = materiale  # str
        self.colore = colore  # str
        self.taglia = taglia  # int
        self.quantita = quantita  # int
        self.prezzo_di_acquisto = prezzo_di_acquisto  # float
        self.prezzo_di_vendita = prezzo_di_vendita  # float
        self.stato = stato  # str
        self.stagione = stagione  # str
        self.data_di_vendita = data_di_vendita  # str
