# model del ordine
class Ordine:

    def __init__(self, cod_fattura, cod_fornitore, data_ordine,  data_arrivo_prevista, data_arrivo_effettiva, stagione, importo_totale, calzature_totali, stato):
        super(Ordine, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.data_ordine = data_ordine  # str
        self.data_arrivo_prevista = data_arrivo_prevista  # float
        self.data_arrivo_effettiva= data_arrivo_effettiva
        self.stagione = stagione  # str
        self.importo_totale= importo_totale
        self.calzature_totali= calzature_totali
        self.stato = stato  # str
