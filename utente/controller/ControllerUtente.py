class ControllerUtente:
    def __init__(self, utente):
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

    def set_nome(self, nome):
        self.model.nome= nome

    def set_cognome(self, cognome):
        self.model.cognome= cognome

    def set_data_nascita(self, data_nascita):
        self.model.data_nascita= data_nascita

    def set_luogo_nascita(self, luogo_nascita):
        self.model.luogo_nascita= luogo_nascita

    def set_eta(self, eta):
        self.model.eta= eta

    def set_cf(self, cf):
        self.model.cf= cf

    def set_codice(self, codice):
        self.model.codice= codice

    def set_telefono(self, telefono):
        self.model.telefono= telefono

    def set_ruolo(self, ruolo):
        self.model.ruolo= ruolo

    def set_stipendio(self, stipendio):
        self.model.stipendio= stipendio

    def set_data_scadenza_contratto(self, data_scadenza_contratto):
        self.model.data_scadenza_contratto= data_scadenza_contratto
