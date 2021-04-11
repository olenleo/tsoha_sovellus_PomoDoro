# tsoha_sovellus_PomoDoro
Repositorio liittyy Helsingin Yliopiston [Tietokantasovellus](https://hy-tsoha.github.io/materiaali/index)-kurssin harjoitustyöhön.
Kurssilla toteutetaan tietokantaa hyödyntävä web-sovellus.

Sovellus on testattavissa [tämän linkin takana](https://tsoha-pomodoro.herokuapp.com/).
Lisätietoa [määrittelydokumentissa](https://github.com/olenleo/tsoha_sovellus_PomoDoro/blob/main/maarittelydokumentti.md)

# Sovelluksen nykytila

Sovelluksen ydintoiminnallisuus on veilä puuttellista, mutta yksinkertaisella tasolla käytettävää.

Pulmakohtia / bugeja on tällä hetkellä kommentoinnissa, joissa kaikki kommentit ovat nähtävillä. Tämä johtuu virheestä uusien *tomaattien* tallennuksessa; tällä hetkellä kaikki tehdyt tomaatit tallennetaan samaan tasksetiin.


**Kysymys:** Taskset-luokan metodin get_taskset_id() toteuttaminen oli pulmallista. Tällä hetkellä välitän tomaatin nimen periaattella <code>taskset.get_taskset_id(tomaatin_nimi)</code>. Tämä aiheuttaa kuitenkin lisämerkkejä merkkijonoon, esimerkiksi <code>('Tehtävän nimi')</code>.

Ratkaisin tämän trimmaamalla merkkijonosta sopivasti merkkejä alusta ja lopusta pythonin avulla. Tämä tuntuu kuitenkin vähän kömpelöltä ratkaisulta. En toisaalta keksi mitään perustetta tehdä trimmausta tietokannan puolella esimerkiksi säännöllisillä lausekkeilla (Regular Expression). Onko 

Sovelluksessa on vielä paljon refaktoroitavaa. Pahoittelut etenkin englannin ja suomen sekakäytöstä.


