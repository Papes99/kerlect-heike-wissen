# DePuy Synthes (Johnson & Johnson MedTech) – CORAIL (zementfrei/zementiert) + PINNACLE

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine EU-IFU gelesen; keine klinische Freigabe. Lauf 001-implantate-luecken (07.10.2026): CORAIL-Bestell-REF vom Claude-Helfer am Original gelesen und von OpenAI gegengeprüft, Maßtabellen 1 Prüfer; ARTICUL/EZE-Köpfe nur aus US-GUDID (kein EU-Nachweis); PINNACLE-Trialdaten bewusst nicht übernommen._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `depuy.corail.zementfrei` | schaft | CORAIL zementfrei (HA) – STD 135°, KHO 135°, KLA 125°, STD 125°, SN 135° | fixation: zementfrei; konus: 12/14 ARTICUL/EZE Mini Taper (AMT); „A DePuy Synthes 12/14 head must be used.“ (gedr. 9 / 19); uebersicht: STD 135° Sz 8-20 · KHO 135° Sz 9-20 · SN 135° Sz 8-14 · STD 125° Sz 8-14 · KLA 125° Sz 9-20 (gedr. 21; Pfeile High/Low −5, SN↔STD125 −5, STD125↔KLA +7); masse_spalten: A Neck Shaft Angle, B Stem Length (längere Strecke), C Stem Length (kürzere Strecke), D Offset, E Neck Length, F Neck height, G Width – B/C beide „Stem Length (mm)“, nur durch Skizze unterschieden; hinweis: STD125/SN135 ohne Kragen nur 8–10 (Maße 7–10); nicht aus anderen Familien ableiten. Keine Größe 17/19.; widersprueche: Gr. 7 (STD 125°, SN 135°) Maße ohne REF; KHO 18/20 ohne vs. mit Kragen unterschiedliche Offset/Neck height; KLA Maßtabelle ohne Kragenangabe; corail_amt: Produktcodes für CORAIL AMT laut gedr. 27 in „CORAIL Upgrade Surgical Technique“ 096172-181205 (nicht geprüft) | corail | REF belegt (Original, 2 Prüfer); Maße belegt (Original, 1 Prüfer) |
| `depuy.corail.zementiert` | schaft | CORAIL Cemented (Standard Offset / High Offset) | fixation: zementiert; konus: 12/14 AMT; varianten: {"Standard Offset": "8–16, 18, 20", "High Offset": "9–16, 18, 20 (Größe 8: keine REF)"}; hinweis: HA-beschichtete Schäfte dürfen nicht zementiert werden; masse: keine Maßtabelle für CORAIL Cemented in „Size Offerings“ – nur REF (gedr. 26) | corail | REF belegt (Original, 2 Prüfer); Maße nicht im Dokument |
| `depuy.pinnacle.schale` | pfanne | PINNACLE Press Fit | fixation: zementfrei; werte: aktuelle EMEA-Matrix Schale × Liner × max. Kopf-Ø offen; schalenbereich: „PINNACLE Hip Solutions Primary components (38 - 72 mm) as well as the PINNACLE Hip Solutions Revision components (54 – 80 mm)“ (gedr. 2 / PDF 5); hinweis: Keine Implantat-REF im Dokument; Bestellinfo gedr. 22 nur Instrumente; Verweis auf „PINNACLE Hip Solutions Primary System Overview“ (nicht geprüft). Probeschalen-/Probeliner-Größen und Farbcodes (gedr. 8–9) sind Instrumentendaten und werden nicht als Implantat übernommen (OpenAI).; keramikliner_hinweis: „If any other bearing surface has been impacted into the cup, a BIOLOX Total Hip System liner cannot be used. BIOLOX Total Hip System liners should only be used in new PINNACLE Hip Solutions acetabular cups with an “as manufactured” taper.“ (gedr. 20 / PDF 22) | pinnacle | offen (REF/Größen); Schalenbereich belegt (Original, 1 Prüfer) |
| `depuy.pinnacle.liner` | inlay | PINNACLE Liner | konfigurationen: Neutral (180° Kopfüberdeckung) · +4 Neutral (4 mm Lateralisation) · +4 10° Face-Changing · Lipped (4 mm build-up, 15° face-change) · Constrained Liners verfügbar (gedr. 10 / PDF 12); material: AltrX/Marathon PE, Keramik – je Schale/Kopf offen; hinweis: Trial-Liner-Farben/-Größen (gedr. 8–9) und Instrumente (Pusher/Gripper) sind keine Implantatdaten – nicht übernommen (OpenAI). Implantat-REF und Schale × Liner × Kopf-Ø nicht im Dokument. | pinnacle | Konfigurationen belegt (Original, 2 Prüfer); REF/Matrix offen |
| `depuy.triloc2.zementiert` | pfanne | TRILOC II-PE (zementiert) | fixation: zementiert; werte: offen – nur Registerbeleg (EPRD zementiert #5) | – | offen |
| `depuy.kopf.biolox_delta` | kopf | ARTICUL/EZE BIOLOX delta | konus: 12/14; werte: Ø/Offsets offen; hinweis: Implantat-Kopf-REF in CORAIL nicht enthalten; GUDID-Keramikköpfe 4734xxxxx (depuy.kopf.keramik_articul_eze) nicht als BIOLOX delta belegt. | corail | offen |
| `depuy.kopf.cocr` | kopf | ARTICUL/EZE Metallkopf 12/14 (GUDID: „Metallic femoral head prosthesis“) | konus: 12/14; werte: Ø 22.225 / 28 / 32 / 36 mm laut US-GUDID; EMEA-Quelle (C-STEM AMT 143325) nicht lesbar; ref_schreibweise: GUDID ohne Bindestriche (z. B. 136511000); Schreibweise 1365-11-000 nicht wörtlich belegt; hinweis: 36 mm +12 ist „ARTICUL/EZE METAL ON METAL FEMORAL HEAD“; 32 mm +17 „Not in Commercial Distribution“. CoCr 36 mm (außer MoM +12) und 40 mm nicht im Treffer-Set.; material: GUDID nennt nur „Metallic“ – CoCr nicht wörtlich belegt | gudid_ae | US – kein EU-Nachweis |
| `depuy.duokopf.self_centering` | duokopf | SELF-CENTERING Bipolar | verwendung: mit CORAIL zementiert (zu prüfen); freigabe: offen – nur US-Technik; in CH häufig: CORAIL zementiert + Cathcart (unipolar) | scb | offen |
| `depuy.duokopf.cathcart` | duokopf | Modular Cathcart Unipolar | art: unipolar (Endokopf), kein bipolarer Duokopf; registerbeleg: SIRIS Tab. 4.34: CORAIL zementiert / J&J Cathcart 2024 n=300 | scb | offen |
| `depuy.corail.dysplasie` | schaft | CORAIL Dysplasia Size 6 (K6S / K6A) | konus: 12/14; ref_bestellinfo: „Standard Dysplasic CORAIL Stem“ L20106 (gedr. 26) – ohne Größen-/Variantenangabe; ob K6S oder K6A, steht dort nicht; warnung: „This stem is contraindicated with hemiarthroplasty surgery. This stem must not be implanted in patient weighing more than 60kg (130lb). All 12/14 heads available in the DePuy Synthes Portfolio are compatible with this stem. The maximum offset for the head is limited to 13 mm.“ (gedr. 13 / PDF 14); resektion: K6S: 45°-Schnitt; K6A: biplanar (gedr. 13); hinweis: Maßtabelle gedr. 23 trägt die Überschrift „135° SHORT NECK (SN) Collared“ – vermutlich Layout, ungeklärt | corail | belegt (Original, 1 Prüfer) |
| `depuy.corail.trochanteric_base` | schaft | CORAIL Stem with Trochanteric Base | ref_bestellinfo: L20006 (gedr. 26 / PDF 27) – ohne Größenangabe; fixation: im Dokument nicht angegeben | corail | belegt (Original, 1 Prüfer) |
| `depuy.kopf.keramik_articul_eze` | kopf | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 (GUDID) | konus: 12/14; werte: Ø 22.225 / 28 / 32 / 36 / 40 mm laut US-GUDID; hinweis: GUDID nennt nur „Ceramic femoral head prosthesis“ – Material-/Markenname BIOLOX delta steht nicht im Datensatz; nicht mit depuy.kopf.biolox_delta (EMEA) gleichsetzen. | gudid_ae | US – kein EU-Nachweis |

### Größen – CORAIL zementfrei (HA) – STD 135°, KHO 135°, KLA 125°, STD 125°, SN 135° (Quelle corail)
| variante | kragen | groesse | ref | ref_spalte | ccd | schaftlaenge_B_mm | schaftlaenge_C_mm | offset_mm | halslaenge_mm | halshoehe_mm | breite_mm | seite_mass | seite_ref | sicherheit | hinweis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 135° Standard STD | ohne Kragen | 8 | 3L92507 | KS No Collar | 135° | 115 | 93 | 38.3 | 39 | 36 | 7 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | REF-Reihe unregelmäßig (8 = 3L92507), so gedruckt (OpenAI) |
| 135° Standard STD | ohne Kragen | 9 | 3L92509 | KS No Collar | 135° | 130 | 108 | 38.8 | 39 | 36 | 8 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 10 | 3L92510 | KS No Collar | 135° | 140 | 118 | 39.5 | 39 | 36 | 8 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 11 | 3L92511 | KS No Collar | 135° | 145 | 123 | 40.3 | 39 | 36 | 9 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 12 | 3L92512 | KS No Collar | 135° | 150 | 128 | 41.0 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 13 | 3L92513 | KS No Collar | 135° | 155 | 133 | 41.7 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 14 | 3L92514 | KS No Collar | 135° | 160 | 138 | 42.3 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 15 | 3L92515 | KS No Collar | 135° | 165 | 143 | 43.0 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 16 | 3L92516 | KS No Collar | 135° | 170 | 148 | 43.8 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 18 | 3L92518 | KS No Collar | 135° | 180 | 158 | 44.8 | 39 | 36 | 11 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | ohne Kragen | 20 | 3L92520 | KS No Collar | 135° | 190 | 168 | 45.8 | 39 | 36 | 11 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 8 | 3L92498 | KA Collar | 135° | 115 | 93 | 38.3 | 39 | 36 | 7 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 9 | 3L92499 | KA Collar | 135° | 130 | 108 | 38.8 | 39 | 36 | 8 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 10 | 3L92500 | KA Collar | 135° | 140 | 118 | 39.5 | 39 | 36 | 8 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 11 | 3L92501 | KA Collar | 135° | 145 | 123 | 40.3 | 39 | 36 | 9 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 12 | 3L92502 | KA Collar | 135° | 150 | 128 | 41.0 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 13 | 3L92503 | KA Collar | 135° | 155 | 133 | 41.7 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 14 | 3L92504 | KA Collar | 135° | 160 | 138 | 42.3 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 15 | 3L92505 | KA Collar | 135° | 165 | 143 | 43.0 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 16 | 3L92506 | KA Collar | 135° | 170 | 148 | 43.8 | 39 | 36 | 10 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Standard STD | mit Kragen | 18 | 3L92508 | KA Collar | 135° | 180 | 158 | 44.8 | 39 | 36 | 11 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | REF-Reihe unregelmäßig (18 = 3L92508, 20 = 3L92521), so gedruckt |
| 135° Standard STD | mit Kragen | 20 | 3L92521 | KA Collar | 135° | 190 | 168 | 45.8 | 39 | 36 | 11 | gedr. 21 / PDF 22 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | REF-Reihe unregelmäßig (18 = 3L92508, 20 = 3L92521), so gedruckt |
| 135° High Offset KHO | ohne Kragen | 9 | L20309 | No Collar | 135° | 130 | 108 | 45.7 | 43 | 35 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 10 | L20310 | No Collar | 135° | 140 | 118 | 46.4 | 43 | 35 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 11 | L20311 | No Collar | 135° | 145 | 123 | 47.2 | 43 | 35 | 9 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 12 | L20312 | No Collar | 135° | 150 | 128 | 47.9 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 13 | L20313 | No Collar | 135° | 155 | 133 | 48.5 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 14 | L20314 | No Collar | 135° | 160 | 138 | 49.2 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 15 | L20315 | No Collar | 135° | 165 | 143 | 49.9 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 16 | L20316 | No Collar | 135° | 170 | 148 | 50.7 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | ohne Kragen | 18 | L20318 | No Collar | 135° | 180 | 158 | 51.8 | 43 | 36 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | KHO ohne/mit Kragen Gr. 18/20 abweichend: Offset 51.8/52.9 vs. 51.7/52.7, Neck height 36 vs. 35 (gedr. 22) – so gedruckt, Druckfehler nicht feststellbar |
| 135° High Offset KHO | ohne Kragen | 20 | L20320 | No Collar | 135° | 190 | 168 | 52.9 | 43 | 36 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | KHO ohne/mit Kragen Gr. 18/20 abweichend: Offset 51.8/52.9 vs. 51.7/52.7, Neck height 36 vs. 35 (gedr. 22) – so gedruckt, Druckfehler nicht feststellbar |
| 135° High Offset KHO | mit Kragen | 9 | L971109 | Collar | 135° | 130 | 108 | 45.7 | 43 | 35 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 10 | L971110 | Collar | 135° | 140 | 118 | 46.4 | 43 | 35 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 11 | L971111 | Collar | 135° | 145 | 123 | 47.2 | 43 | 35 | 9 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 12 | L971112 | Collar | 135° | 150 | 128 | 47.9 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 13 | L971113 | Collar | 135° | 155 | 133 | 48.5 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 14 | L971114 | Collar | 135° | 160 | 138 | 49.2 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 15 | L971115 | Collar | 135° | 165 | 143 | 49.9 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 16 | L971116 | Collar | 135° | 170 | 148 | 50.7 | 43 | 35 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° High Offset KHO | mit Kragen | 18 | L971118 | Collar | 135° | 180 | 158 | 51.7 | 43 | 35 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | KHO ohne/mit Kragen Gr. 18/20 abweichend: Offset 51.8/52.9 vs. 51.7/52.7, Neck height 36 vs. 35 (gedr. 22) – so gedruckt, Druckfehler nicht feststellbar |
| 135° High Offset KHO | mit Kragen | 20 | L971120 | Collar | 135° | 190 | 168 | 52.7 | 43 | 35 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | KHO ohne/mit Kragen Gr. 18/20 abweichend: Offset 51.8/52.9 vs. 51.7/52.7, Neck height 36 vs. 35 (gedr. 22) – so gedruckt, Druckfehler nicht feststellbar |
| 125° High Offset KLA | mit Kragen | 9 | 3L93709 | KLA Collar | 125 | 130 | 108 | 45.6 | 40 | 30 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 10 | 3L93710 | KLA Collar | 125 | 140 | 118 | 46.3 | 40 | 30 | 8 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 11 | 3L93711 | KLA Collar | 125 | 145 | 123 | 47.1 | 40 | 30 | 9 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 12 | 3L93712 | KLA Collar | 125 | 150 | 128 | 47.8 | 40 | 30 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 13 | 3L93713 | KLA Collar | 125 | 155 | 133 | 48.5 | 40 | 30 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 14 | 3L93714 | KLA Collar | 125 | 160 | 138 | 49.1 | 40 | 30 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 15 | 3L93715 | KLA Collar | 125 | 165 | 143 | 49.8 | 40 | 30 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 16 | 3L93716 | KLA Collar | 125 | 170 | 148 | 50.6 | 40 | 30 | 10 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 18 | 3L93718 | KLA Collar | 125 | 180 | 158 | 51.8 | 40 | 31 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° High Offset KLA | mit Kragen | 20 | 3L93720 | KLA Collar | 125 | 190 | 168 | 52.8 | 40 | 31 | 11 | gedr. 22 / PDF 23 | gedr. 24 / PDF 25 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | Maßtabelle „125° HIGH OFFSET (KLA)“ ohne Kragenangabe; REF-Tabelle „(KLA Collar)“; keine kragenlose KLA im Dokument |
| 125° Standard STD | ohne Kragen | 7 | – | No Collar | 125 | 110 | 88 | 37.9 | 35 | 31 | 6 | gedr. 23 / PDF 24 | keine REF in der Bestellinfo | REF fehlt; Maße belegt (Original, 1 Prüfer) | Größe 7 nur in Maßtabelle gedr. 23; Übersicht gedr. 21 „Sz 8-14“, Bestellinfo gedr. 25 ab Größe 8 – keine REF |
| 125° Standard STD | ohne Kragen | 8 | L981208 | No Collar | 125 | 115 | 93 | 38.4 | 35 | 31 | 7 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | ohne Kragen | 9 | L981209 | No Collar | 125 | 130 | 108 | 38.9 | 35 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | ohne Kragen | 10 | L981210 | No Collar | 125 | 140 | 118 | 39.6 | 35 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 7 | – | Collar | 125 | 110 | 88 | 37.9 | 35 | 31 | 6 | gedr. 23 / PDF 24 | keine REF in der Bestellinfo | REF fehlt; Maße belegt (Original, 1 Prüfer) | Größe 7 nur in Maßtabelle gedr. 23; Übersicht gedr. 21 „Sz 8-14“, Bestellinfo gedr. 25 ab Größe 8 – keine REF |
| 125° Standard STD | mit Kragen | 8 | L971208 | Collar | 125 | 115 | 93 | 38.4 | 35 | 31 | 7 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 9 | L971209 | Collar | 125 | 130 | 108 | 38.9 | 35 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 10 | L971210 | Collar | 125 | 140 | 118 | 39.6 | 35 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 11 | L971211 | Collar | 125 | 145 | 123 | 40.4 | 35 | 31 | 9 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 12 | L971212 | Collar | 125 | 150 | 128 | 41.1 | 35 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 13 | L971213 | Collar | 125 | 155 | 133 | 41.7 | 35 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 125° Standard STD | mit Kragen | 14 | L971214 | Collar | 125 | 160 | 138 | 42.4 | 35 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | ohne Kragen | 7 | – | No Collar | 135 | 110 | 88 | 32.5 | 32 | 31 | 6 | gedr. 23 / PDF 24 | keine REF in der Bestellinfo | REF fehlt; Maße belegt (Original, 1 Prüfer) | Größe 7 nur in Maßtabelle gedr. 23; Übersicht gedr. 21 „Sz 8-14“, Bestellinfo gedr. 25 ab Größe 8 – keine REF |
| 135° Short Neck SN | ohne Kragen | 8 | L981308 | No Collar | 135 | 115 | 93 | 33.0 | 32 | 31 | 7 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | ohne Kragen | 9 | L981309 | No Collar | 135 | 130 | 108 | 33.5 | 32 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | ohne Kragen | 10 | L981310 | No Collar | 135 | 140 | 118 | 34.2 | 32 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 7 | – | Collar | 135 | 110 | 88 | 32.5 | 32 | 31 | 6 | gedr. 23 / PDF 24 | keine REF in der Bestellinfo | REF fehlt; Maße belegt (Original, 1 Prüfer) | Größe 7 nur in Maßtabelle gedr. 23; Übersicht gedr. 21 „Sz 8-14“, Bestellinfo gedr. 25 ab Größe 8 – keine REF |
| 135° Short Neck SN | mit Kragen | 8 | L971308 | Collar | 135 | 115 | 93 | 33.0 | 32 | 31 | 7 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 9 | L971309 | Collar | 135 | 130 | 108 | 33.5 | 32 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 10 | L971310 | Collar | 135 | 140 | 118 | 34.2 | 32 | 31 | 8 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 11 | L971311 | Collar | 135 | 145 | 123 | 35.0 | 32 | 31 | 9 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 12 | L971312 | Collar | 135 | 150 | 128 | 35.7 | 32 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 13 | L971313 | Collar | 135 | 155 | 133 | 36.4 | 32 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |
| 135° Short Neck SN | mit Kragen | 14 | L971314 | Collar | 135 | 160 | 138 | 37.0 | 32 | 31 | 10 | gedr. 23 / PDF 24 | gedr. 25 / PDF 26 | belegt (Original, 2 Prüfer) (REF); Maße belegt (Original, 1 Prüfer) | – |

### Größen – CORAIL Cemented (Standard Offset / High Offset) (Quelle corail)
| variante | groesse | ref | seite_ref | sicherheit |
|---|---|---|---|---|
| Standard Offset | 8 | L96408 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 9 | L96409 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 10 | L96410 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 11 | L96411 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 12 | L96412 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 13 | L96413 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 14 | L96414 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 15 | L96415 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 16 | L96416 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 18 | L96418 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| Standard Offset | 20 | L96420 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 8 | – | gedr. 26 / PDF 27 | keine REF (Zelle „–“) |
| High Offset | 9 | L96509 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 10 | L96510 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 11 | L96511 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 12 | L96512 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 13 | L96513 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 14 | L96514 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 15 | L96515 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 16 | L96516 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 18 | L96518 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |
| High Offset | 20 | L96520 | gedr. 26 / PDF 27 | belegt (Original, 2 Prüfer) |

### Größen – ARTICUL/EZE Metallkopf 12/14 (GUDID: „Metallic femoral head prosthesis“) (Quelle gudid_ae)
| ref_gudid | beschreibung | udi_di_gudid | status_us | firma | markt | sicherheit | durchmesser_mm | offset |
|---|---|---|---|---|---|---|---|---|
| 136529000 | ARTICUL/EZE FEMORAL HEAD Diameter 22.225mm +4 12/14 TAPER | 10603295033349 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 22.225 | +4 |
| 136530000 | ARTICUL/EZE FEMORAL HEAD Diameter 22.225mm +7 12/14 TAPER | 10603295033356 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 22.225 | +7 |
| 136511000 | ARTICUL/EZE FEMORAL HEAD Diameter 28mm +1.5 12/14 TAPER | 10603295033066 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 28 | +1.5 |
| 136512000 | ARTICUL/EZE FEMORAL HEAD Diameter 28mm +5 12/14 TAPER | 10603295033080 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 28 | +5 |
| 136513000 | ARTICUL/EZE FEMORAL HEAD Diameter 28mm +8.5 12/14 TAPER | 10603295033103 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 28 | +8.5 |
| 136514000 | ARTICUL/EZE FEMORAL HEAD Diameter 28mm +12 12/14 TAPER | 10603295033127 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 28 | +12 |
| 136515000 | ARTICUL/EZE FEMORAL HEAD Diameter 28mm +15.5 12/14 TAPER | 10603295033134 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 28 | +15.5 |
| 136521000 | ARTICUL/EZE FEMORAL HEAD Diameter 32mm +1 12/14 TAPER | 10603295033172 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 32 | +1 |
| 136522000 | ARTICUL/EZE FEMORAL HEAD Diameter 32mm +5 12/14 TAPER | 10603295033189 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 32 | +5 |
| 136523000 | ARTICUL/EZE FEMORAL HEAD Diameter 32mm +9 12/14 TAPER | 10603295033196 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 32 | +9 |
| 136524000 | ARTICUL/EZE FEMORAL HEAD Diameter 32mm +13 12/14 TAPER | 10603295033202 | In Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 32 | +13 |
| 136525000 | ARTICUL/EZE FEMORAL HEAD Diameter 32mm +17 12/14 TAPER | 10603295033219 | Not in Commercial Distribution | DEPUY (IRELAND) | US | US – kein EU-Nachweis | 32 | +17 |
| 136554000 | ARTICUL/EZE METAL ON METAL FEMORAL HEAD 12/14 TAPER Diameter 36mm +12 | 10603295033974 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | +12 |

### Größen – CORAIL Dysplasia Size 6 (K6S / K6A) (Quelle corail)
| groesse | ref | ccd | schaftlaenge_B_mm | schaftlaenge_C_mm | offset_mm | seite_mass | sicherheit | variante | seite_ref | hinweis |
|---|---|---|---|---|---|---|---|---|---|---|
| 6S | – | 135° | 110 | 93 | 30.8 | gedr. 23 / PDF 24 | belegt (Original, 1 Prüfer) | – | – | – |
| 6A | – | 135° | 110 | 94 | 34.4 | gedr. 23 / PDF 24 | belegt (Original, 1 Prüfer) | – | – | – |
| – | L20106 | – | – | – | – | – | belegt (Original, 1 Prüfer) | Standard Dysplasic CORAIL Stem | gedr. 26 / PDF 27 | Größe/Variante (6S/6A) im Original nicht angegeben |

### Größen – CORAIL Stem with Trochanteric Base (Quelle corail)
| groesse | ref | seite_ref | sicherheit | hinweis |
|---|---|---|---|---|
| – | L20006 | gedr. 26 / PDF 27 | belegt (Original, 1 Prüfer) | keine Größenangabe im Original |

### Größen – ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 (GUDID) (Quelle gudid_ae)
| ref_gudid | beschreibung | udi_di_gudid | status_us | firma | markt | sicherheit | durchmesser_mm | offset |
|---|---|---|---|---|---|---|---|---|
| 473422040 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 22.225mm plus 4 | 10603295503187 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 22.225 | +4 |
| 473422070 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 22.225mm plus 7 | 10603295503163 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 22.225 | +7 |
| 473428015 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 28mm plus 1.5 | 10603295505631 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 28 | +1.5 |
| 473428050 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 28mm plus 5 | 10603295506287 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 28 | +5 |
| 473428085 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 28mm plus 8.5 | 10603295506294 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 28 | +8.5 |
| 473432010 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 32mm plus 1 | 10603295517108 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 32 | +1 |
| 473432050 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 32mm plus 5 | 10603295505662 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 32 | +5 |
| 473432090 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 32mm plus 9 | 10603295517122 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 32 | +9 |
| 473436920 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 36mm minus  2 | 10603295505693 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | -2 |
| 473436015 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 36mm plus 1.5 | 10603295505709 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | +1.5 |
| 473436050 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 36mm plus 5 | 10603295505716 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | +5 |
| 473436085 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 36mm plus 8.5 | 10603295505723 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | +8.5 |
| 473436120 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 36mm plus 12 | 10603295506300 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 36 | +12 |
| 473440920 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 40mm minus  2 | 10603295505747 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 40 | -2 |
| 473440015 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 40mm plus 1.5 | 10603295505754 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 40 | +1.5 |
| 473440050 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 40mm plus 5 | 10603295505761 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 40 | +5 |
| 473440085 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 40mm plus 8.5 | 10603295505778 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 40 | +8.5 |
| 473440120 | ARTICUL/EZE FEMORAL HEAD CERAMIC 12/14 TAPER 40mm plus 12 | 10603295505785 | In Commercial Distribution | DEPUY ORTHOPAEDICS, INC. | US | US – kein EU-Nachweis | 40 | +12 |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `depuy.corail.zementfrei` | `depuy.kopf.biolox_delta` | **bedingt** | „All 12/14 heads available in the DePuy Synthes portfolio are compatible with the CORAIL Stem with a maximum offset of 13 mm“ (Classical heads: all 12/14 ARTICUL/EZE, 12/14 CoCr, 12/14 BIOLOX, aSPHERE ARTICUL/EZE 12/14; Keramikrevision: BIOLOX Delta TS Heads) – konkrete Kopf-REF/Ø nicht im Dokument | corail | gedr. 27 / PDF 28 (Instrumentenseite); gedr. 9 / 19 |
| `depuy.corail.zementfrei` | `depuy.kopf.cocr` | **bedingt** | „All 12/14 heads available in the DePuy Synthes portfolio are compatible with the CORAIL Stem with a maximum offset of 13 mm“ (Classical heads: all 12/14 ARTICUL/EZE, 12/14 CoCr, 12/14 BIOLOX, aSPHERE ARTICUL/EZE 12/14; Keramikrevision: BIOLOX Delta TS Heads) – konkrete Kopf-REF/Ø nicht im Dokument | corail | gedr. 27 / PDF 28 (Instrumentenseite); gedr. 9 / 19 |
| `depuy.pinnacle.schale` | `depuy.pinnacle.liner` | **offen** | Liner-Konfigurationen belegt, Schale × Liner × Kopf-Ø nicht im Dokument (Trialdaten nicht verwendet) | pinnacle | gedr. 10 / PDF 12 |
| `depuy.corail.zementiert` | `depuy.duokopf.self_centering` | **offen** | EU-Freigabe fehlt | scb | – |
| `depuy.corail.zementfrei` | `depuy.kopf.keramik_articul_eze` | **offen** | CORAIL nennt „all 12/14 ARTICUL/EZE“ (gedr. 27); Einzel-REF nur aus US-GUDID – EU-Lieferbarkeit/Identität nicht belegt | corail | gedr. 27 / PDF 28 |

## Regeln
- Dysplasie-Schaft Größe 6 (K6S/K6A): keine Hemiarthroplastik, kein Patientengewicht > 60 kg (130 lb), Kopf-Offset max. 13 mm (gedr. 13). Achtung Widerspruch/Geltungsbereich: gedr. 27 nennt „maximum offset of 13 mm“ für den CORAIL Stem allgemein – nicht aufgelöst, Herstellerdokument/IFU prüfen. (corail gedr. 13 / PDF 14; gedr. 27 / PDF 28)
- HA-beschichtete CORAIL-Schäfte nie zementieren. (corail)
- Nur DePuy-Synthes-12/14-Köpfe laut Produktfreigabe; keine markenübergreifende Freigabe aus 12/14. (corail)
- CORAIL-REF nur laut Bestelltabelle je Variante und Kragen (z. B. STD 135° Gr. 8 ohne Kragen 3L92507); keine Größe 7/17/19 und keine REF aus Zahlenfolgen; STD-REF nicht für KHO/KLA verwenden. (corail gedr. 24–26)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| CORAIL zementfrei HA 12/14 AMT 135° STD ohne Kragen Gr. 12 (REF 3L92512, Lot 5300693; enthält Gr. 11) | BfArM | PIE-1104627 (02257-18), 02/2018 | EU/DE | – | nur diese Charge | `depuy.corail.zementfrei` | https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2018/02257-18_kundeninfo_en.pdf?__blob=publicationFile |
| CORAIL KLA mit Kragen Gr. 9 (REF 3L93709, Lot 5291990) / HO ohne Kragen Gr. 14 (REF L20314, Lot 5292130) vertauscht | BfArM | PIE-863755 (07375-17), 07/2017 | EU/DE | – | nur diese Chargen | `depuy.corail.zementfrei` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07375-17_kundeninfo_de.pdf?__blob=publicationFile |
| CORAIL AMT Probehälse L94003–L94007 (Instrumente, alle Chargen) | BfArM | PIE-1125109 (06669-18), 05/2018 | EU/DE | – | Instrumentenkorrektur (Dichtungsringpartikel), kein Schaft-Rückruf | – | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/06/2018/06669-18_kundeninfo_de.pdf?__blob=publicationFile |
| PINNACLE Pfannen bestimmter Chargen (Gewinde Apex-Loch) | BfArM | Ref. 1896433 (22108-20), aktualisiert 18.02.2021 | EU/DE | kein Abschluss belegt | betrifft alle gelisteten Pfannen unabhängig von Apex-Schraube; Lot-Liste im Anhang | `depuy.pinnacle.schale` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2021/22108-20_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] PINNACLE EMEA: Implantat-REF, Schalengrößen, Schale × Liner (AltrX/Marathon/Keramik) × max. Kopf-Ø („Primary System Overview“)
- [ ] ARTICUL/EZE-Köpfe aus EMEA-Quelle (C-STEM AMT 143325 nicht lesbar): Ø/Offsets/REF und Identität BIOLOX delta; bisher nur US-GUDID
- [ ] CORAIL Größe 7 (STD 125°/SN 135°): REF fehlt; CORAIL Cemented: Maße fehlen; L20106 Zuordnung 6S/6A; L20006 Größe
- [ ] Geltungsbereich „maximum offset 13 mm“ (gedr. 13 nur Dysplasie vs. gedr. 27 allgemein)
- [ ] KHO Gr. 18/20 ohne vs. mit Kragen: abweichende Offset/Neck height – Herstellerbestätigung
- [ ] SELF-CENTERING Bipolar EU-IFU + Freigabe mit CORAIL zementiert
- [ ] TRILOC II-PE Dokument
- [ ] ACTIS EU-Dokument (nur Ranking: EPRD n=3.993, SIRIS 2024 n=606)

## Quellen
- **corail** CORAIL Total Hip System Surgical Technique · 198918-211214 UK, ©2022 · S. S. 9, 11, 13–15, 19–27 / PDF 10, 12, 14–16, 20–28; Size Offerings gedr. 21–23 / PDF 22–24; Ordering Information gedr. 24–26 / PDF 25–27; Köpfe gedr. 27 / PDF 28 · Markt: EMEA (UK-Ausgabe; „not intended for distribution outside the EMEA region“) · gelesen: Grok/Astra 07.10.2026; Claude-Helfer 07.10.2026 (Original); OpenAI 07.10.2026 (Bestellseiten) · https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf
- **pinnacle** PINNACLE Hip Solutions Surgical Technique · 142532-220805 EMEA, ©2022 · S. S. 2 / PDF 5 (Schalenbereich); S. 8–10 / PDF 10–12; S. 16 / PDF 18; S. 20–22 / PDF 22–24 (nur Instrumente) · Markt: EMEA · gelesen: Grok/Astra 07.10.2026; Claude-Helfer 07.10.2026 (Original); OpenAI 07.10.2026 · https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf
- **actis** ACTIS Total Hip System Surgical Technique (nur Ranking-Bezug) · 190156-210922 NZ / AU 2020 · S. Warnung S. 8 / PDF 10; Technical Specifications S. 12 / PDF 14 · Markt: AU/NZ – kein EU-Ersatz · gelesen: Grok/Astra 07.10.2026 · https://www.jnjmedtech.com/system/files/pdf/190156.210922%20NZ_134763.200315AU%20ACTIS%20Surgical%20Technique%20FINAL.pdf
- **scb** SELF-CENTERING Bipolar and Modular Cathcart Unipolar Endo Heads – Surgical Technique · DSUS/JRC/0317/2044 Rev. B, ©2017/2022 · S. – · Markt: US – kein EU-Ersatz · gelesen: Perplexity-Fundstelle · http://synthes.vo.llnwd.net/o16/LLNWMB8/US%20Mobile/Synthes%20North%20America/Product%20Support%20Materials/Technique%20Guides/
- **gudid_ae** FDA AccessGUDID – Suche „ARTICUL/EZE“ (DePuy-Köpfe) · Abfrage 07.10.2026 (151 Treffer) · S. Datensätze je Katalognummer (GMDN Metallic / Ceramic femoral head prosthesis) · Markt: US · gelesen: Claude-Helfer 07.10.2026 (Original) · https://accessgudid.nlm.nih.gov/devices/search?query=ARTICUL%2FEZE

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.
- **v1.1** (2026-10-07, 001-implantate-luecken): CORAIL: alle REF je Variante/Kragen (STD 135°, KHO 135°, KLA 125°, STD 125°, SN 135°, Cemented STD/HO, Dysplasia L20106, Trochanteric Base L20006) mit Maßtabellen; Widersprüche (Gr. 7 ohne REF, Cemented ohne Maße, KHO 18/20, 13-mm-Geltungsbereich) als Hinweis. ARTICUL/EZE Metall (13) und Keramik (18) aus US-GUDID, Keramik nicht als BIOLOX delta bezeichnet. PINNACLE: keine Implantat-REF, Trialdaten nicht übernommen. bild-Schema je Komponente.

Bilder: keine übernommen – Rechte beim Hersteller.
