from listaordini.model.ListaOrdini import ListaOrdini


class ControllerListaOrdini:
    def __init__(self):
        super(ControllerListaOrdini, self).__init__()
        self.model = ListaOrdini()

    def get_lista_ordini(self):
        return self.model.get_lista_ordini()

    def inserisci_ordine(self, ordine):
        self.model.inserisci_ordine(ordine)

    def elimina_ordine_by_codice(self, codice_ordine, lista_dinamica):
        self.model.elimina_ordine_by_codice(codice_ordine, lista_dinamica)

    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()
