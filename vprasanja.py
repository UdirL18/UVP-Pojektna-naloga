#==============================================================================================
# VPRAŠANJA OPISNIH ODGOVOROV
#==============================================================================================
#moram napisati še primere odgovorov
slovar = {1:{"tip":"tip_0", "vprasanje": "Kakšna je dolžina induvidualne sestave?", "odgovor": " 1:15 - 1:30"},
2:{"tip": "tip_0", "vprasanje": "Kakšen je trenutni program za induvidualne tekmovake?", "odgovor": "obroč, žoga, kiji, trak"},
3:{"tip": "tip_0", "vprasanje": "Kakšna je dolžina skupinske sestave?", "odgovor": "2:15 - 2:30"},
4:{"tip": "tip_0", "vprasanje": "Kakšen je program za skupinske sestave?", "odgovor": "sestava z enim tipom rekvizita in z dvema tipoma rekvizitov"},
5:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek za predolgo glasbo?", "odgovor": "0.05"},
6:{"tip": "tip_0", "vprasanje": "Kako dolg je lahko uvod glasbe?", "odgovor": "4 sekunde"},
7:{"tip": "tip_0", "vprasanje": "Kdo odbije odbitek za predolg glasbeni uvod?", "odgovor": "sodnice za artistiko"},
8:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek za predolg glasbeni uvod?", "odgovor": "0.30"},
9:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek za neprimerni glasbo (npr. sirene, motor, itd.)?", "odgovor": "0.50"},
10:{"tip": "tip_0", "vprasanje": "Koliko glasb s petjem ima lahko tekmovalka?", "odgovor": "2"},
11:{"tip": "tip_0", "vprasanje": "Kdo odbije odbitke če glasba ni v skladu s pravilnikom?", "odgovor": "sodnica koordinatorka"},
12:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek če tekmovalka uporabi dodatno glasbo s petjem?", "odgovor": "1.00"},
13:{"tip": "tip_0", "vprasanje": "Kdo sodi težine s telesom in plesne korake?", "odgovor": "D1, D2"},
14:{"tip": "tip_0", "vprasanje": "Kdo sodi rizike in težine z rekvizitom?", "odgovor": "D3, D4"},
15:{"tip": "tip_0", "vprasanje": "Kdo sodi artistične komponente sestave?", "odgovor": "E1, E2"},
16:{"tip": "tip_0", "vprasanje": "Kdo sodi izvedbene napake?", "odgovor": "E3, E4, E5, E6"},
17:{"tip": "tip_0", "vprasanje": "Na kateri del ocene se lahko pritoži trener?", "odgovor": "D"},
18:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek za prestop?", "odgovor": "0.30"},
19:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek za neustrezen rekvizit?", "odgovor": "0.50"},
20:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, če tekmovani dres ne ustreza zahtevam?", "odgovor": "0.30"},
21:{"tip": "tip_0", "vprasanje": "Ali lahko tekmovalke med sestavo komunicirajo?", "odgovor": "ne"},
22:{"tip": "tip_0", "vprasanje": "Ali lahko trener daje napotke tekmovalki med izvajanjem sestave?", "odgovor": "ne"},
23:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, če trenerka kaže vajo med tem ko dekleta tekmujejo?", "odgovor": "0.50"},
24:{"tip": "tip_0", "vprasanje": "Kolikšen je odbitek, če ima tekmovalka nekožnate bandaže?", "odgovor": "0.30"}
}

#========================================================================================================================================
# VPRAŠANJA MULTIPLE IZBIRE
#========================================================================================================================================
vprasanja_multiple_izbire1 = {1:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 1?",
 "odgovor": 0.1, "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://ssl.c.photoshelter.com/img-get/I0000tMsoaFK6TWs/s/860/860/lima384-2-baku20051005por-600tsw.jpg"},
2:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 2?", "odgovor": 0.1,
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/originals/29/98/a8/2998a8e2bc0c39267bb622136873b872.jpg"},
3:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 3?", "odgovor": 0.4, 
"mozni_odg": [0.3, 0.4, 0.5], "slika": "https://www.avrhythmic.org.uk/wp-content/images/Marfa-ball-good-balance-2.jpg"},
4:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 4?", "odgovor": 0.2, 
"mozni_odg": [0.1, 0.2, 0.3], "slika" : "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTsbF9TnzYJMm8MmZ_Pv60Ca7RDGlx0w7wOmQ&usqp=CAU"},
5:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 5?", "odgovor": 0.3,
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQrR3yExQ8NwEp5EkcDKzileH6_nncUnG09fw&usqp=CAU"},
6:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 6?", "odgovor": 0.3,
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://images.haarets.co.il/image/fetch/w_2048,h_1536,c_crop/q_auto,h_900,w_1200,c_fill,f_auto/fl_lossy.any_format.preserve_transparency.progressive:non/https://www.haaretz.co.il/polopoly_fs/1.5531863!/image/1018316866.jpg"},
7:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 7?", "odgovor": 0.3,
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://www.jozikids.co.za/uploadimages/gold_reef_gymnastics3_large.jpg"},
8:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 8?", "odgovor": 0.5,
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://s3media.freemalaysiatoday.com/wp-content/uploads/2019/09/rhythmic-gymnastics-Bernama.jpg"},
9:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 9?", "odgovor": 0.3,
 "mozni_odg": [0.2, 0.3, 0.4], "slika": "https://i.pinimg.com/originals/38/18/68/3818681c77ed4897db05ca8e26604091.jpg"},
10:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 10?", "odgovor": 0.5,
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://c8.alamy.com/comp/PK7JBA/september-11-2018-aleksandra-soldatova-of-russia-during-rhythmic-gymnastics-world-championships-at-the-arena-armeec-in-sofia-at-the-36th-fig-rhythmic-gymnastics-world-championships-ulrik-pedersencsm-PK7JBA.jpg"},
11:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 11?", "odgovor": 0.3,
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://lh6.googleusercontent.com/proxy/7hLtTUZcg3s6xSg8KI1RpAsdUaCAbrS3rCjTC5WujXh4pLpMvOM7Foy-JxBhwOtFeMRTfqS5-DH2b-qMSDfU0v6aiYw9KtkiiJWa1w"},
12:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 12?", "odgovor": 0.3,
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/236x/d0/65/95/d06595a633104bc8e5d51d9e1d273be2--gymnastics-events-gymnastics-clubs.jpg"},
13:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 13?", "odgovor": 0.5,
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://i.pinimg.com/736x/68/83/8c/68838c1ecd55440ef55a6ed5f0f47b7e.jpg"},
14:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 14?", "odgovor": 0.5,
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://c8.alamy.com/comp/TXF6DW/rhythmic-gymnastics-star-anna-bessonova-of-ukraine-balances-with-the-clubs-in-all-around-at-rhythmic-gymnastics-world-championships-in-baku-azerbaijan-october-8-2005-upi-phototom-theobald-TXF6DW.jpg"},
15:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 15?", "odgovor": 0.4,
 "mozni_odg": [0.3, 0.4, 0.5], "slika": "https://ssl.c.photoshelter.com/img-get/I0000hVXW1TY7Gj8/s/860/860/51272zhukova-pat20070921blr300.jpg"},
16:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 16?", "odgovor": 0.2,
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://i.pinimg.com/originals/72/56/2f/72562f626db66c2125ad6432e3c87014.jpg"},
17:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 17?", "odgovor": 0.2,
 "mozni_odg": [0.1, 0.2, 0.3], "slika": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGWuLSsj6itQVDqjFzIymc7rt6aqjdd7g5FUL-ygbquj-dxgA&s"},
18:{"tip":"tip_1", "vprasanje": "Koliko je vredna težina na sliki 18?", "odgovor": 0.4,
 "mozni_odg": [0.4, 0.5, 0.6], "slika": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRt-VJJqT51HMTpdjYVDq56SslkWwD6hta8D67ffxojawjyMyG&s"}}


#===========================================================================================================================================================
# VPRAŠANJA VEČIH PRAVILNIH ODGOVOROV
#===========================================================================================================================================================
# 1 - obro, 2 - žoga, 3 - kiji, 4 - trak
# riziki = {1:{"tip": "tip_2", "vprasanje": [{vpr:[odg]}, {:[]}, ], "mozni_odg": [], "video": "https"}, 2: ...}

riziki = {1:{"tip": "tip_2",
 "vprasanje": [{"Kateri kriteriji se nanašajo na prvi rizik?": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na drugi rizik?": ["3 rotacije", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na tretji rizik?": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na četrti rizik?": ["3 rotacije", "položni met", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na peti rizik?": ["3 rotacije", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "položni met", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/watch?v=ZOPpRz0bwRQ"},
 2:{"tip": "tip_2",
 "vprasanje": [{"Kateri kriteriji se nanašajo na prvi rizik?": ["4 rotacije", "met izven vidnega", "sprememba nivoja/osi"]},
 {"Kateri kriteriji se nanašajo na drugi rizik?": ["3 rotacije", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v eno roko", "ujem v rotacijo ", "jete en tournant with back bend 0.6"]},
 {"Kateri kriteriji se nanašajo na tretji rizik?": ["4 rotacije", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v eno roko", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na četrti rizik?": ["3 rotacije", "sprememba nivoja/osi", "ujem izven vidnega polja", "jete en tournant with ring 0.5"]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v eno roko", "ujem v rotacijo ", "jete en tournant with back bend 0.6", "jete en tournant with ring 0.5"],
 "video": "https://www.youtube.com/watch?v=HjqlQ8VnKqw"},
 3:{"tip": "tip_2",
 "vprasanje": [{"Kateri kriteriji se nanašajo na prvi rizik?": ["4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi"]},
  {"Kateri kriteriji se nanašajo na drugi rizik?": ["4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "sprememba nivoja/osi", "ujem brez pomoči rok"]},
  {"Kateri kriteriji se nanašajo na tretji rizik?": ["2 rotaciji", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "met dveh kijev"]},
  {"Kateri kriteriji se nanašajo na četrti rizik?": ["3 rotacije", "met dveh kijev", "sprememba novoja/osi"]},
  {"Kateri kriteriji se nanašajo na peti rizik?": ["3 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met brez pomoči rok", "sprememba nivoja/osi"]}],
 "mozni_odg": ["2 rotaciji", "3 rotacije", "4 rotacije", "met z rotacijo okoli svoje osi (diametralni met)", "met izven vidnega", "met brez pomoči rok", "met dveh kijev", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/watch?v=wP5e27_0v04"},
 4:{"tip": "tip_2",
 "vprasanje": [{"Kateri kriteriji se nanašajo na prvi rizik?": ["5 rotacij", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v rotacijo"]},
 {"Kateri kriteriji se nanašajo na drugi rizik?": ["4 rotacije", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na tretji rizik (v primeru dobre izvedbe)?": ["4 rotacije", "met izven vidnega", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem v rotacijo "]},
 {"Kateri kriteriji se nanašajo na četrti rizik?": ["3 rotacije", "sprememba nivoja/osi"]}],
 "mozni_odg": ["3 rotacije", "4 rotacije", "5 rotacij", "met izven vidnega", "met brez pomoči rok", "sprememba nivoja/osi", "ujem izven vidnega polja", "ujem brez pomoči rok", "ujem v rotacijo "],
 "video": "https://www.youtube.com/watch?v=VKiOTntDlFM"}
}






    
    