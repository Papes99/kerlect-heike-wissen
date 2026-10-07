# Aesculap (B. Braun) – CoreHip Primary (zf/zem/AS) + Extended zementfrei

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Neuanlage P1 07.10.2026 aus CoreHip-Broschüre DE 02/2024 und O61502. verified: false. Plasmafit/All POLY nur Kontext. Lauf 001-implantate-luecken (07.10.2026): Korrekturen nach OpenAI-Gegenprüfung (CoreHip-Broschüre Nr. 4008487, gedr. 32–35/PDF 17–18), von Julian freigegeben._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.corehip.primary.zementfrei` | schaft | CoreHip Primary zementfrei | fixation: zementfrei; material: ISOTAN F Ti6Al4V + proximales PLASMAPORE; konus: 12/14; linien: {"valgus_VLG": {"ccd_grad": 142, "offset_mm": "30,5–38,0"}, "standard_STD": {"ccd_grad": 132, "offset_mm": "38,0–45,5"}, "varus_VAR": {"ccd_grad": 122, "offset_mm": "45,5–53,0"}, "dysplasie_DYS": {"ccd_grad": 142, "offset_mm": "30,5–38,0", "hinweis": "10 mm kürzer (Maß Kopfmittelpunkt bis Schaftspitze; ch-de gedr. 32–35/PDF 17–18); ASIA-Raspel NT1154"}}; ccd_seite: VLG/DYS 142°, STD 132°, VAR 122°: gedr. 16–17/PDF 9; Offsetgruppen gedr. 24–25/PDF 13; schaftlaenge_hinweis: schaftlaenge_mm = gedruckter Tabellenwert, gilt für VLG/STD/VAR (Kopfmittelpunkt bis Schaftspitze). DYS laut Fußnote 10 mm kürzer: schaftlaenge_dys_mm_berechnet ist berechnet aus Tabellenwert und Fußnote – keine gedruckte Tabellenzelle.; gewicht: max. 60 kg nur für Primary Größe 0 aller vier Linien (VLG/STD/VAR/DYS) und ausschließlich DYS Größe 1 (ch-de) | ch-de | belegt |
| `aesculap.corehip.primary.zementiert` | schaft | CoreHip Primary zementiert / AS | fixation: zementiert; material: ISODUR F CoCrMo; AS = mehrlagiges CrN/CrCN/ZrN-Beschichtungssystem (nicht als bloßes ZrN vereinfachen); konus: 12/14; linien: Valgus / Standard / Varus (keine Dysplasie in zementierter Übersicht); zementmantel_mm: 1.0; centralizer: NK1281/83/85/87/89 zu Größen 1/3/5/7/9; pruefung: Größen 1/3/5/7/9 samt K/Z-REF und Centralizer von OpenAI gegen die Übersicht bestätigt | ch-de | belegt (Original, 2 Prüfer) |
| `aesculap.corehip.extended.zementfrei` | schaft | CoreHip Extended zementfrei | fixation: zementfrei; material: ISOTAN F + PLASMAPORE; konus: 12/14; linien: Valgus / Standard / Varus; pruefung: Extended 0–11 mit REF-/Längenreihen von OpenAI gegen die Übersicht bestätigt – Tabelle vollständig | ch-de | belegt (Original, 2 Prüfer) |
| `aesculap.plasmafit.plus.corehip_kontext` | pfanne | Plasmafit Plus (Kontext CoreHip – Freigabe offen) | fixation: zementfrei; registerbeleg: EPRD COREHIP + PLASMAFIT; detail_datei: implantate/aesculap-excia.json; freigabe: offen | es | offen |
| `aesculap.all_poly.corehip_kontext` | pfanne | Aesculap All POLY zementiert (Kontext CoreHip – Freigabe offen) | fixation: zementiert; registerbeleg: EPRD COREHIP + All POLY; freigabe: offen | es | offen |
| `aesculap.kopf.biolox_delta.corehip` | kopf | BIOLOX delta 12/14 | material: Keramik; konus: 12/14 | ch-de | belegt |
| `aesculap.kopf.isodur.corehip` | kopf | Isodur F CoCr 12/14 | material: CoCrMo; konus: 12/14 | ch-de | belegt |

### Größen – CoreHip Primary zementfrei (Quelle ch-de)
| groesse | ref_dysplasie | ref_valgus | ref_standard | ref_varus | schaftlaenge_mm | gewicht_max_kg | schaftlaenge_dys_mm_berechnet | gewicht_gilt_fuer | gewicht_max_kg_nur_dys |
|---|---|---|---|---|---|---|---|---|---|
| 0 | NK1060T | NK1020T | NK1000T | NK1040T | 119.5 | 60 | 109.5 | VLG, STD, VAR, DYS | – |
| 1 | NK1061T | NK1021T | NK1001T | NK1041T | 121.5 | – | 111.5 | nur DYS (VLG/STD/VAR Größe 1 ohne diese Grenze) | 60 |
| 2 | NK1062T | NK1022T | NK1002T | NK1042T | 123.5 | – | 113.5 | – | – |
| 3 | NK1063T | NK1023T | NK1003T | NK1043T | 125.5 | – | 115.5 | – | – |
| 4 | NK1064T | NK1024T | NK1004T | NK1044T | 127.5 | – | 117.5 | – | – |
| 5 | NK1065T | NK1025T | NK1005T | NK1045T | 129.5 | – | 119.5 | – | – |
| 6 | NK1066T | NK1026T | NK1006T | NK1046T | 131.5 | – | 121.5 | – | – |
| 7 | NK1067T | NK1027T | NK1007T | NK1047T | 133.5 | – | 123.5 | – | – |
| 8 | NK1068T | NK1028T | NK1008T | NK1048T | 135.5 | – | 125.5 | – | – |
| 9 | NK1069T | NK1029T | NK1009T | NK1049T | 137.5 | – | 127.5 | – | – |
| 10 | NK1070T | NK1030T | NK1010T | NK1050T | 139.5 | – | 129.5 | – | – |
| 11 | NK1071T | NK1031T | NK1011T | NK1051T | 141.5 | – | 131.5 | – | – |

### Größen – CoreHip Primary zementiert / AS (Quelle ch-de)
| groesse | ref_valgus | ref_valgus_as | ref_standard | ref_standard_as | ref_varus | ref_varus_as | centralizer | schaftlaenge_mm |
|---|---|---|---|---|---|---|---|---|
| 1 | NK1221K | NK1221Z | NK1201K | NK1201Z | NK1241K | NK1241Z | NK1281 | 121.5 |
| 3 | NK1223K | NK1223Z | NK1203K | NK1203Z | NK1243K | NK1243Z | NK1283 | 125.5 |
| 5 | NK1225K | NK1225Z | NK1205K | NK1205Z | NK1245K | NK1245Z | NK1285 | 129.5 |
| 7 | NK1227K | NK1227Z | NK1207K | NK1207Z | NK1247K | NK1247Z | NK1287 | 133.5 |
| 9 | NK1229K | NK1229Z | NK1209K | NK1209Z | NK1249K | NK1249Z | NK1289 | 137.5 |

### Größen – CoreHip Extended zementfrei (Quelle ch-de)
| groesse | ref_valgus | ref_standard | ref_varus | schaftlaenge_mm |
|---|---|---|---|---|
| 0 | NK1120T | NK1100T | NK1140T | 150.5 |
| 1 | NK1121T | NK1101T | NK1141T | 154.5 |
| 2 | NK1122T | NK1102T | NK1142T | 158.5 |
| 3 | NK1123T | NK1103T | NK1143T | 162.5 |
| 4 | NK1124T | NK1104T | NK1144T | 166.5 |
| 5 | NK1125T | NK1105T | NK1145T | 170.5 |
| 6 | NK1126T | NK1106T | NK1146T | 174.5 |
| 7 | NK1127T | NK1107T | NK1147T | 178.5 |
| 8 | NK1128T | NK1108T | NK1148T | 182.5 |
| 9 | NK1129T | NK1109T | NK1149T | 186.5 |
| 10 | NK1130T | NK1110T | NK1150T | 190.5 |
| 11 | NK1131T | NK1111T | NK1151T | 194.5 |

### Größen – BIOLOX delta 12/14 (Quelle ch-de)
| durchmesser_mm | hals | ref |
|---|---|---|
| 28 | S/M/L | NK460D/NK461D/NK462D |
| 32 | S/M/L/XL | NK560D/NK561D/NK562D/NK563D |
| 36 | S/M/L/XL | NK650D/NK651D/NK652D/NK653D |

### Größen – Isodur F CoCr 12/14 (Quelle ch-de)
| durchmesser_mm | hals | ref |
|---|---|---|
| 28 | S/M/L/XL/XXL | NK429K/NK430K/NK431K/NK432K/NK433K |
| 32 | S/M/L/XL/XXL | NK529K/NK530K/NK531K/NK532K/NK533K |
| 36 | S/M/L/XL/XXL | NK669K/NK670K/NK671K/NK672K/NK673K |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `aesculap.corehip.primary.zementfrei` | `aesculap.kopf.biolox_delta.corehip` | **ja** | Konus 12/14; REF laut Kopfübersicht | ch-de | Implantatübersicht Köpfe |
| `aesculap.corehip.primary.zementfrei` | `aesculap.kopf.isodur.corehip` | **ja** | Konus 12/14 | ch-de | Implantatübersicht Köpfe |
| `aesculap.corehip.primary.zementiert` | `aesculap.kopf.biolox_delta.corehip` | **ja** | Konus 12/14 | ch-de | Implantatübersicht Köpfe |
| `aesculap.corehip.primary.zementfrei` | `aesculap.plasmafit.plus.corehip_kontext` | **offen** | EPRD beobachtet; keine Freigabetabelle in CoreHip-Broschüre | es | Kombi |
| `aesculap.corehip.primary.zementiert` | `aesculap.all_poly.corehip_kontext` | **offen** | EPRD beobachtet; All-POLY-IFU nicht gelesen | es | Kombi |

## Regeln
- Schaftlinie (Valgus/Standard/Varus/Dysplasie) folgt dem Probehalsadapter und der Raspelposition – nicht nur der Größe. (ch-de)
- Dysplasie-Schaft nur mit ASIA-Raspelset NT1154 vorbereiten. (ch-de)
- Plasmafit/All POLY mit CoreHip in EPRD ≠ Herstellerfreigabe. (es)
- Isocer-Köpfe dürfen nur gegen PE/XLPE artikulieren; Keramik/Keramik ausdrücklich ausgeschlossen (Isocer-Familie hier ohne REF). (ch-de gedr. 35/PDF 18)
- Dysplasie-Schaft ist 10 mm kürzer als die gedruckte Primary-Länge (VLG/STD/VAR); DYS-Längen sind berechnet, nicht gedruckt. (ch-de gedr. 32–35/PDF 17–18)
- Max. 60 kg: Primary Größe 0 (alle vier Linien) und nur DYS Größe 1. (ch-de gedr. 32–35/PDF 17–18)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen.
- Nicht dokumentierte Kombinationen: offen – Operateur fragen.

## Offen
- [ ] Isocer-Köpfe: vollständige REF (Regel nur PE/XLPE, Keramik/Keramik nein ist eingetragen)
- [ ] Explizite Freigabe CoreHip ↔ Plasmafit / All POLY
- [ ] BfArM CoreHip
- [ ] DYS-Längen: nur berechnet (Tabellenwert − 10 mm laut Fußnote) – bei Bedarf gedruckte DYS-Längen beim Hersteller erfragen

## Quellen
- **ch-de** AESCULAP CoreHip System (deutsche Broschüre) · Nr. 4008487, 02/2024 · S. gedr. 16–17/PDF 9 (CCD); gedr. 24–25/PDF 13 (Offsetgruppen); gedr. 32–35/PDF 17–18 (Implantatübersicht REF, Fußnoten visuell geprüft, Isocer); Extraktionsadapter 12/14; Köpfe · Markt: DE · gelesen: Grok 07.10.2026; OpenAI 07.10.2026 (Fußnoten visuell geprüft) · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/corehip-broschuere.pdf
- **ch-en** AESCULAP CoreHip SYSTEM (EN Brochure / OP) · O61502 0321/PDF/1 · S. Design; Primary/Extended; REF-Tabellen; BIOLOX/Isodur-Köpfe · Markt: EN (Aesculap AG) · gelesen: Grok 07.10.2026 · https://www.stvincentsboneandjoint.com.au/pdf/aesculap-core-hip.pdf
- **pf** AESCULAP Plasmafit – Acetabular Cup System · O45502 0718/1/4, 07/2018 · S. Poly/Plus · Markt: EN auf DE-Seite · gelesen: Grok 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf
- **es** EPRD / auswahl-dach · Jahresbericht 2025 · S. COREHIP zf #10 / zem #10; Kombi COREHIP+PLASMAFIT; COREHIP+All POLY · Markt: DE (Ranking) · gelesen: Grok 07.10.2026 · https://www.eprd.de/de/downloads/tabellen/jahresbericht2025

## Änderungen
- **v1.0** (2026-10-07, p1-fehlende-systeme): Neuanlage CoreHip Primary zf/zem + Köpfe; Extended und Plasmafit/All POLY als Kontext/offen.
- **v1.1** (2026-10-07, 001-implantate-luecken): OpenAI-Korrektur 8.2: Dysplasie-Schaft 10 mm kürzer (schaftlaenge_dys_mm_berechnet, als berechnet aus Tabelle + Fußnote gekennzeichnet); 60-kg-Grenze maschinenlesbar nur Primary Größe 0 (alle vier Linien) und DYS Größe 1; CCD-/Offset-Fundstellen; AS-Beschichtung mehrlagig CrN/CrCN/ZrN; Regel Isocer nur gegen PE/XLPE; Extended-Tabelle als vollständig bestätigt.

Bilder: keine übernommen – Rechte beim Hersteller.
