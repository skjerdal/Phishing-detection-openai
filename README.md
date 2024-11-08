# Phishingdeteksjon med OpenAI

*Av Thomas Skjerdal, August Langfeldt, Sivert Brattgjerd, 8. November 2024*
**[Test det ut](https://phishing-analyzer.skjerdal.me/)**

---

## Innholdsfortegnelse
1. [Beskrivelse av problemet](#beskriv-problemet)
2. [Metrikkar](#metrikkar)
3. [Data](#data)
4. [Modellering](#modellering)
5. [Deployment](#deployment)
6. [Referansar](#referansar)

---

## Beskrivelse av problemet

### Scope

- **Forretningsmål**: Målet med prosjektet er å utvikle ein nettapplikasjon som kan oppdage phishing-URLar og mistenkelege e-postadresser ved hjelp av maskinlæring, spesielt OpenAI sin GPT-modell. Dette vil bidra til å styrke cybersikkerheita ved å gi brukarar eit verktøy for å identifisere potensielle truslar.

- **Bruk av løysinga**: Løysinga blir brukt gjennom ein webapplikasjon der brukarar kan skrive inn ein URL eller e-postadresse for analyse. Tilsvarande løysingar i dag inkluderer antivirusprogram og nettlesarutvidingar som blokkerer kjende phishing-sider. Utan maskinlæring måtte ein manuelt undersøkt kvar enkelt URL eller e-postadresse, noko som er tidkrevjande og upresist.

- **Ytelsesmåling via "business metrics"**: Ytinga blir målt ved treffsikkerheita i deteksjon av phishing, brukarengasjement, og reduksjon i sikkerheitsbrot for brukarar som nyttar tenesta.

- **Systemkomponentar**: Applikasjonen består av ein Flask-backend som kommuniserer med OpenAI sin GPT-modell og ein frontend for brukarinteraksjon. Endringar i modellen kan påverke analysen, og oppdateringar i API-et kan krevje endringar i koden.

- **Interessentar (Stakeholders)**: Primært individuelle brukarar som ønskjer å verne seg mot phishing. Sekundært organisasjonar som kan integrere løysinga i sine sikkerheitssystem.

- **Tentativ tidslinje**:
  - **Veke 1**: Planlegging og design av system.
  - **Veke 1**: Utvikling av Flask-applikasjonen og integrasjon med OpenAI API.
  - **Veke 2**: Testing og validering av modellen.
  - **Veke 3**: Distribusjon på Vercel og innsamling av brukarfeedback.
  - **Veke 3**: Forbetringar basert på tilbakemeldingar.

- **Ressursar**:
  - Berekningsressursar: Tilgang til OpenAI API og hosting gjennom Vercel.
  - Personell: Ein utviklar med kompetanse i Python, Flask og maskinlæring.
  - Andre: Dataset for testing og validering.

## Metrikkar

- **Minimum "business metric"-ytelse**: Oppnå ein treffsikkerheit på minst 90% i deteksjon av phishing-URL-ar og e-postadresser.

- **Maskinlærings- og software-metrikkar**:
  - **Treffsikkerheit (Accuracy)**: Andelen korrekte klassifiseringar av totalen.
  - **Presisjon (Precision)**: Andelen relevante treff blant dei identifiserte truslane.
  - **Recall (Tilbakekalling)**: Evna til å identifisere alle faktiske truslar.
  - **Latency**: Responstid for analyse etter innsendt førespurnad.
  - **Throughput**: Talet på førespurnader som kan handterast per tidseining.

  Desse metrikkane sikrar at systemet ikkje berre er nøyaktig, men og effektiv og brukarvennleg, noko som er essensielt for å nå forretningsmålet.

## Data

- **Datakjelder og labels**: Modellen nyttar pre-trente data frå OpenAI. Input er brukargenererte URL-ar og e-postadresser.

- **Datamengde**: Sidan modellen er pre-trent, er det ikkje behov for stor mengde treningsdata. For validering trengs eit balansert testsett.

- **Personvern og etikk**: Ingen personlege identifiserbar informasjon blir lagra. GDPR og andre relevante lovverk blir følgd.

- **Datarepresentasjon**: Data blir representert som tekststrengar og behandla direkte av modellen utan behov for omfattande preprosessering.

## Modellering

- **Val av modell**: Etter litt testing hamna valet på GPT 4o modellen sidan denne ga best svar.

- **Baseline-ytelse**: Etablert ved å teste modellen mot eit sett med kjende phishing- og legitime adresser og samanlikne resultata med eksisterande verktøy.

- **Feilprediksjon og feature importance**: Analysere tilfelle der modellen feilar for å justere prompt og systeminstruksjonar, og dermed forbetre modellen si evne til å identifisere subtile phishing-forsøk.

## Deployment

- **Driftsetting av modellen**: Integrert i Flask-applikasjonen og distribuert gjennom Vercel for skalerbarheit, enkel tilgang og deployment av oppdatert kode.

- **Bruk av prediksjonar**: Gi umiddelbar tilbakemelding til brukarar om tryggleiksstatus på innsendte URL-ar og e-postadresser.

- **Monitorering og vedlikehald**: Kontinuerleg overvaking av systemytelse, inkludert nøyaktigheit og responstid. Regelmessige oppdateringar basert på nye phishing-teknikkar og trendar.

- **Forbetringsplanar**: Utvide funksjonaliteten til å inkludere fleire språk, oppdage andre typar cybertruslar, og integrere maskinlæringsmodellen djupare for meir spesialisert deteksjon.

## Referansar

- [OpenAI API-dokumentasjon](https://platform.openai.com/docs/)
- [Flask-dokumentasjon](https://flask.palletsprojects.com)
- [Vercel dokumentasjon](https://vercel.com/docs)
- [GDPR-informasjon](https://gdpr-info.eu/)
