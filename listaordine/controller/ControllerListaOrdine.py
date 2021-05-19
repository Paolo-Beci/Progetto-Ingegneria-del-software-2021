from ordine.model.ListaOrdine import ListaOrdine


class ControllerListaOrdine:
    def __init__(self):
        super(ControllerListaOrdine, self).__init__()
        self.model = ListaOrdine()
    def get_filtra_ordine(self,codice_fattura):
        return self.model.get_lista_ordine()
    def get_lista_ordine(self):
        return self.model.get_lista_ordine()

    def inserisci_ordine(self, ordine):
        self.model.aggiungi_ordine(ordine)

    def save_data(self):
        self.model.save_data()
