

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

    # def get_lista_prodotti_ordine(self):
    #     return self.model.lista_prodotti_ordine()

    # ----------------SET------------------

    def set_cod_fattura(self, cod_fattura):
        self.model.cod_fattura= cod_fattura

    def set_cod_fornitore(self, cod_fornitore):
        self.model.cod_fornitore= cod_fornitore

    def set_data_ordine(self, data_ordine):
        self.model.data_ordine= data_ordine

    def set_data_arrivo_prevista(self, data_arrio_prevista):
        self.model.data_arrivo_prevista= data_arrio_prevista

    def set_data_arrivo_effettiva(self, data_arrio_effettiva):
        self.model.data_arrivo_effettiva = data_arrio_effettiva

    def set_stagione(self, stagione):
        self.model.stagione= stagione

    def set_importo_totale(self, importo_totale):
        self.model.importo_totale= importo_totale

    def set_calzature_totali(self, calzature_totali):
        self.model.calzature_totali= calzature_totali

    def set_stato(self, stato):
        self.model.stato= stato

    # def set_lista_prodotti_ordine(self):
    #     for prodotto in self.controller_lista_prodotti.get_lista_prodotti():
    #         if prodotto.cod_fattura == self.get_cod_fattura():
    #             self.model.lista_prodotti_ordine.append(prodotto)



