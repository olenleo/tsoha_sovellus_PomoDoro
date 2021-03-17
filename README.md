# tsoha_sovellus_PomoDoro
Repositorio liittyy Helsingin Yliopiston [Tietokantasovellus](https://hy-tsoha.github.io/materiaali/index)-kurssin harjoitustyöhön.
Kurssilla toteutetaan tietokantaa hyödyntävä web-sovellus.

# Sovelluksen kuvaus

PomoDoro on [pomodoro-tekniikaan](https://en.wikipedia.org/wiki/Pomodoro_Technique) perustuva web-sovellus. Pomodorot ovat ~25 minuutin aikaviipaleita. Käyttäjä voi seurata muiden käyttäjien työtä sekä kommentoida tsempatakseen!

Käyttäjä voi
- Luoda uniikin tilin - esimerkiksi `@M_Mallikas1985`
- Aloittaa tehtäväkokonaisuuden - esimerkiksi `'Lineaarialgebran opiskelu'`
- Merkitä tehdyn tomaatin - esimerkiksi `@M_Mallikas1985 | 'Lineaarialgebran opiskelu' | "Ominaisvektorit.. huh vaikeaa!"`
- Kommentoida omaa tai toisen julkaistua tomaattia - esimerkiksi `User @AAaberg commented: "Kämpa på! 3blue1brown hade en bra video om det där"`
- Poistaa tilinsä ja kaiken siihen liittyvän informaation


Mahdollisia skenaarioita:
- Käyttäjä kirjautuu sisään
* Käyttäjä saapuu päänäkymään, jossa listataan viimeiset 25 tomaattia.
* Käyttäjä voi myös halutessaan listata vain seuraamiensa käyttäjien tomaatit
* Lista on päivitettävissä.
* Päänäkymässä voi lisätä uuden tehtäväkokonaisuuden tai uuden tehdyn tomaatin.

- Käyttäjä haluaa reagoida toisen käyttäjän tomaattiin
* Vaihtoehto: Kommentoi
   Käyttäjä voi lisätä lyhyen kommentin
* Vaihtoehto: Seuraa / Poista seurattavista
   Toinen käyttäjä lisätään tai poistetaan seurattavien käyttäjien listalta.




# Jatkokehitys
Sovellusta voisi laajentaa graafisella käyttöliittymällä jossa ajastin seuraa jokaisen tehtävän suoritusta. Ajastimen lauetessa käyttäjä syöttää kuvauksen tekemisistään joka lisätään tietokantaaan.

Reaaliaikainen päivitys jollain mukavalla grafiikalla - värillä tai käyttäjän valitsemalla kuvakkeella merkityt tomaatit valuvat hiljalleen alaspäin uusien valmistuessa.
