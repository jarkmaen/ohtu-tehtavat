from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return self.tekoaly.anna_siirto()
