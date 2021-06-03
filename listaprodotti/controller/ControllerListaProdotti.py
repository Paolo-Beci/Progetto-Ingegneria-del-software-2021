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

    def get_prodotto_by_code(self, code):
        return self.model.get_prodotto_by_code(code)

    def get_nome_prodotto_by_code(self, codice):
        return self.model.get_nome_prodotto_by_code(codice)

    def get_anno_prodotto_by_code(self, codice):
        return self.model.get_anno_prodotto_by_code(codice)

    def elimina_prodotto_by_codice(self, codice_prodotto):
        self.model.elimina_prodotto(codice_prodotto)

    def save_data(self):
        self.model.save_data()
