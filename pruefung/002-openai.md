# 002 Knie-TEP – OpenAI Implantat-Recherche und Vorprüfung

Stand: 2026-10-07, 23:31 Europe/Berlin. Ersteller: OpenAI.
Auftrag: Julian „Arbeite an 002“; Fortsetzung der Knie-Implantat-Recherche.
Geprüfter Repo-Stand: `df5d4e2fcad5c1bd4f81b8aee32a56173ba08158`.

**Ergebnis: Recherche konkret ergänzt; Gesamtprüfung und App-Übernahme offen.**
`pakete/002-basis.md` und Knie-Systemdateien unter `implantate/` fehlen am geprüften Stand. Deshalb liegt hier keine vollständige Paketabnahme vor. Der Bericht ersetzt die bisherige reine Prüffeld-Liste durch Registerbelege, 18 konkrete REF-Beispiele, systemspezifische Kompatibilitätsbefunde und eine nachvollziehbare Restliste.

Nur diese eigene Prüfdatei wird geändert. Zuständigkeiten aus README/STATUS bleiben bestehen. Kein Instrumentenprüfbericht, keine Änderung von STATUS, Basisdateien oder Kerlect-Code. App-Ziel bleibt ausschließlich Kerlect Consumer `6aa3f64b0b23cc244ce7686d`.

## 1. Auswahl nach Registerdaten

### Schweiz: konkrete aktuelle Jahreszahlen innerhalb des Reports

Quelle R1, Tabelle 5.8, gedruckte/PDF-Seite 157: primäre Total-Knie-Systeme, alle Diagnosen und Komponentenfixationen. Die Tabelle enthält die Systeme, die zusammen ungefähr 75 % der Fälle 2019–2024 abdecken. Folgende **2024-Spalte**, nach Fallzahl absteigend sortiert, wurde am gerenderten Original kontrolliert:

| System/Untertyp | Fälle 2024 |
| --- | ---: |
| GMK sphere | 3.432 |
| Attune CR-FB | 2.690 |
| Persona CR-MC | 2.631 |
| Attune CR-RP | 1.411 |
| Attune PS-RP | 1.092 |
| Persona CR-UC | 1.080 |
| Balansys CR | 928 |
| Triathlon PS | 838 |
| Persona PS | 835 |
| Origin PS | 681 |
| Balansys PS | 672 |
| Balansys UC | 655 |
| Attune PS-FB | 596 |

Die Tabellenzeile Gesamt nennt 21.371 Fälle 2024 einschließlich „Other systems“. Diese Untertypen sind keine vollständige Rangliste aller Marken. Keine Addition mit deutschen Mehrjahreskohorten; keine Aussage über Überlegenheit oder Lieferbarkeit.

### Deutschland: große dokumentierte Kohorten, keine Jahresmarktanteile

Quelle R2, Tabelle 60, gedruckte Seiten 146–150 (PDF-Doppelseiten 80–82). Beispiele aus **Standard-KTEP, CR, feste Plattform, zementiert, ohne primären Retropatellarersatz**:

| Femur / Tibia | Anzahl | Erfasster Zeitraum | Druckseite |
| --- | ---: | --- | --- |
| COLUMBUS / COLUMBUS | 26.946 | 2013–2024 | 148 |
| NexGen Flex / NexGen | 22.780 | 2012–2024 | 148 |
| LEGION COCR / Genesis II | 19.243 | 2014–2024 | 148 |
| GENESIS II COCR / Genesis II | 12.320 | 2013–2024 | 148 |

Die gedruckte Tabelle erstreckt sich jeweils über eine Doppelseite; die genannten Systemzeilen stehen links. Unterschiedliche Zeiträume und getrennte Fixations-/Stabilisierungsgruppen verhindern eine unveränderte Nutzung als Jahresranking.

R2 dokumentiert außerdem auf S. 60, Tabelle 47, ein NexGen-Insert für Tibia 3–4 zusammen mit Tibia 5 als Größeninkompatibilität; Tabelle 49 zeigt einen ATTUNE-PS-Insert mit CR-Femur als ungeeignete Paarung. Diese Beispiele sind **Negativfälle**, keine zulässigen Sets.

### Österreich

R3 ist ein offizieller Bericht von 2018 zur Versorgung und Ergebnisqualität, keine aktuelle nach Marken aufgeschlüsselte Knie-Rangliste. In diesem Lauf wurde kein belastbares aktuelles österreichisches Markenranking erschlossen. Daher bleibt **AT-Häufigkeit offen**; keine erfundenen DACH-Prozentwerte.

### Konsequenz für die weitere Systemauswahl

Aus den tatsächlich gelesenen Registerabschnitten ergibt sich als Arbeitsauswahl: ATTUNE, Persona, GMK Sphere, balanSys, Triathlon sowie COLUMBUS, NexGen, LEGION und GENESIS II. Origin PS ist zusätzlich durch R1 begründet. Das ist eine Recherchepriorität, keine vollständige Marktübersicht oder klinische Empfehlung. Unikondyläre Systeme und Revisionen erhalten getrennte Datensätze und Auswahlwege.

## 2. 18 konkrete REF-Beispiele

**„Bestätigt“ bedeutet hier: Artikelidentität am genannten Original belegt.** Es bedeutet weder aktuelle DACH-Lieferbarkeit noch Freigabe eines gesamten Implantatsets. Für alle Einträge gilt: laut Herstellerdokument mit dessen Stand; aktuelle IFU und Etikett prüfen. Keine echten Patienten-, Chargen- oder Ablaufdaten aus Beispielen erzeugen.

| Nr. | Hersteller/System | Komponente und Variante | Größe / Seite | REF | Beleg |
| ---: | --- | --- | --- | --- | --- |
| 1 | Zimmer Biomet Persona | Femur CR | 7 rechts | `42-5026-062-02` | P1, Druck S. 46 / PDF 48 |
| 2 | Zimmer Biomet Persona | Femur PS | 7 rechts | `42-5006-062-02` | P1, Druck S. 46 / PDF 48 |
| 3 | Zimmer Biomet Persona | Tibiaplatte, zementiert, mit Schaft | F rechts | `42-5320-075-02` | P1, Druck S. 45 / PDF 47 |
| 4 | Stryker Triathlon | Femur CR, zementiert | 4 links | `5510-F-401` | T1, S. 57 |
| 5 | Stryker Triathlon | Femur CR, zementiert | 4 rechts | `5510-F-402` | T1, S. 57 |
| 6 | Stryker Triathlon | primäre Tibiabasis, zementiert | 4 | `5520-B-400` | T1, S. 57 |
| 7 | Stryker Triathlon | CR-Insert X3 | 4 / 9 mm | `5530-G-409-E` | T1, S. 58 |
| 8 | Smith+Nephew LEGION | Femur CR, zementiert, CoCr | 4 links | `7142-3204` | L1, S. 40 |
| 9 | Smith+Nephew LEGION | Femur CR, zementiert, CoCr | 4 rechts | `7142-3214` | L1, S. 40 |
| 10 | Smith+Nephew LEGION | Femur CR, zementiert, OXINIUM | 4 links | `7142-1234` | L1, S. 40 |
| 11 | Smith+Nephew LEGION | Femur CR, zementiert, OXINIUM | 4 rechts | `7142-1224` | L1, S. 40 |
| 12 | Medacta GMK Sphere | Femur, zementiert, CoCrMo | 4 links | `02.12.0004L` | M1, S. 4 |
| 13 | Medacta GMK Sphere | Femur, zementiert, CoCrMo | 4 rechts | `02.12.0004R` | M1, S. 4 |
| 14 | Medacta GMK Sphere | Femur, zementiert, CoCrMo | 4+ links | `02.12.0024L` | M1, S. 4 |
| 15 | Medacta GMK | feste Tibiabasis, zementiert | t3-i4 links | `02.12.T3i4L` | M1, S. 11 |
| 16 | Medacta GMK Sphere | Flex-Insert, UHMWPE | 4 links / 10 mm | `02.12.0410FL` | M1, S. 6 |
| 17 | Medacta GMK | Resurfacing-Patella, UHMWPE | 1 | `02.07.0033RP` | M1, S. 14 |
| 18 | Aesculap COLUMBUS | CR/PS-Tibiaplateau, modular, zementiert, CoCr29Mo | T2 | `NN073K` | C1, Produktspezifikation |

T1 nennt ausdrücklich REF-Schablonen mit `X` als Größe. Nr. 4–7 sind durch Einsetzen des ausdrücklich erlaubten Wertes `X=4` abgeleitet; keine Fortsetzung vermuteter Nummernfolgen. Seitenspezifität wird bei Tibia/Insert nicht aus der Femur-Seite ergänzt.

P1 wird von der europäischen Produktseite verlinkt. T1 enthält einzelne ausdrücklich als nicht CE-gekennzeichnet markierte Varianten; diese dürfen nicht automatisch in einen DACH-Katalog gelangen. L1 ist ein älterer, US-geprägter Katalog mit regional variierender Verfügbarkeit; seine Artikelbelege benötigen eine aktuelle regionale Gegenprüfung. M1 ist ausdrücklich nicht für den US-Markt bestimmt, verlangt aber eine lokale Zulassungsprüfung. C1 ist ein australischer Herstellerkatalog: kein Nachweis für aktuelle DACH-Verfügbarkeit.

## 3. Kompatibilitätsbefunde und Anforderungen an die Auswahl

| ID | Befund am Original | Konsequenz für 002 |
| --- | --- | --- |
| K01 | Persona führt getrennte CR-, MC-, UC-, PS- und CPS-Matrizen; P1, Druck S. 68–69 / PDF 70–71. | Pro Insert-Typ eine eigene Relation speichern. Eine gemeinsame „Persona passt“-Regel wäre zu weit. |
| K02 | P1, S. 68: Bei Tibia E/F umfasst der CR-Insertbereich Femur 3–11; MC ist unter anderem in 4–5, 6–7 und 8–11 unterteilt. | Femur 7 benötigt in der MC-Auswahl die passende Gruppe 6–7/E–F. Kein Rückschluss vom breiteren CR-Bereich. |
| K03 | ATTUNE A1, S. 130: Femur 4/4N → Insertgröße 4; zugehörige modulare Tibiabasengrößen 2–6. | Femur-, Insert- und Tibiagröße getrennt modellieren. Zusätzlich CR/PS/MS und FB/RP anhand ihrer jeweiligen Vorgaben prüfen. |
| K04 | GMK M1, S. 17: `t3-i4` benötigt Insert 4, `t4-i3` Insert 3. | Tibia-Abdeckung und Insert-Anschlussgröße sind verschiedene Felder. „Gleiche Ziffer“ ist keine allgemeine Prüfregel. |
| K05 | M1, S. 17: Für t3-i4 sind die Femurgruppen 3/3+, 4/4+, 5/5+, 6/6+ eingetragen. | Die freigegebenen Tabellenzellen explizit abbilden; leere Felder nicht ergänzen. |
| K06 | T1, S. 58: X3-REF kommen mit und teilweise ohne `-E` vor. | Suffix im Artikelcode erhalten. Identität und Paarung nicht durch Kürzen der REF bestimmen. |

Diese Befunde sind Anforderungen für den späteren Datenimport, noch keine in der App geprüften Regeln. Insbesondere sind technische Größenpaarung, Band-/Stabilisierungsanforderung, Fixation und regionale Produktzulassung unterschiedliche Prüfschritte.

**Gezielte spätere Abnahmeszenarien:** GMK t3-i4 + Insert 3 ablehnen; Persona MC 8–11/E–F mit Femur 7 ablehnen; ATTUNE CR-Femur + PS-Insert nicht durch bloße Größenübereinstimmung akzeptieren; links/rechts kontrollieren; bei fehlender Quelle Status „ungeprüft“ statt „passt“.

## 4. Sicherheitsfund: chargengenau, keine pauschale Systemsperre

S1: DePuy-Sicherheitsinformation, DPS 2293230, Bezug auf Schreiben vom 18.08.2023, bei Swissmedic veröffentlicht. Betroffen ist ATTUNE zementfreier CR-Femur rechts Größe 4, REF `1504-01-204`, **Lot `3883327`**, GTIN `10603295041474`. Die Quelle beschreibt eine auf zwölf Implantate dieses Lots begrenzte Fehlkennzeichnung: verpackte Größe 4, tatsächliche Abmessungen Größe 5.

Für den späteren Sicherheitseintrag sind REF **und Lot** erforderlich. Die betroffene Charge darf nicht als normales Packungsbeispiel dienen. Daraus folgt keine Behauptung, das gesamte ATTUNE-System sei zurückgerufen. Ein aktueller vollständiger Abgleich aller Systeme mit BfArM/Swissmedic/Hersteller-FSCA ist noch offen; „keinen weiteren Fund geprüft“ darf nicht zu „rückruffrei“ werden.

## 5. Produktbilder und echte Verpackungen

Herstellerseitige **Produktabbildungen** sind als Rechercheeinstieg bei Persona (P0), Triathlon (T0) und GMK Sphere (M0) vorhanden. Sie sind weder Belege für eine bestimmte Verpackung noch automatisch Bilder eines konkreten REF-Artikels.

Für keine der 18 Zeilen wurde in diesem Lauf ein authentisches, eindeutig REF-zugeordnetes Verpackungsfoto verifiziert. Entsprechend bleiben `packungsfoto_url` und eine eventuelle Nutzungserlaubnis offen. Keine Produktgrafik als Verpackungsfoto umetikettieren.

Für Kerlect bleibt der vorhandene Entwurfsansatz sinnvoll: symbolische Packung ausdrücklich als solche kennzeichnen; Firma, System, belegte REF, Größe und Seite aus dem Datensatz anzeigen. LOT, Ablaufdatum und scanbarer UDI-Code bleiben leer, bis reale zugehörige Daten vorliegen. Ein späteres echtes Bild benötigt Herkunft, Artikelbezug, Prüfdatum und Nutzungsstatus. Eine Herstellerabbildung allein belegt keine Sterilität des vorliegenden Produkts.

## 6. Restliste für die Übergabe

| Prüffeld | Stand / konkrete nächste Arbeit |
| --- | --- |
| Register | DE-Mehrjahreskohorten und CH-2024-Zahlen belegt; aktuelle AT-Markenhäufigkeit offen. |
| Systemkataloge | 18 Artikelbeispiele belegt. Vollständige regionale Größen-/REF-Listen fehlen noch, besonders ATTUNE, balanSys, NexGen, GENESIS II und Origin. |
| Kompatibilität | Persona, ATTUNE und GMK mit konkreten Tabellenbefunden. Vollständige REF-Paarungsgraphen und regionale IFU fehlen. |
| Indikationen/Bänder | Keine allgemeine OP-Indikationsprüfung ersetzt. Indikationsgrenzen je System, CR/PS/UC/MC/CPS und Bandstatus noch gegen gültige IFU prüfen. |
| Materialien/Fixation | Nur belegte Varianten übernehmen; keine Materialvererbung auf eine ganze Systemfamilie. |
| Patella | Ein GMK-Artikelbeispiel belegt; übrige Varianten/Größen und systemspezifische Paarungen ausarbeiten. |
| Revision/Uni | Getrennt von primärer Totalprothese halten; nicht allein wegen Hersteller-/Familiennamen einmischen. |
| Sicherheit | Ein gezielter historischer ATTUNE-Lotfund dokumentiert; MR, Sterilisation, Verpackungsprüfung und vollständiger aktueller FSCA-Abgleich offen. |
| Bilder | Hersteller-Produktabbildungen gefunden; echte REF-bezogene Verpackungsfotos weiterhin offen. |
| Pipeline/App | Basis und Knie-JSON fehlen. Danach reguläre Gegenprüfung und Freigabe; erst anschließend Import/Abnahme in Kerlect. |

## 7. Quellenverzeichnis und Nachweis

Alle nachfolgend als Beleg verwendeten Inhalte wurden in diesem Lauf direkt geöffnet. PDF-Tabellen wurden zusätzlich bildlich kontrolliert; keine Übernahme allein aus Such-Snippets. Seitenangaben sind gedruckte Seiten, sofern PDF-Seiten nicht gesondert angegeben sind.

- **R1 – SIRIS Report Hip and Knee 2025**, Tabelle 5.8, S. 157, Daten bis 2024, Schweiz. [Original-PDF](https://www.anq.ch/wp-content/uploads/2025/12/ANQakut_SIRIS_Hips-Knee_Report_2025.pdf), über [ANQ](https://www.anq.ch/de/fachbereiche/akutsomatik/messinformation-akutsomatik/implantatregister-siris-huefte-knie-schulter/).
- **R2 – EPRD-Jahresbericht 2025**, Dateistand 28.10.2025, Tabelle 60 S. 146 ff.; Mismatch-Beispiele S. 60. [Original-PDF](https://www.eprd.de/fileadmin/user_upload/Dateien/Publikationen/Berichte/Jahresbericht2025-Status5_2025-10-28_F.pdf).
- **R3 – Hüft- und Knie-Endoprothetik in Österreich**, Sozialministerium, 2018, Management Summary S. 3 und Datenpräsentation S. 51 ff. [Original-PDF](https://www.sozialministerium.gv.at/dam/jcr:a32545b2-d40c-43f2-ac1f-7c6ce97804a8/endoprothetik-bericht_27.07.18_final.pdf).
- **P0 – Persona, europäische Herstellerseite**, abgerufen 07.10.2026. [Produkt und Originalverlinkung](https://www.zimmerbiomet.eu/en/products/persona-the-personalised-knee).
- **P1 – Persona The Personalized Knee, Surgical Technique**, `3914.1-GLBL-en`, Issue 2022-08. Druck S. 45–46 und 68–69. [Original-PDF über P0](https://assets.ctfassets.net/rc4arfpyhdpw/6R1FpGyC07WTfcszrO2MKP/710ce1e70eb68bda7a449e07909f4859/persona-the-personalized-knee-surgical-technique1.pdf).
- **T0 – Triathlon, deutsche Herstellerseite**, abgerufen 07.10.2026. [Produkt](https://www.stryker.com/de/de/joint-replacement/products/triathlon-total-knee-system/index-eu.html).
- **T1 – Triathlon Knee System, Surgical protocol / Katalogsammlung**, `TRIATH-SP-30_Rev-1_29865`, ©2021, S. 57–58, regionale Hinweise S. 313. [Original-PDF](https://www.stryker.com/content/dam/stryker/joint-replacement/training-and-education/orthopaedic-fellows-summit/resources/1--knees/3.pdf).
- **L1 – LEGION Total Knee System, Total System Specification Guide and Product Catalog**, `02861 V1`, 02/2015, S. 40. Historischer Herstellerkatalog, regionaler Abgleich erforderlich. [Original-PDF](https://smith-nephew.stylelabs.cloud/api/public/content/9b60b8ccb8d34736b556c9582336e376?download=true&v=e3edc939).
- **M0 – GMK Sphere, Herstellerseite**, abgerufen 07.10.2026. [Produkt und Originalverlinkung](https://www.medacta.com/EN/gmk-sphere).
- **M1 – GMK Sphere Specification Guide**, `99.26SPHERE.11SG`, Rev. 02, 12/2020, S. 4, 6, 11, 14, 17, 20. Nicht-US; lokale Zulassung prüfen. [Original-PDF](https://aws-media.medacta.com/media/9926sphere11sg-02.pdf).
- **A1 – ATTUNE Knee System, INTUITION Instruments, Surgical Technique**, `DSUS/JRC/0316/1437 Rev. K`, ©2022, S. 130. US-verlinkte Quelle, DACH-Freigabe gesondert. [Hersteller-Einstieg](https://www.jnjmedtech.com/en-US/product/attune-knee-system), [Original-PDF nach Weiterleitung](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/surgical-technique-guide/attune-knee-system-intuition-instruments-dsusjrc03161437.pdf).
- **C1 – COLUMBUS CR/PS, NN073K**, B. Braun Australien, Produktspezifikation, abgerufen 07.10.2026; Dokumentrevision nicht ausgewiesen. [Herstellerartikel](https://catalogs.bbraun.com.au/en-AU/p/NN073K/columbus-cr-ps-tib-plateau-cemented-t2).
- **S1 – ATTUNE zementfreier CR-Femur, falsche Größe, DPS 2293230**, DePuy/Swissmedic, 2023, PDF S. 1 und 3–4. [Original-Sicherheitsinformation](https://fsca.swissmedic.ch/mep/api/publications/Vk_20230814_04/documents/1).

Die großen Register-PDFs und A1 wurden nach Abrufproblemen des Web-Parsers direkt vom veröffentlichten Original geladen und mit Poppler gelesen/gerendert. Prüfsummen der gelesenen Dateien:

| Quelle | SHA-256 |
| --- | --- |
| R1 | `752e23ea4aa0d48442f520184976a99aa5ba245760d3f908a9be17ac629608f0` |
| R2 | `42f833bc4076ac91536af85df1c93c976a81f63dfc7d4915ea050a26f1e1bd97` |
| A1 | `2876230fb9b6e27e41416e55ac7f5f0fa4a21eb42c6cc2673403434dba84427f` |

## 8. Maschinenlesbarer Übergabestatus

```json
{
  "paket": "002-knie-tep",
  "geprueft_am": "2026-10-07",
  "repo_basis": "df5d4e2fcad5c1bd4f81b8aee32a56173ba08158",
  "ergebnis": "recherche_ergaenzt_gesamtpruefung_offen",
  "klinische_freigabe": false,
  "app_implementiert_in_diesem_lauf": false,
  "artikelbeispiele": 18,
  "basisdatei_vorhanden": false,
  "kompatibilitaetsbefunde": ["K01", "K02", "K03", "K04", "K05", "K06"],
  "offen": [
    "vollstaendige_basis_und_knie_systemdateien",
    "regionale_aktuelle_ref_kataloge_und_ifu",
    "vollstaendige_ref_kompatibilitaetsrelationen",
    "authentische_ref_bezogene_verpackungsfotos",
    "aktuelle_at_markenhaeufigkeit",
    "vollstaendiger_aktueller_sicherheitsabgleich",
    "regulaere_paketpruefung_und_app_abnahme"
  ]
}
```
