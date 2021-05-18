from listaprodotti.model.ListaProdotti import ListaProdotti


class ControllerListaProdotti:
    def __init__(self):
        super(ControllerListaProdotti, self).__init__()
        self.model = ListaProdotti()

    def get_lista_prodotti(self):
        return self.model.get_lista_prodotti()

    def inserisci_prodotto(self, prodotto):
        self.model.aggiungi_prodotto(prodotto)

    def get_prodotto(self, index):
        return self.model.get_prodotto(index)

    def elimina_prodotto(self, codice_utente):
        self.model.elimina_prodotto(codice_utente)

    def save_data(self):
        self.model.save_data()
