import json
import pickle
import os.path  # Ci consente di leggere all'interno di una cartella

from statistica.model.Statistica import Statistica


class ListaStatistiche():
    def __init__(self):
        super(ListaStatistiche, self).__init__()
        self.lista_statistiche = []
        if os.path.isfile('listastatistiche/data/lista_statistiche_salvata.pickle'):
            with open('listastatistiche/data/lista_statistiche_salvata.pickle', 'rb') as f:
                self.lista_statistiche = pickle.load(f)
        else:
            with open('listastatistiche/data/lista_statistiche_iniziali.json') as f:
                lista_statistiche_iniziali = json.load(f)
            for statistica_iniziale in lista_statistiche_iniziali:
                self.aggiungi_statistica(Statistica(statistica_iniziale["nome"],
                                    statistica_iniziale["quantita"], statistica_iniziale["quantita"],))

    #Metodo che ci consente di inserire una statistica alla liste delle statistiche
    def aggiungi_statistica(self, statistica):
        self.lista_statistiche.append(statistica)

    #Metodo che ci consente di ottenere un servizio dalla lista dei servizi grazie all'indice
    def get_statistica_by_index(self, index):
        return self.lista_statistiche[index]

    #Metodo che ci consente di ottenere la lista completa delle statistiche
    def get_lista_statistiche(self):
        return self.lista_statistiche

    #Metodo che ci consente di salvare i dati
    def save_data(self):
        with open('listastatistiche/data/lista_statistiche.pickle', 'wb') as handle:
            pickle.dump(self.lista_statistiche, handle, pickle.HIGHEST_PROTOCOL)
