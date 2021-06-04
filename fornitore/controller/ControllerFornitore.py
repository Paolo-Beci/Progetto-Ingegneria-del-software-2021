class ControllerFornitore:
    def __init__(self, fornitore):
        self.model= fornitore

    ################# GETTER #################

    def get_nome(self):
        return self.model.nome

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_partita_iva(self):
        return self.model.partita_iva

    def get_telefono(self):
        return self.model.telefono

    def get_email(self):
        return self.model.email

    def get_rappresentante(self):
        return self.model.rappresentante

    def get_data_affiliazione(self):
        return self.model.data_affiliazione

    def get_cod_fornitore(self):
        return self.model.codice_fornitore

    def get_stato(self):
        return self.model.stato
    ################# SETTER #################
    
    def set_nome_fornitore(self, nome):
        self.model.nome = nome

    def set_indirizzo(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_partita_iva(self, partita_iva):
        self.model.partita_iva= partita_iva

    def set_telefono(self, telefono):
        self.model.telefono= telefono

    def set_email(self, email):
        self.model.email= email

    def set_rappresentante(self, rappresentante):
        self.model.rappresentante= rappresentante

    def set_data_affiliazione(self, data_affiliazione):
        self.model.data_affiliazione= data_affiliazione

    def set_cod_fornitore(self, codice_fornitore):
        self.model.codice_fornitore= codice_fornitore

    def set_stato(self, stato):
        self.model.stato= stato

    # def elimina_fornitore(self):
    #     return None



