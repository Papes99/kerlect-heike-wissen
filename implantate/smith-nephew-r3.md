# Smith+Nephew – SL-PLUS MIA, POLARSTEM, SPECTRON EF, R3, REFLECTION, TANDEM Bipolar

_Version 1.3 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen. v1.2: Lauf 001-implantate-dach. v1.3 (Lauf 001-implantate-luecken): POLARSTEM-Größen/SAP aus 01217-en V7 und POLARSTEM-Matrixspalten aus 04758 S. 1/7 (Claude-Helfer + OpenAI am Original), Maßwerte 1 Prüfer._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `sn.slplus_mia.schaft` | schaft | SL-PLUS MIA | fixation: zementfrei; konus: 12/14; ccd_grad: {"standard": 131, "lateral": 123}; laengen_mm: Stem length I / II laut 31156-en V2 S. 17 (Definition S. 18); alte Werte 00884-en nicht verwenden; hinweis: Größenbezeichnung als Text: „01“ ≠ „0“; 11/12 optionale Sondergrößen | slmia | belegt |
| `sn.polarstem.zementfrei` | schaft | POLARSTEM zementfrei | fixation: zementfrei; konus: 12/14; material: Ti-6Al-4V ISO 5832-3 (Tabellenkopf gedr. 13 / PDF 16); beschichtung: „All cementless implants are coated with an open-pored titanium plasma/HA coating.“ (gedr. 1 / PDF 4); ccd_grad: {"standard": 135, "lateral": 126, "valgus": 145}; kragen: ohne Kragen – Kragen-Schäfte als eigene Komponente sn.polarstem.zementfrei_kragen; Valgus nur ohne Kragen; groessen_text: Standard 01, 0–11; Lateral 1–11; Valgus 0–7 (Größe „01“ ≠ „0“); masse: Offset/Halslänge/Halshöhe je Kopf-Halslänge (XS/-3 … XXL/+16) aus gedr. 15 / PDF 18; Offset „based on a 32 mm OXINIUM™ head“; Halslänge/-höhe dort als Zeilen „1 - 7“ und „8 - 12“ gedruckt (Größe 12 gibt es in den Artikeltabellen nicht); S/CT aus gedr. 16 / PDF 19 (Einheit nicht angegeben; Standard 01 dort als „O1“ gedruckt). Maßtabellen trennen nicht nach Fixation/Kragen.; fussnoten: „* outlier sizes (optional)   x not available in the US“ (gedr. 13 / PDF 16); demo: Demo-Implantate (Size 3) nicht als Implantate übernommen; us_ifu: 81098832 Rev. 2 (polar-us) – kein EU-Ersatz; registerbeleg: EPRD zf-Schaft #7 (n=20.743); Kombi mit R3 DE #8, CH #3; sicherheit_masse: belegt (Original, 1 Prüfer) | polar-st | Größen/SAP belegt (Original, 2 Prüfer); Maßwerte belegt (Original, 1 Prüfer) |
| `sn.polarstem.zementfrei_kragen` | schaft | POLARSTEM Collar (zementfrei, mit Kragen) | fixation: zementfrei – „Standard and lateral offset stems are also offered in a collared version“ (gedr. 1 / PDF 4); Matrix: „POLARSTEM◊ Cementless (incl. POLARSTEM◊ Collar)“; konus: nicht angegeben (Kragen-Tabelle gedr. 13 / PDF 16); material: nicht angegeben (Kragen-Tabelle gedr. 13 / PDF 16); ccd_grad: nicht angegeben (Kragen-Tabelle gedr. 13 / PDF 16); hinweis: Kragen-Tabelle nennt kein Material, keinen CCD und keinen Konus – nicht ergänzt. Kein Valgus mit Kragen.; masse: eigene Maßangaben für Kragen-Schäfte nicht gefunden; fussnoten: „* outlier sizes (optional)   x not available in the US“; demo: Demo implant (Size 3) Standard 75102217 nicht als Implantat übernommen | polar-st | belegt (Original, 2 Prüfer) |
| `sn.polarstem.zementiert` | schaft | POLARSTEM zementiert | fixation: zementiert; konus: 12/14; material: stainless steel ISO 5832-9 (Tabellenkopf gedr. 14 / PDF 17); ccd_grad: {"standard": 135, "lateral": 126}; groessen_text: Standard 0–8, Lateral 1–8; kein Valgus, kein Kragen (laut Tabelle); masse: Maßtabellen gedr. 15–16 / PDF 18–19 trennen nicht nach zementfrei/zementiert – Gültigkeit für zementierte Schäfte nicht ausgewiesen (Werte siehe sn.polarstem.zementfrei); demo: Demo implant (Size 3) nicht als Implantat übernommen; us_ifu: 81098832 Rev. 2 (polar-us) – kein EU-Ersatz; registerbeleg: EPRD zementiert #8 (n=4.515) | polar-st | belegt (Original, 2 Prüfer) |
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

### Größen – POLARSTEM zementfrei (Quelle polar-st)
| groesse | variante | ccd | sap | fussnote | seite | offset_XS-3 | offset_S+0 | offset_M+4 | offset_L+8 | offset_XL+12 | offset_XXL+16 | halslaenge_XS-3 | halslaenge_S+0 | halslaenge_M+4 | halslaenge_L+8 | halslaenge_XL+12 | halslaenge_XXL+16 | halshoehe_XS-3 | halshoehe_S+0 | halshoehe_M+4 | halshoehe_L+8 | halshoehe_XL+12 | halshoehe_XXL+16 | S | CT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Standard | 135° | 75100462 | * outlier sizes (optional); x not available in the US | gedr. 13 / PDF 16 | – | 37.2 | 40.0 | 42.8 | 45.7 | 48.5 | – | 29.9 | 33.9 | 37.9 | 41.9 | 45.9 | – | 26.4 | 29.3 | 32.1 | 34.9 | 37.8 | 105.6 | 135.8 |
| 0 | Standard | 135° | 75100463 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 35.3 | 37.4 | 40.2 | 43.0 | 45.9 | 48.7 | 27.0 | 29.9 | 33.9 | 37.9 | 41.9 | 45.9 | 24.4 | 26.4 | 29.3 | 32.1 | 34.9 | 37.8 | 111.6 | 141.6 |
| 1 | Standard | 135° | 75100464 | – | gedr. 13 / PDF 16 | 37.9 | 40.0 | 42.8 | 45.6 | 48.4 | 51.3 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 117.6 | 149.7 |
| 2 | Standard | 135° | 75100465 | – | gedr. 13 / PDF 16 | 38.5 | 40.6 | 43.4 | 46.2 | 49.1 | 51.9 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 121.6 | 153.7 |
| 3 | Standard | 135° | 75100466 | – | gedr. 13 / PDF 16 | 39.3 | 41.4 | 44.2 | 47.0 | 49.9 | 52.7 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 125.4 | 157.6 |
| 4 | Standard | 135° | 75100467 | – | gedr. 13 / PDF 16 | 40.0 | 42.0 | 44.9 | 47.7 | 50.5 | 53.3 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 129.8 | 161.9 |
| 5 | Standard | 135° | 75100468 | – | gedr. 13 / PDF 16 | 40.6 | 42.6 | 45.5 | 48.3 | 51.1 | 54.0 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 133.7 | 165.9 |
| 6 | Standard | 135° | 75100469 | – | gedr. 13 / PDF 16 | 41.2 | 43.3 | 46.1 | 48.9 | 51.7 | 54.6 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 137.7 | 170 |
| 7 | Standard | 135° | 75100470 | – | gedr. 13 / PDF 16 | 41.8 | 43.9 | 46.7 | 49.5 | 52.3 | 55.2 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 141.8 | 173.7 |
| 8 | Standard | 135° | 75100471 | – | gedr. 13 / PDF 16 | 42.3 | 44.4 | 47.2 | 50.0 | 52.9 | 55.7 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 145.6 | 177.9 |
| 9 | Standard | 135° | 75100472 | – | gedr. 13 / PDF 16 | 43.0 | 45.1 | 47.9 | 50.8 | 53.6 | 56.4 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 149.6 | 182 |
| 10 | Standard | 135° | 75100473 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 43.7 | 45.7 | 48.5 | 51.4 | 54.2 | 57.0 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 153.6 | 186 |
| 11 | Standard | 135° | 75100509 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 44.3 | 46.3 | 49.1 | 52.0 | 54.8 | 57.6 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 26.2 | 28.2 | 31.0 | 33.9 | 36.7 | 39.5 | 157.9 | 190 |
| 1 | Lateral | 126° | 75100474 | – | gedr. 13 / PDF 16 | 40.8 | 43.2 | 46.4 | 49.7 | 52.9 | 56.1 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 118.7 | 148.8 |
| 2 | Lateral | 126° | 75100475 | – | gedr. 13 / PDF 16 | 41.5 | 43.8 | 47.0 | 50.3 | 53.5 | 56.7 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 122.7 | 152.8 |
| 3 | Lateral | 126° | 75100476 | – | gedr. 13 / PDF 16 | 42.3 | 44.6 | 47.8 | 51.1 | 54.3 | 57.5 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 126.7 | 156.8 |
| 4 | Lateral | 126° | 75100477 | – | gedr. 13 / PDF 16 | 42.9 | 45.3 | 48.5 | 51.7 | 55.0 | 58.2 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 130.7 | 160.8 |
| 5 | Lateral | 126° | 75100478 | – | gedr. 13 / PDF 16 | 43.5 | 45.9 | 49.1 | 52.3 | 55.6 | 58.8 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 134.7 | 164.8 |
| 6 | Lateral | 126° | 75100479 | – | gedr. 13 / PDF 16 | 44.1 | 46.5 | 49.7 | 53.0 | 56.2 | 59.4 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 138.7 | 168.8 |
| 7 | Lateral | 126° | 75100480 | – | gedr. 13 / PDF 16 | 44.7 | 47.1 | 50.3 | 53.6 | 56.8 | 60.0 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 142.7 | 172.8 |
| 8 | Lateral | 126° | 75100481 | – | gedr. 13 / PDF 16 | 45.3 | 47.6 | 50.8 | 54.1 | 57.3 | 60.5 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 146.8 | 176.8 |
| 9 | Lateral | 126° | 75100482 | – | gedr. 13 / PDF 16 | 46.0 | 48.3 | 51.6 | 54.8 | 58.0 | 61.3 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 150.7 | 180.9 |
| 10 | Lateral | 126° | 75100483 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 46.6 | 48.9 | 52.2 | 55.4 | 58.6 | 61.9 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 154.7 | 184.9 |
| 11 | Lateral | 126° | 75100510 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 47.2 | 49.5 | 52.8 | 56.0 | 59.3 | 62.5 | 29.5 | 32.4 | 36.4 | 40.4 | 44.4 | 48.4 | 24.7 | 26.4 | 28.8 | 31.2 | 33.5 | 35.9 | 158.4 | 188.9 |
| 0 | Valgus | 145° | 75102072 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 34.2 | 35.9 | 38.2 | 40.5 | 42.8 | 45.1 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 110.5 | 144.8 |
| 1 | Valgus | 145° | 75102073 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 35.0 | 36.7 | 39.0 | 41.3 | 43.6 | 45.9 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 116.4 | 150.8 |
| 2 | Valgus | 145° | 75102074 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 35.7 | 37.3 | 39.6 | 41.9 | 44.2 | 46.5 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 120.4 | 154.9 |
| 3 | Valgus | 145° | 75102075 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 36.5 | 38.1 | 40.4 | 42.7 | 45.0 | 47.3 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 124.2 | 158.9 |
| 4 | Valgus | 145° | 75102076 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 37.1 | 38.8 | 41.1 | 43.4 | 45.7 | 48.0 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 128.7 | 163 |
| 5 | Valgus | 145° | 75102077 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 37.7 | 39.4 | 41.7 | 44.0 | 46.3 | 48.6 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 132.7 | 167 |
| 6 | Valgus | 145° | 75102078 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 38.3 | 40.0 | 42.3 | 44.6 | 46.9 | 49.2 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 136.5 | 171 |
| 7 | Valgus | 145° | 75102079 | * outlier sizes (optional) | gedr. 13 / PDF 16 | 39.0 | 40.6 | 42.9 | 45.2 | 47.5 | 49.8 | 29.9 | 32.8 | 36.8 | 40.8 | 44.8 | 48.8 | 27.6 | 30.0 | 33.3 | 36.5 | 39.8 | 43.1 | 140.7 | 174.9 |

### Größen – POLARSTEM Collar (zementfrei, mit Kragen) (Quelle polar-st)
| groesse | variante | sap | fussnote | seite |
|---|---|---|---|---|
| 01 | Standard stem with collar | 75018399 | * outlier sizes (optional); x not available in the US | gedr. 13 / PDF 16 |
| 0 | Standard stem with collar | 75018400 | * outlier sizes (optional) | gedr. 13 / PDF 16 |
| 1 | Standard stem with collar | 75018401 | – | gedr. 13 / PDF 16 |
| 2 | Standard stem with collar | 75018402 | – | gedr. 13 / PDF 16 |
| 3 | Standard stem with collar | 75018403 | – | gedr. 13 / PDF 16 |
| 4 | Standard stem with collar | 75018404 | – | gedr. 13 / PDF 16 |
| 5 | Standard stem with collar | 75018405 | – | gedr. 13 / PDF 16 |
| 6 | Standard stem with collar | 75018406 | – | gedr. 13 / PDF 16 |
| 7 | Standard stem with collar | 75018407 | – | gedr. 13 / PDF 16 |
| 8 | Standard stem with collar | 75018408 | – | gedr. 13 / PDF 16 |
| 9 | Standard stem with collar | 75018409 | – | gedr. 13 / PDF 16 |
| 10 | Standard stem with collar | 75018410 | * outlier sizes (optional) | gedr. 13 / PDF 16 |
| 11 | Standard stem with collar | 75018411 | * outlier sizes (optional) | gedr. 13 / PDF 16 |
| 1 | Lateral stem with collar | 75018412 | – | gedr. 13 / PDF 16 |
| 2 | Lateral stem with collar | 75018413 | – | gedr. 13 / PDF 16 |
| 3 | Lateral stem with collar | 75018414 | – | gedr. 13 / PDF 16 |
| 4 | Lateral stem with collar | 75018415 | – | gedr. 13 / PDF 16 |
| 5 | Lateral stem with collar | 75018416 | – | gedr. 13 / PDF 16 |
| 6 | Lateral stem with collar | 75018417 | – | gedr. 13 / PDF 16 |
| 7 | Lateral stem with collar | 75018418 | – | gedr. 13 / PDF 16 |
| 8 | Lateral stem with collar | 75018419 | – | gedr. 13 / PDF 16 |
| 9 | Lateral stem with collar | 75102209 | – | gedr. 13 / PDF 16 |
| 10 | Lateral stem with collar | 75102210 | * outlier sizes (optional) | gedr. 13 / PDF 16 |
| 11 | Lateral stem with collar | 75102211 | * outlier sizes (optional) | gedr. 13 / PDF 16 |

### Größen – POLARSTEM zementiert (Quelle polar-st)
| groesse | variante | ccd | sap | item | seite |
|---|---|---|---|---|---|
| 0 | Standard | 135° | 75002111 | 11000405 | gedr. 14 / PDF 17 |
| 1 | Standard | 135° | 75002112 | 11000406 | gedr. 14 / PDF 17 |
| 2 | Standard | 135° | 75002113 | 11000407 | gedr. 14 / PDF 17 |
| 3 | Standard | 135° | 75002114 | 11000408 | gedr. 14 / PDF 17 |
| 4 | Standard | 135° | 75002115 | 11000409 | gedr. 14 / PDF 17 |
| 5 | Standard | 135° | 75002116 | 11000410 | gedr. 14 / PDF 17 |
| 6 | Standard | 135° | 75002117 | 11000411 | gedr. 14 / PDF 17 |
| 7 | Standard | 135° | 75002118 | 11000412 | gedr. 14 / PDF 17 |
| 8 | Standard | 135° | 75002119 | 11000413 | gedr. 14 / PDF 17 |
| 1 | Lateral | 126° | 75002120 | 11000414 | gedr. 14 / PDF 17 |
| 2 | Lateral | 126° | 75002121 | 11000415 | gedr. 14 / PDF 17 |
| 3 | Lateral | 126° | 75002122 | 11000416 | gedr. 14 / PDF 17 |
| 4 | Lateral | 126° | 75002123 | 11000417 | gedr. 14 / PDF 17 |
| 5 | Lateral | 126° | 75002124 | 11000418 | gedr. 14 / PDF 17 |
| 6 | Lateral | 126° | 75002125 | 11000419 | gedr. 14 / PDF 17 |
| 7 | Lateral | 126° | 75002126 | 11000420 | gedr. 14 / PDF 17 |
| 8 | Lateral | 126° | 75002127 | 11000421 | gedr. 14 / PDF 17 |

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

### T_matrix_polarstem – S+N Kopf ↔ POLARSTEM (Matrix 04758 Ed. 05/26 V12, Hausköpfe) (Quelle matrix, S. 1/7 (PDF 1))
| kopf | durchmesser_mm | hals | sap | zf_std_01 | zf_uebrige | zementiert |
|---|---|---|---|---|---|---|
| OXINIUM | 22 | +0 +4 +8 +12 | 713422-00/ -04/ -08/ -12 | ja | ja | ja |
| OXINIUM | 26 | +0 +4 +8 +12 | 713426-00/ -04/ -08/ -12 | nein | nein | nein |
| OXINIUM | 28 | -3 | 71342803 | nein | ja | ja |
| OXINIUM | 28 | +0 +4 +8 +12 | 713428-00/ -04/ -08/ -12 | ja | ja | ja |
| OXINIUM | 28 | +16 | 71342816 | nein | ja | ja |
| OXINIUM | 32 | -3 | 71343203 | nein | ja | ja |
| OXINIUM | 32 | +0 +4 +8 +12 | 713432-00/ -04/ -08/ -12 | ja | ja | ja |
| OXINIUM | 32 | +16 | 71343216 | nein | ja | ja |
| OXINIUM | 36 | -3 | 71343603 | nein | ja | ja |
| OXINIUM | 36 | +0 +4 +8 +12 | 713436-00/ -04/ -08/ -12 | ja | ja | ja |
| OXINIUM | 40¹ | -4 | 71342340 & sleeve: 71344245 | nein | ja | nein |
| OXINIUM | 40¹ | +0 +4 +8 | 71342340 & sleeve: 713442-47/ -48/ -49 | ja | ja | nein |
| OXINIUM | 44¹ | -4 | 71342344 & sleeve: 71344245 | nein | ja | nein |
| OXINIUM | 44¹ | +0 +4 +8 | 71342344 & sleeve: 713442-47/ -48/ -49 | ja | ja | nein |
| CoCrMo | 22 | +0 +4 +8 +12 | 713022-00/ -04/ -08/ -12 | ja | ja | nein |
| CoCrMo | 26 | +0 +4 +8 +12 | 713026-00/ -04/ -08/ -12 | nein | nein | nein |
| CoCrMo | 28 | -3 | 71302803 | nein | ja | nein |
| CoCrMo | 28 | +0 +4 +8 +12 | 713028-00/ -04/ -08/ -12 | ja | ja | nein |
| CoCrMo | 28 | +16 | 71302816 | nein | ja | nein |
| CoCrMo | 32 | -3 | 71303203 | nein | ja | nein |
| CoCrMo | 32 | +0 +4 +8 +12 | 713032-00/ -04/ -08/ -12 | ja | ja | nein |
| CoCrMo | 32 | +16 | 71303216 | nein | ja | nein |
| CoCrMo | 36 | -3 | 71303603 | nein | ja | nein |
| CoCrMo | 36 | +0 +4 +8 +12 | 713036-00/ -04/ -08/ -12 | ja | ja | nein |
| CoCrMo | 40¹ | -4 | 71342640 & sleeve: 71344245 | nein | ja | nein |
| CoCrMo | 40¹ | +0 +4 +8 | 71342640 & sleeve: 713442-47/ -48/ -49 | ja | ja | nein |
| CoCrMo | 44¹ | -4 | 71342644 & sleeve: 71344245 | nein | ja | nein |
| CoCrMo | 44¹ | +0 +4 +8 | 71342644 & sleeve: 713442-47/ -48/ -49 | ja | ja | nein |
| BIOLOX delta (765391/713460, hellblau = Inc.) | 32 | +0 +4 +8 | 765391-60/ -61/ -62 | ja | ja | ja |
| BIOLOX delta (765391/713460, hellblau = Inc.) | 36 | +0 +4 +8 +12 | 765391-65/ -66/ -67/ -53 | ja | ja | ja |
| BIOLOX delta (765391/713460, hellblau = Inc.) | 40 | +0 +4 +8 | 713460-04/ -05/ -06 | ja | ja | ja |
| BIOLOX delta (750074, pfirsich = Orthopaedics AG) | 28 | S M L | 750074-51/ -52/ -53 | ja | ja | ja |
| BIOLOX delta (750074, pfirsich = Orthopaedics AG) | 32 | S M L XL | 750074-60/ -61/ -62/ -63 | ja | ja | ja |
| BIOLOX delta (750074, pfirsich = Orthopaedics AG) | 36 | S M L XL | 750074-48/ -49/ -50/ -47 | ja | ja | ja |
_Spalten: zf_std_01 = POLARSTEM Cementless (incl. Collar) „Size std. 01³“ (³ „SAP no.: 75100462 and 75018399.“); zf_uebrige = Cementless (incl. Collar) „All other sizes²“; zementiert = POLARSTEM Cemented „All sizes²“. ja = grün/Häkchen „Combination is approved by Smith & Nephew“; nein = rot „Combination is not approved by Smith & Nephew“. ¹ „These femoral heads must only be used together with the corresponding Ti-sleeves.“ ² „Includes all POLARSTEM stem types (Standard, Lateral, Valgus and Medial). Valgus and Medial are only available for the cementless collarless type. …“ (Typ „Medial“ kommt in 01217-en V7 nicht vor). SAP-Zellen OXINIUM/CoCrMo/BIOLOX delta 765391/713460 hellblau = Smith & Nephew Inc.; BIOLOX delta 750074 pfirsich = Smith & Nephew Orthopaedics AG (Farbzuordnung laut Legende). Halslänge↔SAP-Suffix nur über Reihenfolge gedruckt. Nicht übernommen (keine Hausköpfe): Stainless Steel (nur Spalte zementiert ja, 26 mm nein) und BIOLOX OPTION (40 XL in allen Spalten nein). Markt-Vorbehalt (wörtlich): „The following matrix shows the compatibility of Femoral Ball Heads and Stems distributed by Smith & Nephew and used in Total Hip Arthroplasty. Each compatibility statement is based on the current evidence about the technical safety of the corresponding product combination. Combinations listed in the matrix may not be approved in all individual markets or geographies. The information contained in this matrix does not supersede the instructions for use (Package insert) in force in the markets where the products are being used. Please refer to your local Smith & Nephew representative to confirm the approval status in your country or region if you have questions about how Smith & Nephew products can be used.“_

### T_polarstem_specification – POLARSTEM Dimensions / Specification (Quelle polar-st, S. gedr. 15 / PDF 18)
| groesse | stem_length_I | stem_length_II | shoulder_1_AP | resection_2_ML | resection_2_AP | lateral_flair_3_L>C | flair_3_ML | flair_3_AP | mid_stem_4_ML | mid_stem_4_AP |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | 119.5 | 101.5 | 14.2 | 25.6 | 11.9 | 6.8 | 16.7 | 9.5 | 10.0 | 8.1 |
| 0 | 125.5 | 107.5 | 14.7 | 27.2 | 12.5 | 8.0 | 18.2 | 10.1 | 10.8 | 8.6 |
| 1 | 131.5 | 113.5 | 15.2 | 28.7 | 13.0 | 8.7 | 19.7 | 10.7 | 11.9 | 9.1 |
| 2 | 135.5 | 117.5 | 15.7 | 30.2 | 13.5 | 9.6 | 21.2 | 11.2 | 13.1 | 9.6 |
| 3 | 139.5 | 121.5 | 16.4 | 31.5 | 14.2 | 10.2 | 22.2 | 11.9 | 14.4 | 10.4 |
| 4 | 143.5 | 125.5 | 16.9 | 32.7 | 14.6 | 10.9 | 23.4 | 12.1 | 15.5 | 10.4 |
| 5 | 147.5 | 129.5 | 17.5 | 33.9 | 15.1 | 11.5 | 24.5 | 12.3 | 16.6 | 10.4 |
| 6 | 151.5 | 133.5 | 18.0 | 35.1 | 15.5 | 12.2 | 25.6 | 12.5 | 17.6 | 10.4 |
| 7 | 155.5 | 137.5 | 18.4 | 36.2 | 15.9 | 12.8 | 26.6 | 12.6 | 18.6 | 10.4 |
| 8 | 159.5 | 141.5 | 18.8 | 36.5 | 16.2 | 13.4 | 26.7 | 12.6 | 19.7 | 10.4 |
| 9 | 163.5 | 145.5 | 19.3 | 37.3 | 16.9 | 13.9 | 28.1 | 13.6 | 20.7 | 11.6 |
| 10 | 167.5 | 149.5 | 19.7 | 37.9 | 17.3 | 14.3 | 29.2 | 13.8 | 21.8 | 11.7 |
| 11 | 171.5 | 153.5 | 20.1 | 38.5 | 17.6 | 15.2 | 30.7 | 14.4 | 22.8 | 11.7 |
_Einheiten im Tabellenkopf nicht genannt; Tabelle trennt nicht nach Standard/Lateral/Valgus oder zementfrei/zementiert (so gedruckt). Belegt (Original, 1 Prüfer)._

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
| `sn.polarstem.zementfrei` | `sn.kopf.oxinium` | **bedingt** | Ø/Hals/Spalte laut T_matrix_polarstem: 26 mm nein; Größe „01“ nicht mit −3, −4, +16; Ø40/44 nur mit zugehöriger Ti-Hülse; Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementfrei` | `sn.kopf.cocr` | **bedingt** | wie OXINIUM laut T_matrix_polarstem (26 mm nein; „01“ nicht mit −3/−4/+16; Ø40/44 nur mit Ti-Hülse); Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementfrei` | `sn.kopf.biolox_delta` | **ja** | nur die gelisteten SAP-Gruppen beider Familien (765391/713460 und 750074) laut T_matrix_polarstem, alle Größen inkl. „01“; keine Interpolation; Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementfrei_kragen` | `sn.kopf.oxinium` | **bedingt** | Ø/Hals/Spalte laut T_matrix_polarstem: 26 mm nein; Größe „01“ nicht mit −3, −4, +16; Ø40/44 nur mit zugehöriger Ti-Hülse; Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementfrei_kragen` | `sn.kopf.cocr` | **bedingt** | wie OXINIUM laut T_matrix_polarstem (26 mm nein; „01“ nicht mit −3/−4/+16; Ø40/44 nur mit Ti-Hülse); Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementfrei_kragen` | `sn.kopf.biolox_delta` | **ja** | nur die gelisteten SAP-Gruppen beider Familien (765391/713460 und 750074) laut T_matrix_polarstem, alle Größen inkl. „01“; keine Interpolation; Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementiert` | `sn.kopf.oxinium` | **bedingt** | laut T_matrix_polarstem: Ø22–36 ja (inkl. −3/+16 bei 28/32, −3 bei 36); 26 mm nein; Ø40/44 nein; Markt-Vorbehalt | matrix | 1/7 |
| `sn.polarstem.zementiert` | `sn.kopf.cocr` | **nein** | alle CoCrMo-Zeilen in Spalte „Cemented“ rot (nicht freigegeben); dazu 01217-en gedr. 2 / PDF 5: Edelstahlschaft nur mit Edelstahlköpfen, Ausnahme OXINIUM und BIOLOX OPTION | matrix | 1/7 |
| `sn.polarstem.zementiert` | `sn.kopf.biolox_delta` | **ja** | nur die gelisteten SAP-Gruppen beider Familien laut T_matrix_polarstem; Markt-Vorbehalt | matrix | 1/7 |

## Regeln
- Kopf gegen die zutreffende Schaftspalte prüfen – auch Nein-Zeilen (z. B. Ø26 nicht mit SL-PLUS MIA; +16 nicht mit Größe 01). (matrix S. 2/6)
- OXINIUM/CoCr Ø40/44 nur mit der zugehörigen Ti-Hülse; keine Hülsen fremder Systeme. (matrix)
- TANDEM Bipolar mit SPECTRON EF: Innenkopf nur S+N OXINIUM/CoCr 12/14 Ø22/28; TANDEM Unipolar ist ein anderes Produkt. (tandem PDF 17, s3 S. 14)
- R3-XLPE-Innen-Ø nur in den Schalengrößen laut Grafik; Variante (0°/20°/+4) getrennt. (s4 S. 13)
- POLARSTEM: Kopf gegen die zutreffende Spalte prüfen – Größe „01“ (SAP 75100462/75018399) hat eigene Spalte: kein −3, −4, +16; Ø26 in allen Spalten nein; CoCrMo nie am zementierten POLARSTEM; OXINIUM/CoCrMo Ø40/44 nicht am zementierten POLARSTEM. (matrix S. 1/7)
- „Stainless steel (FeCrNiMoNbN) heads and stainless steel stems should only be used together. Neither should be used with other metal components. This limitation excludes OXINIUM™ and BIOLOX OPTION heads, which have been tested and approved in combination with cemented POLARSTEM™ made of stainless steel.“ (polar-st gedr. 2 / PDF 5)
- Köpfe nur mit Schäften identischer Konusdimension; Kombination mit Komponenten anderer Hersteller (z. B. Smith & Nephew Inc.) nur, wenn in Matrix 04758 (ifu.smith-nephew.com) gelistet. (polar-st gedr. 2 / PDF 5)

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
- POLARSTEM-Matrix 04758 Markt-Vorbehalt (wörtlich, S. 1/7): „The following matrix shows the compatibility of Femoral Ball Heads and Stems distributed by Smith & Nephew and used in Total Hip Arthroplasty. Each compatibility statement is based on the current evidence about the technical safety of the corresponding product combination. Combinations listed in the matrix may not be approved in all individual markets or geographies. The information contained in this matrix does not supersede the instructions for use (Package insert) in force in the markets where the products are being used. Please refer to your local Smith & Nephew representative to confirm the approval status in your country or region if you have questions about how Smith & Nephew products can be used.“
- „This compatibility matrix can only be accessed online via Smith & Nephew's website ifu.smith-nephew.com. It is the responsibility of the user to consult the Smith & Nephew website to ensure the currency of compatibility information.“ (Matrix 04758 S. 1/7)
- POLARSTEM: Größe „01“ ist als Text geführt und ≠ „0“; „x not available in the US“, „* outlier sizes (optional)“ (polar-st gedr. 13 / PDF 16). US-IFU 81098832 (polar-us) ist kein EU-Ersatz.

## Offen
- [ ] EU-IFUs (ifu.smith-nephew.com, REF nötig)
- [ ] REFLECTION zementfrei/All-Poly aktuelle EU-Unterlage; Müller-PE-Pfanne von S+N
- [ ] TANDEM Bipolar: Größen/REF; EU-Verfügbarkeit XLPE- vs. INTL-Variante
- [ ] GTIN
- [ ] POLARCUP (zementiert, EPRD #11) – bei Bedarf
- [ ] POLARSTEM: EU-IFU (ifu.smith-nephew.com) nicht gelesen; Kragen-Schäfte ohne Material-/CCD-/Konusangabe in der Tabelle; Maßwerte nicht nach Fixation/Kragen getrennt
- [ ] POLARSTEM: Matrix-Fußnote 2 nennt Typ „Medial“, der in 01217-en V7 nicht vorkommt – bei S+N klären

## Quellen
- **s1** SL-PLUS MIA INTEGRATION-PLUS – Surgical Technique · 00884-en (1524) V4, 01/15 · S. gedr. 16–19/PDF 18–21 (CCD S. 16, Implantate S. 18–19); Kennung PDF 28 · Markt: EN international · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true
- **matrix** Hip implant compatibility matrix – Stem and Femoral Ball Head Combinations · Lit. No. 04758, Ed. 05/26 V12 · S. S. 1/7 (POLARSTEM), 2/7 (SL-PLUS MIA), 6/7 (SPECTRON) · Markt: international mit lokalen Zulassungsvorbehalten · gelesen: Grok/Astra 07.10.2026; S. 1/7: Claude-Helfer 07.10.2026 (Original); OpenAI 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de
- **s3** SPECTRON EF – Surgical Technique · 21885 V3, 71380478 REVB 03/23, ©2023 · S. Specs gedr. 1/PDF 4; Katalog gedr. 12/PDF 15; TANDEM Unipolar gedr. 14/PDF 17; Kompatibilität gedr. 16/PDF 19; Kennung PDF 20 · Markt: EN · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true
- **s4** R3 Acetabulum-System – Operationstechnik · 7138-1560-de REVB 06/12, ©2017 · S. gedr.=PDF 13 Kombi-Grafik; 17–18 XLPE-Katalog; Kennung 32 · Markt: DE · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew-delivery.stylelabs.cloud/api/public/content/1bd7a20b4fdf4a158b95aad5987f2686?v=e321be27&download=true
- **tandem** TANDEM Bipolar and Unipolar Hip System – INTL Surgical Technique · 29073 V2, 71380925 REVA 02/23 · S. PDF 17 Implant Compatibility (unnummeriert); Kennung PDF 20 · Markt: INTL mit EU-Fußnoten · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/8af4fc46aafd4be4a8d289f62a72ee8e?download=true&v=bdf205cd
- **reflection** REFLECTION – Surgical Technique (historisch) · 00811 V1, 10/13, ©2013 · S. Titelblatt/Impressum · Markt: historische EN-Unterlage, kein aktueller EU-Nachweis · gelesen: Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/7cada363f2224bc3957ac5e0fde018ad?download=true&v=eca89761
- **slmia** SL-PLUS MIA Surgical Technique · 31156-en V2, 11/2024 · S. S. 17–18 / PDF 20–21; Warnungen S. 2 / PDF 5 · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/c38ee11595e14dfdbdd7ade71a170ac9?v=3e0dbffa&download=true
- **polar-us** POLARSTEM Non-Cemented and Cemented Stem System – Instructions for Use 81098832 · Rev. 2, 06/2021 · S. S. 1 (nur USA), S. 4, S. 2/5 · Markt: USA – kein EU-Ersatz (EU-Werte aus polar-st) · gelesen: Grok Lauf 001 (US-IFU) · https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283
- **polar-st** Surgical Technique – POLARSTEM™ Cementless and Cemented Stem System · 01217-en V7 10/24, ©2024 Smith & Nephew; CE 0123; Hersteller Smith & Nephew Orthopaedics AG, Zug · S. gedr. 2 / PDF 5 Kombinationsvorgaben; gedr. 13 / PDF 16 zementfrei + Collar; gedr. 14 / PDF 17 zementiert; gedr. 15 / PDF 18 Dimensions, Offset, Halslänge, Halshöhe; gedr. 16 / PDF 19 S/CT; Kennung PDF 28 (gedr. = PDF − 3) · Markt: EN mit CE 0123; keine allgemeine Marktangabe; Fußnote „x not available in the US“ an Größe 01 · gelesen: Claude-Helfer 07.10.2026 (Original); OpenAI 07.10.2026 · https://smith-nephew.stylelabs.cloud/api/public/content/d0db346865434eb18cfdd88134a43380?v=004c6504&download=true

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.
- **v1.2** (2026-10-07, 001-implantate-dach): POLARSTEM zementfrei/zementiert wieder aufgenommen (DACH-Regel; nur US-Fundstelle, EU offen); SL-PLUS MIA Längen I/II aus 31156-en V2; R3-Rückrufe R-2020-04/R-2023-13 = Schale (Liner-Zuordnung entfernt).
- **v1.3** (2026-10-07, 001-implantate-luecken): POLARSTEM aus EU-OP-Technik 01217-en V7 10/24 (CE 0123): zementfrei Standard 135° 01–11, Lateral 126° 1–11, Valgus 145° 0–7 mit SAP, Fußnoten und Maßwerten (Offset/Halslänge/Halshöhe/S/CT); neue Komponente sn.polarstem.zementfrei_kragen (Standard 01–11, Lateral 1–11, SAP); zementiert Standard 0–8, Lateral 1–8 mit SAP/Item; Tabelle T_matrix_polarstem (Matrix 04758 S. 1/7, inkl. Nein-Zeilen) + Spezifikationstabelle; passt_zu POLARSTEM × OXINIUM/CoCr/BIOLOX delta; bild-Schema je Komponente; US-IFU als kein EU-Ersatz belassen.

Bilder: keine übernommen – Rechte beim Hersteller.
