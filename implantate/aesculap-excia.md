# Aesculap (B. Braun) – Excia T – zementfrei, zementiert, Duokopf; Plasmafit

_Version 1.2 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen. Lauf 001-implantate-luecken (07.10.2026): Plasmafit-Poly-Tabelle von Claude-Helfer und OpenAI am Original gelesen; Bipolar-Paarung weiter offen._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.excia_t.zementfrei` | schaft | Excia T zementfrei | fixation: zementfrei; material: Ti6Al4V / PLASMAPORE; konus: 12/14; ccd_grad: {"standard_T": 135, "lateral_TL": "128 (+6 mm Offset)"} | e1 | belegt |
| `aesculap.excia_t.zementiert` | schaft | Excia T zementiert | fixation: zementiert; material: CoCr; konus: 12/14; ccd_grad: {"standard_T": 135, "lateral_TL": "128 (+6 mm Offset)"} | e1 | belegt |
| `aesculap.plasmafit.plus` | pfanne | Plasmafit Plus | fixation: zementfrei; varianten: Plus / Plus 3 / Plus 7 (Plus 7 bei 40/42/44 nur fünf Schraubenlöcher, e2 S. 20); liner: Keramik oder PE (e2 S. 5) | e2 | belegt |
| `aesculap.plasmafit.poly` | pfanne | Plasmafit Poly | fixation: zementfrei; liner: nur PE (e2 S. 5: „Only for polyethylene liners“); material: ISOTAN F (Plasmafit Poly ISOTAN®F); seite: gedr./PDF 18–19 (Bild geprüft); systemtext: „Plasmafit® Poly is a dedicated cup implant line exclusively for the use with polyethylene liners.“ … 36-mm-Vitelene ab Schale 50, bis 40 mm Artikulation ab Schale 54 (gedr./PDF 6); verschlussstopfen: „Plasmafit® Poly no screw holes, with closing plug“ – zentraler Verschlussstopfen bei Schalen ohne Schraubenlöcher automatisch mitgeliefert; NV001T einzeln bestellbar (gedr./PDF 19) | e2 | belegt (Original, 2 Prüfer) |
| `aesculap.pe_pfanne.zementiert` | pfanne | Aesculap PE-Pfanne zementiert | fixation: zementiert; familie: Cemented Polyethylene Cups (Flat-/Full-profile) – Einzelprodukt/Profil/REF offen; hinweis: nicht als Müller-Pfanne umbenennen | e4 | offen |
| `aesculap.inlay.biolox_delta` | inlay | BIOLOX delta Inlay | material: Keramik; nur_fuer: Plasmafit Plus; nicht_fuer: Plasmafit Poly; beispiel_ref_36: Plus 52=NV113D, 54=NV114D, 56=NV115D, 58/60/62=NV116D, 64–70=NV117D (e2 S. 20–21) | e2 | belegt |
| `aesculap.inlay.pe_standard` | inlay | PE-Inlay Standard (UHMWPE) | material: UHMWPE (ISO 5834-2) – konventionelles PE, REF ohne „E“; fuer: Plasmafit Poly (Auswahl Julian 07.10.2026); Plasmafit Plus ebenfalls PE möglich (Plus-REF nicht in diesem Lauf); seite: gedr./PDF 18–19 (Bild geprüft); Materialliste gedr./PDF 24; bereich: symmetrisch 32 bei 46–62; mit Schulter 28 bei 42/44; mit Schulter 32 bei 46–62; Schale 40/B ohne UHMWPE-Liner; keine UHMWPE-Liner 22,2/36/40; hinweis: Standard-UHMWPE deutlich enger als Vitelene – keine 36-/40-mm-Zeilen aus Vitelene ableiten; NV201 ≠ NV201E. „with shoulder“ (UHMWPE) und „posterior wall“ (Vitelene) haben dieselben Ziffern – ob dasselbe Design, sagt das Dokument nicht. | e2 | belegt (Original, 2 Prüfer) |
| `aesculap.inlay.vitelene` | inlay | Vitelene-Liner (Plasmafit Poly) | material: Vitelene® – UHMWPE-XE vitamin E stabilized highly crosslinked polyethylene (REF mit Endung „E“); fuer: Plasmafit Poly (REF-Tabelle gedr./PDF 18–19); Plus-Zuordnung siehe T8 (REF für Plus nicht in diesem Lauf); seite: gedr./PDF 18–19 (Bild geprüft); Beschreibung gedr./PDF 12; Materialliste gedr./PDF 24; bereich: symmetrisch: 22,2 bei 40/42; 28 bei 42–54; 32 bei 46–62; 36 bei 50–62; 40 bei 54–62. posterior wall: wie symmetrisch, ohne 40 mm. asymmetrisch: 22,2 bei 40/42; 28 bei 42/44/46; 32 bei 46–62; pruefung: Schalenbereiche je Variante/Innen-Ø von OpenAI bestätigt (2 Prüfer); Einzel-REF nur vom Claude-Helfer gelesen; beschreibung: 80 kGy Elektronenstrahl, 0,1 % α-Tocopherol, EO-sterilisiert, keine thermische Nachbehandlung (gedr./PDF 12); hinweis: nicht die von Julian gewählte Standard-PE-Familie – nicht gegen UHMWPE austauschen; NV201E ≠ NV201 | e2 | belegt (Original, 1 Prüfer) |
| `aesculap.kopf.biolox_delta` | kopf | BIOLOX delta | material: Keramik; konus: 12/14; halslaenge_mm: {"28": "S/M/L = −3,5/0/+3,5", "32-40": "S/M/L/XL = −4/0/+4/+8"} | e1 | belegt |
| `aesculap.kopf.isodur_cocr` | kopf | Isodur CoCr (Metallkopf (e1), ISODUR F (e2)) | material: CoCrMo (ISO 5832-12); in e2 S. 24 als ISODUR F mit identischen REF; konus: 12/14; halslaenge_mm: {"28": "S/M/L/XL/XXL = −3,5/0/+3,5/+7/+10,5", "32-40": "S/M/L/XL/XXL = −4/0/+4/+8/+12"}; hinweis: Ø22,2 (nur M/L, NK330K/NK331K) steht nicht in der Excia-T-Kopfübersicht – nicht für Excia T anbieten | e1 | belegt |
| `aesculap.duokopf.bipolar_cup` | duokopf | Bipolar Cup | verwendung: mit Excia T zementiert; freigabe: offen – nur Anwendungsfall bb-web, keine Kopf-/Größen-Freigabetabelle | e3 | hausabhängig |

### Größen – Excia T zementfrei (Quelle e1)
| groesse | ref_standard_T | ref_lateral_TL |
|---|---|---|
| 8 | NU208T | NU228T |
| 9 | NU209T | NU229T |
| 10 | NU210T | NU230T |
| 11 | NU211T | NU231T |
| 12 | NU212T | NU232T |
| 13 | NU213T | NU233T |
| 14 | NU214T | NU234T |
| 15 | NU215T | NU235T |
| 16 | NU216T | NU236T |
| 17 | NU217T | NU237T |
| 18 | NU218T | NU238T |
| 19 | NU219T | NU239T |
| 20 | NU220T | NU240T |

### Größen – Excia T zementiert (Quelle e1)
| groesse | ref_standard_T | ref_lateral_TL |
|---|---|---|
| 10 | NU270K | NU290K |
| 12 | NU272K | NU292K |
| 14 | NU274K | NU294K |
| 16 | NU276K | NU296K |
| 18 | NU278K | NU298K |
| 20 | NU280K | NU300K |

### Größen – Plasmafit Plus (Quelle e2)
| groesse | liner_code |
|---|---|
| 40 | A |
| 42 | B |
| 44 | C |
| 46 | D |
| 48 | E |
| 50 | F |
| 52 | G |
| 54 | H |
| 56 | I |
| 58 | J |
| 60 | J |
| 62 | J |
| 64 | K |
| 66 | K |
| 68 | K |
| 70 | K |

### Größen – Plasmafit Poly (Quelle e2)
| groesse | liner_code | ref |
|---|---|---|
| 40 | B | NV040T |
| 42 | C | NV042T |
| 44 | D | NV044T |
| 46 | E | NV046T |
| 48 | F | NV048T |
| 50 | G | NV050T |
| 52 | H | NV052T |
| 54 | I | NV054T |
| 56 | J | NV056T |
| 58 | K | NV058T |
| 60 | L | NV060T |
| 62 | M | NV062T |

### Größen – BIOLOX delta Inlay (Quelle e2)
| innen_mm | plus_schalen |
|---|---|
| 28 | 44–54 |
| 32 | 48–70 |
| 36 | 52–70 |
| 40 | 56–70 |

### Größen – PE-Inlay Standard (UHMWPE) (Quelle e2)
| variante | innen_mm | schale_poly_mm | liner_code | ref |
|---|---|---|---|---|
| symmetrical UHMWPE | 32 | 46 | E | NV201 |
| symmetrical UHMWPE | 32 | 48 | F | NV202 |
| symmetrical UHMWPE | 32 | 50 | G | NV203 |
| symmetrical UHMWPE | 32 | 52 | H | NV204 |
| symmetrical UHMWPE | 32 | 54 | I | NV205 |
| symmetrical UHMWPE | 32 | 56 | J | NV206 |
| symmetrical UHMWPE | 32 | 58 | K | NV207 |
| symmetrical UHMWPE | 32 | 60 | L | NV208 |
| symmetrical UHMWPE | 32 | 62 | M | NV209 |
| with shoulder UHMWPE | 28 | 42 | C | NV289 |
| with shoulder UHMWPE | 28 | 44 | D | NV290 |
| with shoulder UHMWPE | 32 | 46 | E | NV301 |
| with shoulder UHMWPE | 32 | 48 | F | NV302 |
| with shoulder UHMWPE | 32 | 50 | G | NV303 |
| with shoulder UHMWPE | 32 | 52 | H | NV304 |
| with shoulder UHMWPE | 32 | 54 | I | NV305 |
| with shoulder UHMWPE | 32 | 56 | J | NV306 |
| with shoulder UHMWPE | 32 | 58 | K | NV307 |
| with shoulder UHMWPE | 32 | 60 | L | NV308 |
| with shoulder UHMWPE | 32 | 62 | M | NV309 |

### Größen – Vitelene-Liner (Plasmafit Poly) (Quelle e2)
| variante | innen_mm | schale_poly_mm | liner_code | ref |
|---|---|---|---|---|
| symmetrical Vitelene | 22,2 | 40 | B | NV183E |
| symmetrical Vitelene | 22,2 | 42 | C | NV184E |
| symmetrical Vitelene | 28 | 42 | C | NV189E |
| symmetrical Vitelene | 28 | 44 | D | NV190E |
| symmetrical Vitelene | 28 | 46 | E | NV191E |
| symmetrical Vitelene | 28 | 48 | F | NV192E |
| symmetrical Vitelene | 28 | 50 | G | NV193E |
| symmetrical Vitelene | 28 | 52 | H | NV194E |
| symmetrical Vitelene | 28 | 54 | I | NV195E |
| symmetrical Vitelene | 32 | 46 | E | NV201E |
| symmetrical Vitelene | 32 | 48 | F | NV202E |
| symmetrical Vitelene | 32 | 50 | G | NV203E |
| symmetrical Vitelene | 32 | 52 | H | NV204E |
| symmetrical Vitelene | 32 | 54 | I | NV205E |
| symmetrical Vitelene | 32 | 56 | J | NV206E |
| symmetrical Vitelene | 32 | 58 | K | NV207E |
| symmetrical Vitelene | 32 | 60 | L | NV208E |
| symmetrical Vitelene | 32 | 62 | M | NV209E |
| symmetrical Vitelene | 36 | 50 | G | NV213E |
| symmetrical Vitelene | 36 | 52 | H | NV214E |
| symmetrical Vitelene | 36 | 54 | I | NV215E |
| symmetrical Vitelene | 36 | 56 | J | NV216E |
| symmetrical Vitelene | 36 | 58 | K | NV217E |
| symmetrical Vitelene | 36 | 60 | L | NV218E |
| symmetrical Vitelene | 36 | 62 | M | NV219E |
| symmetrical Vitelene | 40 | 54 | I | NV225E |
| symmetrical Vitelene | 40 | 56 | J | NV226E |
| symmetrical Vitelene | 40 | 58 | K | NV227E |
| symmetrical Vitelene | 40 | 60 | L | NV228E |
| symmetrical Vitelene | 40 | 62 | M | NV229E |
| posterior wall Vitelene | 22,2 | 40 | B | NV283E |
| posterior wall Vitelene | 22,2 | 42 | C | NV284E |
| posterior wall Vitelene | 28 | 42 | C | NV289E |
| posterior wall Vitelene | 28 | 44 | D | NV290E |
| posterior wall Vitelene | 28 | 46 | E | NV291E |
| posterior wall Vitelene | 28 | 48 | F | NV292E |
| posterior wall Vitelene | 28 | 50 | G | NV293E |
| posterior wall Vitelene | 28 | 52 | H | NV294E |
| posterior wall Vitelene | 28 | 54 | I | NV295E |
| posterior wall Vitelene | 32 | 46 | E | NV301E |
| posterior wall Vitelene | 32 | 48 | F | NV302E |
| posterior wall Vitelene | 32 | 50 | G | NV303E |
| posterior wall Vitelene | 32 | 52 | H | NV304E |
| posterior wall Vitelene | 32 | 54 | I | NV305E |
| posterior wall Vitelene | 32 | 56 | J | NV306E |
| posterior wall Vitelene | 32 | 58 | K | NV307E |
| posterior wall Vitelene | 32 | 60 | L | NV308E |
| posterior wall Vitelene | 32 | 62 | M | NV309E |
| posterior wall Vitelene | 36 | 50 | G | NV313E |
| posterior wall Vitelene | 36 | 52 | H | NV314E |
| posterior wall Vitelene | 36 | 54 | I | NV315E |
| posterior wall Vitelene | 36 | 56 | J | NV316E |
| posterior wall Vitelene | 36 | 58 | K | NV317E |
| posterior wall Vitelene | 36 | 60 | L | NV318E |
| posterior wall Vitelene | 36 | 62 | M | NV319E |
| asymmetrical Vitelene | 22,2 | 40 | B | NV383E |
| asymmetrical Vitelene | 22,2 | 42 | C | NV384E |
| asymmetrical Vitelene | 28 | 42 | C | NV389E |
| asymmetrical Vitelene | 28 | 44 | D | NV390E |
| asymmetrical Vitelene | 28 | 46 | E | NV391E |
| asymmetrical Vitelene | 32 | 46 | E | NV401E |
| asymmetrical Vitelene | 32 | 48 | F | NV402E |
| asymmetrical Vitelene | 32 | 50 | G | NV403E |
| asymmetrical Vitelene | 32 | 52 | H | NV404E |
| asymmetrical Vitelene | 32 | 54 | I | NV405E |
| asymmetrical Vitelene | 32 | 56 | J | NV406E |
| asymmetrical Vitelene | 32 | 58 | K | NV407E |
| asymmetrical Vitelene | 32 | 60 | L | NV408E |
| asymmetrical Vitelene | 32 | 62 | M | NV409E |

### Größen – BIOLOX delta (Quelle e1)
| durchmesser_mm | hals | ref |
|---|---|---|
| 28 | S/M/L | NK460D/NK461D/NK462D |
| 32 | S/M/L/XL | NK560D/NK561D/NK562D/NK563D |
| 36 | S/M/L/XL | NK650D/NK651D/NK652D/NK653D |
| 40 | S/M/L/XL | NK750D/NK751D/NK752D/NK753D |

### Größen – Isodur CoCr (Quelle e1)
| durchmesser_mm | hals | ref |
|---|---|---|
| 28 | S/M/L/XL/XXL | NK429K/NK430K/NK431K/NK432K/NK433K |
| 32 | S/M/L/XL/XXL | NK529K/NK530K/NK531K/NK532K/NK533K |
| 36 | S/M/L/XL/XXL | NK669K/NK670K/NK671K/NK672K/NK673K |
| 40 | S/M/L/XL/XXL | NK769K/NK770K/NK771K/NK772K/NK773K |

### T8_plasmafit_liner – Plasmafit Liner (symmetrisch) ↔ Schalen (Quelle e2, S. 18–21)
| liner | innen_mm | poly | plus |
|---|---|---|---|
| Vitelene | 22,2 | 40/42 | 40/42/44 |
| Vitelene | 28 | 42–54 | 44–56 |
| Vitelene | 32 | 46–62 | 48–70 |
| Vitelene | 36 | 50–62 | 52–70 |
| Vitelene | 40 | 54–62 | 56–70 |
| BIOLOX delta | 28 | nicht vorgesehen | 44–54 |
| BIOLOX delta | 32 | nicht vorgesehen | 48–70 |
| BIOLOX delta | 36 | nicht vorgesehen | 52–70 |
| BIOLOX delta | 40 | nicht vorgesehen | 56–70 |
_jeweils 2-mm-Schritte; gilt nur für symmetrische Liner; gleicher Liner-Buchstabe allein genügt nicht (Poly und Plus ordnen gleiche Schalen-Ø verschiedenen Codes zu)_

### T18_poly_uhmwpe – Plasmafit Poly Schale ↔ Liner-Code ↔ Schalen-REF ↔ Standard-UHMWPE-Liner (Quelle e2, S. 18–19 (Bild geprüft))
| schale | code | ref_schale | uhmwpe_symmetrisch_32 | uhmwpe_schulter_28 | uhmwpe_schulter_32 |
|---|---|---|---|---|---|
| 40 | B | NV040T | — | — | — |
| 42 | C | NV042T | — | NV289 | — |
| 44 | D | NV044T | — | NV290 | — |
| 46 | E | NV046T | NV201 | — | NV301 |
| 48 | F | NV048T | NV202 | — | NV302 |
| 50 | G | NV050T | NV203 | — | NV303 |
| 52 | H | NV052T | NV204 | — | NV304 |
| 54 | I | NV054T | NV205 | — | NV305 |
| 56 | J | NV056T | NV206 | — | NV306 |
| 58 | K | NV058T | NV207 | — | NV307 |
| 60 | L | NV060T | NV208 | — | NV308 |
| 62 | M | NV062T | NV209 | — | NV309 |
_„—“ = im Original Strich, keine REF. Standard-UHMWPE (REF ohne E) nicht durch Vitelene (REF mit E) ersetzen; keine 22,2-/36-/40-mm-UHMWPE-Zeilen._

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `aesculap.plasmafit.plus` | `aesculap.inlay.biolox_delta` | **bedingt** | Innen-Ø nur in den Schalen laut T8 | e2 | 18–21 |
| `aesculap.plasmafit.poly` | `aesculap.inlay.biolox_delta` | **nein** | Poly nur PE-Liner | e2 | 5 |
| `aesculap.plasmafit.poly` | `aesculap.inlay.pe_standard` | **bedingt** | nur Schale/Innen-Ø laut T18: symmetrisch 32 bei 46–62; mit Schulter 28 bei 42/44; mit Schulter 32 bei 46–62; 40/B ohne UHMWPE-Liner | e2 | 18–19 |
| `aesculap.excia_t.zementfrei` | `aesculap.kopf.biolox_delta` | **ja** | Ø/Hals laut Excia-T-Kopfübersicht | e1 | 19 |
| `aesculap.excia_t.zementfrei` | `aesculap.kopf.isodur_cocr` | **ja** | Ø 28–40 laut Excia-T-Kopfübersicht; nicht Ø22,2 | e1 | 19 |
| `aesculap.excia_t.zementiert` | `aesculap.kopf.biolox_delta` | **ja** | Ø/Hals laut Excia-T-Kopfübersicht | e1 | 19 |
| `aesculap.excia_t.zementiert` | `aesculap.kopf.isodur_cocr` | **ja** | Ø 28–40 laut Excia-T-Kopfübersicht; nicht Ø22,2 | e1 | 19 |
| `aesculap.inlay.biolox_delta` | `aesculap.kopf.isodur_cocr` | **nein** | keinen Metallkopf mit Keramikinlay freigeben | e2 | 24 |
| `aesculap.excia_t.zementiert` | `aesculap.duokopf.bipolar_cup` | **offen** | nur Anwendungsfall (bb-web); weder Excia-T-DE-Broschüre Nr. 4008516 (01/2026) noch EN O56002 (09/2020) noch Bipolar-Cup-Katalog belegen die Paarung ausdrücklich; gemeinsamer Hersteller/12/14 ist kein Nachweis | bb-web; e1; e5; e3 | Operationstechniken |
| `aesculap.plasmafit.poly` | `aesculap.inlay.vitelene` | **bedingt** | nur Variante/Innen-Ø in den Schalen laut REF-Tabelle (Komponente aesculap.inlay.vitelene); Code-Buchstabe laut Poly-Tabelle | e2 | 18–19 |
| `aesculap.plasmafit.plus` | `aesculap.inlay.vitelene` | **bedingt** | Schalenbereiche Plus laut T8 (Lauf 001-implantate); Plus-REF in diesem Lauf nicht gelesen – Poly-REF nicht auf Plus übertragen | e2 | 18–21 |

## Regeln
- Plasmafit Poly nur mit PE-Liner; Keramikinlay nur bei Plasmafit Plus und nur in den Schalengrößen laut Tabelle. (e2 S. 5, 18–21)
- Keinen Metallkopf (Isodur/ISODUR F) mit Keramikinlay kombinieren. (e2 S. 24)
- Excia 12/14 (O90301) ist eine andere Schaftlinie – Größen/REF nicht auf Excia T übertragen. (excia-old, e1)
- Bipolar Cup nur mit freigegebenem zementiertem Schaft; Freigabetabelle mit Excia T zementiert fehlt. (bb-web, e3)
- Standard-UHMWPE (REF ohne E) und Vitelene (REF mit E) strikt trennen: gleiche Ziffern, anderes Material und anderer Größenbereich (UHMWPE nur 28/32). (e2 S. 18–19)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| VITELENE-Einsätze (nicht BIOLOX delta) | BfArM | FSCA 279 (12190/24), 17.04.2024 | EU/DE | – | nur relevant, falls Vitelene-Liner verwendet werden | `aesculap.inlay.vitelene` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/12190-24_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] EU-IFU Excia T zementiert / Bipolar Cup (Freigabetabelle) – auch in Nr. 4008516 01/2026 und O56002 09/2020 nicht belegt
- [ ] Einzelprodukt/Profil/REF der zementierten PE-Pfanne
- [ ] GTIN
- [ ] UHMWPE „with shoulder“ vs. Vitelene „posterior wall“: gleiche Ziffern, Design-Identität im Dokument nicht angegeben
- [ ] Plasmafit Plus: PE-/Vitelene-REF (gedr./PDF 20–23) nicht in diesem Lauf
- [ ] Plasmafit-Dokument O45502 0718 (EN): Aktualität unbekannt

## Quellen
- **e1** AESCULAP Excia T – Hüftendoprothesensystem · Nr. 4008516, 01/2026 · S. CCD gedr. 11/PDF 6; Schäfte gedr. 18/PDF 10; Köpfe gedr. 19/PDF 10; Kennung PDF 13 · Markt: DE-Fassung · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf
- **e2** AESCULAP Plasmafit – Acetabular Cup System · O45502 0718/1/4, 07/2018 · S. gedr.=PDF 5–7 Konzept; 12 Vitelene; 18–19 Plasmafit Poly Implantate (Bild geprüft); 20–21 Plus; 24 Köpfe/Materialien; Kennung 34 · Markt: EN auf DE-Herstellerseite · gelesen: Grok/Astra 07.10.2026; Claude-Helfer 07.10.2026 (Original); OpenAI 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf
- **e3** B. Braun Produktkatalog: Bipolar Cup (PRID00004418) · HTML, undatiert · S. Produktbeschreibung · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://catalogs.bbraun.com/en-01/p/PRID00004418/bipolar-cup
- **e4** B. Braun Produktkatalog: Cemented Polyethylene Cups (PRID00002464) · HTML, undatiert · S. Produktbeschreibung (Flat-/Full-profile, XLPE mit Vitamin E, Ø 22,2–36) · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://catalogs.bbraun.com/en-01/p/PRID00002464/cemented-polyethylene-cups
- **bb-web** B. Braun – Zementierte Hüftprothese (Anwendungsfall Bipolarpfanne + zementierter Excia-T-Gradschaft) · HTML, undatiert · S. Abschnitt Operationstechniken · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/de/produkte-und-loesungen/therapien/orthopaedischer-gelenkersatz-und-regenerative-therapien/hueftendoprothetik/zementierte-hueftprothese.html
- **excia-old** AESCULAP Excia 12/14 – andere Schaftlinie (nur Abgrenzung) · O90301 1119/PDF/5, 11/2019 · S. gedr.=PDF 14, 16 · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-1214.pdf
- **e5** AESCULAP Excia T Hip Endoprosthesis System (EN) · O56002 0920/PDF/5, 09/2020 · S. Gesamtdokument geöffnet; kein positiver Paarungsbeleg Bipolar Cup × Excia T zementiert · Markt: EN auf DE-Herstellerseite; anderer Dokumentstand als e1 (Nr. 4008516, 01/2026) · gelesen: OpenAI 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-t.pdf

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.
- **v1.2** (2026-10-07, 001-implantate-luecken): Plasmafit Poly: Schalen-REF NV040T–NV062T je Liner-Code B–M; Standard-UHMWPE-Liner (symmetrisch 32, mit Schulter 28/32) mit REF und Schalenbereich (T18, 2 Prüfer); Vitelene-Liner (symmetrisch/posterior wall/asymmetrisch je Innen-Ø) als eigene Komponente mit REF, Rückruf FSCA 279 verknüpft; Bipolar Cup × Excia T zementiert bleibt offen (Excia-T DE 01/2026 und EN O56002 ohne Paarung).

Bilder: keine übernommen – Rechte beim Hersteller.
