class Ordine:

    def __init__(self, codice_fattura, codice_fornitore, stagione, stato, data_ordine , data_arrivo_prevista):
        super(Ordine, self).__init__()
        self.codice_fattura = codice_fattura
        self.codice_fornitore = codice_fornitore
        self.stagione = stagione
        self.stato=stato
        self.data_ordine = data_ordine
        self.data_arrivo_prevista=data_arrivo_prevista


