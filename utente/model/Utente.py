class Utente:
    def __init__(self, cod_utente, nome, cognome, data_nascita, luogo_nascita, cf, data_inizio_contratto,
                 data_scadenza_contratto, ruolo, indirizzo, telefono, stipendio, username, password):
        super(Utente, self).__init__()
        self.cod_utente = cod_utente
        self.nome= nome
        self.cognome= cognome
        self.data_nascita= data_nascita
        self.luogo_nascita= luogo_nascita
        self.cf = cf
        self.data_inizio_contratto= data_inizio_contratto
        self.data_scadenza_contratto = data_scadenza_contratto
        self.ruolo = ruolo
        self.indirizzo= indirizzo
        self.telefono = telefono
        self.stipendio = stipendio
        self.username = username
        self.password = password







