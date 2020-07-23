#Spletni vmesnik
import model
import bottle

kviz = model.Kviz()
#spremeni index.tpl tudi def index je lah neki drugega
@bottle.get("/")
def index():
    return bottle.template("index.tpl") #prva stran- navodila

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = kviz.nova_igra() #vrne id igre
    bottle.response.set_cookie("idigre", "idigre{0}".format(id_igre), path="/")
    bottle.redirect("/igra/") #nas usmeri k igri


@bottle.get("/igra/")
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
    igra, poskus = kviz.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, poskus=poskus)    

@bottle.post("/igra/")
def ugibaj():
    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
    # if stanje == 'R'
    if kviz.igre[id_igre][1] == model.KVIZ_RIZIKI: 
        #odgovori tip_2 # vrednost for ključ, vrednost in [('k', 'v1'), ('k', 'v2'),..] v1 so vsi odgovori na eno vpr
        odgovor = [vrednost for polje, vrednost in bottle.request.forms.allitems()] #['v1', 'v2']
    else:
        odgovor = bottle.request.forms.getunicode("odgovor")
    kviz.ugibaj(id_igre, odgovor)
    return bottle.redirect("/igra/")

    

bottle.run(reloader=True, debug=True)