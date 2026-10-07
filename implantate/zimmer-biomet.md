# Zimmer Biomet – Avenir, Fitmore, CLS Spotorno, Alloclassic + Allofit / G7; zementiert M.E.M., MS-30 + Flachprofil

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine EU-IFU gelesen; keine klinische Freigabe._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `zb.avenir.zementfrei` | schaft | Avenir (zementfrei) | fixation: zementfrei; hinweis: Avenir ≠ Avenir Complete (eigene EPRD-Zeile Avenir Complete Collarless n=4.820); werte: Größen/REF offen | avenir | offen |
| `zb.avenir.zementiert` | schaft | Avenir zementiert | fixation: zementiert; werte: offen; Duokopf in CH: Avenir zementiert + ZB bipolar (SIRIS 2024 n=151) | – | offen |
| `zb.fitmore` | schaft | Fitmore | fixation: zementfrei; konus: 12/14; material: Protasul-64; familien: A, B, B Extended Offset, C – je Größen 1–14; ccd_grad: 140 / 137 / 129 / 127 (Zuordnung je Familie laut Original S. 12–15); hinweis: A Größe 1 nicht USA; 13/14 auf Anfrage; konflikt: B Extended Gr. 12 (REF 01.00551.312): Offset 50,0 mm (S. 14) vs. 50,75 mm (S. 16) – Wert offen | fitmore | belegt |
| `zb.cls_spotorno` | schaft | CLS Spotorno | fixation: zementfrei; werte: EU-Größen offen (nur JP/US-Ausgaben gefunden) | – | offen |
| `zb.alloclassic` | schaft | Alloclassic Zweymüller | fixation: zementfrei; werte: EU-Größen offen; Konus je Variante am Etikett (8/10 nicht pauschal) | – | offen |
| `zb.mem` | schaft | M.E.M. Geradschaft (zementiert) | fixation: zementiert; hinweis: M.E.M. ≠ MS-30; werte: offen – nur Registerbeleg (EPRD zementiert #1) | – | offen |
| `zb.ms30` | schaft | MS-30 (zementiert) | fixation: zementiert; konus: 12/14; varianten: {"Standard": "CCD 130–135°, Offset 37,7–43,3 mm", "Lateral": "CCD 124,3–128°, Offset 42,2–48,4 mm"} | ms30 | belegt |
| `zb.allofit` | pfanne | Allofit / Allofit-S | fixation: zementfrei; werte: Größen/Liner/max. Kopf-Ø offen; Allofit, Allofit-S, Allofit IT getrennt führen | liners | offen |
| `zb.g7` | pfanne | G7 | fixation: zementfrei; liner: PE Neutral/High Wall/10°, +5 Lateralized, Keramik, Freedom, Dual Mobility – getrennt; hinweis: 70/72 und J nur OsseoTi Multi Hole | g7 | belegt |
| `zb.flachprofil` | pfanne | Flachprofil (zementiert) | fixation: zementiert; werte: offen – nur Registerbeleg (EPRD zementiert #1) | – | offen |
| `zb.kopf.biolox_delta` | kopf | BIOLOX delta 12/14 (ZB) | konus: 12/14; hinweis: Chart markiert Avenir/CLS/Fitmore/Alloclassic-Zeilen; Ø/Offset je Zeile offen; BIOLOX OPTION eigene Familie | ceramic | bedingt |
| `zb.kopf.cocr` | kopf | CoCr 12/14 (ZB) | konus: 12/14; hinweis: Protasul-S30 (Edelstahl) und Metasul getrennt führen | cocr | offen |
| `zb.duokopf.bipolar` | duokopf | Zimmer Biomet Bipolarkopf | chart: MS-30-Zeile: AP 1946/1989 markiert, Multipolar nicht markiert; Fußnote 1 verlangt zusätzlich Artikulations- und Kopf/Schaft-Tabellen; registerbeleg: SIRIS: Avenir zementiert + ZB bipolar 2024 n=151 | bipolar | bedingt |

### Größen – Fitmore (Quelle fitmore)
| familie | groessen |
|---|---|
| A | 1–14 |
| B | 1–14 |
| B Extended Offset | 1–14 |
| C | 1–14 |

### Größen – MS-30 (zementiert) (Quelle ms30)
| groesse | ref_standard | laenge_mm | offset_mm | ccd | ref_lateral | laenge_lat_mm | offset_lat_mm | ccd_lat |
|---|---|---|---|---|---|---|---|---|
| 6 | 30.00.49-060 | 115 | 37.7 | 130 | 01.00351.001 | 116 | 42.2 | 124.3 |
| 8 | 30.00.49-080 | 132 | 38.9 | 131 | 01.00351.002 | 133 | 43.6 | 125.3 |
| 10 | 30.00.49-100 | 136 | 40.1 | 132 | 01.00351.003 | 137 | 44.9 | 126.3 |
| 12 | 30.00.49-120 | 140.5 | 41.3 | 133 | 01.00351.004 | 140.5 | 46.2 | 127.3 |
| 14 | 30.00.49-140 | 146 | 42.3 | 134 | 01.00351.005 | 146 | 47.3 | 127.7 |
| 16 | 30.00.49-160 | 152.5 | 43.3 | 135 | 01.00351.006 | 152.5 | 48.4 | 128 |

### G7_PE – G7 Schale ↔ PE-Liner Kopf-Ø (Quelle g7, S. 4–5 / PDF 7–8)
| schale_mm | alpha | neutral_highwall_10 | plus5_lateralized |
|---|---|---|---|
| 42, 44 | A | 28 | 28 |
| 46 | B | 28, 32 | 28, 32 |
| 48 | C | 28, 32, 36 | 28, 32 |
| 50 | D | 28, 32, 36 | 28, 32, 36 |
| 52 | E | 28, 32, 36, 40 | 28, 32, 36 |
| 54, 56 | F | 28, 32, 36, 40 | 28, 32, 36, 40 |
| 58, 60 | G | 28, 32, 36, 40, 44 | 28, 32, 36, 40 |
| 62, 64 | H | 32, 36, 40, 44 | 32, 36, 40, 44 |
| 66, 68, 70*, 72* | I | 36, 40, 44 | 36, 40, 44 |
| 74*, 76*, 78*, 80* | J | 36, 40, 44 | 36, 40, 44 |
_* nur OsseoTi Multi Hole; nicht auf Keramik/Freedom/Dual Mobility übertragen_

### G7_Keramik – G7 Schale ↔ Keramikliner Kopf-Ø (Quelle g7, S. 7 / PDF 10)
| alpha | kopf_mm |
|---|---|
| A | – |
| B | 28 |
| C | 32 |
| D | 32 |
| E | 32, 36 |
| F | 32, 36 |
| G | 32, 36, 40 |
| H | 32, 36, 40 |
| I | 32, 36, 40 |
| J | – |
_keine Ableitung aus PE-Tabelle_

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `zb.fitmore` | `zb.kopf.biolox_delta` | **bedingt** | nur markierte Chart-Zeile; Ø/Offset/Markt prüfen | ceramic | PDF 1 |
| `zb.avenir.zementfrei` | `zb.kopf.biolox_delta` | **bedingt** | nur markierte Chart-Zeile | ceramic | PDF 1 |
| `zb.cls_spotorno` | `zb.kopf.biolox_delta` | **bedingt** | nur markierte Chart-Zeile | ceramic | PDF 1 |
| `zb.alloclassic` | `zb.kopf.biolox_delta` | **bedingt** | nur markierte 12/14-Zeilen; OPTION 8/10 nicht markiert | ceramic | PDF 1 |
| `zb.g7` | `zb.kopf.biolox_delta` | **bedingt** | Kopf-Ø je Alpha und exaktem Liner laut G7-Tabellen | g7 | 4–7 |
| `zb.ms30` | `zb.duokopf.bipolar` | **bedingt** | AP 1946/1989 markiert; innere Kopfgröße, Kopf-Schaft-Paar und EU-IFU noch prüfen | bipolar | PDF 2 |

## Regeln
- G7: Kopf-Ø hängt von Schale (Alpha) UND Liner ab – z. B. 48/C mit +5 kein 36 mm; Keramik eigene Tabelle. (g7 S. 4–7)
- Kopf nur über tatsächlich markierte Chart-Zeile plus Fußnoten/IFU – gleiche 12/14-Bezeichnung genügt nicht. (ceramic, cocr)
- Nach Keramikbruch keine Metallkopf-Gleitpaarung der betroffenen Liste verwenden (Hersteller nennt Keramik/Keramik oder Keramik/PE). (FA2016-10)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| Allofit-S Alloclassic shell mit Polschraube: Gr. 52/II (REF 4265, Lot 2984922); Gr. 54 (REF 4266, Lots 2984958, 2984959) – Größenbezeichnung laut Original | BfArM | ZFA2019-00187 (10144-19), 30.07.2019 | EU/DE | – | nur diese Chargen; keine pauschale Allofit-Sperre | `zb.allofit` | https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2019/10144-19_kundeninfo_en.pdf?__blob=publicationFile |
| Avenir Müller Gr. 1 (REF 01.06010.001, Lot 2955599) enthält Gr. 2 | BfArM | ZFA2018-00572 / FA2018-06 (13742-18), 31.10.2018 | EU/DE | – | nicht Avenir Complete oder alle Avenir | – | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/13742-18_kundeninfo_de.pdf?__blob=publicationFile |
| Modulare CoCr-Köpfe, Protasul-S30, Metasul (nach Keramikbruch) | BfArM | FA 2016-10 / ZFA 2016-150 (01461-17), 13.02.2017 | EU/DE | – | Sicherheitsinformation zu Revisionen nach Keramikbruch | `zb.kopf.cocr` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/01461-17_Kundeninfo_de.pdf?__blob=publicationFile&v=1 |
| CPT-Schaft – erhöhtes Risiko periprothetischer Femurfraktur | BfArM | ZFA2024-00121 (21393-24), 01.07.2024 | EU/DE | – | CPT nicht in der Auswahl; nicht allein aus Katalog freigeben | – | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/21393-24_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] Avenir (nicht Complete), CLS, Alloclassic, Allofit/Allofit-S: aktuelle EU-Größen/REF/Liner-Tabellen (Modular Liners and Cups 05/2019 lesen)
- [ ] M.E.M. Geradschaft und Flachprofil: Dokumente
- [ ] Kopf-REF/Ø/Offset je Schaft aus Charts
- [ ] Bipolarkopf: Innenkopf und EU-IFU
- [ ] Fitmore B Extended Gr. 12 Offset
- [ ] Implantat-REF (außer MS-30)

## Quellen
- **fitmore** Fitmore Hip Stem Surgical Technique · 1013.3-GLBL-en, 2025-04 · S. S. 12–16 / PDF 14–18; Bestelltabellen S. 16 ff. · Markt: global · gelesen: Grok/Astra 07.10.2026 · https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/fitmore/1013.3-GLBL-en%20Fitmore%20Hip%20Stem%20Surg%20Tech%20A4%20DIGITAL.pdf
- **avenir** Avenir Complete Surgical Technique · 1624.4-GLBL-en, 2021-11-10 · S. PDF 7, 9 (12 Seiten, keine Bestelltabelle) · Markt: global · gelesen: Grok/Astra 07.10.2026 · https://assets.ctfassets.net/rc4arfpyhdpw/4PulT0mR4JdEX4f5n00BxC/88cc646adbb9dbc5309025ed0769cd3e/1624.4-GLBL-en_Avenir_SurgTech.pdf
- **g7** G7 Acetabular System Surgical Technique · 2336.6-GLBL-en, 2026-09-09 · S. S. 3–5 / PDF 6–8 (Thickness Guide); Keramik S. 7 / PDF 10 · Markt: global; lokale Verfügbarkeit prüfen · gelesen: Grok/Astra 07.10.2026 · https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/g7-acetabular-system/2336.6-GLBL-en%20G7%20Acetabular%20System%20Surgical%20Technique.pdf
- **ms30** MS-30 Cemented Hip Stem Surgical Technique · 5087.1-GLBL-en, 2025-12 · S. S./PDF 25–26, 29–30 · Markt: global · gelesen: Grok/Astra 07.10.2026 · https://assets.ctfassets.net/rc4arfpyhdpw/141dC8Nk3O5X6zFJkF1ba2/11cb417e096fc3f917a1cebfee73a33b/5087.1-GLBL-en_MS-30_Cemented_Hip_Stem_Upgraded_Instruments_Surg_Tech_A4_DIGITAL.pdf
- **ceramic** Head and Stem Combinations: Ceramic Femoral Heads · Revised 5/6/2019 · S. PDF 1–3 (Zeilen Alloclassic/Avenir/CLS/Fitmore, Fußnoten) · Markt: EU-Seite; „funktionelle Kompatibilität ≠ regulatorische Zulassung“ · gelesen: Grok/Astra 07.10.2026 · https://assets.ctfassets.net/rc4arfpyhdpw/6LuflsxnuxzS6yod8Wbg5c/75d5c277cb99658423118798f590191e/Ceramic_Femoral_Heads_NEW.pdf
- **cocr** Head and Stem Combinations: CoCr Femoral Heads · Revised 7/15/2020 · S. PDF 1–3 · Markt: EU-Seite · gelesen: Grok/Astra 07.10.2026 · https://assets.ctfassets.net/rc4arfpyhdpw/iV1BfgVRHhLqYPmt2Zt2G/bc7ac72e2ad60e1eed7f7d9f5628fa51/CoCr-Femoral-Heads_NEW.pdf
- **bipolar** Head and Stem Combinations: Unipolar and Bipolar Femoral Heads · Revised 5/6/2019 · S. PDF 1–2 (Zeile MS-30, Fußnote 1) · Markt: EU-Seite · gelesen: Grok/Astra 07.10.2026 · https://assets.ctfassets.net/rc4arfpyhdpw/32LNW4qj9EF9gZTbsgW3XK/aff2b857d83db63fa9441c1d96e1237d/Unipolar_and_Bipolar_Femoral_Heads_NEW.pdf
- **liners** Modular Liners and Cups (Allofit u. a.) · Revised 05/03/2019 · S. gesamt · Markt: EU · gelesen: Perplexity-Fundstelle – noch nicht gelesen · https://assets.ctfassets.net/rc4arfpyhdpw/4cFuQfD9ptPL2LNaoqXCYj/f032b9a0ac0920a7c3e2b2b65949fa47/Liners_and_Cups_Final.pdf

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.

Bilder: keine übernommen – Rechte beim Hersteller.
