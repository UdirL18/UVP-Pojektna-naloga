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
    odgovor = bottle.request.forms.getunicode("odgovor")
    kviz.ugibaj(id_igre, odgovor)
    return bottle.redirect("/igra/")

#@bottle.post("/nov_level/")
#def nov_level():
    #id_igre = kviz.nov_lavel() #vrne id igre
    #bottle.response.set_cookie("idigre", "idigre{0}".format(id_igre), path="/")
    #bottle.redirect("/kviz_multiple/") #nas usmeri k igri

#@bottle.get("/igra_mul/")
#def pokazi_igro_mul():
#    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
#    igra, poskus = kviz.igre[id_igre]
#    return bottle.template("igra_mul.tpl", igra=igra, poskus=poskus)

#@bottle.post("/igra/")
#def ugibaj_mul():
#    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
#    odgovor = bottle.request.forms.getunicode("odgovor")
#    kviz.ugibaj(id_igre, odgovor)
#    bottle.redirect("/igra_mul/")

#@bottle.get('/kviz_multiple/')
#def kviz_multiple():
#    id_igre = int(bottle.request.get_cookie("idigre").split("e")[1])
#    level, poskus = kviz.igre[id_igre]
#    return bottle.template("multiple.tpl", level=level, poskus=poskus)
    



bottle.run(reloader=True, debug=True)