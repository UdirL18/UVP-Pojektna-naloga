import random
from vprasanja import slovar, vprasanja_multiple_izbire1, riziki #riziki_obroc, riziki_zoga, riziki_kiji, riziki_trak

STEVILO_DOVOLJENIH_NAPAK = 8 #potem spremeni na 3
STEVILO_PRAVILNIH = 12
KVIZ_MULTIPLE = 4
KVIZ_RIZIKI = 8
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
        self.vprasanja_riziki = random.sample(list(riziki), 1)[0] #vrne npr "trak"

    def trenutno_vprasanje(self):
        if self.pravilni_odgovori >= KVIZ_RIZIKI:
            #ali obstaja bolj eleganten način?
            return riziki.get(self.vprasanja_riziki) #vrne "Določi kriterije rizikov s trakom."
        if self.pravilni_odgovori in range(KVIZ_MULTIPLE, KVIZ_RIZIKI):
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
        if self.pravilni_odgovori >= KVIZ_RIZIKI:
            pravilen_odgovor = True
        if self.pravilni_odgovori in range(KVIZ_MULTIPLE, KVIZ_RIZIKI): #vprasanja_multiple_izbire1['Koliko je vredna...?'] vrne '0.1'
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