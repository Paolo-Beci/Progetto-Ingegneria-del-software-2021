
class ControllerUtente:
    def __init__(self, utente):
        self.model= utente

    # GETTER

    def get_cod_utente(self):
        return self.model.cod_utente

    def get_nome(self):
        return self.model.nome

    def get_cognome(self):
        return self.model.cognome

    def get_data_nascita(self):
        return self.model.data_nascita

    def get_luogo_nascita(self):
        return self.model.luogo_nascita

    def get_cf(self):
        return self.model.cf

    def get_data_inizio_contratto(self):
        return self.model.data_inizio_contratto

    def get_data_scadenza_contratto(self):
        return self.model.data_scadenza_contratto

    def get_ruolo(self):
        if self.model.ruolo=="D":
            return "Dipendente"
        else:
            return "Amministratore"

    def get_indirizzo(self):
        return self.model.indirizzo

    def get_telefono(self):
        return self.model.telefono

    def get_stipendio(self):
        return  self.model.stipendio

    def get_username(self):
        if self.model.ruolo== "A":
            return self.model.username
        else:
            raise EOFError

    def get_password(self):
        if self.model.ruolo== "A":
            return self.model.password
        else:
            raise EOFError

    # SETTER

    def set_cod_utente(self, codice):
        self.model.cod_utente= codice

    def set_nome(self, nome):
        self.model.nome= nome

    def set_cognome(self, cognome):
        self.model.cognome= cognome

    def set_data_nascita(self, data_nascita):
        self.model.data_nascita= data_nascita

    def set_luogo_nascita(self, luogo_nascita):
        self.model.luogo_nascita= luogo_nascita

    def set_cf(self, cf):
        self.model.cf= cf

    def set_data_inizio_contratto(self, data_inizio_contratto):
        self.model.data_inizio_contratto= data_inizio_contratto

    def set_data_scadenza_contratto(self, data_scadenza_contratto):
        self.model.data_scadenza_contratto= data_scadenza_contratto

    def set_ruolo(self, ruolo):
        if ruolo=="Dipendente":
            self.model.ruolo= "D"
        else:
            self.model.ruolo= "A"

    def set_indirizzo(self, indirizzo):
        self.model.indirizzo= indirizzo

    def set_telefono(self, telefono):
        self.model.telefono= telefono

    def set_stipendio(self, stipendio):
        self.model.stipendio= stipendio

    def set_username(self, username):
        if self.model.ruolo=="A":
            self.model.username= username
        else:
            raise EOFError

    def set_password(self, password):
        if self.model.ruolo=="A":
            self.model.password= password
        else:
            raise EOFError

