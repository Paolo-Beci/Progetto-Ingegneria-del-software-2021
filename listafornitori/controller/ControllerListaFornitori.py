from listafornitori.model.ListaFornitori import ListaFornitori


class ControllerListaFornitori():
    def __init__(self):
        super(ControllerListaFornitori, self).__init__()
        self.model= ListaFornitori()

    def get_lista_fornitori(self):
        return self.model.get_lista_fornitori()

    def inserisci_fornitore(self, fornitore):
        self.model.inserisci_fornitore(fornitore)

    def filtra_fornitori(self):
        return None

    def get_fornitore_by_index(self, index):
        return self.model.get_fornitore_by_index(index)

    # Giuseppe
    def get_foritore_by_code(self, codice):
        return self.model.get_fornitore_by_code(codice)

    # Giuseppe
    def get_stato_fornitore_by_code(self, codice):
        return self.model.get_stato_fornitore_by_code(codice)

    def elimina_fornitore_by_codice(self, codice_fornitore, lista_dinamica):
        self.model.elimina_fornitore_by_codice(codice_fornitore, lista_dinamica)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()
