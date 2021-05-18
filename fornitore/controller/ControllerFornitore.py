class ControllerFornitore:
    def __init__(self, fornitore):
        self.model= fornitore

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

    def get_codice_fornitore(self):
        return self.model.codice_fornitore

    def get_stato(self):
        return self.model.stato

    def elimina_fornitore(self):
        return None

    def modifica_nome_fornitore(self):
        return None

    def modifica_indirizzo_fornitore(self):
        return None

    def modifica_partita_iva(self):
        return None

    def modifica_telefono_fornitore(self):
        return None

    def modifica_email_fornitore(self):
        return None

    def modifica_rappresentante(self):
        return None

    def modifica_data_affiliazione(self):
        return None

    def modifica_codice_fornitore(self):
        return None

    def modifica_stato_fornitore(self):
        return None

