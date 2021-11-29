from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_list = []

    def tavaroita_korissa(self): 
        tavaroita = 0
        for ostos in self.ostokset_list:
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        summa = 0
        for ostos in self.ostokset_list:
            summa += ostos.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset_list:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        self.ostokset_list.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset_list:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                return

    def tyhjenna(self):
        self.ostokset_list.clear()

    def ostokset(self):
        return self.ostokset_list
