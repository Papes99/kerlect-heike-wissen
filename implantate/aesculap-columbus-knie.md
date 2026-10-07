# Aesculap (B. Braun) · Columbus (CR, CR Deep Dish, UC, UCR, RP, PS; AS-Beschichtung)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/aesculap-columbus-knie.json`.

## Quellen
- **ac1** – Aesculap Columbus Knee Arthroplasty Operating Technique with IQ Instruments (O47502) · Stand: O47502 0414-1-1 (2014) · Seiten: PDF-S. 4 Varianten; S. 45 Gleitflächenhöhen; S. 49/67 Patella; S. 65 Femurmaße; S. 68–81 Bestellinformation und Implantatmatrix · Markt: englisch, 2014; Datei liegt auf Händler-Server (Drittanbieter) – nur Fundstelle, kein aktueller Hersteller-Nachweis · gelesen: Grok 08.10.2026 · https://www.onmed.spb.ru/upload/iblock/2bb/2bb9d5cf080a58538a5b0133cdbe5eab.pdf
- **ac2** – Columbus Knieendoprothesensystem – Produktseite · Stand: Webseite, abgerufen 2026-10-07 · Seiten: Produktbeschreibung · Markt: DE · gelesen: Grok 07.10.2026 · https://www.bbraun.de/de/products/b/columbus-knieendoprothesensystem.html

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.columbus.femur_cr_zem` | femur | Columbus CR/RP Femur zementiert | kopplung: CR (auch für RP); groessen: F1, F2N, F2, F3N, F3, F4N, F4, F5N, F5, F6N, F6, F7, F8; seiten: L/R; fixation: zementiert; as_variante: AS-Beschichtung: gleiche Nummer mit Endung Z statt K (laut Bestellinfo) | ac1 | Fundstelle (2014, Drittanbieter-Kopie) |
| `aesculap.columbus.femur_cr_zf` | femur | Columbus CR/RP Femur zementfrei | kopplung: CR; groessen: F1, F2N, F2, F3N, F3, F4N, F4, F5N, F5, F6N, F6, F7, F8; fixation: zementfrei | ac1 | Fundstelle |
| `aesculap.columbus.femur_ps` | femur | Columbus PS Femur zementiert | kopplung: PS; groessen: F1, F2N, F2, F3N, F3, F4N, F4, F5N, F5, F6N, F6, F7, F8; fixation: zementiert; as_variante: Z-Nummern nicht für alle Größen gelistet (z. B. F2N, F8) | ac1 | Fundstelle |
| `aesculap.columbus.tibia_crps` | tibia | Columbus CR/PS Tibiaplateau modular | groessen: T0, T0+, T1, T1+, T2, T2+, T3, T3+, T4, T4+, T5; fixation: zementiert (K, AS = Z) oder zementfrei | ac1 | Fundstelle |
| `aesculap.columbus.tibia_rp` | tibia | Columbus RP Tibiaplateau (Rotating Platform) | groessen: T1–T5 (inkl. +); plattform: mobil; fixation: zementiert NN271K–NN279K, zementfrei NN281K–NN289K | ac1 | Fundstelle |
| `aesculap.columbus.tibia_ucr` | tibia | Columbus UCR Tibiaplateau zementiert *(nicht Primärstandard)* | groessen: T0–T5; ref_bereich: NN670K, NN668K (T0+), NN671K–NN679K | ac1 | Fundstelle |
| `aesculap.columbus.gleit_dd` | insert | Columbus CR Deep Dish Gleitfläche | kopplung: CR DD; groessengruppen: T0/0+, T1/1+, T2/2+, T3/3+, T4/4+, T5; hoehen_mm: 10, 12, 14, 16, 18, 20 | ac1 | Fundstelle |
| `aesculap.columbus.gleit_uc` | insert | Columbus UC (Ultra Congruent) Gleitfläche | kopplung: UC (kreuzbandopfernd); hoehen_mm: 10–20 | ac1 | Fundstelle |
| `aesculap.columbus.gleit_rp` | insert | Columbus RP Gleitfläche | kopplung: RP (mobil); hoehen_mm: 10–16 | ac1 | Fundstelle |
| `aesculap.columbus.gleit_ps` | insert | Columbus PS Gleitfläche inkl. Fixationsschraube | kopplung: PS; hoehen_mm: 10–20; hinweis: PS-Schraube nach Aushärten des Zements festziehen (PDF-S. 51) | ac1 | Fundstelle |
| `aesculap.columbus.patella` | patella | Columbus Patella 3-Peg | groessen_mm: P1 Ø26 × 7, P2 Ø29 × 8, P3 Ø32 × 9, P4 Ø35 × 10, P5 Ø38 × 11 | ac1 | Fundstelle |

## Größen und REF (nur wie im Original gesehen)

**Columbus CR/RP Femur zementiert** (`aesculap.columbus.femur_cr_zem`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| F1 | NN001K | NN011K |
| F2N | NN800K | NN810K |
| F2 | NN002K | NN012K |
| F3N | NN801K | NN811K |
| F3 | NN003K | NN013K |
| F4N | NN899K | NN909K |
| F4 | NN004K | NN014K |
| F5N | NN900K | NN910K |
| F5 | NN005K | NN015K |
| F6N | NN901K | NN911K |
| F6 | NN006K | NN016K |
| F7 | NN007K | NN017K |
| F8 | NN008K | NN018K |

**Columbus CR/RP Femur zementfrei** (`aesculap.columbus.femur_cr_zf`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| F1 | NN021K | NN031K |
| F2N | NN820K | NN830K |
| F2 | NN022K | NN032K |
| F3N | NN821K | NN831K |
| F3 | NN023K | NN033K |
| F4N | NN919K | NN929K |
| F4 | NN024K | NN034K |
| F5N | NN920K | NN930K |
| F5 | NN025K | NN035K |
| F6N | NN921K | NN931K |
| F6 | NN026K | NN036K |
| F7 | NN027K | NN037K |
| F8 | NN028K | NN038K |

**Columbus PS Femur zementiert** (`aesculap.columbus.femur_ps`)

| groesse | ref_links | ref_rechts |
|---|---|---|
| F1 | NN161K | NN171K |
| F2N | NN840K | NN850K |
| F2 | NN162K | NN172K |
| F3N | NN841K | NN851K |
| F3 | NN163K | NN173K |
| F4N | NN939K | NN949K |
| F4 | NN164K | NN174K |
| F5N | NN940K | NN950K |
| F5 | NN165K | NN175K |
| F6N | NN941K | NN951K |
| F6 | NN166K | NN176K |
| F7 | NN167K | NN177K |
| F8 | NN168K | NN178K |

**Columbus CR/PS Tibiaplateau modular** (`aesculap.columbus.tibia_crps`)

| groesse | ref_zementiert | ref_zementfrei |
|---|---|---|
| T0 | NN070K | NN080K |
| T0+ | NN058K | NN059K |
| T1 | NN071K | NN081K |
| T1+ | NN072K | NN082K |
| T2 | NN073K | NN083K |
| T2+ | NN074K | NN084K |
| T3 | NN075K | NN085K |
| T3+ | NN076K | NN086K |
| T4 | NN077K | NN087K |
| T4+ | NN078K | NN088K |
| T5 | NN079K | NN089K |

**Columbus CR Deep Dish Gleitfläche** (`aesculap.columbus.gleit_dd`)

| ref_schema | seite_quelle |
|---|---|
| NN2{Gruppe 0–5}{0–5 = 10–20 mm}, z. B. NN200 = T0/0+ 10 mm, NN210 = T1/1+ 10 mm | PDF-S. 73 |

**Columbus UC (Ultra Congruent) Gleitfläche** (`aesculap.columbus.gleit_uc`)

| ref_schema | seite_quelle |
|---|---|
| NN4xx, z. B. NN400 = T0/0+ 10 mm | PDF-S. 74 |

**Columbus RP Gleitfläche** (`aesculap.columbus.gleit_rp`)

| ref_schema | seite_quelle |
|---|---|
| NN3xx, z. B. NN310 = T1/1+ 10 mm | PDF-S. 74 |

**Columbus PS Gleitfläche inkl. Fixationsschraube** (`aesculap.columbus.gleit_ps`)

| ref_schema | seite_quelle |
|---|---|
| NN5xx, z. B. NN500 = T0/0+ 10 mm | PDF-S. 76 |

**Columbus Patella 3-Peg** (`aesculap.columbus.patella`)

| groesse | ref |
|---|---|
| P1 | NX041 |
| P2 | NX042 |
| P3 | NX043 |
| P4 | NX044 |
| P5 | NX045 |

## Original-Tabellen

**Varianten und Fixation** (`T_columbus_varianten`, ac1 PDF-S. 4)

- RP: mobil, zementiert/zementfrei
- UCR: fest, zementiert
- CR DD: fest, zementiert/zementfrei
- UC: fest, zementiert/zementfrei
- PS: fest, zementiert
- _Legende: AS-beschichtete Implantate für Patienten mit Metallsensitivität (PDF-S. 4). B. Braun DE: 14 Femur-, 11 Tibiagrößen, PE bis 20 mm (ac2) – Abweichung zu 13 Femurgrößen im Dokument 2014._

**Patella / Femur** (`T_columbus_patella`, ac1 PDF-S. 79)

- Patella P1–P5 (NX041–NX045) für Femur F1–F8
- _Legende: Implantatmatrix_

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `aesculap.columbus.femur_cr_zem` | `aesculap.columbus.gleit_dd` | **bedingt** | Gleitfläche nach Tibia-Größengruppe; Kombination aus Bezeichnung CR abgeleitet – Herstellertabelle nicht gefunden | ac1 | PDF-S. 4/73 |
| `aesculap.columbus.femur_cr_zem` | `aesculap.columbus.gleit_rp` | **bedingt** | Femur ausdrücklich „CR/RP“; RP-Tibia + RP-Gleitfläche | ac1 | PDF-S. 68/74 |
| `aesculap.columbus.femur_cr_zem` | `aesculap.columbus.gleit_uc` | **offen** | UC (kreuzbandopfernd) – Freigabe mit CR-Femur im Dokument nicht als Tabelle gefunden | ac1 | PDF-S. 4/74 |
| `aesculap.columbus.femur_ps` | `aesculap.columbus.gleit_ps` | **bedingt** | PS-Gleitfläche mit PS-Femur auf CR/PS-Tibia; nur zementiert | ac1 | PDF-S. 4/76 |
| `aesculap.columbus.gleit_ps` | `aesculap.columbus.tibia_crps` | **bedingt** | gleiche Tibia-Größengruppe (z. B. T2/2+ auf T2 oder T2+) | ac1 | PDF-S. 76 |
| `aesculap.columbus.patella` | `aesculap.columbus.femur_cr_zem` | **ja** | P1–P5 für F1–F8 | ac1 | PDF-S. 79 |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **gleitflaeche** – Größengruppe = Tibia: Gleitfläche T0/0+ … T5 passend zur Tibiagröße wählen. (ac1 PDF-S. 73–76)
- **ps** – Schraube: PS-Fixationsschraube erst nach Aushärten des Zements festziehen. (ac1 PDF-S. 51)
- **as** – K vs. Z: Standard (K) und AS-beschichtet (Z) am Etikett unterscheiden. (ac1 PDF-S. 68–70)

## Rückrufe / Sicherheitsinformationen
- keine im Lauf gefunden (nicht systematisch gesucht)

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.

## Offen
- Aktuelle B.-Braun-OP-Technik/IFU nicht abrufbar (DE- und US-PDF 404, Katalogseiten nur mit JavaScript) – Daten aus Dokument 2014 auf Drittanbieter-Server.
- Femur-Tibia-Größenkombination: keine Tabelle gefunden.
- Femurgrößen: Dokument 2014 13 Größen, B.-Braun-Seite nennt 14 – aktuellen Stand klären.
- IFU TA012000 (Kontraindikationen) nicht gelesen.

_Neuanlage 08.10.2026 aus Aesculap O47502 (2014, Drittanbieter-Kopie) und B.-Braun-Produktseite. verified: false. REF nur als Fundstelle – vor Nutzung mit aktuellem Hersteller-Katalog abgleichen._

