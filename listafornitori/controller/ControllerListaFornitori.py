import datetime

from dateutil.relativedelta import relativedelta

from listafornitori.model.ListaFornitori import ListaFornitori


class ControllerListaFornitori():
    def __init__(self):
        super(ControllerListaFornitori, self).__init__()
        self.model= ListaFornitori()
        self.controllo_stato()

    def get_lista_fornitori(self):
        return self.model.get_lista_fornitori()

    def inserisci_fornitore(self, fornitore):
        self.model.inserisci_fornitore(fornitore)

    def get_stato_fornitore_by_code(self, codice):
        return self.model.get_stato_fornitore_by_code(codice)

    def elimina_fornitore_by_codice(self, codice_fornitore, lista_dinamica):
        self.model.elimina_fornitore_by_codice(codice_fornitore, lista_dinamica)

    # Controllo: dopo 2 anni da data_affiliazione lo stato passa da Standard a Premium
    def controllo_stato(self):
        data_odierna = datetime.datetime.now()
        for fornitore in self.get_lista_fornitori():
            data= fornitore.data_affiliazione
            data_split= data.split("/")
            gg= data_split[0]
            mm= data_split[1]
            aaaa= data_split[2]
            data_affiliazione= datetime.datetime(int(aaaa), int(mm), int(gg))
            difference= relativedelta(data_odierna, data_affiliazione)
            if int(difference.years) >=2:
                fornitore.stato = "P"



    def refresh_data(self):
        self.model.refresh_data()

    def save_data(self):
        self.model.save_data()
