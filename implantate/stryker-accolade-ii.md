# Stryker – Accolade II (zementfrei) + Trident II Tritanium + X3 + V40-Köpfe

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `stryker.accolade2.schaft` | schaft | Accolade II | konus: V40; fixation: zementfrei (press-fit); ccd_grad: {"standard": 132, "high_offset": 127}; indikation_eu: nur Hüft-TEP – in EU/EMEA (CE) und Australien NICHT für Hemiarthroplastik (q1 S. 3); probe_hals: [{"groessen": "0–1", "laenge_mm": 27, "farbe": "gelb"}, {"groessen": "2–3", "laenge_mm": 30, "farbe": "blau"}, {"groessen": "4–6", "laenge_mm": 35, "farbe": "grün"}, {"groessen": "7–9", "laenge_mm": 37, "farbe": "schwarz"}, {"groessen": "10–11", "laenge_mm": 40, "farbe": "rot"}]; raspel_ref: 1020-5200 bis 1020-5211 (Raspeln Gr. 0–11, q1 S. 22/24) – keine Implantat-REF; implantat_ref: offen (nicht in ACCII-SP-1) | q1 | belegt |
| `stryker.v40.biolox_delta` | kopf | V40 BIOLOX delta Keramikkopf | konus: V40; material: BIOLOX delta; katalog: 6570-0-XXX (keine Einzel-REF aus XXX bilden); durchmesser_offset_mm: {"28": [-4, -2.7, 0, 4], "32": [-4, 0, 4], "36": [-5, -2.5, 0, 2.5, 5, 7.5]} | q1 | belegt |
| `stryker.v40.lfit_cocr` | kopf | V40 CoCr (LFIT) | konus: V40; material: CoCr (LFIT); katalog: 6260-9-XXX (keine Einzel-REF aus XXX bilden); durchmesser_offset_mm: {"22": [0, 3, 8], "26": [-3, 0, 4, 8, 12], "28": [-4, 0, 4, 6, 8, 12], "32": [-4, 0, 4, 8, 12], "36": [-5, 0, 5, 10], "40": [-4, 0, 4, 8, 12], "44": [-4, 0, 4, 8, 12]} | q1 | belegt |
| `stryker.v40.probekopf` | probekopf | V40 Probeköpfe | konus: V40; durchmesser_mm: [28, 32, 36]; hinweis: Probekopfwerte nicht auf Implantatköpfe übertragen | q2 | belegt |
| `stryker.trident2.schale` | pfanne | Trident II Tritanium | fixation: zementfrei; markt: EU/Canada (q5 S. 2); varianten: {"Solidback/Clusterhole": "42–66 mm, 2-mm-Schritte", "Multihole": "42–72 mm, 2-mm-Schritte (I/J nur Multihole)"} | q5 | belegt |
| `stryker.x3.inlay` | inlay | X3 Polyethylen | material: hochvernetztes PE (X3); varianten: {"X3 0°/10°": "Kopf-Ø je Alpha laut Tabelle T3 († = nur 0°)", "X3 Eccentric 10°": "C/D: Ø28; E–J: Ø28/32/36", "X3 Elevated Rim": "C/D: Ø28; E–J: Ø28/32/36", "X3 Eccentric 0°": "nicht CE-gekennzeichnet / nicht EU-vermarktet (q5 S. 4/21)"}; konflikt_26mm: Tabelle 1 ohne 26 mm, Katalog S. 21 listet X3 10° 26C–26J (REF 623-10-26C bzw. 723-10-26C) – offen, Hersteller klären | q5 | belegt |

### Größen – Accolade II (Quelle q1)
| groesse | varianten | ref |
|---|---|---|
| 0 | ['132° Standard', '127° High Offset'] | – |
| 1 | ['132° Standard', '127° High Offset'] | – |
| 2 | ['132° Standard', '127° High Offset'] | – |
| 3 | ['132° Standard', '127° High Offset'] | – |
| 4 | ['132° Standard', '127° High Offset'] | – |
| 5 | ['132° Standard', '127° High Offset'] | – |
| 6 | ['132° Standard', '127° High Offset'] | – |
| 7 | ['132° Standard', '127° High Offset'] | – |
| 8 | ['132° Standard', '127° High Offset'] | – |
| 9 | ['132° Standard', '127° High Offset'] | – |
| 10 | ['132° Standard', '127° High Offset'] | – |
| 11 | ['132° Standard', '127° High Offset'] | – |

### Größen – Trident II Tritanium (Quelle q5)
| groesse | alpha | max_kopf_mm_x3_0_10 |
|---|---|---|
| 42 | A | 28 |
| 44 | B | 32 |
| 46 | C | 32 |
| 48 | D | 36 |
| 50 | D | 36 |
| 52 | E | 40 |
| 54 | E | 40 |
| 56 | F | 44 |
| 58 | F | 44 |
| 60 | G | 44 |
| 62 | G | 44 |
| 64 | H | 44 |
| 66 | H | 44 |
| 68 | I | 44 |
| 70 | I | 44 |
| 72 | J | 44 |

### T3_trident_x3 – Trident II Schale ↔ X3 0°/10° Kopf-Ø (Quelle q5, S. gedr.=PDF 4, Abgleich 20–21)
| alpha | schalen_mm | kopf_mm | max_kopf_mm |
|---|---|---|---|
| A | 42 | 22, 28† | 28 |
| B | 44 | 22, 28†, 32† | 32 |
| C | 46 | 22, 28, 32† | 32 |
| D | 48, 50 | 22, 28, 32, 36† | 36 |
| E | 52, 54 | 22, 28, 32, 36, 40† | 40 |
| F | 56, 58 | 22, 28, 32, 36, 40†, 44† | 44 |
| G | 60, 62 | 22, 28, 32, 36, 40†, 44† | 44 |
| H | 64, 66 | 22, 28, 32, 36, 40†, 44† | 44 |
| I | 68, 70 | 22, 28, 32, 36, 40†, 44† | 44 |
| J | 72 | 22, 28, 32, 36, 40†, 44† | 44 |
_† = nur 0°; nur für X3 0°/10°_

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `stryker.accolade2.schaft` | `stryker.v40.biolox_delta` | **ja** | Konus V40; Ø/Offset laut Tabelle | q1 | 12 |
| `stryker.accolade2.schaft` | `stryker.v40.lfit_cocr` | **ja** | Konus V40; Ø/Offset laut Tabelle | q1 | 12 |
| `stryker.trident2.schale` | `stryker.x3.inlay` | **ja** | Variante und Kopf-Ø je Alpha laut T3; Eccentric 0° nicht EU; 26 mm offen | q5 | 4, 20–21 |
| `stryker.x3.inlay` | `stryker.v40.biolox_delta` | **bedingt** | Kopf-Ø ≤ max. Ø der Schale (T3); Kopf-Ø-Freigabe ist keine Freigabe jeder Kopffamilie – Familie am Etikett/IFU prüfen | q5 | 4 |
| `stryker.x3.inlay` | `stryker.v40.lfit_cocr` | **bedingt** | Kopf-Ø ≤ max. Ø der Schale (T3); 26 mm offen; Familie am Etikett/IFU prüfen | q5 | 4 |

## Regeln
- Accolade II: nur V40-Köpfe (BIOLOX delta, LFIT CoCr). (q1 S. 12)
- Offsets je Kopf-Ø unterschiedlich (z. B. +7,5 nur BIOLOX delta 36 mm; +10 nur LFIT 36 mm). (q1 S. 12)
- Kein Duokopf/Hemi auf Accolade II in der EU. (q1 S. 3)
- X3 Eccentric 0° ist laut TRITRI-SP-3 nicht CE-gekennzeichnet/nicht im EU-Markt. (q5 S. 4/21)
- Kopf-Ø nie größer als das Maximum der Schale laut Tabelle 1 (z. B. Schale 52 → max. 40, und 40 nur mit 0°-Inlay). (q5 S. 4)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| LFIT V40 / V40 / PCA Vitallium Femurköpfe | BfArM | RA2014-170 (06414/15), 02.10.2015 | EU/DE | – | bestimmte Chargen; Kopf–Konus-Montage | `stryker.v40.lfit_cocr` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2015/06414-15_kundeninfo_de.pdf?__blob=publicationFile |
| LFIT Anatomic CoCr V40 | BfArM | RA2016-028 (08312/16), 26.09.2016 | EU/DE | – | bestimmte ältere Größen/Chargen | `stryker.v40.lfit_cocr` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2016/08312-16_kundeninfo_de.pdf?__blob=publicationFile |
| LFIT Anatomic CoCr V40 | BfArM | RA2018-1757583 (06604/18), 12.06.2018 | EU/DE | EU-Abschluss nicht gefunden | Köpfe vor 04.03.2011; REF-Widerspruch im Brief (S. 1 6260-9-126, Tabelle S. 2 6260-9-136) – bei Stryker klären | `stryker.v40.lfit_cocr` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/06604-18_kundeninfo_de.pdf?__blob=publicationFile |
| LFIT Anatomic V40 Femoral Head (REF 6260-9-236) | FDA | Z-2299-2018, Event 80059 | US | beendet 08.05.2020 (US) | nur US-Datensatz; kein EU-Abschluss | `stryker.v40.lfit_cocr` | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm?ID=164630 |
| BIOLOX delta Ceramic V40 Femurkopf | BfArM | RA2022-2911584 (01953/22), 18.01.2022 | EU/DE | Abschluss/Folgemeldung nicht gefunden; Verbindung zu FDA Z-0842-2022 nicht belegt | ursprünglich REF 6570-0-032 Chargen 89648801–89648805; REF 6570-0-136 Charge 89549404; REF 6570-0-232 Charge 89546202 | `stryker.v40.biolox_delta` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2022/01953-22_kundeninfo_de.pdf?__blob=publicationFile |
| BIOLOX delta Ceramic V40 Femoral Head (REF 6570-0-032, Ø32/−4) | FDA | Z-0842-2022, Event 89592, PFA 2902313 | US | Open, Classified (US) | Update 17.03.2022: nur Charge 89648802 verbleibt; laut FDA-Text keine nichtkonformen Produkte nach Deutschland gelangt | `stryker.v40.biolox_delta` | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id=191999 |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] EU-IFU Accolade II, V40-Köpfe, Trident II, X3 – Suchschlüssel Stryker-eIFU: QIN 4351 (X3), QIN 0095-3-200 (V40 CoCr), QIN 4350 (BIOLOX delta V40) (Fundstelle Perplexity, Trident-Tritanium-Protokoll S. 3)
- [ ] Implantat-REF Accolade II (nicht in ACCII-SP-1)
- [ ] X3 26 mm: Tabelle 1 vs. Katalog S. 21
- [ ] EU-Abschluss RA2018-1757583 und RA2022-2911584
- [ ] REF/GTIN der Köpfe (nur Katalogmuster XXX)

## Quellen
- **q1** Accolade II Femoral Hip System – Surgical protocol · ACCII-SP-1_Rev-4_34423, ©2022 · S. gedr.=PDF 3 EU/EMEA-Indikation; 4–5 Größen/CCD; 11 Halsproben; 12 Köpfe; 22/24 Raspeln; Kennung 25 · Markt: global, EU/EMEA- und Australien-Abschnitte (S. 3) · gelesen: Grok/Astra 07.10.2026 · https://cdn.stryker.com/SYKGCSDOC-2-45343
- **q2** Accolade II – Tray Layout · ACCII-TL-1_25643, ©2020 · S. PDF 1 Basic tray, 2 Broach tray, 3 CE-Hinweis · Markt: CE-Hinweis PDF 3 · gelesen: Grok/Astra 07.10.2026 · https://www.stryker.com/content/dam/stryker/joint-replacement/products/accoladeii/resources/Accolade%20II%20Tray%20Layout_ACCII-TL-1_25643.pdf
- **q5** Trident II Tritanium Acetabular System – Surgical protocol · TRITRI-SP-3_Rev-6_29553, ©2022 · S. gedr.=PDF 2 EU/Canada; 4 Tabelle 1; 20–21 Katalog; Kennung 31 · Markt: EU und Canada; X3 Eccentric 0° ausgenommen · gelesen: Grok/Astra 07.10.2026 · https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf
- **fda-lfit** FDA Class 2 Device Recall LFIT Anatomic V40 Femoral Head (Z-2299-2018, Event 80059) · beendet 08.05.2020 · S. HTML Recall Status · Markt: US · gelesen: Grok/Astra 07.10.2026 · https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm?ID=164630
- **fda-delta** FDA Class 2 Device Recall BIOLOX delta Ceramic V40 Femoral Head (Z-0842-2022, Event 89592, PFA 2902313) · Update 17.03.2022, Open, Classified · S. HTML Recall Status/Product/Action · Markt: US mit Länderhinweisen · gelesen: Grok/Astra 07.10.2026 · https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id=191999

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.

Bilder: keine übernommen – Rechte beim Hersteller.
