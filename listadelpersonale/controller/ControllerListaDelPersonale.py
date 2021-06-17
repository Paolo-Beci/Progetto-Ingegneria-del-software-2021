from listadelpersonale.model.ListaDelPersonale import ListaDelPersonale


class ControllerListaDelPersonale:
    def __init__(self):
        super(ControllerListaDelPersonale, self).__init__()
        self.model = ListaDelPersonale()

    def get_lista_del_personale(self):
        return self.model.get_lista_del_personale()

    def get_lista_dinamica(self):
        return self.model.get_lista_dinamica()

    def refresh_data(self):
        self.model.refresh_data()

    def inserisci_utente(self, utente):
        self.model.lista_del_personale.append(utente)

    def get_utente_by_index(self, index):
        return self.model.get_utente_by_index(index)

    def elimina_utente_by_codice(self, codice_utente, lista_dinamica):
        self.model.elimina_utente_by_codice(codice_utente, lista_dinamica)

    def save_data(self):
        self.model.save_data()

    def get_status(self):
        return self.model.login

    def set_status(self, value):
        self.model.login= value