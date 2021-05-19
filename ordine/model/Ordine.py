# model del ordine
class ordine:

    def __init__(self, cod_fattura, cod_fornitore, data_ordine,  data_arrivo_prevista, stagione, stato,):
        super(Prodotto, self).__init__()
        self.cod_fattura = cod_fattura  # str
        self.cod_fornitore = cod_fornitore  # int
        self.data_ordine = data_ordine  # str
        self.cod_prodotto = cod_prodotto  # int
        self.data_arrivo_prevista = data_arrivo_prevista  # float
        self.stagione = stagione  # str
        self.stato = stato  # str

