from listastatistiche.model.ListaStatistiche import ListaStatistiche


class ControllerListaStatistiche():
    def __init__(self):
        super(ControllerListaStatistiche, self).__init__()
        self.model = ListaStatistiche()

    #Metodo dedicato a richiamare il metodo nella classe ListaStatistiche per ottenere la lista delle statistiche
    def get_lista_statistiche(self):
        return self.model.get_lista_statistiche()

    #Metodo dedicato a richiamare il metodo nella classe ListaStatistiche per ottenere una statistica dalla lista grazie all'indice
    def get_statistica_by_index(self, index):
        return self.model.get_statistica_by_index(index)

    #Metodo dedicato a richiamare il metodo nella classe ListaStatistiche per slvare la lista delle statistiche
    def save_data(self):
        self.model.save_data()

    def costruzione_dizionario(self):
        self.model.costruzione_dizionario()