class Fornitore:
    def __init__(self, nome, indirizzo, partita_iva, telefono, email, rappresentante,
                 data_affiliazione, codice_fornitore, stato):
        super(Fornitore, self).__init__()
        self.nome= nome
        self.indirizzo= indirizzo
        self.partita_iva= partita_iva
        self.telefono= telefono
        self.email= email
        self.rappresentante= rappresentante
        self.data_affiliazione= data_affiliazione
        self.codice_fornitore= codice_fornitore
        self.stato= stato
