# tsoha_sovellus_PomoDoro
Repositorio liittyy Helsingin Yliopiston [Tietokantasovellus](https://hy-tsoha.github.io/materiaali/index)-kurssin harjoitustyöhön.
Kurssilla toteutetaan tietokantaa hyödyntävä web-sovellus.

Sovellus on testattavissa [tämän linkin takana](https://tsoha-pomodoro.herokuapp.com/).


# Sovelluksen kuvaus

PomoDoro-sovellus tarjoaa mahdollisuuden jakaa suorittamiaan PomoDoroja - 25 minuutin aikaviipaleita - muille sovelluksen käyttäjille. Käyttäjä voi myös seurata yksittäisiä muita käyttäjiä ja tarkastella vain seuraamiensa käyttäjien tekemisiä.

Kukin suoritettu PomoDoro sisältää kommentointimahdollisuuden. Näin ollen käyttäjät voivat viestitellä keskenään, tsempatakseen tai vaihtaakseen ideoita.

Lisätietoa [määrittelydokumentissa](https://github.com/olenleo/tsoha_sovellus_PomoDoro/blob/main/maarittelydokumentti.md)

# Sovelluksen nykytila

Sovelluksesta on toteutettu valtaosa määrittelydokumentin toiminnallisuudesta. Puutteita:
- Admin-tila ei tällä hetkellä tee mitään.
- Kommentin muokkaus tai poisto ei vielä implementoitu.
- Käyttäjän informaation poisto ei implementoitu.

Määrittelydokumentissa ei mainita asiaa, mutta taskset:eja ei tällä hetkellä hyödynnetä oikeastaan mitenkään.

Sovellus on täysin käyttökelpoinen, mutta ollakseen oikeasti hyödyllinen (tai mukava) työkalu tulisi yllä olevat puutteet korjata.

# Mahdollinen jatkokehitys

Ajastin lisäisi käytettävyyttä huomattavasti - aikaviipaleiden seuraaminen on kuitenkin pomodoro-tekniikan perusidea. Tämä olisi tehtävissä pienellä JavaScript-ohjelmalla. TaskSet:ien hyödyntäminen ja kaikkien valikkojen käytettävyyden lisääminen olisi kuitenkin kätevämpää esimerkiksi Reactin avulla. Tällä hetkellä taskset:in valinta-menu tulee pian käyttökelvottomaksi jos näitä taskset:ejä lisätään paljon.


