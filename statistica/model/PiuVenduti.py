from statistica.model.Statistica import Statistica


class PiuVenduti(Statistica):
    piu_venduti = []
    def __init__(self):
        super(PiuVenduti, self).__init__("più venduti", "prodotti", 10)



