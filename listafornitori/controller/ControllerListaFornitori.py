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

    def save_data(self):
        self.model.save_data()
