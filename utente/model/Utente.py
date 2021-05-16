class Utente:
    def __init__(self, nome, cognome, data_nascita, luogo_nascita, eta, cf, codice_utente, telefono, ruolo, stipendio, data_scadenza_contratto):
        super(Utente, self).__init__()
        self.nome= nome
        self.cognome= cognome
        self.data_nascita= data_nascita
        self.luogo_nascita= luogo_nascita
        self.eta= eta
        self.cf= cf
        self.codice_utente= codice_utente
        self.telefono= telefono
        self.ruolo= ruolo
        self.stipendio= stipendio
        self.data_scadenza_contratto= data_scadenza_contratto
