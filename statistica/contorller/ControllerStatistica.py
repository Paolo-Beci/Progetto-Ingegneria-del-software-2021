class ControllerStatistica():
    def __init__(self, statistica):
        self.model = statistica

    def get_nome_statistica(self):
        return self.model.nome

    def get_tipo_statistica(self):
        return self.model.tipo

    def get_quantita_statistica(self):
        return self.model.quantita

    def calcola_statistica(self):
        pass