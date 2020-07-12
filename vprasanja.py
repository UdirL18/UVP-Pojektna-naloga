
#moram napisati še primere odgovorov
slovar = {"Kakšna je dolžina induvidualne sestave?":" 1:15 - 1:30",
"Kakšen je trenutni program za induvidualne tekmovake?":"obroč, žoga, kiji, trak",
"Kakšna je dolžina skupinske sestave?":"2:15 - 2:30",
"Kakšen je program za skupinske sestave?":"sestava z enim tipom rekvizita in z dvema tipoma rekvizitov",
"Kolikšen je odbitek za predolgo glasbo":"0.05",
"Kako dolg je lahko uvod glasbe?":"4 sekunde",
"Kdo odbije odbitek za predolg glasbeni uvod?":"sodnice za artistiko",
"Kolikšen je odbitek za predolg glasbeni uvod?":"0.30",
"Kolikšen je odbitek za neprimerni glasbo (npr. sirene, motor, itd.)?":"0.50",
"Koliko glasb s petjem ima lahko tekmovalka?":"2",
"Kdo odbije odbitke če glasba ni v skladu s pravilnikom?":"sodnica koordinatorka",
"Kolikšen je odbitek če tekmovalka uporabi dodatno glasbo s petjem?":"1.00",
"Kdo sodi težine s telesom in plesne korake?":"D1, D2",
"Kdo sodi rizike in težine z rekvizitom?":"D3, D4",
"Kdo sodi artistične komponente sestave?":"E1, E2",
"Kdo sodi izvedbene napake?":"E3, E4, E5, E6",
"Na kateri del ocene se lahko pritoži trener?":"D",
"Kolikšen je odbitek za prestop?":"0.30",
"Kolikšen je odbitek za neustrezen rekvizit?":"0.50",
"kolikšen je odbitek, če tekmovani dres ne ustreza zahtevam?":"0.30",
"Ali lahko tekmovalke med sestavo komunicirajo?":"ne",
"Ali lahko trener daje napotke tekmovalki med izvajanjem sestave?":"ne",
"Kolikšen je odbitek, če trenerka kaže vajo med tem ko dekleta tekmujejo?":"0.50",
"Kolikšen je odbitek, če ima tekmovalka nekožnate bandaže?":"0.30"
}

#pod prvo možnostjo je naveden pravilni odgovor
vprasanja_multiple_izbire = {
    "Koliko je vredna težina na sliki1?":{"pravilen":"a", "odgovori":[0.1, 0.2, 0.3]},
    "Koliko je vredna težina na sliki2?":{"pravilen":"b", "odgovori":[0.1, 0.2, 0.3]},
    "Koliko je vredna težina na sliki3?":{"pravilen":"a", "odgovori":[0.2, 0.3, 0.4]},
    "Koliko je vredna težina na sliki4?":{"pravilen":"b", "odgovori":[0.2, 0.3, 0.4]},
    "Koliko je vredna težina na sliki5?":{"pravilen":"a", "odgovori":[0.3, 0.4, 0.5]},
    "Koliko je vredna težina na sliki6?":{"pravilen":"a", "odgovori":[0.4, 0.5, 0.6]},
    "Koliko je vredna težina na sliki7?":{"pravilen":"a", "odgovori":[0.2, 0.3, 0.4]},
    "Koliko je vredna težina na sliki8?":{"pravilen":"b", "odgovori":[0.2, 0.3, 0.4]},
    "Koliko je vredna težina na sliki9?":{"pravilen":"b", "odgovori":[0.3, 0.4, 0.5]},
    "Koliko je vredna težina na sliki10?":{"pravilen":"b", "odgovori":[0.4, 0.5, 0.6]},    
}

oznacbe_odgovorov = ["a", "b", "c"]

#a,b,a,b,a,a,a,b,b,b
vprasanja_multiple = [
    'Koliko je vredna težina na sliki1?\n(a) 0.1\n(b) 0.2\n(c) 0.3\n\n',
    'Koliko je vredna težina na sliki2?\n(a) 0.1\n(b) 0.2\n(c) 0.3\n\n',
    'Koliko je vredna težina na sliki3?\n(a) 0.2\n(b) 0.3\n(c) 0.4\n\n',
    'Koliko je vredna težina na sliki4?\n(a) 0.2\n(b) 0.3\n(c) 0.4\n\n',
    'Koliko je vredna težina na sliki5?\n(a) 0.3\n(b) 0.4\n(c) 0.5\n\n',
    'Koliko je vredna težina na sliki6?\n(a) 0.4\n(b) 0.5\n(c) 0.6\n\n',
    'Koliko je vredna težina na sliki7?\n(a) 0.2\n(b) 0.3\n(c) 0.4\n\n',
    'Koliko je vredna težina na sliki8?\n(a) 0.2\n(b) 0.3\n(c) 0.4\n\n',
    'Koliko je vredna težina na sliki9?\n(a) 0.3\n(b) 0.4\n(c) 0.5\n\n',
    'Koliko je vredna težina na sliki10?\n(a) 0.4\n(b) 0.5\n(c) 0.6\n\n'
]


#resitve_multiple =[
    #Igra(vprasanja_multiple[0],'a'),
    #Igra(vprasanja_multiple[1],'b'),
    #Igra(vprasanja_multiple[2],'a'),
    #Igra(vprasanja_multiple[3],'b'),
    #Igra(vprasanja_multiple[4],'a'),
    #Igra(vprasanja_multiple[5],'a'),
    #Igra(vprasanja_multiple[6],'a'),
    #Igra(vprasanja_multiple[6],'a'),
    #Igra(vprasanja_multiple[7],'b'),
    #Igra(vprasanja_multiple[8],'b'),
    #Igra(vprasanja_multiple[9],'b')
#]

#poiskati moraš še 10 slik in oddati pravilne odgovore
vprasanja_multiple_izbire1 = {"Koliko je vredna težina na sliki 1?":"0.1",
    "Koliko je vredna težina na sliki 2?":"0.1",
    "Koliko je vredna težina na sliki 3?":"0.1",
    "Koliko je vredna težina na sliki 4?":"0.1",
    "Koliko je vredna težina na sliki 5?":"0.1",
    "Koliko je vredna težina na sliki 6?":"0.1",
    "Koliko je vredna težina na sliki 7?":"0.1",
    "Koliko je vredna težina na sliki 8?":"0.1",
    "Koliko je vredna težina na sliki 9?":"0.1",
    "Koliko je vredna težina na sliki 10?":"0.1",
    "Koliko je vredna težina na sliki 11?":"0.1",
    "Koliko je vredna težina na sliki 12":"0.1",
    "Koliko je vredna težina na sliki 13?":"0.1",
    "Koliko je vredna težina na sliki 14?":"0.1",
    "Koliko je vredna težina na sliki 15?":"0.1",
    "Koliko je vredna težina na sliki 16?":"0.1",
    "Koliko je vredna težina na sliki 17?":"0.1",
    "Koliko je vredna težina na sliki 18?":"0.1",
    "Koliko je vredna težina na sliki 19?":"0.1",
    "Koliko je vredna težina na sliki 20?":"0.1"}

    
    