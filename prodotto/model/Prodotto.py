"""
     Model del Prodotto
"""
class Prodotto:

    def __init__(self, cod_fattura, cod_fornitore, data_ordine, cod_prodotto, marca, nome, tipo, genere, materiale,
                 colore, taglia, quantita, prezzo_acquisto, prezzo_vendita, stagione, stato,
                 sconto_consigliato, sconto, data_vendita):
        super(Prodotto, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.data_ordine = data_ordine  # str
        self.cod_prodotto = cod_prodotto  # int
        self.marca = marca  # str
        self.nome = nome  # str
        self.tipo = tipo  # str
        self.genere = genere  # str
        self.materiale = materiale  # str
        self.colore = colore  # str
        self.taglia = taglia  # int
        self.quantita = quantita  # int
        self.prezzo_acquisto = prezzo_acquisto  # float
        self.prezzo_vendita = prezzo_vendita  # float
        self.stagione = stagione  # str
        self.stato = stato  # str
        self.sconto_consigliato = sconto_consigliato  # int
        self.sconto = sconto  # int
        self.data_vendita = data_vendita  # str


"""
    LEGENDA CODICI DATABASE:
    > TIPO:
        - Eleganti
        - Sneakers
        - Sportive
        - Trekking
    > GENERE:
        - Uomo -> U
        - Donna -> D
        - Bambino -> BO
        - Bambina -> BA
    > STAGIONE:
        - Primavera/estate -> P/E
        - Atunno/inverno -> A/I
"""
