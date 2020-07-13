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
  <blockquote>
    <h2>{{igra.trenutno_vprasanje()}}</h2>
    <!--img src="3.jpg" alt="slika 1" /-->
  </blockquote>
  
  <!-- komentar: poravnaj da ne zgleda tok kiljavo-->
  % if igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 1?":
        <img src="https://ssl.c.photoshelter.com/img-get/I0000tMsoaFK6TWs/s/860/860/lima384-2-baku20051005por-600tsw.jpg" 
          width=12% height=12% style="float:left";margin:50px 0px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 2?":
        <img src="https://i.pinimg.com/originals/29/98/a8/2998a8e2bc0c39267bb622136873b872.jpg" 
          width=12% height=12% style="float:left";margin:50px 0px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 3?":
        <img src="https://www.avrhythmic.org.uk/wp-content/images/Marfa-ball-good-balance-2.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 4?":
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTsbF9TnzYJMm8MmZ_Pv60Ca7RDGlx0w7wOmQ&usqp=CAU" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 5?":
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQrR3yExQ8NwEp5EkcDKzileH6_nncUnG09fw&usqp=CAU" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 6?":
        <img src="https://images.haarets.co.il/image/fetch/w_2048,h_1536,c_crop/q_auto,h_900,w_1200,c_fill,f_auto/fl_lossy.any_format.preserve_transparency.progressive:none/https://www.haaretz.co.il/polopoly_fs/1.5531863!/image/1018316866.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 7?":
        <img src="https://www.jozikids.co.za/uploadimages/gold_reef_gymnastics3_large.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 8?":
        <img src="https://s3media.freemalaysiatoday.com/wp-content/uploads/2019/09/rhythmic-gymnastics-Bernama.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 9?":
        <img src="https://gymnasticmoments.com/galeriak/33rd-european-rhythmic-gymnastics-championships/158%2016%20AVERINA%20Arina%20-%20RUS%20DSC_2782.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 10?":
        <img src="https://editorial01.shutterstock.com/wm-preview-1500/9879309jf/2ae76b8f/rhythmic-gymnastics-world-championships-day-2-sofia-usa-shutterstock-editorial-9879309jf.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 11?":
        <img src="https://c8.alamy.com/comp/PK7JBA/september-11-2018-aleksandra-soldatova-of-russia-during-rhythmic-gymnastics-world-championships-at-the-arena-armeec-in-sofia-at-the-36th-fig-rhythmic-gymnastics-world-championships-ulrik-pedersencsm-PK7JBA.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 12?":
        <img src="https://lh6.googleusercontent.com/proxy/7hLtTUZcg3s6xSg8KI1RpAsdUaCAbrS3rCjTC5WujXh4pLpMvOM7Foy-JxBhwOtFeMRTfqS5-DH2b-qMSDfU0v6aiYw9KtkiiJWa1w" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 13?":
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRO3Mn7L5SPEMOp7z5k59HQPzCx1pWUgQcxe0nWBlJ73OFfgE&s" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 14?":
        <img src="https://i.pinimg.com/236x/d0/65/95/d06595a633104bc8e5d51d9e1d273be2--gymnastics-events-gymnastics-clubs.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 15?":
        <img src="https://i.pinimg.com/736x/68/83/8c/68838c1ecd55440ef55a6ed5f0f47b7e.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 16?":
        <img src="https://c8.alamy.com/comp/TXF6DW/rhythmic-gymnastics-star-anna-bessonova-of-ukraine-balances-with-the-clubs-in-all-around-at-rhythmic-gymnastics-world-championships-in-baku-azerbaijan-october-8-2005-upi-phototom-theobald-TXF6DW.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 17?":
        <img src="https://ssl.c.photoshelter.com/img-get/I0000hVXW1TY7Gj8/s/860/860/51272zhukova-pat20070921blr300.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 18?":
        <img src="https://i.pinimg.com/originals/72/56/2f/72562f626db66c2125ad6432e3c87014.jpg" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 19?":
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGWuLSsj6itQVDqjFzIymc7rt6aqjdd7g5FUL-ygbquj-dxgA&s" 
          width=12% height=12% style="float:left";margin:50px 50px">
  % elif igra.trenutno_vprasanje() == "Koliko je vredna težina na sliki 20?":
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRt-VJJqT51HMTpdjYVDq56SslkWwD6hta8D67ffxojawjyMyG&s" 
          width=12% height=12% style="float:left";margin:50px 50px">
  %end

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
<form action="/igra/" method="post">
    % if igra.stevilo_pravilnih() >= 4:
        <form action="/igra/" method="post"> 
          <input type="radio" name="odgovor">'0.1'<br>
          <input type="radio" name="odgovor">'0.2'<br>
          <input type="radio" name="odgovor">'0.3'<br>
          <input type="radio" name="odgovor">'0.4'<br>
          <input type="radio" name="odgovor">'0.5'<br>
          <input type="radio" name="odgovor">'0.6'<br>
          <button type="submit">Pošlji odgovor</button>
        </form>
    %else:
      Odgovor: <input type="text" name="odgovor">
      <button type="submit">Pošlji odgovor</button>
    %end
</form>

%end

%end