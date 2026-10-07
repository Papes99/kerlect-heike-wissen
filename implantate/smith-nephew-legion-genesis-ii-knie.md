# Smith+Nephew · LEGION / GENESIS II (primär: CR, CR Deep Dish, PS; CoCr und OXINIUM)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/smith-nephew-legion-genesis-ii-knie.json`.

## Quellen
- **sl1** – LEGION Total Knee System – Total System Specification Guide and Product Catalog · Stand: 02861 V1 02/15 · Seiten: S. 12 Sägeblatt/Stylus; S. 21–25 Compatibility Guide und Insert-Austauschbarkeit; S. 40–48 Katalog (Femur, Inserts, Patella, Tibia) · Markt: US-Katalog 2015 („Product availability may vary by country“) – kein EU-Ersatz · gelesen: Grok 08.10.2026; OpenAI 07.10.2026 (S. 40) · https://smith-nephew.stylelabs.cloud/api/public/content/9b60b8ccb8d34736b556c9582336e376?download=true&v=e3edc939

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `sn.legion.femur_cr` | femur | LEGION CR Femur zementiert (CoCr oder OXINIUM) | kopplung: CR; groessen: 2, 3N, 3, 4N, 4, 5N, 5, 6N, 6, 7, 8; material: CoCr / OXINIUM (oxidiertes Zirkonium); fixation: zementiert | sl1 | belegt (US-Katalog) |
| `sn.legion.femur_cr_zf` | femur | LEGION CR Femur zementfrei (CoCr porös, mit/ohne HA) | kopplung: CR; groessen: 2–8; fixation: zementfrei | sl1 | belegt (US-Katalog) |
| `sn.legion.femur_ps` | femur | LEGION PS Femur zementiert (CoCr oder OXINIUM) | kopplung: PS; groessen: 2, 3N, 3, 4N, 4, 5N, 5, 6N, 6, 7, 8; fixation: zementiert | sl1 | belegt (US-Katalog) |
| `sn.genesis2.tibia` | tibia | LEGION/GENESIS II Tibial Baseplate zementiert (male tapered) | groessen: 1–8; seiten: L/R; fixation: zementiert | sl1 | belegt (US-Katalog) |
| `sn.legion.insert_cr` | insert | LEGION (GENESIS II) CR Standard-Insert | kopplung: CR; groessenpaare: 1-2, 3-4, 5-6, 7-8; hoehen_mm: 9, 11, 13, 15, 18 | sl1 | belegt |
| `sn.legion.insert_crdd` | insert | LEGION (GENESIS II) CR Deep Dish Insert | kopplung: CR Deep Dish; hoehen_mm: 9, 11, 13, 15, 18, 21 | sl1 | belegt |
| `sn.legion.insert_ps` | insert | LEGION (GENESIS II) PS Insert | kopplung: PS; hoehen_mm: 9, 11, 13, 15, 18, 21, 25 | sl1 | belegt |
| `sn.legion.insert_hf_xlpe` | insert | High-Flex- und XLPE-Varianten (CRHF, PSHF, CR/PS XLPE) *(nicht Primärstandard)* | hinweis: eigene REF-Reihen 7142-15xx, 7145-3xxx | sl1 | belegt |
| `sn.genesis2.patella` | patella | GENESIS II Patella (biconvex / resurfacing / oval resurfacing) | groessen_mm: biconvex 23/26/29/32; resurfacing 26/29/32/35; oval 29/32/35/38/41; hinweis: 7,5-mm-Patella nur USA/Israel | sl1 | belegt |

## Größen und REF (nur wie im Original gesehen)

**LEGION CR Femur zementiert (CoCr oder OXINIUM)** (`sn.legion.femur_cr`)

| groesse | cocr_links | cocr_rechts | oxinium_links | oxinium_rechts |
|---|---|---|---|---|
| 2 | 7142-3202 | 7142-3212 | 7142-1232 | 7142-1222 |
| 3N | 7193-3640 | 7193-3644 | 7142-1243 | 7142-1253 |
| 3 | 7142-3203 | 7142-3213 | 7142-1233 | 7142-1223 |
| 4N | 7193-3641 | 7193-3645 | 7142-1244 | 7142-1254 |
| 4 | 7142-3204 | 7142-3214 | 7142-1234 | 7142-1224 |
| 5N | 7193-3642 | 7193-3646 | 7142-1245 | 7142-1255 |
| 5 | 7142-3205 | 7142-3215 | 7142-1235 | 7142-1225 |
| 6N | 7193-3643 | 7193-3647 | 7142-1246 | 7142-1256 |
| 6 | 7142-3206 | 7142-3216 | 7142-1236 | 7142-1226 |
| 7 | 7142-3207 | 7142-3217 | 7142-1237 | 7142-1227 |
| 8 | 7142-3208 | 7142-3218 | 7142-1238 | 7142-1228 |

**LEGION CR Femur zementfrei (CoCr porös, mit/ohne HA)** (`sn.legion.femur_cr_zf`)

| ref_schema | seite_quelle |
|---|---|
| ohne HA 7142-324x (L) / 7142-325x (R); mit HA 7142-520x (L) / 7142-521x (R); x = Größe | S. 40 |

**LEGION PS Femur zementiert (CoCr oder OXINIUM)** (`sn.legion.femur_ps`)

| groesse | cocr_links | cocr_rechts | oxinium_links | oxinium_rechts |
|---|---|---|---|---|
| 2 | 7142-3222 | 7142-3232 | 7142-1212 | 7142-1202 |
| 3N | 7193-3648 | 7193-3652 | 7142-1263 | 7142-1273 |
| 3 | 7142-3223 | 7142-3233 | 7142-1213 | 7142-1203 |
| 4N | 7193-3649 | 7193-3653 | 7142-1264 | 7142-1274 |
| 4 | 7142-3224 | 7142-3234 | 7142-1214 | 7142-1204 |
| 5N | 7193-3650 | 7193-3654 | 7142-1265 | 7142-1275 |
| 5 | 7142-3225 | 7142-3235 | 7142-1215 | 7142-1205 |
| 6N | 7193-3651 | 7193-3655 | 7142-1266 | 7142-1276 |
| 6 | 7142-3226 | 7142-3236 | 7142-1216 | 7142-1206 |
| 7 | 7142-3227 | 7142-3237 | 7142-1217 | 7142-1207 |
| 8 | 7142-3228 | 7142-3238 | 7142-1218 | 7142-1208 |

**LEGION/GENESIS II Tibial Baseplate zementiert (male tapered)** (`sn.genesis2.tibia`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 7142-0160 | 7142-0176 |
| 2 | 7142-0162 | 7142-0180 |
| 3 | 7142-0164 | 7142-0182 |
| 4 | 7142-0166 | 7142-0184 |
| 5 | 7142-0168 | 7142-0186 |
| 6 | 7142-0170 | 7142-0188 |
| 7 | 7142-0172 | 7142-0190 |
| 8 | 7142-0174 | 7142-0191 |

**LEGION (GENESIS II) CR Standard-Insert** (`sn.legion.insert_cr`)

| ref_schema | seite_quelle |
|---|---|
| z. B. Größe 3-4: 7142-0490 (9 mm) … 7142-0498 (18 mm) | S. 42 |

**LEGION (GENESIS II) CR Deep Dish Insert** (`sn.legion.insert_crdd`)

| ref_schema | seite_quelle |
|---|---|
| z. B. Größe 3-4: 7142-0766 (9 mm) … 7142-0776 (21 mm) | S. 42 |

**LEGION (GENESIS II) PS Insert** (`sn.legion.insert_ps`)

| ref_schema | seite_quelle |
|---|---|
| z. B. Größe 3-4: 7142-0816 (9 mm) … 7142-0828 (25 mm) | S. 43 |

**GENESIS II Patella (biconvex / resurfacing / oval resurfacing)** (`sn.genesis2.patella`)

| variante | groesse | ref | seite_quelle |
|---|---|---|---|
| oval resurfacing | 29–41 mm | 7142-1029 / -1032 / -1035 / -1038 / -1041 | S. 45 |

## Original-Tabellen

**Insert-Austauschbarkeit mit LEGION CR/PS-Femur** (`T_legion_insert`, sl1 S. 25)

- CR-Standard-Inserts: mit allen Femurgrößen austauschbar
- Insert 1-2 PS/CRDD/PSCon: Femur 1–3; PSHF/CRHF: Femur 1–4
- Insert 3-4 PS/CRDD/PSCon: Femur 2–5; PSHF/CRHF: 2–6
- Insert 5-6 PS/CRDD/PSCon: Femur 4–7; PSHF/CRHF: 4–8
- Insert 7-8 PS/CRDD/PSCon: Femur 6–8; PSHF/CRHF: 6–9* (*9 nur GENESIS II, eingeschränkt)
- _Legende: Für GENESIS II CR/PS gleiche Austauschbarkeit, außer Constrained-Inserts (nicht mit GENESIS-II-Primärfemur)._

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `sn.legion.femur_cr` | `sn.legion.insert_cr` | **ja** | alle Größen | sl1 | S. 25 |
| `sn.legion.femur_cr` | `sn.legion.insert_crdd` | **bedingt** | Größe laut Tabelle; CRDD nur LEGION CR (nicht PS) | sl1 | S. 22/25 |
| `sn.legion.femur_ps` | `sn.legion.insert_crdd` | **nein** | CRDD: LEGION PS „No“ | sl1 | S. 22 |
| `sn.legion.femur_ps` | `sn.legion.insert_ps` | **bedingt** | Größe laut Tabelle | sl1 | S. 25 |
| `sn.legion.femur_cr` | `sn.genesis2.tibia` | **ja** | GENESIS II Tibial Baseplate male tapered mit LEGION CR, PS, RK | sl1 | S. 21 |
| `sn.legion.femur_ps` | `sn.genesis2.tibia` | **ja** | wie oben | sl1 | S. 21 |
| `sn.legion.insert_cr` | `sn.genesis2.tibia` | **offen** | Größenregel Insert ↔ Baseplate im Katalog nicht ausdrücklich gefunden | sl1 | – |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **insert** – Größenpaar: Insert-Größenpaar (1-2, 3-4 …) gegen Femurgröße laut Tabelle S. 25 prüfen; CR-Standard frei. (sl1 S. 25)
- **markt** – US-Katalog: Verfügbarkeit länderabhängig; 7,5-mm-Patella nur USA/Israel. (sl1 S. 1/45)

## Rückrufe / Sicherheitsinformationen
- keine im Lauf gefunden (nicht systematisch gesucht)

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.

## Offen
- Nur US-Katalog 02/2015 – EU-Katalog/IFU offen.
- Insert ↔ Tibia-Baseplate-Größenregel nicht ausdrücklich gefunden.
- Zuordnung Standard-CR/PS-Insert zu Femurtyp in Tabelle S. 22 mehrdeutig – Hersteller fragen.
- GENESIS II Femur (eigene Komponente, EPRD Rang 10) nicht separat ausgewertet.

_Neuanlage 08.10.2026 aus LEGION Spec Guide/Katalog 02/15 (US). verified: false._

