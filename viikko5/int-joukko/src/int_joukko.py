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

    def alkio_listalla(self, n):
        return n in self.alkiolista[:self.alkioiden_lkm]

    def lisaa(self, n):
        ei_ole = 0

        if self.alkioiden_lkm == 0:
            self.alkiolista[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.alkio_listalla(n):
            self.alkiolista[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.alkiolista) == 0:
                taulukko_old = self.alkiolista
                self.kopioi_lista(self.alkiolista, taulukko_old)
                self.alkiolista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.alkiolista)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.alkiolista[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.alkiolista[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.alkiolista[j]
                self.alkiolista[j] = self.alkiolista[j + 1]
                self.alkiolista[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.alkiolista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.alkiolista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.alkiolista[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.alkiolista[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
