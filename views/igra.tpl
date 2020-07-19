%import model
%rebase("base.tpl", title="Kviz")

  <h1>Kviz</h1>

%if poskus == model.ZMAGA:
  <h1>ZMAGA!</h1>
  <b>Za začetek nove igre kliknite na gumb Nova igra.</b>
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
            Odgovor: <input type="text" name="odgovor">
            <button type="submit">Pošlji odgovor</button>
        </form>

    
    <!-- MULTIPLE ODGOVORI -->
    % elif igra.trenutno_vprasanje().get("tip") == "tip_1":
        
        <blockquote>
            <h2>{{igra.trenutno_vprasanje().get("vprasanje")}}</h2>
        </blockquote>

        <img src= {{igra.trenutno_vprasanje().get("slika")}} width="280" height="320" style="float:left";margin:50px 0px">
        
        <form action="/igra/" method="post"> 
          <input type="radio" name="odgovor">{{igra.trenutno_vprasanje().get("mozni_odg")[0]}}<br>
          <input type="radio" name="odgovor">{{igra.trenutno_vprasanje().get("mozni_odg")[1]}}<br>
          <input type="radio" name="odgovor">{{igra.trenutno_vprasanje().get("mozni_odg")[2]}}<br>
          <button type="submit">Pošlji odgovor</button>
        </form>


   <!--VEČ PRAVILNIH ODGOVOROV % elif igra.trenutno_vprasanje().get("tip") == "tip_2": -->
    
    % end

%end

%end