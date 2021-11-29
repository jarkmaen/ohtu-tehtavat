KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.lukujono = [0] * kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lukumaara = 0

    def kuuluu(self, luku):
        return luku in self.lukujono

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        elif self.alkioiden_lukumaara == len(self.lukujono):
            vanha_taulukko = self.lukujono
            self.kopioi_taulukko(self.lukujono, vanha_taulukko)
            self.lukujono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
            self.kopioi_taulukko(vanha_taulukko, self.lukujono)

        self.lukujono[self.alkioiden_lukumaara] = luku
        self.alkioiden_lukumaara += 1

        return True

    def poista(self, luku):
        for i in range(0, self.alkioiden_lukumaara):
            if luku == self.lukujono[i]:
                self.lukujono.pop(i)
                self.alkioiden_lukumaara -= 1
                return True

        return False

    def kopioi_taulukko(self, a_taulukko, b_taulukko):
        for i in range(0, len(a_taulukko)):
            b_taulukko[i] = a_taulukko[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a_joukko, b_joukko):
        tulos = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            tulos.lisaa(b_taulu[i])

        return tulos

    @staticmethod
    def leikkaus(a_joukko, b_joukko):
        tulos = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    tulos.lisaa(b_taulu[j])

        return tulos

    @staticmethod
    def erotus(a_joukko, b_joukko):
        tulos = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            tulos.poista(b_taulu[i])

        return tulos

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
            tuotos = tuotos + "}"
            return tuotos
