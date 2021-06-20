class ControllerFornitore:
    def __init__(self, fornitore):
        self.model= fornitore

    ################# GETTER #################

    def get_cod_fornitore(self):
        return self.model.cod_fornitore

    def get_nome(self):
        return self.model.nome

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_telefono(self):
        return self.model.telefono

    def get_partita_iva(self):
        return self.model.partita_iva

    def get_sito_web(self):
        return self.model.sito_web

    def get_rappresentante(self):
        return self.model.rappresentante

    def get_data_affiliazione(self):
        return self.model.data_affiliazione

    def get_stato(self):
        if self.model.stato == "S":
            return "Standard"
        else:
            return "Premium"

    ################# SETTER #################

    def set_cod_fornitore(self, codice_fornitore):
        self.model.cod_fornitore= codice_fornitore

    def set_nome(self, nome):
        self.model.nome = nome

    def set_indirizzo(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_partita_iva(self, partita_iva):
        self.model.partita_iva= partita_iva

    def set_telefono(self, telefono):
        self.model.telefono= telefono

    def set_sito_web(self, sito_web):
        self.model.sito_web= sito_web

    def set_rappresentante(self, rappresentante):
        self.model.rappresentante= rappresentante

    def set_data_affiliazione(self, data_affiliazione):
        if self.model.data_affiliazione is None:
            return "00/00/0000"
        else:
            return self.model.data_affiliazione

    def set_stato(self, stato):
        if stato=="Standard":
            self.model.stato= "S"
        else:
            self.model.stato= "P"



