class ControlloreOrdine:
    def __init__(self, Ordine):
        self.model = Ordine

    def get_elimina_Ordine(self):
        if self.model.is_elimina_Ordine():
        del self.model.elimina_Ordine
            return "cancellato con sucesso"
        else:
            return "errore"

    def get_modifica_ordine(self):
        if self.model.is_modifica_ordine():
            return "modificato"
        else:
            return "errore"

    def get_modifica_codice_fattura(self):
        if self.model.is_modifica_codice_fattura():
            return "modificato"
        else:
            return "errore"

    def get_modifica_codice_fornitore(self):
        if self.model.is_modifica_codice_fornitore():
            return "mofificato"
        else:
            return "errore"

    def get_modifica_stagione(self):
        if self.model.is_modifica_stagione():
            return "modificato"
        else:
            return "errore"
    def get_modifica_stato(self):
        if self.model.is_modifica_stato():
            return "modificato"
        else:
            return "errore"

    def get_modifica_data_Ordine(self):
        if self.model.is_modifica_data_Ordine():
                return "modificato"
            else:
                return "errore"

    def get_data_di_arrivo_prevista(self):
        if self.model.is_data_di_arrivo_prevista():
                return "modificato"
            else:
                return "errore"