class ControllerUtente:
    def __init__(self, utente) -> object:
        self.model= utente

    def get_nome(self):
        return self.model.nome

    def get_cognome(self):
        return self.model.cognome

    def get_data_nascita(self):
        return self.model.data_nascita

    def get_luogo_nascita(self):
        return self.model.luogo_nascita

    def get_eta(self):
        return self.model.eta

    def get_cf(self):
        return self.model.cf

    def get_codice_utente(self):
        return self.model.codice_utente

    def get_telefono(self):
        return self.model.telefono

    def get_ruolo(self):
        return self.model.ruolo

    def get_stipendio(self):
        return  self.model.stipendio

    def get_data_scadenza_contratto(self):
        return self.model.data_scadenza_contratto
