LISTAN_KOKO = 5
OLETUSKASVATUSKOKO = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, listan_koko=LISTAN_KOKO, kasvatuskoko=OLETUSKASVATUSKOKO):
        if not isinstance(listan_koko, int) or listan_koko < 0:
            raise ValueError("Kapasiteetin täytyy olla positiivinen kokonaisluku!")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon täytyy olla positiivinen kokonaisluku!")
            
        self.listan_koko = listan_koko
        self.kasvatuskoko = kasvatuskoko
        self.alkiolista = self._luo_lista(self.listan_koko)
        self.alkioiden_lkm = 0

    def alkio_listalla(self, luku):
        return luku in self.alkiolista[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if self.alkio_listalla(luku):
            return False
        
        if self.alkioiden_lkm == len(self.alkiolista):
            self._kasvata_listaa()
        
        self.alkiolista[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True
    
    def _kasvata_listaa(self):
        uusi_lista = self._luo_lista(len(self.alkiolista) + self.kasvatuskoko)
        self.kopioi_lista(self.alkiolista, uusi_lista)
        self.alkiolista = uusi_lista

    def poista(self, luku):
        indeksi = self.alkiolista.index(luku, 0, self.alkioiden_lkm)
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.alkiolista[i] = self.alkiolista[i + 1]
        
        self.alkioiden_lkm -= 1
        return True

    def kopioi_lista(self, alkuperainen_lista, uusi_lista):
        uusi_lista[:len(alkuperainen_lista)] = alkuperainen_lista

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.alkiolista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        for alkio in joukko_a.to_int_list() + joukko_b.to_int_list():
            tulosjoukko.lisaa(alkio)
        return tulosjoukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        set_a = set(joukko_a.to_int_list())
        set_b = set(joukko_b.to_int_list())

        for alkio in set_a & set_b:
            tulosjoukko.lisaa(alkio)

        return tulosjoukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        tulosjoukko = IntJoukko()
        set_a = set(joukko_a.to_int_list())
        set_b = set(joukko_b.to_int_list())

        for alkio in set_a - set_b:
            tulosjoukko.lisaa(alkio)

        return tulosjoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.alkiolista[:self.alkioiden_lkm])) + "}"
