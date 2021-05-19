# model del Prodotto
class Prodotto:

    def __init__(self, cod_fattura, cod_fornitore, data_ordine, cod_prodotto, genere, marca, materiale,
                 colore, taglia, quantita, prezzo_acquisto, prezzo_vendita, stagione, stato,
                 data_vendita, sconto_consigliato, sconto):
        super(Prodotto, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.data_ordine = data_ordine  # str
        self.cod_prodotto = cod_prodotto  # int
        self.genere = genere  # str
        self.marca = marca  # str
        self.materiale = materiale  # str
        self.colore = colore  # str
        self.taglia = taglia  # int
        self.quantita = quantita  # int
        self.prezzo_acquisto = prezzo_acquisto  # float
        self.prezzo_vendita = prezzo_vendita  # float
        self.stagione = stagione  # str
        self.stato = stato  # str
        self.data_vendita = data_vendita  # str
        self.sconto_consigliato = sconto_consigliato  # int
        self.sconto = sconto  # int
