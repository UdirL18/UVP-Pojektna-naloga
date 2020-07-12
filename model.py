import random
from vprasanja import slovar, vprasanja_multiple_izbire1

STEVILO_DOVOLJENIH_NAPAK = 4
STEVILO_PRAVILNIH = 8
PRAVILEN_ODGOVOR = "+"
NI_ODGOVORA = "0"
NAPACEN_ODGOVOR = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "S"

class Igra:
    def __init__(self, st_vprasanj):
        self.trenutno_vprasanje_idx = 0
        self.pravilni_odgovori = 0
        self.vprasanja_mul = random.sample(list(vprasanja_multiple_izbire1), st_vprasanj)
        self.vprasanja = random.sample(list(slovar), st_vprasanj)

    def trenutno_vprasanje(self):
        if self.pravilni_odgovori >= 4:
            return self.vprasanja_mul[self.trenutno_vprasanje_idx] #vrne 'Koliko je vredna težina na sliki 11?'
        else:
            return self.vprasanja[self.trenutno_vprasanje_idx]

    def stevilo_napacnih(self):
        return self.trenutno_vprasanje_idx - self.pravilni_odgovori

    def stevilo_pravilnih(self):
        return self.pravilni_odgovori

    def zmaga(self):
        return self.pravilni_odgovori >= STEVILO_PRAVILNIH
    
    def poraz(self):
        return self.stevilo_napacnih() > STEVILO_DOVOLJENIH_NAPAK

    def ugibaj(self, odgovor):
        if odgovor == "":
            return NI_ODGOVORA
        if self.pravilni_odgovori >= 4: #vprasanja_multiple_izbire1['Koliko je vredna...?'] vrne '0.1'
            pravilen_odgovor = vprasanja_multiple_izbire1[self.trenutno_vprasanje()] 
        else:    
            pravilen_odgovor = slovar[self.trenutno_vprasanje()]
        self.trenutno_vprasanje_idx += 1
        if odgovor == pravilen_odgovor:
            self.pravilni_odgovori += 1
            if self.zmaga(): 
                return ZMAGA
            return PRAVILEN_ODGOVOR
        else:
            if self.poraz():
                return PORAZ
            return NAPACEN_ODGOVOR

def nova_igra():
    return Igra(STEVILO_PRAVILNIH + STEVILO_DOVOLJENIH_NAPAK)

class Kviz:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, odgovor):
        igra = self.igre[id_igre][0]
        stanje = igra.ugibaj(odgovor)
        self.igre[id_igre] = (igra, stanje)