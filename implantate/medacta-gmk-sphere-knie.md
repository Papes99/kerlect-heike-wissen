# Medacta · GMK Sphere (medial-pivot; Flex und CR)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/medacta-gmk-sphere-knie.json`.

## Quellen
- **mg1** – GMK Sphere Specification Guide · Stand: ref: 99.26SPHERE.11SG rev. 02, Last update December 2020 · Seiten: S. 4–5 Femur; S. 6–10 Inserts; S. 11–13 Tibia; S. 14 Resurfacing-Patella; S. 15 Inset-Patella; S. 16 Stiel; S. 17–19 Kompatibilität · Markt: „not intended for the US market“ – Zulassung lokal prüfen · gelesen: Grok 08.10.2026; OpenAI 07.10.2026 · https://aws-media.medacta.com/media/9926sphere11sg-02.pdf

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `medacta.gmk.femur_zem` | femur | GMK Sphere Femur zementiert (CoCrMo) | groessen: 1, 1+, 2, 2+, 3, 3+, 4, 4+, 5, 5+, 6, 6+, 7; seiten: L/R; fixation: zementiert | mg1 | belegt (vollständige REF-Liste S. 4) |
| `medacta.gmk.femur_sensitin` | femur | GMK Sphere SensiTiN Femur zementiert (TiNbN-beschichtet) | groessen: 1, 1+, 2, 2+, 3, 3+, 4, 4+, 5, 5+, 6, 6+, 7; fixation: zementiert; beschichtung: TiNbN | mg1 | belegt |
| `medacta.gmk.femur_zf` | femur | GMK Sphere Femur zementfrei | groessen: 1, 1+, 2, 2+, 3, 3+, 4, 4+, 5, 5+, 6, 6+, 7; fixation: zementfrei | mg1 | belegt |
| `medacta.gmk.insert_flex` | insert | GMK Sphere Flex Insert (UHMWPE) / Flex E-Cross (Vit.-E-XLPE) | kopplung: medial-pivot (Sphere Flex); groessen: 1–6; hoehen_mm: 10, 11, 12, 13, 14, 17, 20 | mg1 | belegt |
| `medacta.gmk.insert_cr` | insert | GMK Sphere CR Insert / CR E-Cross | kopplung: CR; groessen: 1–6; hoehen_mm: 10, 11, 12, 13, 14 | mg1 | belegt |
| `medacta.gmk.tibia_zem` | tibia | GMK Tibial Baseplate zementiert (CoCrMo) inkl. Sphere t3-i4 / t4-i3 | groessen: 1–6, t3-i4 (Tibia 3 für Insert 4), t4-i3 (Tibia 4 für Insert 3); fixation: zementiert | mg1 | belegt |
| `medacta.gmk.tibia_sensitin` | tibia | GMK Sphere SensiTiN Tibial Baseplate zementiert | groessen: 1–6; beschichtung: TiNbN | mg1 | belegt |
| `medacta.gmk.patella_resurf` | patella | GMK Resurfacing Patella (UHMWPE / E-Cross) | groessen: 1–4 (M/L 32/35/38/41 mm, Höhe 10 mm) | mg1 | belegt |
| `medacta.gmk.patella_inset` | patella | GMK Inset Patella | groessen: 1–4 (Ø 20/24/28/32 mm) | mg1 | belegt |
| `medacta.gmk.stiel` | stiel | GMK Stem Extension *(nicht Primärstandard)* | laengen_mm: 30, 65; durchmesser_mm: 11 | mg1 | belegt |

## Größen und REF (nur wie im Original gesehen)

**GMK Sphere Femur zementiert (CoCrMo)** (`medacta.gmk.femur_zem`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 02.12.0001L | 02.12.0001R |
| 1+ | 02.12.0021L | 02.12.0021R |
| 2 | 02.12.0002L | 02.12.0002R |
| 2+ | 02.12.0022L | 02.12.0022R |
| 3 | 02.12.0003L | 02.12.0003R |
| 3+ | 02.12.0023L | 02.12.0023R |
| 4 | 02.12.0004L | 02.12.0004R |
| 4+ | 02.12.0024L | 02.12.0024R |
| 5 | 02.12.0005L | 02.12.0005R |
| 5+ | 02.12.0025L | 02.12.0025R |
| 6 | 02.12.0006L | 02.12.0006R |
| 6+ | 02.12.0026L | 02.12.0026R |
| 7 | 02.12.0007L | 02.12.0007R |

**GMK Sphere SensiTiN Femur zementiert (TiNbN-beschichtet)** (`medacta.gmk.femur_sensitin`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 02.12.0701L | 02.12.0701R |
| 1+ | 02.12.0721L | 02.12.0721R |
| 2 | 02.12.0702L | 02.12.0702R |
| 2+ | 02.12.0722L | 02.12.0722R |
| 3 | 02.12.0703L | 02.12.0703R |
| 3+ | 02.12.0723L | 02.12.0723R |
| 4 | 02.12.0704L | 02.12.0704R |
| 4+ | 02.12.0724L | 02.12.0724R |
| 5 | 02.12.0705L | 02.12.0705R |
| 5+ | 02.12.0725L | 02.12.0725R |
| 6 | 02.12.0706L | 02.12.0706R |
| 6+ | 02.12.0726L | 02.12.0726R |
| 7 | 02.12.0707L | 02.12.0707R |

**GMK Sphere Femur zementfrei** (`medacta.gmk.femur_zf`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 02.12.1001L | 02.12.1001R |
| 1+ | 02.12.1021L | 02.12.1021R |
| 2 | 02.12.1002L | 02.12.1002R |
| 2+ | 02.12.1022L | 02.12.1022R |
| 3 | 02.12.1003L | 02.12.1003R |
| 3+ | 02.12.1023L | 02.12.1023R |
| 4 | 02.12.1004L | 02.12.1004R |
| 4+ | 02.12.1024L | 02.12.1024R |
| 5 | 02.12.1005L | 02.12.1005R |
| 5+ | 02.12.1025L | 02.12.1025R |
| 6 | 02.12.1006L | 02.12.1006R |
| 6+ | 02.12.1026L | 02.12.1026R |
| 7 | 02.12.1007L | 02.12.1007R |

**GMK Sphere Flex Insert (UHMWPE) / Flex E-Cross (Vit.-E-XLPE)** (`medacta.gmk.insert_flex`)

| ref_schema | beispiel | seite_quelle |
|---|---|---|
| 02.12.0{Größe}{Höhe}FL/FR; E-Cross: 02.12.E0{Größe}{Höhe}FL/FR | 02.12.0410FL = Größe 4, 10 mm, links | S. 6–7 |

**GMK Sphere CR Insert / CR E-Cross** (`medacta.gmk.insert_cr`)

| ref_schema | seite_quelle |
|---|---|
| 02.12.0{Größe}{Höhe}CRL/CRR; E-Cross: 02.12.E0{Größe}{Höhe}CRL/CRR | S. 8–9 |

**GMK Tibial Baseplate zementiert (CoCrMo) inkl. Sphere t3-i4 / t4-i3** (`medacta.gmk.tibia_zem`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 02.07.1201L | 02.07.1201R |
| 2 | 02.07.1202L | 02.07.1202R |
| 3 | 02.07.1203L | 02.07.1203R |
| 4 | 02.07.1204L | 02.07.1204R |
| 5 | 02.07.1205L | 02.07.1205R |
| 6 | 02.07.1206L | 02.07.1206R |
| t3-i4 | 02.12.t3i4L | 02.12.t3i4R |
| t4-i3 | 02.12.t4i3L | 02.12.t4i3R |

**GMK Sphere SensiTiN Tibial Baseplate zementiert** (`medacta.gmk.tibia_sensitin`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| 1 | 02.07.2801L | 02.07.2801R |
| 2 | 02.07.2802L | 02.07.2802R |
| 3 | 02.07.2803L | 02.07.2803R |
| 4 | 02.07.2804L | 02.07.2804R |
| 5 | 02.07.2805L | 02.07.2805R |
| 6 | 02.07.2806L | 02.07.2806R |

**GMK Resurfacing Patella (UHMWPE / E-Cross)** (`medacta.gmk.patella_resurf`)

| groesse | ref | ref_ecross |
|---|---|---|
| 1 | 02.07.0033RP | 02.12.E001RP |
| 2 | 02.07.0034RP | 02.12.E002RP |
| 3 | 02.07.0035RP | 02.12.E003RP |
| 4 | 02.07.0036RP | 02.12.E004RP |

**GMK Inset Patella** (`medacta.gmk.patella_inset`)

| groesse | ref |
|---|---|
| 1 | 02.07.0040IP |
| 2 | 02.07.0041IP |
| 3 | 02.07.0042IP |
| 4 | 02.07.0043IP |

**GMK Stem Extension** (`medacta.gmk.stiel`)

| ref | laenge_mm |
|---|---|
| 02.07.F11030 | 30 |
| 02.07.F11066 | 65 |

## Original-Tabellen

**Tibia / Femur / Insert** (`T_gmk_comp`, mg1 S. 17)

- Tibia 1/2/3: Femur 1/1+ bis 3/3+ → Insert gleiche Größe wie Tibia
- Tibia t4-i3: Femur 1/1+ bis 3/3+ → Insert 3
- Tibia t3-i4: Femur 4/4+ bis 7 → Insert 4
- Tibia 4/5/6: Femur 4/4+ bis 7 → Insert gleiche Größe wie Tibia
- _Legende: Insert = GMK Sphere Flex oder CR. Alle Tibiaplateaus mit oder ohne Stiel; alle GMK-Patellae mit allen Sphere-Femurgrößen._

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `medacta.gmk.femur_zem` | `medacta.gmk.insert_flex` | **bedingt** | Femur 1–3+ mit Insert 1–3; Femur 4–7 mit Insert 4–6 | mg1 | S. 17 |
| `medacta.gmk.femur_zem` | `medacta.gmk.insert_cr` | **bedingt** | wie Flex | mg1 | S. 17 |
| `medacta.gmk.insert_flex` | `medacta.gmk.tibia_zem` | **bedingt** | Insertgröße = Tibiagröße; Ausnahme t3-i4 → Insert 4, t4-i3 → Insert 3 | mg1 | S. 11/17 |
| `medacta.gmk.patella_resurf` | `medacta.gmk.femur_zem` | **ja** | alle Femurgrößen | mg1 | S. 17 |
| `medacta.gmk.patella_inset` | `medacta.gmk.femur_zem` | **ja** | alle Femurgrößen | mg1 | S. 17 |
| `medacta.gmk.stiel` | `medacta.gmk.tibia_zem` | **ja** | alle festen Tibiaplateaus | mg1 | S. 17 |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **insert** – insert.groesse == tibia.insertgroesse: Insertgröße entspricht der Tibiagröße; t3-i4 braucht Insert 4, t4-i3 Insert 3. (mg1 S. 11/17)
- **femur** – Gruppe: Femur 1–3+ nur mit Insert 1–3; Femur 4–7 nur mit Insert 4–6. (mg1 S. 17)
- **insert_cr** – hoehe ≤ 14: CR-Inserts nur 10–14 mm; Flex auch 17/20 mm. (mg1 S. 6–10)

## Rückrufe / Sicherheitsinformationen
- keine im Lauf gefunden (nicht systematisch gesucht)

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.

## Offen
- EU-IFU nicht gelesen; Spec Guide Dezember 2020 – aktuellen Stand beim Hersteller prüfen.
- Zementfreie Tibia im Spec Guide nicht enthalten.
- Medacta-Robotik/MyKnee-PSI nicht ausgewertet.

_Neuanlage 08.10.2026 aus GMK Sphere Specification Guide rev. 02 (12/2020). Femur-REF nach Tabelle S. 4 systematisch übertragen (Plus-Größen = 21–26). verified: false._

