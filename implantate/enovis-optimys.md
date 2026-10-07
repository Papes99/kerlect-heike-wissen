# Enovis (Mathys) – optimys + RM Pressfit vitamys

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine EU-IFU gelesen; keine klinische Freigabe. Lauf 001-implantate-luecken (07.10.2026): Größen/REF/Kombinationen aus dem Mathys-e-IFU (OP-Techniken 2023-06/2023-07/2024-06, Gebrauchsanweisungen) von einem Claude-Helfer am Original gelesen; OpenAI konnte die Dokumente nicht öffnen (Fachkreis-Gate) – daher nur 1 Prüfer._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `enovis.optimys.schaft` | schaft | optimys | fixation: zementfrei (Kurzschaft); varianten: standard / lateral, je XS und 0–12; material: TiAl6V4 beschichtet mit TPS + CaP (S. 18) bzw. „Ti6AL4V + TPS / CaP“ (S. 24); konus: 12 / 14 mm; ccd: 135° für beide – standard / lateral; masse: Länge (L), Offset (O), Halslänge (N) in mm laut Kap. 4.1 (gedr./PDF 24); seite: REF gedr./PDF 18; Maße gedr./PDF 24; raspel_hinweis: „Für Implantate der Grössen kleiner 1 müssen zwingend die Raspeln XS und 0 verwendet werden.“ (gedr./PDF 26); indikation: „Primäre oder sekundäre Coxarthrose · Femurhalsfrakturen“ (gedr./PDF 5); e_ifu: XS und 0 (52.34.1165–1168) im e-IFU-REF-Index gelistet, obwohl XS in der OP-Technik als derzeit nicht verfügbar markiert ist | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.rm_pressfit_vitamys` | pfanne | RM Pressfit vitamys | fixation: zementfrei; bauart: Monoblock – kein separates modulares Inlay; material: Vitamin-E-stabilisiertes hochvernetztes Polyethylen (VEPE), TiCP-beschichtet, Ti6Al4V; seite: gedr./PDF 27 (gerendert geprüft); groessen_hinweis: 42–70; 28 mm ab 42, 32 mm ab 46, 36 mm ab 50 („–“ = keine REF); implantatwahl: „In Standardfällen wird ein Pfannenimplantat ausgewählt, dessen Grössenbezeichnung mit der des zuletzt verwendeten geradzahligen Fräsers übereinstimmt.“ (gedr./PDF 13); kopf_hinweis: Kopfdurchmesser bis 36 mm (gedr./PDF 4); Testkopf passend zum Innendurchmesser der Pfanne (gedr./PDF 21); e_ifu: e-IFU-Bezeichnung z. B. „RM Pressfit cup TiCP vitamys 50/36“ = 52.34.0066 | mx-rm-ot | belegt (Original, 1 Prüfer) |
| `enovis.rm_pressfit_ueberhoeht` | pfanne | RM Pressfit überhöht (vitamys) (RM Pressfit cup hooded) | fixation: zementfrei; bauart: Monoblock; material: Vitamin-E-stabilisiertes hochvernetztes Polyethylen (VEPE), TiCP-beschichtet, Ti6Al4V; seite: gedr./PDF 27 (gerendert geprüft); e_ifu: „RM Pressfit cup hooded“ | mx-rm-ot | belegt (Original, 1 Prüfer) |
| `enovis.rm_pressfit_uhmwpe` | pfanne | RM Pressfit UHMWPE | fixation: zementfrei; bauart: Monoblock; material: UHMWPE, Ti6Al4V, TiCP; seite: gedr./PDF 28; groessen_hinweis: 46–64; 32 mm erst ab 52 | mx-rm-ot | belegt (Original, 1 Prüfer) |
| `enovis.rm_schraube` | schraube | RM Spezialschraube Ø 4 mm | durchmesser_mm: 4; material: TiCP; seite: gedr./PDF 28; hinweis: „Um eine Beschädigung des Kugelkopfs beim Reponieren zu vermeiden, müssen die Schraubenköpfe vollständig in den Schraubenlöchern versenkt sein.“ (gedr./PDF 20); nicht_fuer: Pfannen mit „*“ (keine Schraubenlöcher) | mx-rm-ot | belegt (Original, 1 Prüfer) |
| `enovis.kopf.ceramys` | kopf | ceramys | material: ZrO2-AI2O3; konus: 12 / 14 mm; hinweis_original: Für die Keramik-Keramik-Paarung sind nur Keramik-Köpfe mit Keramik-Einsätzen der Firma Mathys zu verwenden. ceramys kann mit Mathys Polyethylenen und allen Mathys Keramiken kombiniert werden.; seite: optimys-OP-Technik gedr./PDF 19–21 (Kopftabellen; identisch mit twinSys-OP-Technik gedr./PDF 28–30); e_ifu: alle REF im Mathys-e-IFU-REF-Index gefunden (07.10.2026) | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.kopf.symarec` | kopf | symarec | material: AI2O3-ZrO2; konus: 12 / 14 mm; hinweis_original: Für die Keramik-Keramik-Paarung sind nur Keramik-Köpfe mit Keramik-Einsätzen der Firma Mathys zu verwenden. symarec kann mit Mathys Polyethylenen und allen Mathys Keramiken kombiniert werden.; seite: optimys-OP-Technik gedr./PDF 19–21 (Kopftabellen; identisch mit twinSys-OP-Technik gedr./PDF 28–30); e_ifu: alle REF im Mathys-e-IFU-REF-Index gefunden (07.10.2026) | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.kopf.ceramys_revision` | kopf | ceramys Revisionskopf | material: ZrO2-AI2O3, TiAI6V4; konus: 12 / 14 mm; hinweis_original: Die ceramys Revisionsköpfe können mit allen Mathys Schaftsystemen mit einem «12 / 14 Konus» verwendet werden. Die ceramys Revisionsköpfe können mit Pfannen oder Einsätzen aus Mathys Keramiken oder Mathys Polyethylenen kombiniert werden.; seite: optimys-OP-Technik gedr./PDF 19–21 (Kopftabellen; identisch mit twinSys-OP-Technik gedr./PDF 28–30); e_ifu: alle REF im Mathys-e-IFU-REF-Index gefunden (07.10.2026); geltungsbereich: nicht in Kopf-IFU Tab. 3/4 (Geltungsbereich dort: Stahl, CoCrMo, ceramys, symarec) | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.kopf.cocr` | kopf | Hüftkopf CoCrMo | material: CoCrMo; konus: 12 / 14 mm; hinweis_original: CoCrMo-Hüftköpfe dürfen nur mit Mathys Polyethylen-Pfannen oder -Einsätzen kombiniert werden.; seite: optimys-OP-Technik gedr./PDF 19–21 (Kopftabellen; identisch mit twinSys-OP-Technik gedr./PDF 28–30); e_ifu: alle REF im Mathys-e-IFU-REF-Index gefunden (07.10.2026) | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.kopf.stahl` | kopf | Hüftkopf Stahl | material: FeCrNiMnMoNbN; konus: 12 / 14 mm; hinweis_original: Stahl-Hüftköpfe dürfen nur mit Mathys Polyethylen-Pfannen oder -Einsätzen kombiniert werden.; seite: optimys-OP-Technik gedr./PDF 19–21 (Kopftabellen; identisch mit twinSys-OP-Technik gedr./PDF 28–30); e_ifu: alle REF im Mathys-e-IFU-REF-Index gefunden (07.10.2026) | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.hemikopf.stahl` | hemikopf | Hemikopf Stahl | material: FeCrNiMnMoNbN; konus: 12 / 14 mm; seite: optimys-OP-Technik gedr./PDF 23; Bipolar-/Hemi-OP-Technik gedr./PDF 14; halslaenge: nur S und M freigegeben (Bipolar-/Hemi-IFU Tab. 4); schaefte: CCA Stahl / CoCrMo, optimys, twinSys zementiert / unzementiert, stellaris (IFU Tab. 4); indikation: „Frakturen des Femurhalses“; Kontraindikation u. a. „Primäre oder sekundäre Arthrose der Hüfte“ (Bipolar-/Hemi-OP-Technik gedr./PDF 5); gedruckt: zwei Teiltabellen „Grössen 38 – 44 mm“ und „Grössen 46 – 58 mm“; e_ifu: z. B. „Hemihead SS 58 M“ = 67102 | mx-optimys-ot | belegt (Original, 1 Prüfer) |
| `enovis.ds_evolution` | pfanne | DS Evolution (Dual Mobility Pfanne von Mathys) | hinweis: nur als Ausschluss geführt: „Der optimys Schaft ist nicht mit der Dual Mobility Pfanne von Mathys (DS Evolution) kombinierbar.“ (gedr./PDF 17) | mx-optimys-ot | belegt (Original, 1 Prüfer) |

### Größen – optimys (Quelle mx-optimys-ot)
| variante | groesse | ref | laenge_mm | offset_mm | halslaenge_mm | ccd | verfuegbarkeit |
|---|---|---|---|---|---|---|---|
| standard | XS | 52.34.1165 | 77 | 28 | 27,5 | 135° | „* Derzeit nicht verfügbar“ (OP-Technik 2023-06); im e-IFU-REF-Index gelistet |
| standard | 0 | 52.34.1166 | 80 | 29 | 28,0 | 135° | – |
| standard | 1 | 52.34.0191 | 84 | 30 | 28,5 | 135° | – |
| standard | 2 | 52.34.0192 | 88 | 32 | 30,0 | 135° | – |
| standard | 3 | 52.34.0193 | 91 | 35 | 31,5 | 135° | – |
| standard | 4 | 52.34.0194 | 94 | 37 | 33,0 | 135° | – |
| standard | 5 | 52.34.0195 | 97 | 39 | 34,5 | 135° | – |
| standard | 6 | 52.34.0196 | 100 | 41 | 36,0 | 135° | – |
| standard | 7 | 52.34.0197 | 103 | 43 | 37,5 | 135° | – |
| standard | 8 | 52.34.0198 | 106 | 46 | 39,0 | 135° | – |
| standard | 9 | 52.34.0199 | 109 | 48 | 40,5 | 135° | – |
| standard | 10 | 52.34.0200 | 112 | 50 | 42,0 | 135° | – |
| standard | 11 | 52.34.0211 | 115 | 53 | 43,5 | 135° | – |
| standard | 12 | 52.34.0212 | 118 | 55 | 45,0 | 135° | – |
| lateral | XS | 52.34.1167 | 77 | 33 | 31,0 | 135° | „* Derzeit nicht verfügbar“ (OP-Technik 2023-06); im e-IFU-REF-Index gelistet |
| lateral | 0 | 52.34.1168 | 80 | 34 | 31,5 | 135° | – |
| lateral | 1 | 52.34.0201 | 84 | 35 | 32,0 | 135° | – |
| lateral | 2 | 52.34.0202 | 88 | 37 | 33,5 | 135° | – |
| lateral | 3 | 52.34.0203 | 91 | 40 | 35,0 | 135° | – |
| lateral | 4 | 52.34.0204 | 94 | 42 | 36,5 | 135° | – |
| lateral | 5 | 52.34.0205 | 97 | 44 | 38,0 | 135° | – |
| lateral | 6 | 52.34.0206 | 100 | 46 | 39,5 | 135° | – |
| lateral | 7 | 52.34.0207 | 103 | 48 | 41,0 | 135° | – |
| lateral | 8 | 52.34.0208 | 106 | 51 | 42,5 | 135° | – |
| lateral | 9 | 52.34.0209 | 109 | 53 | 44,0 | 135° | – |
| lateral | 10 | 52.34.0210 | 112 | 55 | 45,5 | 135° | – |
| lateral | 11 | 52.34.0221 | 115 | 58 | 47,0 | 135° | – |
| lateral | 12 | 52.34.0222 | 118 | 60 | 48,5 | 135° | – |

### Größen – RM Pressfit vitamys (Quelle mx-rm-ot)
| groesse | artikulation_mm | ref | schraubenloecher |
|---|---|---|---|
| 42 | 28 | 52.34.0029 | keine („* keine Schraubenlöcher“) |
| 44 | 28 | 52.34.0032 | keine („* keine Schraubenlöcher“) |
| 46 | 28 | 52.34.0033 | – |
| 48 | 28 | 52.34.0034 | – |
| 50 | 28 | 52.34.0035 | – |
| 52 | 28 | 52.34.0036 | – |
| 54 | 28 | 52.34.0037 | – |
| 56 | 28 | 52.34.0038 | – |
| 58 | 28 | 52.34.0039 | – |
| 60 | 28 | 52.34.0040 | – |
| 62 | 28 | 52.34.0041 | – |
| 64 | 28 | 52.34.0042 | – |
| 66 | 28 | 52.34.0043 | – |
| 68 | 28 | 52.34.0044 | – |
| 70 | 28 | 52.34.0045 | – |
| 46 | 32 | 52.34.0049 | keine („* keine Schraubenlöcher“) |
| 48 | 32 | 52.34.0052 | – |
| 50 | 32 | 52.34.0053 | – |
| 52 | 32 | 52.34.0054 | – |
| 54 | 32 | 52.34.0055 | – |
| 56 | 32 | 52.34.0056 | – |
| 58 | 32 | 52.34.0057 | – |
| 60 | 32 | 52.34.0058 | – |
| 62 | 32 | 52.34.0059 | – |
| 64 | 32 | 52.34.0060 | – |
| 66 | 32 | 52.34.0061 | – |
| 68 | 32 | 52.34.0062 | – |
| 70 | 32 | 52.34.0063 | – |
| 50 | 36 | 52.34.0066 | keine („* keine Schraubenlöcher“) |
| 52 | 36 | 52.34.0067 | – |
| 54 | 36 | 52.34.0068 | – |
| 56 | 36 | 52.34.0069 | – |
| 58 | 36 | 52.34.0070 | – |
| 60 | 36 | 52.34.0071 | – |
| 62 | 36 | 52.34.0072 | – |
| 64 | 36 | 52.34.0073 | – |
| 66 | 36 | 52.34.0074 | – |
| 68 | 36 | 52.34.0075 | – |
| 70 | 36 | 52.34.0076 | – |

### Größen – RM Pressfit überhöht (vitamys) (Quelle mx-rm-ot)
| groesse | artikulation_mm | ref | schraubenloecher |
|---|---|---|---|
| 42 | 28 | 52.34.1222 | keine („* keine Schraubenlöcher“) |
| 44 | 28 | 52.34.1223 | keine („* keine Schraubenlöcher“) |
| 46 | 28 | 52.34.1224 | – |
| 48 | 28 | 52.34.1225 | – |
| 50 | 28 | 52.34.1226 | – |
| 52 | 28 | 52.34.1227 | – |
| 54 | 28 | 52.34.1228 | – |
| 56 | 28 | 52.34.1229 | – |
| 58 | 28 | 52.34.1230 | – |
| 60 | 28 | 52.34.1231 | – |
| 62 | 28 | 52.34.1232 | – |
| 64 | 28 | 52.34.1233 | – |
| 66 | 28 | 52.34.1234 | – |
| 68 | 28 | 52.34.1235 | – |
| 70 | 28 | 52.34.1236 | – |
| 46 | 32 | 52.34.1237 | keine („* keine Schraubenlöcher“) |
| 48 | 32 | 52.34.1238 | – |
| 50 | 32 | 52.34.1239 | – |
| 52 | 32 | 52.34.1240 | – |
| 54 | 32 | 52.34.1241 | – |
| 56 | 32 | 52.34.1242 | – |
| 58 | 32 | 52.34.1243 | – |
| 60 | 32 | 52.34.1244 | – |
| 62 | 32 | 52.34.1245 | – |
| 64 | 32 | 52.34.1246 | – |
| 66 | 32 | 52.34.1247 | – |
| 68 | 32 | 52.34.1248 | – |
| 70 | 32 | 52.34.1249 | – |
| 50 | 36 | 52.34.1250 | keine („* keine Schraubenlöcher“) |
| 52 | 36 | 52.34.1251 | – |
| 54 | 36 | 52.34.1252 | – |
| 56 | 36 | 52.34.1253 | – |
| 58 | 36 | 52.34.1254 | – |
| 60 | 36 | 52.34.1255 | – |
| 62 | 36 | 52.34.1256 | – |
| 64 | 36 | 52.34.1257 | – |
| 66 | 36 | 52.34.1258 | – |
| 68 | 36 | 52.34.1259 | – |
| 70 | 36 | 52.34.1260 | – |

### Größen – RM Pressfit UHMWPE (Quelle mx-rm-ot)
| groesse | artikulation_mm | ref |
|---|---|---|
| 46 | 28 | 55.22.1046 |
| 48 | 28 | 55.22.1048 |
| 50 | 28 | 55.22.1050 |
| 52 | 28 | 55.22.1052 |
| 54 | 28 | 55.22.1054 |
| 56 | 28 | 55.22.1056 |
| 58 | 28 | 55.22.1058 |
| 60 | 28 | 55.22.1060 |
| 62 | 28 | 55.22.1062 |
| 64 | 28 | 55.22.1064 |
| 52 | 32 | 55.22.3252 |
| 54 | 32 | 55.22.3254 |
| 56 | 32 | 55.22.3256 |
| 58 | 32 | 55.22.3258 |
| 60 | 32 | 55.22.3260 |
| 62 | 32 | 55.22.3262 |
| 64 | 32 | 55.22.3264 |

### Größen – RM Spezialschraube Ø 4 mm (Quelle mx-rm-ot)
| laenge_mm | variante | ref |
|---|---|---|
| 22 | steril | 4.14.015S |
| 22 | unsteril | 4.14.015 |
| 24 | steril | 4.14.014S |
| 24 | unsteril | 4.14.014 |
| 26 | steril | 4.14.013S |
| 26 | unsteril | 4.14.013 |
| 28 | steril | 4.14.000S |
| 28 | unsteril | 4.14.000 |
| 32 | steril | 4.14.001S |
| 32 | unsteril | 4.14.001 |
| 34 | steril | 4.14.002S |
| 34 | unsteril | 4.14.002 |
| 36 | steril | 4.14.003S |
| 36 | unsteril | 4.14.003 |
| 38 | steril | 4.14.004S |
| 38 | unsteril | 4.14.004 |
| 40 | steril | 4.14.005S |
| 40 | unsteril | 4.14.005 |
| 44 | steril | 4.14.006S |
| 44 | unsteril | 4.14.006 |
| 48 | steril | 4.14.007S |
| 48 | unsteril | 4.14.007 |
| 52 | steril | 4.14.008S |
| 52 | unsteril | 4.14.008 |

### Größen – ceramys (Quelle mx-optimys-ot)
| durchmesser_mm | halslaenge | ref |
|---|---|---|
| 28 | S - 3,5 mm | 54.47.0010 |
| 28 | M 0 mm | 54.47.0011 |
| 28 | L + 3,5 mm | 54.47.0012 |
| 32 | S - 4 mm | 54.47.0110 |
| 32 | M 0 mm | 54.47.0111 |
| 32 | L + 4 mm | 54.47.0112 |
| 32 | XL + 8 mm | 54.47.0113 |
| 36 | S - 4 mm | 54.47.0210 |
| 36 | M 0 mm | 54.47.0211 |
| 36 | L + 4 mm | 54.47.0212 |
| 36 | XL + 8 mm | 54.47.0213 |

### Größen – symarec (Quelle mx-optimys-ot)
| durchmesser_mm | halslaenge | ref |
|---|---|---|
| 28 | S - 3,5 mm | 54.48.0010 |
| 28 | M 0 mm | 54.48.0011 |
| 28 | L + 3,5 mm | 54.48.0012 |
| 32 | S - 4 mm | 54.48.0110 |
| 32 | M 0 mm | 54.48.0111 |
| 32 | L + 4 mm | 54.48.0112 |
| 32 | XL + 8 mm | 54.48.0113 |
| 36 | S - 4 mm | 54.48.0210 |
| 36 | M 0 mm | 54.48.0211 |
| 36 | L + 4 mm | 54.48.0212 |
| 36 | XL + 8 mm | 54.48.0213 |

### Größen – ceramys Revisionskopf (Quelle mx-optimys-ot)
| durchmesser_mm | halslaenge | ref |
|---|---|---|
| 28 | S - 3,5 mm | 54.47.2010 |
| 28 | M 0 mm | 54.47.2020 |
| 28 | L + 3,5 mm | 54.47.2030 |
| 28 | XL + 7 mm | 54.47.2040 |
| 32 | S - 3,5 mm | 54.47.2110 |
| 32 | M 0 mm | 54.47.2120 |
| 32 | L + 3,5 mm | 54.47.2130 |
| 32 | XL + 7 mm | 54.47.2140 |
| 36 | S - 3,5 mm | 54.47.2210 |
| 36 | M 0 mm | 54.47.2220 |
| 36 | L + 3,5 mm | 54.47.2230 |
| 36 | XL + 7 mm | 54.47.2240 |

### Größen – Hüftkopf CoCrMo (Quelle mx-optimys-ot)
| durchmesser_mm | halslaenge | ref |
|---|---|---|
| 22,2 | S - 3 mm | 52.34.0125 |
| 22,2 | M 0 mm | 52.34.0126 |
| 22,2 | L + 3 mm | 52.34.0127 |
| 28 | S - 4 mm | 2.30.010 |
| 28 | M 0 mm | 2.30.011 |
| 28 | L + 4 mm | 2.30.012 |
| 28 | XL + 8 mm | 2.30.013 |
| 28 | XXL +12 mm | 2.30.014 |
| 32 | S - 4 mm | 2.30.020 |
| 32 | M 0 mm | 2.30.021 |
| 32 | L + 4 mm | 2.30.022 |
| 32 | XL + 8 mm | 2.30.023 |
| 32 | XXL +12 mm | 2.30.024 |
| 36 | S - 4 mm | 52.34.0686 |
| 36 | M 0 mm | 52.34.0687 |
| 36 | L + 4 mm | 52.34.0688 |
| 36 | XL + 8 mm | 52.34.0689 |
| 36 | XXL + 12 mm | 52.34.0690 |

### Größen – Hüftkopf Stahl (Quelle mx-optimys-ot)
| durchmesser_mm | halslaenge | ref |
|---|---|---|
| 22,2 | S - 3 mm | 54.11.1031 |
| 22,2 | M 0 mm | 54.11.1032 |
| 22,2 | L + 3 mm | 54.11.1033 |
| 28 | S - 4 mm | 2.30.410 |
| 28 | M 0 mm | 2.30.411 |
| 28 | L + 4 mm | 2.30.412 |
| 28 | XL + 8 mm | 2.30.413 |
| 28 | XXL + 12 mm | 2.30.414 |
| 32 | S - 4 mm | 2.30.400 |
| 32 | M 0 mm | 2.30.401 |
| 32 | L + 4 mm | 2.30.402 |
| 32 | XL + 8 mm | 2.30.403 |
| 32 | XXL + 12 mm | 2.30.404 |

### Größen – Hemikopf Stahl (Quelle mx-optimys-ot)
| aussen_mm | halslaenge | ref |
|---|---|---|
| 38 | S - 4 mm | 2.30.420 |
| 38 | M 0 mm | 67092 |
| 40 | S - 4 mm | 2.30.421 |
| 40 | M 0 mm | 67093 |
| 42 | S - 4 mm | 2.30.422 |
| 42 | M 0 mm | 67094 |
| 44 | S - 4 mm | 2.30.423 |
| 44 | M 0 mm | 67095 |
| 46 | S - 4 mm | 2.30.424 |
| 46 | M 0 mm | 67096 |
| 48 | S - 4 mm | 2.30.425 |
| 48 | M 0 mm | 67097 |
| 50 | S - 4 mm | 2.30.426 |
| 50 | M 0 mm | 67098 |
| 52 | S - 4 mm | 2.30.427 |
| 52 | M 0 mm | 67099 |
| 54 | S - 4 mm | 2.30.428 |
| 54 | M 0 mm | 67100 |
| 56 | S - 4 mm | 2.30.429 |
| 56 | M 0 mm | 67101 |
| 58 | S - 4 mm | 2.30.430 |
| 58 | M 0 mm | 67102 |

### T3_kopf_pfanne – Tabelle 3: Kombination von Keramik-Hüftköpfen (ceramys / symarec) oder Metall-Hüftköpfen (Stahl / CoCrMo) mit den entsprechenden Pfannen oder Inlays – Spalten RM Pressfit (Quelle mx-heads-ifu, S. 5 (gerendert geprüft))
| produkt | groesse_mm | halslaenge | rm_pressfit_vitamys_ueberhoeht | rm_pressfit_uhmwpe |
|---|---|---|---|---|
| Keramik-Hüftkopf ceramys | 28 | S, M, L | ja | ja |
| Keramik-Hüftkopf ceramys | 32 | S, M, L, XL | ja | ja |
| Keramik-Hüftkopf ceramys | 36 | S, M, L, XL | ja | nein |
| Keramik-Hüftkopf symarec | 28 | S, M, L | ja | ja |
| Keramik-Hüftkopf symarec | 32 | S, M, L, XL | ja | ja |
| Keramik-Hüftkopf symarec | 36 | S, M, L, XL | ja | nein |
| Metall-Hüftkopf Stahl | 22,2 | S, M, L | nein | nein |
| Metall-Hüftkopf Stahl | 28 | S, M, L, XL, XXL | ja | ja |
| Metall-Hüftkopf Stahl | 32 | S, M, L, XL, XXL | ja | ja |
| Metall-Hüftkopf CoCrMo | 22,2 | S, M, L | nein | nein |
| Metall-Hüftkopf CoCrMo | 28 | S, M, L, XL, XXL | ja | ja |
| Metall-Hüftkopf CoCrMo | 32 | S, M, L, XL, XXL | ja | ja |
| Metall-Hüftkopf CoCrMo | 36 | S, M, L, XL, XXL | ja | nein |
_Kopf-IFU Abschnitt 8: „Eine Kombination ist nicht zulässig, wenn dies mit «nein» gekennzeichnet ist. Eine Kombination mit einem Produkt, das nicht aufgeführt ist, ist nicht zulässig.“ Nur die Spalten der Pfannen/Inlays dieser Datei; übrige Spalten der Originaltabelle: CCB, RM Classic (Vollprofil/angeschrägt/Revision), aneXys vitamys/ceramys, seleXys UHMWPE (siehe enovis-twinsys bzw. nicht erfasst)._

### T4_kopf_schaft – Tabelle 4: Kombination von Keramik-Hüftköpfen (ceramys / symarec) oder Metall-Hüftköpfen (Stahl / CoCrMo) mit den entsprechenden Hüftschäften oder Bipolarköpfen Stahl – Spalte optimys (Quelle mx-heads-ifu, S. 6 (bei 150 dpi gerendert geprüft))
| produkt | groesse_mm | halslaenge | optimys |
|---|---|---|---|
| Keramik-Hüftkopf ceramys | 28 | S, M, L | ja |
| Keramik-Hüftkopf ceramys | 32 | S, M, L, XL | ja |
| Keramik-Hüftkopf ceramys | 36 | S, M, L, XL | ja |
| Keramik-Hüftkopf symarec | 28 | S, M, L | ja |
| Keramik-Hüftkopf symarec | 32 | S, M, L, XL | ja |
| Keramik-Hüftkopf symarec | 36 | S, M, L, XL | ja |
| Metall-Hüftkopf CoCrMo | 22,2 | S, M, L | ja |
| Metall-Hüftkopf CoCrMo | 28 | S, M, L, XL, XXL | ja |
| Metall-Hüftkopf CoCrMo | 32 | S, M, L, XL, XXL | ja |
| Metall-Hüftkopf CoCrMo | 36 | S, M, L, XL, XXL | ja |
_Auffälligkeit im Original: Die Überschrift nennt Metall-Hüftköpfe Stahl, die Tabelle enthält aber keine Stahl-Zeilen – daraus nichts abgeleitet. ceramys-Revisionsköpfe sind nicht Teil dieser Tabelle. Nur die Spalten dieser Datei; übrige Spalten: CCA Stahl / CoCrMo, twinSys, stellaris, Bipolarkopf Stahl (Bipolar siehe enovis-twinsys)._

### T4_hemi_schaft – Bipolar-/Hemi-IFU Tabelle 4: Kombination von Hemiköpfen Stahl mit entsprechenden Hüftschäften – Spalte optimys (Quelle mx-bh-ifu, S. 5 (gerendert geprüft))
| produkt | groesse_mm | halslaenge | optimys |
|---|---|---|---|
| Hemikopf Stahl | 38 – 58 | S, M | ja |
_übrige Spalten im Original: CCA Stahl / CoCrMo, twinSys zementiert / unzementiert, stellaris (alle ja)._

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `enovis.optimys.schaft` | `enovis.kopf.ceramys` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Halslängen je Zeile laut Tabelle; optimys-OP-Technik S. 10: „mit sämtlichen Mathys Kugelköpfen in allen Halslängen“ | mx-heads-ifu | 6 |
| `enovis.optimys.schaft` | `enovis.kopf.symarec` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Halslängen je Zeile laut Tabelle; optimys-OP-Technik S. 10: „mit sämtlichen Mathys Kugelköpfen in allen Halslängen“ | mx-heads-ifu | 6 |
| `enovis.optimys.schaft` | `enovis.kopf.cocr` | **ja** | Kopf-Ø 22,2, 28, 32, 36 mm laut Tabelle ja; Halslängen je Zeile laut Tabelle; optimys-OP-Technik S. 10: „mit sämtlichen Mathys Kugelköpfen in allen Halslängen“ | mx-heads-ifu | 6 |
| `enovis.optimys.schaft` | `enovis.kopf.stahl` | **bedingt** | optimys-IFU Abb. 1 nennt „Hüftköpfe Metall – Edelstahl, CoCrMo“ als getestete/zugelassene Kombination (Abschnitt 8), ohne Größen; Kopf-IFU Tab. 4 hat trotz Überschrift keine Stahl-Zeilen – Größen offen | mx-optimys-ifu | 4 (Abb. 1) |
| `enovis.optimys.schaft` | `enovis.kopf.ceramys_revision` | **ja** | optimys-IFU Abb. 1 „ceramys Revisionskopf“; OP-Technik: Revisionsköpfe mit allen Mathys-Schaftsystemen mit 12/14-Konus; nicht in Kopf-IFU Tab. 4 | mx-optimys-ifu | 4 (Abb. 1); OP-Technik gedr./PDF 21 |
| `enovis.optimys.schaft` | `enovis.hemikopf.stahl` | **bedingt** | nur Halslänge S und M; Hemikopf 38–58 mm (Indikation Femurhalsfraktur) | mx-bh-ifu | 5 |
| `enovis.optimys.schaft` | `enovis.ds_evolution` | **nein** | „Der optimys Schaft ist nicht mit der Dual Mobility Pfanne von Mathys (DS Evolution) kombinierbar.“ | mx-optimys-ot | 17 |
| `enovis.kopf.ceramys` | `enovis.rm_pressfit_vitamys` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.symarec` | `enovis.rm_pressfit_vitamys` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.stahl` | `enovis.rm_pressfit_vitamys` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 22,2 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.cocr` | `enovis.rm_pressfit_vitamys` | **bedingt** | nur Kopf-Ø 28, 32, 36 mm (ja); Kopf-Ø 22,2 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.ceramys` | `enovis.rm_pressfit_ueberhoeht` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.symarec` | `enovis.rm_pressfit_ueberhoeht` | **ja** | Kopf-Ø 28, 32, 36 mm laut Tabelle ja; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.stahl` | `enovis.rm_pressfit_ueberhoeht` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 22,2 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.cocr` | `enovis.rm_pressfit_ueberhoeht` | **bedingt** | nur Kopf-Ø 28, 32, 36 mm (ja); Kopf-Ø 22,2 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 27) | mx-heads-ifu | 5 |
| `enovis.kopf.ceramys` | `enovis.rm_pressfit_uhmwpe` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 36 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 28) | mx-heads-ifu | 5 |
| `enovis.kopf.symarec` | `enovis.rm_pressfit_uhmwpe` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 36 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 28) | mx-heads-ifu | 5 |
| `enovis.kopf.stahl` | `enovis.rm_pressfit_uhmwpe` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 22,2 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 28) | mx-heads-ifu | 5 |
| `enovis.kopf.cocr` | `enovis.rm_pressfit_uhmwpe` | **bedingt** | nur Kopf-Ø 28, 32 mm (ja); Kopf-Ø 22,2, 36 mm: nein; Kopf-Ø muss der Artikulation der Pfanne entsprechen (REF-Tabelle gedr./PDF 28) | mx-heads-ifu | 5 |
| `enovis.kopf.ceramys_revision` | `enovis.rm_pressfit_vitamys` | **ja** | RM-Pressfit-vitamys-IFU Abb. 1 nennt „ceramys Revisionskopf“; Kopf-Ø = Artikulation der Pfanne | mx-rmv-ifu | 3 (Abb. 1) |
| `enovis.kopf.ceramys_revision` | `enovis.rm_pressfit_ueberhoeht` | **offen** | nur allgemeiner OP-Technik-Text (Revisionsköpfe mit Mathys Polyethylenen kombinierbar); keine Tabellenzeile, Revisionskopf nicht im Geltungsbereich der Kopf-IFU Tab. 3 | mx-optimys-ot | 21 |
| `enovis.kopf.ceramys_revision` | `enovis.rm_pressfit_uhmwpe` | **offen** | nur allgemeiner OP-Technik-Text (Revisionsköpfe mit Mathys Polyethylenen kombinierbar); keine Tabellenzeile, Revisionskopf nicht im Geltungsbereich der Kopf-IFU Tab. 3 | mx-optimys-ot | 21 |
| `enovis.rm_pressfit_vitamys` | `enovis.rm_schraube` | **bedingt** | nur Pfannen mit Schraubenlöchern (nicht „*“); Schraubenköpfe vollständig versenken | mx-rm-ot | 20, 27–28 |
| `enovis.rm_pressfit_ueberhoeht` | `enovis.rm_schraube` | **bedingt** | nur Pfannen mit Schraubenlöchern (nicht „*“); Schraubenköpfe vollständig versenken | mx-rm-ot | 20, 27–28 |

## Regeln
- RM Pressfit vitamys ist Monoblock – kein Inlay anbieten. (rm)
- seleXys TH+/TPS nicht in die Auswahl (historische TGA-Warnung 2015, Australien; seleXys PC nicht betroffen). (TGA 16.09.2015)
- Der endgültige Kopfdurchmesser muss zum Innendurchmesser der Pfanne passen; erlaubte Kopf-Ø je Pfanne laut Kopf-IFU Tab. 3 (RM Pressfit UHMWPE: kein 36). (mx-optimys-ot S. 17; mx-heads-ifu Tab. 3)
- Stahl- und CoCrMo-Hüftköpfe nur mit Mathys Polyethylen-Pfannen oder -Einsätzen; kein Metallkopf mit Keramik-Inlay. (mx-optimys-ot S. 19; mx-heads-ifu Kap. 4.3)
- Keramikköpfe nur auf neuen und unbeschädigten Schaftkonen; keine Montage auf zuvor verwendetem Konus. (mx-heads-ifu Kap. 4.3)
- optimys nicht mit der Dual-Mobility-Pfanne DS Evolution kombinieren. (mx-optimys-ot S. 17)
- Hemikopf Stahl nur mit Halslänge S oder M (freigegeben für CCA, optimys, twinSys, stellaris). (mx-bh-ifu Tab. 4)
- „Mathys AG Bettlach empfiehlt dringend, ihre Produkte nicht mit Implantatsystemen anderer Hersteller zu kombinieren.“ (mx-heads-ifu S. 6)
- Für Implantate der Größen kleiner 1 zwingend die Raspeln XS und 0 verwenden; XS laut OP-Technik 2023-06 derzeit nicht verfügbar. (mx-optimys-ot S. 18, 26)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| optimys lateral TAV Gr. 7 unzementiert (REF 52.34.0207, Lot 2240248) – Siegelnaht | BfArM | FSCA 17/02 (07038-17), 18.07.2017 | EU/DE | – | nur diese Charge | `enovis.optimys.schaft` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07038-17_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.
- Mathys-Werte (Lauf 001-implantate-luecken) aus dem öffentlichen Mathys-e-IFU-Portal ifu.mathysmedical.com (aktuelle DE-OP-Techniken/IFUs) – nur ein Prüfer am Original.

## Offen
- [ ] optimys XS: OP-Technik 2023-06 „derzeit nicht verfügbar“, aber im e-IFU-REF-Index gelistet – Lieferbarkeit beim Hersteller klären
- [ ] Stahl-Köpfe × optimys: Kopf-IFU Tab. 4 nennt Stahl in der Überschrift, hat aber keine Stahl-Zeilen; optimys-IFU Abb. 1 nennt Edelstahl ohne Größen
- [ ] ceramys-Revisionskopf × RM Pressfit überhöht / UHMWPE: keine Tabellenzeile
- [ ] Duokopf: Bipolarkopf siehe enovis-twinsys (optimys-IFU Abb. 1 zeigt keinen Bipolarkopf)
- [ ] Packungs-/Etikettbilder: in keinem gelesenen Mathys-Dokument abgebildet
- [ ] Zweitprüfung der Mathys-Werte (OpenAI kam nicht an die Dokumente – Fachkreis-Gate)
- [ ] GTIN/UDI-DI

## Quellen
- **optimys** Enovis optimys – Produktseite · undatiert, Abruf 07.10.2026 · S. Product details · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/en/products/325/optimys.html
- **rm** RM Pressfit vitamys – Product Information · 336.010.121 03-0123-01, 2023-01 · S. PDF 2–5 (Monoblock) · Markt: EN/international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4724/file/produktinformation_rm-pressfit_en_v3.0.pdf
- **heads** Mathys Ceramic Product Information · 336.010.127 03-0319-01, 2019-03 · S. PDF 2–3 · Markt: international; keine Schaftmatrix · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf
- **optimys-ot** optimys Operationstechnik (DE) · Art. 316.010.109, 04-0920 (V04), 09/2020 · S. Implantate S. 18; Dimensionen S. 24 · Markt: EU/CH · gelesen: Perplexity-Fundstelle – alter Link leitet laut Astra um; ersetzt durch mx-optimys-ot (aktuelle Fassung 2023-06, am Original gelesen) · https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_optimys_DE_V04.pdf
- **mx-optimys-ot** Mathys OPERATIONSTECHNIK optimys (DE) · Art. Nr. 316.010.109 · 05-0623-01 · 2023-06; e-IFU valid_from 28.06.2023, Version 1 (Versions-ID c46d0e57-851e-4903-9836-6fd1fd85ba61) · S. gedr.=PDF 4, 5, 10, 15, 17 Hinweise; 18 Schäfte REF; 19–23 Köpfe/Bipolar/Hemi; 24 Dimensionen (Kap. 4.1); 26 Instrumente; Kennung 32 · Markt: Mathys-e-IFU, 33 Länder (AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IS, IE, IT, LV, LI, LT, LU, MT, NL, NO, PL, PT, RO, RS, SK, SI, ES, SE, CH, GB) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/0550a5ee-9284-42e3-ac10-6c36d5934f2c
- **mx-optimys-ifu** Mathys Gebrauchsanweisung optimys (DE) · Art. Nr. 78855 · 01-0623-DV · 2023-06 (Versions-ID e18170a3-1d70-40e4-be27-565d249da283) · S. S. 4 Abb. 1 „Übersicht über mögliche Kombinationen“; Abschnitt 8; Kap. 9 Verpackung · Markt: Mathys-e-IFU (inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/0550a5ee-9284-42e3-ac10-6c36d5934f2c
- **mx-rm-ot** Mathys OPERATIONSTECHNIK RM Pressfit (DE; deckt RM Pressfit und RM Pressfit vitamys ab) · Art. Nr. 316.010.164 · 02-0723-01 · 2023-07; e-IFU Version 2, valid_from 03.07.2023 (Versions-ID 89b2c1bd-1dbb-48ae-8e09-07ebb21b056b) · S. gedr.=PDF 4, 13, 20, 21 Hinweise; 27 Pfannen-REF vitamys/überhöht; 28 UHMWPE-Pfanne und Schrauben; Kennung 44 · Markt: Mathys-e-IFU (inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/fbbaeda3-d2e7-4214-8e79-f317a0032bc4
- **mx-rmv-ifu** Mathys Gebrauchsanweisung RM Pressfit vitamys (DE) · Art. Nr. 78691 · 01-1122-DV · 2022-11; e-IFU valid_from 05.12.2022 (Versions-ID 5fbff2c6-dad8-472a-b4c9-010ba06c56e3) · S. S. 3 Abb. 1 „Mögliche Kombinationen der RM Pressfit vitamys Pfannen“ · Markt: Mathys-e-IFU (inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/fbbaeda3-d2e7-4214-8e79-f317a0032bc4
- **mx-heads-ifu** Mathys E-LEAFLET Gebrauchsanweisung Hüftköpfe (DE) – Kombinationstabellen 3 und 4 · Art. Nr. 79490 · 01-0624-DV · 2024-06; e-IFU valid_from 25.06.2024 (Versions-ID 939a531f-7148-4db1-b652-94b0ad599c1f) · S. S. 1 Symbole; Kap. 4.3 Kontraindikationen; Abschnitt 8 S. 4–6; Tab. 3 S. 5; Tab. 4 S. 6 · Markt: Mathys-e-IFU (EU-Länderliste inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/cce16579-f64e-4ea0-93a0-1fc8044b1822
- **mx-bh-ot** Mathys OPERATIONSTECHNIK Bipolar- und Hemiköpfe (DE) · Art. Nr. 316.010.147 · 02-0624-01 · 2024-06; e-IFU valid_from 11.06.2024 (Versions-ID b7c49293-6abc-4f3d-9996-0e4a46702a12) · S. gedr.=PDF 5 Indikation; 7–8 Hinweise; 11 Bipolarkopf Stahl; 12–13 Innenköpfe; 14 Hemikopf; 15–16 Instrumente; Kennung 20 · Markt: Mathys-e-IFU (inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/cce16579-f64e-4ea0-93a0-1fc8044b1822
- **mx-bh-ifu** Mathys Gebrauchsanweisung Bipolarköpfe und Hemiköpfe (DE) · Art. Nr. 79437 · 01-0624-DV · 2024-06 (Erste Fassung 2024-06); e-IFU valid_from 06.06.2024 (Versions-ID 2c832159-c028-4eb7-9249-3687e7cbee3c) · S. Tab. 1–2; Tab. 4 Hemikopf × Schaft, Tab. 5/6 Bipolarkopf × Innenkopf (S. 5); Kap. 12 Patientenetiketten · Markt: Mathys-e-IFU (inkl. DE/AT/CH) · gelesen: Claude-Helfer 07.10.2026 (Original) · https://ifu.mathysmedical.com/products/cce16579-f64e-4ea0-93a0-1fc8044b1822

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.
- **v1.1** (2026-10-07, 001-implantate-luecken): Mathys-e-IFU (DE): optimys standard/lateral XS–12 mit REF, Länge/Offset/Halslänge, CCD 135°, 12/14, XS „derzeit nicht verfügbar“, Ausschluss DS Evolution; RM Pressfit vitamys/überhöht 42–70 × 28/32/36 und UHMWPE 46–64 mit REF, Schrauben Ø 4; Hüftköpfe Stahl/CoCrMo/ceramys/symarec/ceramys-Revision mit REF; Hemikopf Stahl 38–58 (S/M); Kopf-IFU Tab. 3/4 und Hemi-Tab. 4 als tabellen + passt_zu (nur optimys/RM Pressfit).

Bilder: keine übernommen – Rechte beim Hersteller.
