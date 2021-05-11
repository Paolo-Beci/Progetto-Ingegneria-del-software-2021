class Prodotto:

    def __init__(self, codice_fattura, cod_fornitore, data_ordine, cod_prodotto, materiale,
                 colore, taglia, quantita, prezzo, stato, stagione):

        super(Prodotto, self).__init__()
        self.codice_fattura = codice_fattura
        self.cod_fornitore = cod_fornitore
        self.data_ordine = data_ordine
        self.cod_prodotto = cod_prodotto
        self.materiale = materiale
        self.colore = colore
        self.taglia = taglia
        self.quantita = quantita
        self.prezzo = prezzo
        self.stato = stato
        self.stagione = stagione
