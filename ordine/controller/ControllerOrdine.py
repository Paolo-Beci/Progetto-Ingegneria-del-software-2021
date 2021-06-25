class ControllerOrdine:
    def __init__(self, ordine):
        self.model = ordine

    ################# GETTER #################

    def get_cod_fattura(self):
        return self.model.cod_fattura

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_data_ordine(self):
        if self.model.data_ordine is None:
            return "0000-00-00"
        else:
            return self.model.data_ordine

    def get_data_arrivo_prevista(self):
        if self.model.data_arrivo_prevista is None:
            return "9999-12-31"
        else:
            return self.model.data_arrivo_prevista

    def get_data_arrivo_effettiva(self):
        if self.model.data_arrivo_effettiva is None:
            return "9999-12-31"
        else:
            return self.model.data_arrivo_effettiva

    def get_stagione(self):
        return self.model.stagione

    def get_stato(self):
        return self.model.stato

    ################# SETTER #################

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

    def set_stato(self, stato):
        self.model.stato= stato


