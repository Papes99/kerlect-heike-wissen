# Smith+Nephew – SL-PLUS MIA, POLARSTEM, SPECTRON EF, R3, REFLECTION, TANDEM Bipolar

_Version 1.2 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen. v1.2: Lauf 001-implantate-dach._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `sn.slplus_mia.schaft` | schaft | SL-PLUS MIA | fixation: zementfrei; konus: 12/14; ccd_grad: {"standard": 131, "lateral": 123}; laengen_mm: Stem length I / II laut 31156-en V2 S. 17 (Definition S. 18); alte Werte 00884-en nicht verwenden; hinweis: Größenbezeichnung als Text: „01“ ≠ „0“; 11/12 optionale Sondergrößen | slmia | belegt |
| `sn.polarstem.zementfrei` | schaft | POLARSTEM zementfrei | fixation: zementfrei; konus: 12/14; ccd_varianten_us: Standard 135°, lateral 126°, valgus 145°; Standard/lateral auch mit Kragen (US-IFU); registerbeleg: EPRD zf-Schaft #7 (n=20.743); Kombi mit R3 DE #8, CH #3; werte: EU-Größen/REF offen | polar-us | Fundstelle (US) |
| `sn.polarstem.zementiert` | schaft | POLARSTEM zementiert | fixation: zementiert; konus: 12/14; material: Edelstahl (US-IFU); registerbeleg: EPRD zementiert #8 (n=4.515); werte: EU offen | polar-us | Fundstelle (US) |
| `sn.spectron_ef.schaft` | schaft | SPECTRON EF | fixation: zementiert; konus: 12/14; ccd_grad: 131 | s3 | belegt |
| `sn.r3.schale` | pfanne | R3 | fixation: zementfrei; schalen_mm: 40–80 laut Grafik | s4 | belegt (1 Prüfer: Astra visuell) |
| `sn.reflection.zementfrei` | pfanne | REFLECTION (zementfrei) | fixation: zementfrei; dokument: nur historische EN-Unterlage 00811 (2013); aktuelle EU-Unterlage offen | reflection | offen |
| `sn.reflection.all_poly` | pfanne | REFLECTION All-Poly (zementiert) | fixation: zementiert; dokument: offen | – | offen |
| `sn.mueller_pe` | pfanne | Müller-PE-Pfanne (S+N) | fixation: zementiert; dokument: kein Herstellernachweis gefunden | – | offen |
| `sn.r3.xlpe` | inlay | R3 XLPE | material: hochvernetztes PE; varianten: 0°, 20°, 0°+4, 20°+4 (getrennte REF); beispiel_ref: Ø36/Schale 52: 7133-2752 / 7133-5752 / 7133-6952 / 7133-8552; Ø36/66–70: 7133-0766 / 7133-1266 / 7133-1566 / 7133-2666; hinweis: keine REF durch Zahlenfortsetzung erzeugen | s4 | belegt |
| `sn.kopf.oxinium` | kopf | OXINIUM | konus: 12/14; hinweis: Ø40/44 nur mit zugehöriger Ti-Hülse; SAP Ø40/44: 71342340/71342344 | matrix | belegt |
| `sn.kopf.biolox_delta` | kopf | BIOLOX delta | konus: 12/14; familien: 765391/713460 (Halslänge in mm) und 750074 (S/M/L/XL) – am Etikett unterscheiden; hinweis: BIOLOX OPTION ist eine eigene Familie, nicht als BIOLOX delta führen; OPTION Ø40 XL nicht freigegeben | matrix | belegt |
| `sn.kopf.cocr` | kopf | CoCr | material: CoCrMo; konus: 12/14; hinweis: SAP Ø40/44: 71342640/71342644 (mit Ti-Hülse) | matrix | belegt |
| `sn.duokopf.tandem_bipolar` | duokopf | TANDEM Bipolar (Bi-Polar Head (frühere Bezeichnung in dieser Datei)) | verwendung: mit SPECTRON EF; innenkopf: S+N OXINIUM/CoCr 12/14, Ø22/28 (tandem PDF 17); keine BIOLOX-delta-Bipolar-Freigabe; varianten: TANDEM Bipolar (XLPE) und TANDEM INTL Bipolar (UHMWPE) getrennt; fussnoten: * Kombination in EU nicht genehmigt; ** Größe 01 nicht mit +16 oder TANDEM INTL Bipolar; *** 10/12 nicht in EU verkauft – SPECTRON EF ohne Sperrstern | tandem | belegt; Auswahl Julian 07.10.2026 (DACH-häufig) |

### Größen – SL-PLUS MIA (Quelle slmia)
| groesse | sap_standard | sap_lateral | stem_length_I_mm | stem_length_II_mm |
|---|---|---|---|---|
| 01 | 75000172 | – | 128 | 109 |
| 0 | 75000173 | – | 132 | 113 |
| 1 | 75000174 | 75000186 | 137 | 117 |
| 2 | 75000175 | 75000187 | 141 | 121 |
| 3 | 75000176 | 75000188 | 145 | 124 |
| 4 | 75000177 | 75000189 | 150 | 128 |
| 5 | 75000178 | 75000190 | 154 | 132 |
| 6 | 75000179 | 75000191 | 159 | 136 |
| 7 | 75000180 | 75000192 | 163 | 140 |
| 8 | 75000181 | 75000193 | 168 | 144 |
| 9 | 75000182 | 75000194 | 173 | 148 |
| 10 | 75000183 | 75000195 | 178 | 152 |
| 11 | 75000184 | 75000196 | 183 | 157 |
| 12 | 75000185 | 75000197 | 188 | 162 |

### Größen – SPECTRON EF (Quelle s3)
| groesse | laenge_mm | ref_standard | ref_high_offset |
|---|---|---|---|
| 1 / 1H | 115 | 71312101 | 71312111 |
| 2 / 2H | 125 | 71312102 | 71312112 |
| 3 / 3H | 135 | 71312103 | 71312113 |
| 4 / 4H | 135 | 71312104 | 71312114 |
| 5 / 5H | 135 | 71312105 | 71312115 |

### T12_matrix – S+N Kopf ↔ Schaft (Matrix 04758 Ed. 05/26 V12) (Quelle matrix, S. 2/7, 6/7)
| kopf | durchmesser_mm | hals | sl_plus_mia_01 | sl_plus_mia_uebrige | spectron |
|---|---|---|---|---|---|
| OXINIUM/CoCrMo | 22 | 0,+4,+8,+12 | ja | ja | ja |
| OXINIUM/CoCrMo | 26 | 0,+4,+8,+12 | nein | nein | ja |
| OXINIUM/CoCrMo | 28 | −3,0,+4,+8,+12 | ja | ja | ja |
| OXINIUM/CoCrMo | 28 | +16 | nein | ja | ja |
| OXINIUM/CoCrMo | 32 | −3,0,+4,+8,+12 | ja | ja | ja |
| OXINIUM/CoCrMo | 32 | +16 | nein | ja | ja |
| OXINIUM/CoCrMo | 36 | −3,0,+4,+8,+12 | ja | ja | ja |
| OXINIUM/CoCrMo | 40/44 | −4,0,+4,+8 (Ti-Hülse zwingend: 71344245/47/48/49) | ja | ja | ja |
| BIOLOX delta (765391/713460) | 32 | 0,+4,+8 (SAP 765391-60/61/62) | ja | ja | ja |
| BIOLOX delta (765391/713460) | 36 | 0,+4,+8,+12 (SAP 765391-65/66/67/53) | ja | ja | ja |
| BIOLOX delta (765391/713460) | 40 | 0,+4,+8 (SAP 713460-04/05/06) | ja | ja | ja |
| BIOLOX delta (750074) | 28 | S/M/L (SAP 750074-51/52/53) | ja | ja | ja |
| BIOLOX delta (750074) | 32 | S/M/L/XL (SAP 750074-60/61/62/63) | ja | ja | ja |
| BIOLOX delta (750074) | 36 | S/M/L/XL (SAP 750074-48/49/50/47) | ja | ja | ja |
_ja/nein = Herstellerstatus; lokale Zulassung prüfen; Stainless Steel nicht freigegeben; Spalte SL-PLUS Japan ist keine MIA-Spalte_

### T15_r3 – R3 Schale ↔ XLPE-Innen-Ø (Quelle s4, S. 13, 17–18)
| schalen_mm | innen_mm |
|---|---|
| 40/42/44 | 22 |
| 46 | 28 |
| 48/50 | 28,32 |
| 52/54 | 28,32,36 |
| 56/58 | 28,32,36,40 |
| 60 | 28,32,36,40,44 |
| 62 | 32,36,40,44 |
| 64/66/68/70/72/74/76/78/80 | 36,40,44 |
_aus Grafik visuell gelesen (Astra, 1 Prüfer); alte Keramik-Spalten nicht verwenden_

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `sn.slplus_mia.schaft` | `sn.kopf.oxinium` | **bedingt** | Ø/Hals laut T12 inkl. Nein-Zeilen (26 mm nein; +16 nicht bei Größe 01) | matrix | 2/7 |
| `sn.slplus_mia.schaft` | `sn.kopf.cocr` | **bedingt** | wie OXINIUM laut T12 | matrix | 2/7 |
| `sn.slplus_mia.schaft` | `sn.kopf.biolox_delta` | **bedingt** | Familie/Ø/Hals laut T12 | matrix | 2/7 |
| `sn.spectron_ef.schaft` | `sn.kopf.oxinium` | **ja** | Ø 22–44 laut T12 | matrix | 6/7 |
| `sn.spectron_ef.schaft` | `sn.kopf.cocr` | **ja** | Ø 22–44 laut T12 | matrix | 6/7 |
| `sn.spectron_ef.schaft` | `sn.kopf.biolox_delta` | **bedingt** | Familie/Ø laut T12 | matrix | 6/7 |
| `sn.r3.schale` | `sn.r3.xlpe` | **bedingt** | Innen-Ø je Schale laut T15 | s4 | 13, 17–18 |
| `sn.spectron_ef.schaft` | `sn.duokopf.tandem_bipolar` | **ja** | Innenkopf OXINIUM/CoCr 12/14 Ø22/28; EU-Fußnoten beachten | tandem | PDF 17 |

## Regeln
- Kopf gegen die zutreffende Schaftspalte prüfen – auch Nein-Zeilen (z. B. Ø26 nicht mit SL-PLUS MIA; +16 nicht mit Größe 01). (matrix S. 2/6)
- OXINIUM/CoCr Ø40/44 nur mit der zugehörigen Ti-Hülse; keine Hülsen fremder Systeme. (matrix)
- TANDEM Bipolar mit SPECTRON EF: Innenkopf nur S+N OXINIUM/CoCr 12/14 Ø22/28; TANDEM Unipolar ist ein anderes Produkt. (tandem PDF 17, s3 S. 14)
- R3-XLPE-Innen-Ø nur in den Schalengrößen laut Grafik; Variante (0°/20°/+4) getrennt. (s4 S. 13)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| R3 XLPE Acetabular Liner | BfArM | R-2013-10 (03050/13), 29.05.2013 | EU/DE | – | zwei Produktlose mit vertauschter Kennzeichnung | `sn.r3.xlpe` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2013/03050-13_kundeninfo_de.pdf?__blob=publicationFile |
| R3 Acetabular Shells, bestimmte Chargen | BfArM | R-2020-04 (05608/20) | EU/DE | kein behördlicher Abschluss gefunden | Verriegelungsfehler kann Liner betreffen, Liner aber nicht Rückrufprodukt; Rücknahme laut Hersteller abgewickelt – kein behördlicher Abschluss | `sn.r3.schale` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2020/05608-20_1_kundeninfo_de.pdf?__blob=publicationFile |
| R3 0 HOLE ACET SHELL 54 mm (REF 71331854, Lot 23HM03659) – Verpackung enthält 3-HOLE-Schale | BfArM | R-2023-13 (35762/23), 20.11.2023 | EU/DE | kein Abschluss gefunden | betroffene Ware lokalisieren/quarantänisieren/zurücksenden (Astra: Original gelesen; Perplexity bestätigt Schale) | `sn.r3.schale` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] EU-IFUs (ifu.smith-nephew.com, REF nötig)
- [ ] REFLECTION zementfrei/All-Poly aktuelle EU-Unterlage; Müller-PE-Pfanne von S+N
- [ ] TANDEM Bipolar: Größen/REF; EU-Verfügbarkeit XLPE- vs. INTL-Variante
- [ ] GTIN
- [ ] POLARSTEM: aktuelle EU-OP-Technik/IFU, Größen/REF, Matrix-Zeilen 04758
- [ ] POLARCUP (zementiert, EPRD #11) – bei Bedarf

## Quellen
- **s1** SL-PLUS MIA INTEGRATION-PLUS – Surgical Technique · 00884-en (1524) V4, 01/15 · S. gedr. 16–19/PDF 18–21 (CCD S. 16, Implantate S. 18–19); Kennung PDF 28 · Markt: EN international · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true
- **matrix** Hip implant compatibility matrix – Stem and Femoral Ball Head Combinations · Lit. No. 04758, Ed. 05/26 V12 · S. S. 2/7 (SL-PLUS MIA), 6/7 (SPECTRON) · Markt: international mit lokalen Zulassungsvorbehalten · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de
- **s3** SPECTRON EF – Surgical Technique · 21885 V3, 71380478 REVB 03/23, ©2023 · S. Specs gedr. 1/PDF 4; Katalog gedr. 12/PDF 15; TANDEM Unipolar gedr. 14/PDF 17; Kompatibilität gedr. 16/PDF 19; Kennung PDF 20 · Markt: EN · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true
- **s4** R3 Acetabulum-System – Operationstechnik · 7138-1560-de REVB 06/12, ©2017 · S. gedr.=PDF 13 Kombi-Grafik; 17–18 XLPE-Katalog; Kennung 32 · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew-delivery.stylelabs.cloud/api/public/content/1bd7a20b4fdf4a158b95aad5987f2686?v=e321be27&download=true
- **tandem** TANDEM Bipolar and Unipolar Hip System – INTL Surgical Technique · 29073 V2, 71380925 REVA 02/23 · S. PDF 17 Implant Compatibility (unnummeriert); Kennung PDF 20 · Markt: INTL mit EU-Fußnoten · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/8af4fc46aafd4be4a8d289f62a72ee8e?download=true&v=bdf205cd
- **reflection** REFLECTION – Surgical Technique (historisch) · 00811 V1, 10/13, ©2013 · S. Titelblatt/Impressum · Markt: historische EN-Unterlage, kein aktueller EU-Nachweis · gelesen: Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/7cada363f2224bc3957ac5e0fde018ad?download=true&v=eca89761
- **slmia** SL-PLUS MIA Surgical Technique · 31156-en V2, 11/2024 · S. S. 17–18 / PDF 20–21; Warnungen S. 2 / PDF 5 · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/c38ee11595e14dfdbdd7ade71a170ac9?v=3e0dbffa&download=true
- **polar-us** POLARSTEM Non-Cemented and Cemented Stem System – Instructions for Use 81098832 · Rev. 2, 06/2021 · S. S. 1 (nur USA), S. 4, S. 2/5 · Markt: USA – kein EU-Ersatz · gelesen: Grok Lauf 001 (US-IFU) · https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.
- **v1.2** (2026-10-07, 001-implantate-dach): POLARSTEM zementfrei/zementiert wieder aufgenommen (DACH-Regel; nur US-Fundstelle, EU offen); SL-PLUS MIA Längen I/II aus 31156-en V2; R3-Rückrufe R-2020-04/R-2023-13 = Schale (Liner-Zuordnung entfernt).

Bilder: keine übernommen – Rechte beim Hersteller.
