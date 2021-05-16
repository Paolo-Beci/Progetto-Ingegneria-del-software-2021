from listadelpersonale.model.ListaDelPersonale import ListaDelPersonale


class ControllerListaDelPersonale:
    def __init__(self):
        super(ControllerListaDelPersonale, self).__init__()
        self.model = ListaDelPersonale()

    def get_lista_del_personale(self):
        return self.model.get_lista_del_personale()

    def inserisci_utente(self, utente):
        self.model.lista_del_personale.append(utente)

    def save_data(self):
        self.model.save_data()