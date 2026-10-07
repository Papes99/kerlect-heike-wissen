### PRÜFUNG 001-hueft-tep v1.0 – 07.10.2026

Gegenprüfung Grok · Quellen selbst geöffnet (WebFetch/curl + pdftotext) · nichts geschätzt · ohne Quelle `quelle: null`

#### A. Prüfung der belegten Zeilen

| Abschnitt | Zeile | Quelle | Ergebnis (bestätigt / zu weit / nicht gefunden) | Bemerkung |
|---|---|---|---|---|
| facts | Primäre Hüft-TEP | AMBOSS | bestätigt | AMBOSS: Hüft-TEP = Ersatz von Pfanne + Femurkopf/-hals (vs. Hemi nur Kopf). „Primär“ = Paket-Scope; Stand Seite 10.07.2026. |
| position | DAA: Rückenlage | AMBOSS | bestätigt | Anteriorer Zugang/DAA: Lagerung Rückenlagerung. |
| position | Anterolateral: Seite oder Rücken | AMBOSS | bestätigt | Watson-Jones: Seiten- oder Rückenlagerung. |
| position | Lateral: Rücken oder Schrägseite | AMBOSS | bestätigt | Bauer/transgluteal: Rücken- oder Schrägseitenlage. |
| position | Posterolateral: Seitenlage | AMBOSS | bestätigt | Posterolateral: Seitenlagerung. |
| position | NE-Kontakt kontrollieren | HEBU GAHF113 | bestätigt | GAHF113V004 (20.02.2026): Haftung der Neutralelektrode nach jeder Lageänderung prüfen; vollflächiger Hautkontakt; monopolar erfordert NE. |
| draping | Flüssigkeitsdichte Abdeckung | KRINKO | bestätigt | Empf. postop. WI 2018, S. 460 (Kat. IB): bei zu erwartendem Durchfeuchten flüssigkeitsundurchlässige Abdeckungen. |
| trays | DAA: LINK-Instrumentenbeispiel | LINK DAA OP-Technik | bestätigt | MAR-01209 / 2022-06, S. 8–11: Instrumentarium DAA inkl. doppelt abgewinkelte Handgriffe, Einschlagstößel gebogen, Schwalbenschwanzretraktor, Hohmann-Varianten – herstellerspezifisch. |
| workflow | Anästhesie vor Zement informieren | BCIS (Heraeus Factsheet) | bestätigt | Factsheet S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über **jeden Schritt** des Zementiervorgangs informieren. Paketformulierung „vor Zement“ ist inhaltlich zutreffend, aber enger als die Quelle (siehe B). |
| pitfalls | Alkoholansammlungen vermeiden | HEBU GAHF113 | zu weit | HEBU: Brandgefahr durch Entzündung von Hautreinigungs-/Desinfektionsmitteln; Flüssigkeit zwischen Patient und NE vermeiden. **Nicht** explizit „Alkoholansammlungen vermeiden / abtrocknen“. Klarer Beleg: KRINKO S. 460 Kat. II (keine Flüssigkeitsansammlung des Hautantiseptikums → Nekrose/Verpuffung). |
| Heike | „Welcher Zugang und welche Fixation? …“ | AMBOSS | bestätigt | Zugang bestimmt Lagerung; Fixation zementiert/unzementiert/teilzementiert laut AMBOSS-TEP-Prinzip – Implikation für Lagerung/Siebe/Zement nachvollziehbar. |
| Heike | „Zementiert? Sag der Anästhesie vor dem Einbringen Bescheid.“ | BCIS | bestätigt | Entspricht BCIS-Kommunikation; Quelle fordert Information über jeden Zementierschritt (Präzisierung in B). |

**Sum A:** 11× bestätigt · 1× zu weit · 0× nicht gefunden. AMBOSS-Inhalt war ohne Login lesbar (Kapiteltext vollständig im Abruf).

Zusatz: In `pakete/001-hueft-tep.json` gibt es genau **10** Einträge mit `"sicherheit":"belegt"` – deckungsgleich mit den 📖-Zeilen in A (ohne die zwei Heike-Sätze, die nur im Markdown 📖 tragen). Alle 10 wurden oben mitgeprüft.

#### B. Änderungsvorschläge

| Nr | Abschnitt | Betroffener Eintrag (oder „neu“) | Art (Korrektur / Ergänzung / Streichung / Präzisierung) | Vorschlag (konkret, Schema-Felder) | Begründung | Quelle (Titel, Stand, Seite, URL) | Priorität (hoch = Sicherheit / mittel / niedrig) |
|---|---|---|---|---|---|---|---|
| 1 | pitfalls | Alkoholansammlungen vermeiden | Korrektur | `label`: Alkoholansammlungen vermeiden; `gilt_fuer`: hf_mono; `sicherheit`: belegt; `quelle`: Q_KRINKO (ggf. zusätzlich Q_HEBU als Brandhinweis); `hinweis`: Vor HF: keine Pfützen Hautantiseptikum; Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; NE nicht unter Flüssigkeit. | Aussage ist sicherheitsrelevant, aber aktuell falsch nur auf HEBU gestützt. | KRINKO Prävention postop. WI, 2018, S. 460 Kat. II; https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf?isAllowed=y&sequence=1 · HEBU GAHF113V004 20.02.2026 (Brand/Flüssigkeit unter NE) | hoch |
| 2 | workflow | Anästhesie vor Zement informieren | Präzisierung | `label`: Anästhesie vor Zement informieren; `spez`: Anästhesie über **jeden Schritt** des Zementiervorgangs informieren (nicht nur einmal „vor Einbringen“); `gilt_fuer`: zementiert, hybrid; `sicherheit`: belegt; `quelle`: Q_BCIS | BCIS-Factsheet verlangt Schritt-für-Schritt-Kommunikation – engere Formulierung untertreibt die Vorsorge. | Heraeus PALACADEMY Factsheet Implantationssyndrom/BCIS, PDF S. 1; https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf | hoch |
| 3 | Heike | „Zementiert? Sag der Anästhesie …“ | Präzisierung | Text analog: „Zementiert? Anästhesie über jeden Zementierschritt informieren.“ `quelle`: Q_BCIS | Gleicher Sicherheitsbezug wie Nr. 2. | wie Nr. 2 | hoch |
| 4 | implants / pitfalls | neu | Ergänzung | `label`: EU: keine Hemi mit Accolade II; `gilt_fuer`: alle (Haus Stryker Accolade II); `sicherheit`: belegt; `hausabhaengig`: true; `optional`: false; `quelle`: Accolade II Surgical Protocol; `hinweis`: Accolade II in EU/EMEA/CE/Australia **nicht** für Hemiarthroplastik indiziert → UHR/Duokopf-Kombi mit Accolade II in EU nicht als freigegeben führen; nur TEP laut IFU. | Verwechslung TEP/Hemi mit Haus-Schaft wäre sicherheitsrelevant. | Accolade II Femoral Hip System Surgical Protocol ACCII-SP-1 Rev-4 (©2022), Indications EU p. 3 und Footnote Trial heads p. 12; https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf | hoch |
| 5 | draping | Flüssigkeitsdichte Abdeckung | Präzisierung | `spez`: Bei erwartetem Durchfeuchten: flüssigkeits**undurchlässige** Abdeckung (Kat. IB); bei geringem Anfall abweisend möglich – Haus/Risiko. | Paket sagt nur „flüssigkeitsdicht“; KRINKO differenziert. | KRINKO 2018, S. 460 | mittel |
| 6 | position | NE-Kontakt kontrollieren | Präzisierung | `hinweis`: HEBU-GAHF113 ist produktspezifisch; **Haus-NE-IFU** des verwendeten Produkts ist maßgeblich (Paket-Offenheit bestätigt). | Vermeidet falsche Generalisierung einer Marken-IFU. | HEBU GAHF113V004; Paket 001 Offen | mittel |
| 7 | sutures | alle Einträge mit „Nadel offen“ | Präzisierung | `sicherheit`: hausabhängig; `quelle`: null; Nadeln/Artikelnummern erst nach Julian/Haus-SOP; CT-1-Beispiel nur als Artikelprüfung, nicht als Standardbeleg. | Paket selbst: Mengen/Nadeln nicht als allgemeiner Hüft-TEP-Standard belegt – „belegt“ darf hier nicht suggeriert werden. | Paket 001 Offen / Julian-Liste | mittel |
| 8 | supplies | Mengen (Kompressen 20, Bauchtücher 5, Spülvorrat 3 l, …) | Präzisierung | `sicherheit`: hausabhängig; `quelle`: null; Mengen bleiben Vorschläge bis Hausfreigabe. | Keine Quelle belegt konkrete Vorratsmengen als allgemeinen Standard. | Paket 001 Offen | mittel |
| 9 | count | neu | Ergänzung | `label`: Implantierter Markraumstopper zählen; `gilt_fuer`: zementiert, hybrid; `sicherheit`: üblich; `hausabhaengig`: true; `quelle`: null; `hinweis`: Beabsichtigt belassenes Material doku laut Haus-Zählplan/APS-Prinzip (000). | Julian-Liste und 000 APS: belassenes Material gesondert. | APS Flyer „Jeder Tupfer zählt!“ (000); Paket 001 Julian-Liste | mittel |
| 10 | trays | DAA: LINK-Instrumentenbeispiel | Präzisierung | `hinweis` belassen/stärken: nur bei DAA **und** LINK-Konzept; andere Hersteller-DAA-Siebe nicht übernehmen. | Bereits im Paket angelegt; gegen Verwechslung beibehalten. | LINK DAA OP-Technik 2022-06, S. 8–11 | niedrig |

#### C. Implantate (Haus-Systeme)

Nur Zeilen mit selbst gelesenem Herstellerdokument + Seite; sonst „offen“. ClinicalTrials.gov / Pressemitteilungen / GUDID allein = nicht ausreichend.

| Hersteller | System | Komponente | Angabe | Wert | Dokument/Stand/Seite/URL |
|---|---|---|---|---|---|
| Stryker | Accolade II | Schaft | Fixation | zementfrei (cementless / press-fit) | Accolade II Surgical Protocol ACCII-SP-1 Rev-4 ©2022, S. 3–4 · https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf |
| Stryker | Accolade II | Schaft | Konus | V40 (designed for use with Stryker V40 femoral heads) | ACCII-SP-1 Rev-4, S. 4 · gleiche URL |
| Stryker | Accolade II | Schaft | EU-Indikation Hemi | **nicht** für Hemiarthroplastik in EU/EMEA (CE) und Australia; dort nur total hip arthroplasty / cementless | ACCII-SP-1 Rev-4, S. 3 und Footnote S. 12 · gleiche URL |
| Stryker | Accolade II | Schaft | Halswinkel/Offset-Optionen | 132° standard offset; 127° high offset | ACCII-SP-1 Rev-4, S. 4 / Trialing · gleiche URL |
| Stryker | Accolade II | Kopf V40 BIOLOX delta | Durchmesser / Offset | Ø 28: −4/−2,7/0/+4; Ø 32: −4/0/+4; Ø 36: −5/−2,5/0/+2,5/+5/+7,5 mm (nicht pauschal −5…+7,5 für alle Ø) | ACCII-SP-1 Rev-4, S. 12 · gleiche URL |
| Stryker | Accolade II | Kopf Universal Taper BIOLOX delta | Durchmesser / Offset / Adapter | Ø 28/32/36/40/44; Offset −2,5/0/+4 (nicht nur 0); nur mit Universal Taper Sleeve #6519-T-XX | ACCII-SP-1 Rev-4, S. 12 · gleiche URL |
| Stryker | Accolade II | Probekopf V40 | Tray-Beispiel | V40 Head Trials u. a. 28/32/36 mm (weitere Offsets im Tray) | Accolade II Tray Layout ACCII-TL-1 (PDF gelesen) |
| Stryker | Trident II Tritanium | Pfanne | Existenz / Bauarten | Tritanium Solidback / Clusterhole / Multihole u. a. auf Produktseite genannt; **Außen-Ø / max. Kopf / Inlay-Innen-⌀: offen** | Produktseite DE gelesen; keine gelesene OP-Technik/Größentabelle · https://www.stryker.com/de/de/joint-replacement/products/trident-ii.html |
| Stryker | UHR Universal Head | Duokopf | Außen-Ø-Reihe | 36–61 mm (Katalog UH1-…; Innenköpfe 22/26/28 mm je Größe) | UHR Broschüre Japan HE01-160 Rev1 (PDF gelesen) · https://www.stryker.com/content/dam/stryker/ja/ja/portfolios/orthopaedics/joint-replacement/HE01-160_Rev1_UHR_BipolarSystem_s.pdf |
| Stryker | UHR + Accolade II (EU) | Duokopf+Schaft | Kompatibilität / Freigabe | **offen / für EU-Hemi nicht freigegeben** (Accolade II EU ohne Hemi-Indikation; UHR-PDF nennt keinen V40/Accolade-II-Bezug) | ACCII-SP-1 + UHR HE01-160 |
| Mathys | twinSys / RM Pressfit vitamys / seleXys PC / RM Classic / Bipolarkopf | Schaft/Pfanne/Duokopf | alle Entwurfswerte | **offen** | mathysmedical.com PDFs HTTP 415; Enovis/eIFU HCP-Login – Dokumente nicht lesbar |
| Mathys | zementierte Pfanne | Pfanne | Name / Größen / REF | **offen** | kein gelesenes Herstellerdokument |
| Smith+Nephew | POLARSTEM zementfrei | Schaft | Material / Oberfläche | Titanlegierung mit poröser Titanplasma-/HA-Beschichtung (Ti/HA); single use, ohne Zement | POLARSTEM IFU 81098832 Rev. 2 · https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283 |
| Smith+Nephew | POLARSTEM zementiert | Schaft | Material / Köpfe | Edelstahl; mit Knochenzement; Köpfe laut IFU nur OXINIUM oder BIOLOX delta | IFU 81098832 Rev. 2 · gleiche URL |
| Smith+Nephew | POLARSTEM | Schaft | Konus | 12/14 taper | IFU 81098832 Rev. 2 · gleiche URL |
| Smith+Nephew | POLARSTEM zementfrei | Schaft | Offset-Varianten | Standard CCD 135°; lateral 126°; valgus 145°; teilweise mit Collar | IFU 81098832 Rev. 2 · gleiche URL |
| Smith+Nephew | R3 Acetabular System | Pfanne | Größen / Inlays / max. Kopf | **offen** (Julian: R3 bestätigt im Haus) | Produktseite ohne belastbare Größentabelle; keine gelesene OP-Technik |
| Smith+Nephew | zementierte Pfanne | Pfanne | Name / Größen / REF | **offen** | kein gelesenes Herstellerdokument |
| Smith+Nephew | OXINIUM Kopf | Kopf | Existenz / Größen | Existenz genannt; Größen/Offset **offen** | IFU (Kombinationshinweis); keine Größentabelle gelesen |
| Smith+Nephew | TANDEM Bipolar | Duokopf | Bau / Größen / Taper-Sleeve | **offen**; FDA-Recall-Hinweis im Entwurf = Behördenmeldung, keine Größenquelle | Produktseite; Recall ≠ IFU-Größen |

**Korrektur Entwurf Stryker (verified:false):** Offset-Angaben Universal Taper und pauschales „−5 bis +7,5“ für alle V40-BIOLOX-Ø korrigieren; Trident-Größen und UHR+Accolade-II-EU als offen/nicht freigegeben führen – nicht aus ClinicalTrials/GUDID übernehmen.

#### D. JSON

```json
{
  "paket": "001-hueft-tep",
  "version": "1.0",
  "geprueft_am": "2026-10-07",
  "korrekturen": [
    {
      "abschnitt": "pitfalls",
      "label": "Alkoholansammlungen vermeiden",
      "menge": null,
      "einheit": null,
      "spez": "Keine Flüssigkeitsansammlung Hautantiseptikum; vor HF abtrocknen laut Antiseptikum-IFU; NE nicht unter Flüssigkeit",
      "schicht": null,
      "gilt_fuer": ["hf_mono"],
      "optional": false,
      "sicherheit": "belegt",
      "hausabhaengig": true,
      "quelle": {
        "titel": "Prävention postoperativer Wundinfektionen",
        "stand": "2018",
        "seite": "460",
        "url": "https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf?isAllowed=y&sequence=1"
      },
      "hinweis": "Bisherige Allein-Zuordnung zu HEBU zu weit; HEBU nur Brand/Flüssigkeit unter NE ergänzend"
    },
    {
      "abschnitt": "workflow",
      "label": "Anästhesie vor Zement informieren",
      "menge": null,
      "einheit": null,
      "spez": "Anästhesie über jeden Schritt des Zementiervorgangs informieren",
      "schicht": null,
      "gilt_fuer": ["zementiert", "hybrid"],
      "optional": false,
      "sicherheit": "belegt",
      "hausabhaengig": false,
      "quelle": {
        "titel": "Factsheet Implantationssyndrom / BCIS",
        "stand": "Download 2026-10-07",
        "seite": "1",
        "url": "https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf"
      },
      "hinweis": "BCIS Nr.1 Chirurgie – Schritt-für-Schritt, nicht nur einmal vor Einbringen"
    },
    {
      "abschnitt": "heike",
      "label": "Heike-Satz Anästhesie Zement",
      "menge": null,
      "einheit": null,
      "spez": "Zementiert? Anästhesie über jeden Zementierschritt informieren.",
      "schicht": null,
      "gilt_fuer": ["zementiert", "hybrid"],
      "optional": false,
      "sicherheit": "belegt",
      "hausabhaengig": false,
      "quelle": {
        "titel": "Factsheet Implantationssyndrom / BCIS",
        "stand": "Download 2026-10-07",
        "seite": "1",
        "url": "https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf"
      },
      "hinweis": null
    }
  ],
  "ergaenzungen": [
    {
      "abschnitt": "implants",
      "label": "EU: keine Hemi mit Accolade II",
      "menge": null,
      "einheit": null,
      "spez": "Accolade II in EU/EMEA/CE/Australia nicht für Hemiarthroplastik indiziert",
      "schicht": null,
      "gilt_fuer": ["alle"],
      "optional": false,
      "sicherheit": "belegt",
      "hausabhaengig": true,
      "quelle": {
        "titel": "Accolade II Femoral Hip System Surgical Protocol ACCII-SP-1",
        "stand": "Rev-4 ©2022",
        "seite": "3, 12",
        "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf"
      },
      "hinweis": "UHR/Duokopf+Accolade II in EU nicht als freigegebene Kombi führen"
    },
    {
      "abschnitt": "count",
      "label": "Markraumstopper mitzählen",
      "menge": null,
      "einheit": null,
      "spez": "Implantierten/belassenen Markraumstopper in Zähl-/Implantatdokumentation",
      "schicht": null,
      "gilt_fuer": ["zementiert", "hybrid"],
      "optional": false,
      "sicherheit": "üblich",
      "hausabhaengig": true,
      "quelle": null,
      "hinweis": "Ableitung APS belassenes Material + Julian-Liste; Haus-Zählplan maßgeblich"
    },
    {
      "abschnitt": "draping",
      "label": "Flüssigkeitsdichte Abdeckung",
      "menge": null,
      "einheit": null,
      "spez": "Bei erwartetem Durchfeuchten flüssigkeitsundurchlässig (Kat. IB)",
      "schicht": null,
      "gilt_fuer": ["alle"],
      "optional": false,
      "sicherheit": "belegt",
      "hausabhaengig": true,
      "quelle": {
        "titel": "Prävention postoperativer Wundinfektionen",
        "stand": "2018",
        "seite": "460",
        "url": "https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf?isAllowed=y&sequence=1"
      },
      "hinweis": "Präzisierung zur bestehenden Zeile"
    }
  ],
  "streichungen": [],
  "quellen_neu": [
    {
      "id": "Q_ACCOLADE_SP",
      "titel": "Accolade II Femoral Hip System Surgical Protocol",
      "stand": "ACCII-SP-1 Rev-4 ©2022",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf"
    },
    {
      "id": "Q_POLARSTEM_IFU",
      "titel": "POLARSTEM femoral stems Instructions for Use",
      "stand": "81098832 Rev. 2",
      "url": "https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283"
    },
    {
      "id": "Q_UHR_JP",
      "titel": "UHR Universal Head Bipolar System Broschüre",
      "stand": "HE01-160 Rev1",
      "url": "https://www.stryker.com/content/dam/stryker/ja/ja/portfolios/orthopaedics/joint-replacement/HE01-160_Rev1_UHR_BipolarSystem_s.pdf"
    }
  ],
  "implantate": [
    {
      "hersteller": "Stryker",
      "system": "Accolade II",
      "angabe": "fixation",
      "wert": "zementfrei",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "3-4",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "Accolade II",
      "angabe": "konus",
      "wert": "V40",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "4",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "Accolade II",
      "angabe": "eu_hemiarthroplastik",
      "wert": "nicht indiziert (EU/EMEA CE / Australia)",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "3, 12",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "V40 BIOLOX delta",
      "angabe": "durchmesser_offset_mm",
      "wert": "28: -4/-2.7/0/+4; 32: -4/0/+4; 36: -5/-2.5/0/+2.5/+5/+7.5",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "12",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "Universal Taper BIOLOX delta",
      "angabe": "durchmesser_offset_adapter",
      "wert": "28/32/36/40/44; Offset -2.5/0/+4; Sleeve 6519-T-XX Pflicht",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "12",
      "url": "https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-45343/OrTQyxQIqD2-WhrxKy8f3JDuPuEV4Q/ACCII_SP_1.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "Trident II Tritanium",
      "angabe": "aussen_d_mm_kopfbereich",
      "wert": "offen",
      "dokument": null,
      "seite": null,
      "url": null,
      "verified": false
    },
    {
      "hersteller": "Stryker",
      "system": "UHR",
      "angabe": "aussen_d_mm",
      "wert": "36-61 (Katalog UH1)",
      "dokument": "HE01-160 Rev1",
      "seite": "Katalogtabelle",
      "url": "https://www.stryker.com/content/dam/stryker/ja/ja/portfolios/orthopaedics/joint-replacement/HE01-160_Rev1_UHR_BipolarSystem_s.pdf",
      "verified": true
    },
    {
      "hersteller": "Stryker",
      "system": "UHR + Accolade II EU",
      "angabe": "freigabe",
      "wert": "offen / EU-Hemi nicht freigegeben",
      "dokument": "ACCII-SP-1 Rev-4",
      "seite": "3, 12",
      "url": null,
      "verified": true
    },
    {
      "hersteller": "Mathys",
      "system": "twinSys / RM / seleXys / Bipolar",
      "angabe": "alle Entwurfswerte",
      "wert": "offen",
      "dokument": null,
      "seite": null,
      "url": null,
      "verified": false
    },
    {
      "hersteller": "Smith+Nephew",
      "system": "POLARSTEM",
      "angabe": "konus",
      "wert": "12/14",
      "dokument": "IFU 81098832 Rev. 2",
      "seite": "Product-specific Information",
      "url": "https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283",
      "verified": true
    },
    {
      "hersteller": "Smith+Nephew",
      "system": "POLARSTEM zementfrei",
      "angabe": "material",
      "wert": "Titanlegierung Ti/HA-beschichtet",
      "dokument": "IFU 81098832 Rev. 2",
      "seite": "Product-specific Information",
      "url": "https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283",
      "verified": true
    },
    {
      "hersteller": "Smith+Nephew",
      "system": "POLARSTEM zementiert",
      "angabe": "material_koepfe",
      "wert": "Edelstahl; Köpfe nur OXINIUM oder BIOLOX delta laut IFU",
      "dokument": "IFU 81098832 Rev. 2",
      "seite": "Product-specific Information",
      "url": "https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283",
      "verified": true
    },
    {
      "hersteller": "Smith+Nephew",
      "system": "R3 / TANDEM Größen",
      "angabe": "groessen_kompatibilitaet",
      "wert": "offen",
      "dokument": null,
      "seite": null,
      "url": null,
      "verified": false
    }
  ],
  "pruefung_a_statistik": {
    "bestaetigt": 11,
    "zu_weit": 1,
    "nicht_gefunden": 0
  }
}
```

## Kurznotiz Methodik
- Paketquelle: GitHub `pakete/001-hueft-tep.md` + `.json` (aktuell; lokaler Mirror veraltet).
- Quellen A: AMBOSS HTML, KRINKO PDF, LINK PDF, BCIS PDF, HEBU PDF – alle 200, Text extrahiert.
- Implantate: Accolade SP, Accolade Tray, UHR JP, POLARSTEM IFU gelesen; Mathys Domains 415 / Enovis-Login → offen; Trident-Größentabelle ohne OP-Technik → offen.
