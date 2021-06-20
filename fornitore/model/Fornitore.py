class Fornitore:
    def __init__(self, cod_fornitore, nome, indirizzo, telefono, partita_iva, sito_web, rappresentante,
                 data_affiliazione, stato):
        super(Fornitore, self).__init__()
        self.cod_fornitore = cod_fornitore#
        self.nome= nome#
        self.indirizzo= indirizzo#
        self.telefono = telefono#
        self.partita_iva= partita_iva
        self.sito_web= sito_web
        self.rappresentante= rappresentante#
        self.data_affiliazione= data_affiliazione
        self.stato= stato
