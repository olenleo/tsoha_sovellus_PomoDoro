# tsoha_sovellus_PomoDoro
Repositorio liittyy Helsingin Yliopiston [Tietokantasovellus](https://hy-tsoha.github.io/materiaali/index)-kurssin harjoitustyöhön.
Kurssilla toteutetaan tietokantaa hyödyntävä web-sovellus.

Sovellus on testattavissa [tämän linkin takana](https://tsoha-pomodoro.herokuapp.com/).
Lisätietoa [määrittelydokumentissa](https://github.com/olenleo/tsoha_sovellus_PomoDoro/blob/main/maarittelydokumentti.md)

# Sovelluksen nykytila

Sovelluksen ydintoiminnallisuus on vielä puuttellista, mutta yksinkertaisella tasolla käytettävää.

Pulmakohtia / bugeja on tällä hetkellä kommentoinnissa, joissa kaikki kommentit ovat nähtävillä. Tämä johtuu virheestä uusien *tomaattien* tallennuksessa; tällä hetkellä kaikki tehdyt tomaatit tallennetaan samaan tasksetiin. Tämä löytyy Routes-luokan <code>@app.route("/comment", methods=["POST"])</code>-metodista.

Mietin josko minun tulisi suorittaa kaksi SQL-kyselyä tuossa metodissa: hakea oikea task_id (tomatoes-luokan metodina) ja sitten suorittaa varsinainen post-pyyntö.

**Kysymys:** Taskset-luokan metodin get_taskset_id() toteuttaminen oli pulmallista. Tällä hetkellä välitän tomaatin nimen periaattella <code>taskset.get_taskset_id(tomaatin_nimi)</code>. Tämä aiheuttaa kuitenkin lisämerkkejä merkkijonoon, esimerkiksi <code>('Tehtävän nimi'),</code>.

Ratkaisin tämän trimmaamalla merkkijonosta sopivasti merkkejä alusta ja lopusta pythonin avulla. Tämä tuntuu kuitenkin vähän kömpelöltä. En toisaalta keksi mitään perustetta tehdä trimmausta tietokannan puolella esimerkiksi säännöllisillä lausekkeilla (Regular Expression). Tämä on melko yksinkertainen tapaus, mutta epäilen että vastaavissa tilanteissa on mahdollisia kompastuskivia sovelluksen laajennettavuuden suhteen. Eli, onko jotain ohjenuoraa missä kohtaa merkkijonojen (tai muiden syötteiden) käsittely olisi hyvä suorittaa?

Sovelluksessa on vielä paljon refaktoroitavaa. Pahoittelut etenkin englannin ja suomen sekakäytöstä - siistin nämä ensi palautukseen mennessä!

# Toimintasuunnitelma jatkoa varten

Ratkaisen ensiksi kommentointiin liittyvät pulmat. Tämän jälkeen on vuorossa muitten käyttäjien seuraamisen implementointi, joka johtaakin luontevasti syötteen filtteröintiin. Viestin poistomahdollisuusa olisi varmasti hyvä lisätä käyttömukavuuden kannalta...

Tämän yllä olevan ohella tutustun tarkemmin sovelluksen tietoturvaan.



