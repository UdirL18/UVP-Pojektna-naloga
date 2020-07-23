#===========================================================================================
#Spletni vmesnik
#===========================================================================================
import model
import bottle
from bottle import error

kviz = model.Kviz()
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
        odgovor = [(polje, vrednost) for polje, vrednost in bottle.request.forms.allitems()] #[('odgovor_0', '3 rotacije'), ('odgovor_1', '3 rotacije'), ('odgovor_2', 'met z rotacijo okoli svoje osi (diametralni met)'), ('odgovor_3', '4 rotacije'), ('odgovor_4', 'met brez pomoči rok')]
    else:
        odgovor = bottle.request.forms.getunicode("odgovor")
    kviz.ugibaj(id_igre, odgovor)
    return bottle.redirect("/igra/")

##odkomentiraj ko bo vse delao
#@error(404)
#def error404(error):
#    return bottle.template("error.tpl")

#@error(400)
#def error400(error):
#    return bottle.template("error.tpl")

#@error(500)
#def error500(error):
#    return bottle.template("error.tpl")

#@error(501)
#def error501(error):
#    return bottle.template("error.tpl")

#@error(505)
#def error505(error):
#    return bottle.template("error.tpl")


    

bottle.run(reloader=True, debug=True)