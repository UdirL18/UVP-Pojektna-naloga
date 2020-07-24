%import model
%rebase("base.tpl", title="Kviz")

  <h1>Kviz 
    <a href="https://www.gymnastics.sport/publicdir/rules/files/en_RG%20CoP%202017-2020%20with%20Errata%20Dec.%2017.pdf" target="_blank">
      <img src="https://image.slidesharecdn.com/codigo20132016-120327205544-phpapp02/95/code-of-pointsgr-2013-2016-english-1-728.jpg?cb=1333531041" 
      width=8% height=10% style="float: left">
    </a>
  </h1>

  <h6> Pokukajte v pravilnik.</h6>


%if poskus == model.ZMAGA:
  <h1>ČESTITAMO! ZMAGALI STE :)</h1>
  <h3>Za začetek nove igre kliknite na gumb <i>Nova igra</i>.</h3>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <div id="gumb">
      <button type="submit">Nova igra</button>
    </div>
  </form>

%elif poskus == model.PORAZ:
  <h1>O, NE ... IZGUBILI STE :(</h1>
  <h3>Za začetek nove igre kliknite na gumb <i>Nova igra</i>. Ponovno preizkusite svojo srečo.</h3>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <div id="gumb">
      <button type="submit">Nova igra</button>
    </div>
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

        <blockquote>
            <h3><small>Primer odgovora: {{igra.trenutno_vprasanje().get("primer_odg")}}</small></h3>
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

        <img src= {{igra.trenutno_vprasanje().get("slika")}} width="180" height="220"> 
        
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
      <iframe width="920" height="580" src={{igra.trenutno_vprasanje().get("video")}} 
        frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen >
      </iframe>
    </div>  

    <blockquote>
    <form action="/igra/" method="post">
      <!-- ... in [(0, {'vpr':'','odg':[]}), (1, {'vpr':'','odg':[]})]-->
      %for i, slovar_vpr in enumerate(igra.trenutno_vprasanje().get("vprasanje")): 
        <h4>{{slovar_vpr.get("vpr")}}</h4> 

          % for odg in igra.trenutno_vprasanje().get("mozni_odg"):
              <input type="checkbox" name="odgovor_{{i}}" value="{{odg}}"> {{odg}} <br>
          %end
      % end
      <h4> Še enkrat preverite odgovore, drugače boste morali ponovno rešiti nalogo. </h4>
      <button type="submit">Odgovori</button>
      </form>
    </blockquote>                  

    % end

%end

%end