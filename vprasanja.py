#==============================================================================================
# VPRAŠANJA OPISNIH ODGOVOROV
#==============================================================================================
#moram napisati še primere odgovorov
slovar = {1:{"tip":"tip_0", "vprasanje": "Kolikšna je dolžina induvidualne sestave?", "primer_odg": "m:ss-m:ss", "odgovor": ["1:15-1:30"]},
2:{"tip": "tip_0", "vprasanje": "Kakšen je trenutni program za induvidualne tekmovake?", "primer_odg": "Naštej rekvizite po vrsti, kot se tekmujejo na F.I.G. tekmovanjih.", "odgovor": ["OBROČ,ŽOGA,KIJI,TRAK"]}, 
3:{"tip": "tip_0", "vprasanje": "Kolikšna je dolžina skupinske sestave?", "primer_odg": "m:ss - m:ss", "odgovor": ["2:15-2:30"]},
4:{"tip": "tip_0", "vprasanje": "Kakšen je program za skupinske sestave?", "primer_odg": "3+2, 5, 6, 3+3", "odgovor": ["3+2,5", "5,3+2"]},
5:{"tip": "tip_0", "vprasanje": "Kolikšen je 'odbitek za predolgo glasbo'?", "primer_odg": "0.10", "odgovor": ["0.05"]},
6:{"tip": "tip_0", "vprasanje": "Kolikšna je dovoljena dolžina glasbenega uvoda?", "primer_odg": "n sekunde", "odgovor": ["4sekunde", "4s", "4"] },
7:{"tip": "tip_0", "vprasanje": "Kdo odbije 'odbitek za predolg glasbeni uvod'?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["E1,E2", "E1,E2"]},
8:{"tip": "tip_0", "vprasanje": "Kolikšen je 'odbitek za predolg glasbeni uvod'?", "primer_odg": "0.10", "odgovor": ["0.30", "0.3"]},
9:{"tip": "tip_0", "vprasanje": "Kolikšen je 'odbitek za neprimerno glasbo' (npr. sirene, motor, itd.)?", "primer_odg": "0.10", "odgovor": ["0.50", "0.5"]},
10:{"tip": "tip_0", "vprasanje": "Koliko od štirih glasb, na katere tekmovalka izvaja vajo, lahko vsebuje besedilo (melodija s petjem)?", "primer_odg": "4", "odgovor": ["2", "DVE"]},
11:{"tip": "tip_0", "vprasanje": "Kdo odbija odbitke, v primeru ko glasba ni v skladu s pravilnikom?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["D1"]},
12:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, v primeru ko tekmovalka uporabi dodatno glasbo s petjem?", "primer_odg": "0.01", "odgovor": ["1.00", "1"]},
13:{"tip": "tip_0", "vprasanje": "Kdo sodi težine s telesom in plesne korake?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["D1,D2", "D2,D1"]},
14:{"tip": "tip_0", "vprasanje": "Kdo sodi rizike in težine z rekvizitom?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["D3,D4", "D4,D3"]},
15:{"tip": "tip_0", "vprasanje": "Kdo sodi artistične komponente sestave?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["E1,E2", "E2,E1"]},
16:{"tip": "tip_0", "vprasanje": "Kdo sodi izvedbene napake?", "primer_odg": "D1, D2, D3, D4, E1, E2, E3, E4, E5, E6", "odgovor": ["E3,E4,E5,E6"]}, 
17:{"tip": "tip_0", "vprasanje": "Na kateri del ocene se lahko pritoži trener?", "primer_odg": "D, E", "odgovor": ["D"]},
18:{"tip": "tip_0", "vprasanje": "Kolikšen je 'odbitek za prestop'?", "primer_odg": "0.10", "odgovor": ["0.30", "0.3"]},
19:{"tip": "tip_0", "vprasanje": "Kolikšen je 'odbitek za neustrezen rekvizit'?", "primer_odg": "0.10", "odgovor": ["0.50", "0.5"]},
20:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, v primeru ko tekmovani dres ne ustreza zahtevam?", "primer_odg": "0.10", "odgovor": ["0.30", "0.3"]},
21:{"tip": "tip_0", "vprasanje": "Ali lahko tekmovalke med sestavo komunicirajo?", "primer_odg": "da", "odgovor": ["NE"]},
22:{"tip": "tip_0", "vprasanje": "Ali trener med izvajanjem sestave lahko podaja napotke tekmovalki?", "primer_odg": "ne", "odgovor": ["NE"]},
23:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, če trenerka nakaže vajo tekmovalkam, med tem ko le-te tekmujejo?", "primer_odg": "0.10", "odgovor": ["0.50", "0.5"]},
24:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, če ima tekmovalka nekožnate bandaže?", "primer_odg": "0.10", "odgovor": ["0.30", "0.3"]}
}

#========================================================================================================================================
# VPRAŠANJA MULTIPLE IZBIRE
#========================================================================================================================================
vprasanja_multiple_izbire = {1:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?",
 "odgovor": "0.1", "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://ssl.c.photoshelter.com/img-get/I0000tMsoaFK6TWs/s/860/860/lima384-2-baku20051005por-600tsw.jpg"},
2:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.1",
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/originals/29/98/a8/2998a8e2bc0c39267bb622136873b872.jpg"},
3:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.4", 
"mozni_odg": [0.3, 0.4, 0.5], "slika": "https://www.avrhythmic.org.uk/wp-content/images/Marfa-ball-good-balance-2.jpg"},
4:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.2", 
"mozni_odg": [0.1, 0.2, 0.3], "slika" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTsbF9TnzYJMm8MmZ_Pv60Ca7RDGlx0w7wOmQ&usqp=CAU"},
5:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.3",
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQrR3yExQ8NwEp5EkcDKzileH6_nncUnG09fw&usqp=CAU"},
6:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.4",
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://gymnastics.sport/publicdir/wog/72-77/76-eng/images/150912339-rg-wch-stuttgart-ger-2015-mamun-margarita-rus-crop-u52330.jpg"},
7:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.3",
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://www.jozikids.co.za/uploadimages/gold_reef_gymnastics3_large.jpg"},
8:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.5",
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://s3media.freemalaysiatoday.com/wp-content/uploads/2019/09/rhythmic-gymnastics-Bernama.jpg"},
9:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.3",
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://i.pinimg.com/originals/38/18/68/3818681c77ed4897db05ca8e26604091.jpg"},
10:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.5",
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://c8.alamy.com/comp/PK7JBA/september-11-2018-aleksandra-soldatova-of-russia-during-rhythmic-gymnastics-world-championships-at-the-arena-armeec-in-sofia-at-the-36th-fig-rhythmic-gymnastics-world-championships-ulrik-pedersencsm-PK7JBA.jpg"},
11:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.3",
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://lh6.googleusercontent.com/proxy/7hLtTUZcg3s6xSg8KI1RpAsdUaCAbrS3rCjTC5WujXh4pLpMvOM7Foy-JxBhwOtFeMRTfqS5-DH2b-qMSDfU0v6aiYw9KtkiiJWa1w"},
12:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.3",
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/236x/d0/65/95/d06595a633104bc8e5d51d9e1d273be2--gymnastics-events-gymnastics-clubs.jpg"},
13:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.5",
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://i.pinimg.com/736x/68/83/8c/68838c1ecd55440ef55a6ed5f0f47b7e.jpg"},
14:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.5",
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://c8.alamy.com/comp/TXF6DW/rhythmic-gymnastics-star-anna-bessonova-of-ukraine-balances-with-the-clubs-in-all-around-at-rhythmic-gymnastics-world-championships-in-baku-azerbaijan-october-8-2005-upi-phototom-theobald-TXF6DW.jpg"},
15:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.4",
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://ssl.c.photoshelter.com/img-get/I0000hVXW1TY7Gj8/s/860/860/51272zhukova-pat20070921blr300.jpg"},
16:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.2",
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/originals/72/56/2f/72562f626db66c2125ad6432e3c87014.jpg"},
17:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.2",
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGWuLSsj6itQVDqjFzIymc7rt6aqjdd7g5FUL-ygbquj-dxgA&s"},
18:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki?", "odgovor": "0.5",
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://teamengland.org/media/20222_1517833173-image(_x1000).jpg"}}


#===========================================================================================================================================================
# VPRAŠANJA VEČIH PRAVILNIH ODGOVOROV
#===========================================================================================================================================================
# 1 - obro, 2 - žoga, 3 - kiji, 4 - trak
# riziki = {1:{"tip": "tip_2", "vprasanje": [{vpr:[odg]}, {:[]}, ], "mozni_odg": [], "video": "https"}, 2: ...}

riziki = {1:{"tip": "tip_2",
 "vprasanje": [{"vpr": "Kateri kriteriji se nanašajo na prvi rizik?", "odg": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na drugi rizik?", "odg": ["3 rotacije", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na tretji rizik?", "odg": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na četrti rizik?", "odg": ["3 rotacije", "položni met", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na peti rizik?", "odg": ["3 rotacije", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "položni met", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/embed/mdlKiwK6biI?autoplay=0"},
 2:{"tip": "tip_2",
 "vprasanje": [{"vpr": "Kateri kriteriji se nanašajo na prvi rizik?", "odg": ["4 rotacije", "met izven vidnega polja", "sprememba nivoja in/ali osi"]},
 {"vpr": "Kateri kriteriji se nanašajo na drugi rizik?", "odg": ["3 rotacije", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v eno roko", "ujem v rotacijo ", "jete en tournant with back bend 0.6"]},
 {"vpr": "Kateri kriteriji se nanašajo na tretji rizik?", "odg": ["4 rotacije", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v eno roko", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na četrti rizik?", "odg": ["3 rotacije", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "jete en tournant with ring 0.5"]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v eno roko", "ujem v rotacijo ", "jete en tournant with back bend 0.6", "jete en tournant with ring 0.5"],
 "video": "https://www.youtube.com/embed/PZZz0kp-IZE?autoplay=0"},
 3:{"tip": "tip_2",
 "vprasanje": [{"vpr": "Kateri kriteriji se nanašajo na prvi rizik?", "odg": ["4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi"]},
  {"vpr": "Kateri kriteriji se nanašajo na drugi rizik?", "odg": ["4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "sprememba nivoja in/ali osi", "ujem brez pomoči rok"]},
  {"vpr": "Kateri kriteriji se nanašajo na tretji rizik?", "odg": ["2 rotaciji", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "met dveh kijev"]},
  {"vpr": "Kateri kriteriji se nanašajo na četrti rizik?", "odg": ["3 rotacije", "met dveh kijev", "sprememba novoja/osi"]},
  {"vpr": "Kateri kriteriji se nanašajo na peti rizik?", "odg": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met brez pomoči rok", "sprememba nivoja in/ali osi"]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega polja", "met brez pomoči rok", "met dveh kijev", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/embed/wP5e27_0v04?autoplay=0"},
 4:{"tip": "tip_2",
 "vprasanje": [{"vpr": "Kateri kriteriji se nanašajo na prvi rizik?", "odg": ["5 rotacij", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v rotacijo"]},
 {"vpr": "Kateri kriteriji se nanašajo na drugi rizik?", "odg": ["4 rotacije", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na tretji rizik (v primeru dobre izvedbe)?", "odg": ["4 rotacije", "met izven vidnega polja", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"vpr": "Kateri kriteriji se nanašajo na četrti rizik?", "odg": ["3 rotacije", "sprememba nivoja in/ali osi"]}],
 "mozni_odg": ["3 rotacije", "4 rotacije", "5 rotacij", "met izven vidnega polja", "met brez pomoči rok", "sprememba nivoja in/ali osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/embed/VKiOTntDlFM?autoplay=0"}
}







    
    