import random
from vprasanja import slovar, vprasanja_multiple_izbire, riziki 

#======================================================================================
#Definicija konstant
#======================================================================================
STEVILO_DOVOLJENIH_NAPAK = 5 
STEVILO_PRAVILNIH = 9
STEVILO_KVIZ_MULTIPLE = 4
STEVILO_KVIZ_RIZIKI = 8
PRAVILEN_ODGOVOR = "+"
NI_ODGOVORA = "0"
NAPACEN_ODGOVOR = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "S"
KVIZ_MULTIPLE = "M"
KVIZ_RIZIKI = "R"

#=============================================================================================
#Razred Igra
#=============================================================================================
class Igra:
    def __init__(self, st_vprasanj):
        self.trenutno_vprasanje_idx = 0
        self.pravilni_odgovori = 0
        self.vprasanja_mul = random.sample(list(vprasanja_multiple_izbire), st_vprasanj) #[1, 2,...]
        self.vprasanja = random.sample(list(slovar), st_vprasanj) #[5, 7, ...]
        self.vprasanja_riziki = random.sample(list(riziki), 1) #želim da bo na eno igro samo en video (vrne npr [1])

    def trenutno_vprasanje(self):
        if self.pravilni_odgovori >= STEVILO_KVIZ_RIZIKI:
            # želim da izpiše vseh 5 (oz 4) vprašanja
            vpr_2 = int(self.vprasanja_riziki[0]) # vrne npr 1
            return riziki.get(2) # vrne {"tip": "tip_2", "vprasanje": [{'vpr':'', 'odg': [odg]}, {:[]}, ], "mozni_odg": [], "video": "https"}
        if self.pravilni_odgovori in range(STEVILO_KVIZ_MULTIPLE, STEVILO_KVIZ_RIZIKI):
            vpr_1 = self.vprasanja_mul[self.trenutno_vprasanje_idx] #vrne npr 18
            return vprasanja_multiple_izbire.get(vpr_1) #{'tip': 'tip_1', 'vprasanje': 'Koliko je vredna težina na sliki 18?', 'odgovor': '0.4', 'mozni_odg': [0.4, 0.5, 0.6], 'slika': 'http'}
        else:
            vpr_0 = self.vprasanja[self.trenutno_vprasanje_idx] #vrne npr 4
            return slovar.get(vpr_0) #{'tip': 'tip_0', 'vprasanje': '?', 'primer_odg':'', 'odgovor': ''}

    def stevilo_napacnih(self):
        return self.trenutno_vprasanje_idx - self.pravilni_odgovori

    def stevilo_pravilnih(self):
        return self.pravilni_odgovori

    def tip_2(self):
        return self.pravilni_odgovori == STEVILO_KVIZ_RIZIKI

    def tip_1(self):
        return self.pravilni_odgovori in range(STEVILO_KVIZ_MULTIPLE, STEVILO_KVIZ_RIZIKI)

    def zmaga(self):
        return self.pravilni_odgovori == STEVILO_PRAVILNIH
    
    def poraz(self):
        return self.stevilo_napacnih() > STEVILO_DOVOLJENIH_NAPAK

## uredi ker imaš dvakrat za brez veze if za isto stvar
    def enakost_odgovorov(self, odgovor):
        if self.pravilni_odgovori >= STEVILO_KVIZ_RIZIKI:
            seznam_vpr = self.trenutno_vprasanje().get('vprasanje') # [{'vpr':'','odg':[]}, {vpr:odg}, ...]
        pravilen_odgovor = []
        for slovar_vpr in vpr:
            pravilen_odg_na_eno_vpr = slovar_vpr.get('odg')
            pravilen_odgovor.append(pravilen_odg_na_eno_vpr) #[['3 rotacije', 'takojšen odboj / ponovni met '], [za 2 vpr], [za 3 vpr], ...] 
            self.trenutno_vprasanje_idx += 1
            #iz serverja odgovori: [('odgovor_0', '2 rotaciji'), ('odgovor_1', '3 rotacije')]
            samo_odgovori = []
            for polje, vrednost in odgovor:
                samo_odgovori.append(vrednost) #['2 rotaciji', '3 rotacije']
            return samo_odgovori == pravilen_odgovor                                       
        if self.pravilni_odgovori in range(STEVILO_KVIZ_MULTIPLE, STEVILO_KVIZ_RIZIKI): 
            pravilen_odgovor = self.trenutno_vprasanje().get("odgovor") # vrne npr 0.4
            self.trenutno_vprasanje_idx += 1
            return odgovor == pravilen_odgovor #vrne True 
        else: 
            pravilen_odgovor = self.trenutno_vprasanje().get("odgovor") # vrne list
            self.trenutno_vprasanje_idx += 1 
            return any(x.upper().replace(" ","") == odgovor.upper().replace(" ","") for x in pravilen_odgovor) 
            #odgovorom, ki pridejo iz serverja ostranim space in jih dam v velike črke, 
            #to naredim še za odgovore iz slovarja, če bo kdo slučajno kdaj dodajal vprašanja



    def ugibaj(self, odgovor):
        if odgovor == "":
            return NI_ODGOVORA #vrne "0"
        if self.enakost_odgovorov(odgovor) == True:
            self.pravilni_odgovori += 1
            if self.tip_2(): 
                return KVIZ_RIZIKI
            elif self.tip_1(): 
                return KVIZ_MULTIPLE                            
            if self.zmaga(): 
                return ZMAGA
            return PRAVILEN_ODGOVOR
        else:
            if self.poraz():
                return PORAZ
            return NAPACEN_ODGOVOR

#===========================================================================================
#Funkcija, ki vrne novo igro.
#===========================================================================================
def nova_igra():
    return Igra(STEVILO_PRAVILNIH + STEVILO_DOVOLJENIH_NAPAK)
# STEVILO_PRAVILNIH + STEVILO_DOVOLJENIH_NAPAK ne sme biti večje od št vprašanj v slovarjih

#================================================================================================
#Razred Kviz
#================================================================================================
class Kviz:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1 #dict_keys([1, 2]), max vrne 2, prost_id_igre vrne 3

    def nova_igra(self):
        igra = nova_igra() #Igra(st_vprasanj)
        id_igre = self.prost_id_igre() 
        self.igre[id_igre] = (igra, ZACETEK) #igre[id_igre] vrne vrednosti pri tem ključu 
        return id_igre

    def ugibaj(self, id_igre, odgovor):
        igra = self.igre[id_igre][0] 
        stanje = igra.ugibaj(odgovor)
        self.igre[id_igre] = (igra, stanje) # stanje "R", "M", "W", "X" in "0", "-", "+"

