# Aesculap (B. Braun) – Excia T – zementfrei, zementiert, Duokopf; Plasmafit

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.excia_t.zementfrei` | schaft | Excia T zementfrei | fixation: zementfrei; material: Ti6Al4V / PLASMAPORE; konus: 12/14; ccd_grad: {"standard_T": 135, "lateral_TL": "128 (+6 mm Offset)"} | e1 | belegt |
| `aesculap.excia_t.zementiert` | schaft | Excia T zementiert | fixation: zementiert; material: CoCr; konus: 12/14; ccd_grad: {"standard_T": 135, "lateral_TL": "128 (+6 mm Offset)"} | e1 | belegt |
| `aesculap.plasmafit.plus` | pfanne | Plasmafit Plus | fixation: zementfrei; varianten: Plus / Plus 3 / Plus 7 (Plus 7 bei 40/42/44 nur fünf Schraubenlöcher, e2 S. 20); liner: Keramik oder PE (e2 S. 5) | e2 | belegt |
| `aesculap.plasmafit.poly` | pfanne | Plasmafit Poly | fixation: zementfrei; liner: nur PE (e2 S. 5: „Only for polyethylene liners“) | e2 | belegt |
| `aesculap.pe_pfanne.zementiert` | pfanne | Aesculap PE-Pfanne zementiert | fixation: zementiert; familie: Cemented Polyethylene Cups (Flat-/Full-profile) – Einzelprodukt/Profil/REF offen; hinweis: nicht als Müller-Pfanne umbenennen | e4 | offen |
| `aesculap.inlay.biolox_delta` | inlay | BIOLOX delta Inlay | material: Keramik; nur_fuer: Plasmafit Plus; nicht_fuer: Plasmafit Poly; beispiel_ref_36: Plus 52=NV113D, 54=NV114D, 56=NV115D, 58/60/62=NV116D, 64–70=NV117D (e2 S. 20–21) | e2 | belegt |
| `aesculap.inlay.pe_standard` | inlay | PE-Inlay Standard (UHMWPE) | material: UHMWPE; fuer: Plasmafit Poly (Auswahl Julian 07.10.2026); Plasmafit Plus ebenfalls PE möglich; werte: symmetrische UHMWPE-Zeilen in e2 noch nicht übernommen – Größe vom Etikett | e2 | hausabhängig |
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
| groesse | liner_code |
|---|---|
| 40 | B |
| 42 | C |
| 44 | D |
| 46 | E |
| 48 | F |
| 50 | G |
| 52 | H |
| 54 | I |
| 56 | J |
| 58 | K |
| 60 | L |
| 62 | M |

### Größen – BIOLOX delta Inlay (Quelle e2)
| innen_mm | plus_schalen |
|---|---|
| 28 | 44–54 |
| 32 | 48–70 |
| 36 | 52–70 |
| 40 | 56–70 |

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

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `aesculap.plasmafit.plus` | `aesculap.inlay.biolox_delta` | **bedingt** | Innen-Ø nur in den Schalen laut T8 | e2 | 18–21 |
| `aesculap.plasmafit.poly` | `aesculap.inlay.biolox_delta` | **nein** | Poly nur PE-Liner | e2 | 5 |
| `aesculap.plasmafit.poly` | `aesculap.inlay.pe_standard` | **bedingt** | nur PE; Größe vom Etikett (UHMWPE-Zeilen noch nicht übernommen) | e2 | 5 |
| `aesculap.excia_t.zementfrei` | `aesculap.kopf.biolox_delta` | **ja** | Ø/Hals laut Excia-T-Kopfübersicht | e1 | 19 |
| `aesculap.excia_t.zementfrei` | `aesculap.kopf.isodur_cocr` | **ja** | Ø 28–40 laut Excia-T-Kopfübersicht; nicht Ø22,2 | e1 | 19 |
| `aesculap.excia_t.zementiert` | `aesculap.kopf.biolox_delta` | **ja** | Ø/Hals laut Excia-T-Kopfübersicht | e1 | 19 |
| `aesculap.excia_t.zementiert` | `aesculap.kopf.isodur_cocr` | **ja** | Ø 28–40 laut Excia-T-Kopfübersicht; nicht Ø22,2 | e1 | 19 |
| `aesculap.inlay.biolox_delta` | `aesculap.kopf.isodur_cocr` | **nein** | keinen Metallkopf mit Keramikinlay freigeben | e2 | 24 |
| `aesculap.excia_t.zementiert` | `aesculap.duokopf.bipolar_cup` | **offen** | nur Anwendungsfall; Freigabetabelle fehlt | bb-web | Operationstechniken |

## Regeln
- Plasmafit Poly nur mit PE-Liner; Keramikinlay nur bei Plasmafit Plus und nur in den Schalengrößen laut Tabelle. (e2 S. 5, 18–21)
- Keinen Metallkopf (Isodur/ISODUR F) mit Keramikinlay kombinieren. (e2 S. 24)
- Excia 12/14 (O90301) ist eine andere Schaftlinie – Größen/REF nicht auf Excia T übertragen. (excia-old, e1)
- Bipolar Cup nur mit freigegebenem zementiertem Schaft; Freigabetabelle mit Excia T zementiert fehlt. (bb-web, e3)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| VITELENE-Einsätze (nicht BIOLOX delta) | BfArM | FSCA 279 (12190/24), 17.04.2024 | EU/DE | – | nur relevant, falls Vitelene-Liner verwendet werden | – | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/12190-24_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] EU-IFU Excia T zementiert / Bipolar Cup (Freigabetabelle)
- [ ] Einzelprodukt/Profil/REF der zementierten PE-Pfanne
- [ ] UHMWPE-Liner (symmetrisch) Plasmafit: Zeilen aus e2 übernehmen
- [ ] GTIN

## Quellen
- **e1** AESCULAP Excia T – Hüftendoprothesensystem · Nr. 4008516, 01/2026 · S. CCD gedr. 11/PDF 6; Schäfte gedr. 18/PDF 10; Köpfe gedr. 19/PDF 10; Kennung PDF 13 · Markt: DE-Fassung · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf
- **e2** AESCULAP Plasmafit – Acetabular Cup System · O45502 0718/1/4, 07/2018 · S. gedr.=PDF 5–7 Konzept; 18–21 Implantate/Liner; 24 Köpfe; Kennung 34 · Markt: EN auf DE-Herstellerseite · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf
- **e3** B. Braun Produktkatalog: Bipolar Cup (PRID00004418) · HTML, undatiert · S. Produktbeschreibung · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://catalogs.bbraun.com/en-01/p/PRID00004418/bipolar-cup
- **e4** B. Braun Produktkatalog: Cemented Polyethylene Cups (PRID00002464) · HTML, undatiert · S. Produktbeschreibung (Flat-/Full-profile, XLPE mit Vitamin E, Ø 22,2–36) · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://catalogs.bbraun.com/en-01/p/PRID00002464/cemented-polyethylene-cups
- **bb-web** B. Braun – Zementierte Hüftprothese (Anwendungsfall Bipolarpfanne + zementierter Excia-T-Gradschaft) · HTML, undatiert · S. Abschnitt Operationstechniken · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/de/produkte-und-loesungen/therapien/orthopaedischer-gelenkersatz-und-regenerative-therapien/hueftendoprothetik/zementierte-hueftprothese.html
- **excia-old** AESCULAP Excia 12/14 – andere Schaftlinie (nur Abgrenzung) · O90301 1119/PDF/5, 11/2019 · S. gedr.=PDF 14, 16 · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-1214.pdf

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.

Bilder: keine übernommen – Rechte beim Hersteller.
