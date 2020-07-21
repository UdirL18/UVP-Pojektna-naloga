%import model
%rebase("base.tpl", title="Kviz")

  <h1>Kviz</h1>

%if poskus == model.ZMAGA:
  <h1>ZMAGA!</h1>
  <b>Za začetek nove igre kliknite na gumb.</b>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

%elif poskus == model.PORAZ:
  <h1>IZGUBILI STE!</h1>
  <b>Za začetek nove igre kliknite na gumb Nova igra.</b>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

%else:

  <table>
    <tr>
      <td>
        Število napak: <b>{{igra.stevilo_napacnih()}}</b>
      </td>
    </tr>
    <tr>  
      <td>
        Število pravilnih odgovorov: <b>{{igra.stevilo_pravilnih()}}</b>
      </td>
    </tr>
  </table>

<h3> </h3>
    <!-- OPISNI ODGOVORI -->
    % if igra.trenutno_vprasanje().get("tip") == "tip_0":

        <blockquote>
            <h2>{{igra.trenutno_vprasanje().get("vprasanje")}}</h2>
        </blockquote>

        <form action="/igra/" method="post">
            <h3>Odgovor: <input type="text" name="odgovor"></h3>
            <div id="gumb">
              <button type="submit">Pošlji odgovor</button>
            </div>
        </form>

    
    <!-- MULTIPLE ODGOVORI -->
    % elif igra.trenutno_vprasanje().get("tip") == "tip_1":
        
        <blockquote>
            <h2>{{igra.trenutno_vprasanje().get("vprasanje")}}</h2>
        </blockquote>

        <img src= {{igra.trenutno_vprasanje().get("slika")}} width="280" height="320">
        
        <form action="/igra/" method="post"> 
          % for vrednost in igra.trenutno_vprasanje().get("mozni_odg"):
          <div id="mozniOdgovori">
            <input type="radio" value="{{vrednost}}" 
            name="odgovor">{{vrednost}}<br>
          </div>
          % end
          <div id="gumb">
            <button type="submit">Pošlji odgovor</button>
          </div>
        </form>


   <!--VEČ PRAVILNIH ODGOVOROV -->
    % elif igra.trenutno_vprasanje().get("tip") == "tip_2": 

        <div id="video">
          <iframe width="420" height="315" src={{igra.trenutno_vprasanje().get("video")}} 
            frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen >
          </iframe>
        </div>  

        <blockquote>
          %for slovar_vpr in igra.trenutno_vprasanje().get("vprasanje"):
            <h4>{{slovar_vpr.get("vpr")}}</h4> 
            <form action="/igra/" method="post">
              % for odg in igra.trenutno_vprasanje().get("mozni_odg"):
                <div id="mozniOdgovori2">
                  <input type="checkbox" name="odgovor" value="{{odg}}"> {{odg}} <br>
                </div>
              %end
            </form> 
          % end
          <form action="/igra/" method="post">
          <button type="submit">Odgovori</button>
          </form>
        </blockquote>                  

    % end

%end

%end