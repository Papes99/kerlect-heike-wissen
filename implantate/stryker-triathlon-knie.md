# Stryker · Triathlon Knee System (primär: CR, CS, PS, PSR; Tritanium)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/stryker-triathlon-knie.json`.

## Quellen
- **st1** – Triathlon Knee System – Surgical protocol compendium · Stand: TRIATH-SP-30_Rev-1_29865, © 2021 · Seiten: S. 2 Kompatibilität; S. 3 Indikationen; S. 44 Patella-Probeteile; S. 57–60 Implantat-REF; S. 310 Tritanium-Baseplate · Markt: Sammel-Dokument (US und Rest der Welt); einzelne Produkte laut Dokument nicht CE-gekennzeichnet (z. B. Screw-Fix-Baseplate) · gelesen: Grok 08.10.2026; REF-Beispiele auch OpenAI 07.10.2026 · https://www.stryker.com/content/dam/stryker/joint-replacement/training-and-education/orthopaedic-fellows-summit/resources/1--knees/3.pdf

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `stryker.triathlon.femur_cr_zem` | femur | Triathlon CR Femoral Component – zementiert | kopplung: CR; groessen: 1–8; seiten: L (X01) / R (X02); fixation: zementiert | st1 | belegt |
| `stryker.triathlon.femur_cr_zf` | femur | Triathlon CR Femoral Component – zementfrei Beaded mit Peri-Apatite | kopplung: CR; groessen: 1–8; fixation: zementfrei – nicht mit Zement verwenden | st1 | belegt |
| `stryker.triathlon.femur_ps_zem` | femur | Triathlon PS Femoral Component – zementiert | kopplung: PS; groessen: 1–8; fixation: zementiert | st1 | belegt |
| `stryker.triathlon.femur_ps_zf` | femur | Triathlon PS Femoral Component – zementfrei Beaded mit Peri-Apatite | kopplung: PS; groessen: 1–8; fixation: zementfrei | st1 | belegt |
| `stryker.triathlon.tibia_primary_zem` | tibia | Triathlon Primary Tibial Baseplate – zementiert | groessen: 0–8; fixation: zementiert | st1 | belegt |
| `stryker.triathlon.tibia_primary_pa` | tibia | Triathlon Primary Tibial Baseplate – Beaded mit Peri-Apatite | groessen: 1–8; fixation: zementfrei | st1 | belegt |
| `stryker.triathlon.tibia_tritanium` | tibia | Triathlon Tritanium Baseplate | groessen: 0–8; fixation: zementfrei und zementiert (Indikation S. 3) | st1 | belegt |
| `stryker.triathlon.insert_cr` | insert | Triathlon CR Tibial Insert (konventionelles PE / X3) | kopplung: CR; hoehen_mm: 9, 10, 11, 12, 13, 14, 16, 19; groessen: PE 1–8; X3 0–8 (19 mm ohne Größe 0) | st1 | belegt |
| `stryker.triathlon.insert_cs` | insert | Triathlon CS Tibial Insert (PE / X3) | kopplung: CS; hoehen_mm: 9, 10, 11, 12, 13, 14, 16, 19, 22 | st1 | belegt |
| `stryker.triathlon.insert_ps` | insert | Triathlon PS Tibial Insert (PE / X3) | kopplung: PS; hoehen_mm: 9, 10, 11, 12, 13, 14, 16, 19, 22; groessen: PE 1–8; X3 0–8 (22 mm ohne 0) | st1 | belegt |
| `stryker.triathlon.insert_psr` | insert | Triathlon PSR Tibial Insert *(nicht Primärstandard)* | kopplung: PSR; hinweis: PS-Probeinsert darf zum Trial für PSR verwendet werden (S. 2) | st1 | belegt (Tabelle); REF nicht übernommen |
| `stryker.triathlon.patella_sym` | patella | Triathlon Symmetric Patella (PE / X3) | groessen_mm: 27 × 8, 29 × 8, 31 × 9, 33 × 9, 36 × 10, 39 × 11 | st1 | belegt |
| `stryker.triathlon.patella_asym` | patella | Triathlon Asymmetric Patella | groessen_mm: 29×33×9, 32×36×10, 35×39×10, 38×42×11, 40×44×11 (S/I × M/L × Höhe, laut Probeteilen) | st1 | belegt (Probeteile S. 44); Implantat-REF nicht übernommen |

## Größen und REF (nur wie im Original gesehen)

**Triathlon CR Femoral Component – zementiert** (`stryker.triathlon.femur_cr_zem`)

| ref_schema | beispiel | seite_quelle |
|---|---|---|
| 5510-F-X01 (links) / 5510-F-X02 (rechts), X = Größe 1–8 | 5510-F-401 / 5510-F-402 = Größe 4 | S. 57 |

**Triathlon CR Femoral Component – zementfrei Beaded mit Peri-Apatite** (`stryker.triathlon.femur_cr_zf`)

| ref_schema | seite_quelle |
|---|---|
| 5517-F-X01 / 5517-F-X02 | S. 57 |

**Triathlon PS Femoral Component – zementiert** (`stryker.triathlon.femur_ps_zem`)

| ref_schema | seite_quelle |
|---|---|
| 5515-F-X01 / 5515-F-X02 | S. 57 |

**Triathlon PS Femoral Component – zementfrei Beaded mit Peri-Apatite** (`stryker.triathlon.femur_ps_zf`)

| ref_schema | seite_quelle |
|---|---|
| 5516-F-X01 / 5516-F-X02 | S. 57 |

**Triathlon Primary Tibial Baseplate – zementiert** (`stryker.triathlon.tibia_primary_zem`)

| ref_schema | beispiel | seite_quelle |
|---|---|---|
| 5520-B-X00 | 5520-B-400 = Größe 4 | S. 57 |

**Triathlon Primary Tibial Baseplate – Beaded mit Peri-Apatite** (`stryker.triathlon.tibia_primary_pa`)

| ref_schema | seite_quelle |
|---|---|
| 5526-B-X00 | S. 57 |

**Triathlon Tritanium Baseplate** (`stryker.triathlon.tibia_tritanium`)

| ref_schema | seite_quelle |
|---|---|
| 5536-B-X00 | S. 310 |

**Triathlon CR Tibial Insert (konventionelles PE / X3)** (`stryker.triathlon.insert_cr`)

| ref_schema | beispiel | seite_quelle |
|---|---|---|
| 5530-P-XNN (PE), 5530-G-XNN bzw. 5530-G-XNN-E (X3); NN = Höhe | 5530-G-409-E = Größe 4, 9 mm X3 | S. 58 |

**Triathlon CS Tibial Insert (PE / X3)** (`stryker.triathlon.insert_cs`)

| ref_schema | seite_quelle |
|---|---|
| 5531-P-XNN / 5531-G-XNN(-E) | S. 59 |

**Triathlon PS Tibial Insert (PE / X3)** (`stryker.triathlon.insert_ps`)

| ref_schema | seite_quelle |
|---|---|
| 5532-P-XNN / 5532-G-XNN(-E) | S. 59–60 |

**Triathlon Symmetric Patella (PE / X3)** (`stryker.triathlon.patella_sym`)

| ref_schema | beispiel | seite_quelle |
|---|---|---|
| 5550-L-DDT (PE), 5550-G-DDT(-E) (X3) | 5550-L-278 = 27 mm × 8 mm | S. 60 |

## Original-Tabellen

**Femur / Insert-Typ** (`T_tri_femur_insert`, st1 S. 2)

- CR zementiert: CR ja, CS ja, PS nein, PSR nein, TS nein
- PS zementiert: CR nein, CS ja, PS ja, PSR ja, TS ja
- TS zementiert: CR nein, CS nein, PS ja, PSR ja, TS ja
- CR Beaded PA (zementfrei): CR ja, CS ja, PS/PSR/TS nein
- PS Beaded PA (zementfrei): CR nein, CS nein, PS ja, PSR ja, TS ja
- _Legende: Größenregel: Femur eine Größe auf/ab zu Insert/Baseplate (z. B. Femur 5 mit Insert/Baseplate 4 oder 6). Gilt für X3-Inserts mit REF-Endung E._

**Baseplate / Insert-Typ** (`T_tri_baseplate_insert`, st1 S. 2)

- Cemented Primary: CR, CS, PS, PSR ja; TS nein
- Cemented Universal: CR, CS, PS, PSR, TS ja
- Beaded PA Primary: CR, CS, PS, PSR ja; TS nein
- Beaded PA Screw Fix*: CR, CS, PS, PSR ja; TS nein (*nicht CE-gekennzeichnet)
- Tritanium: CR, CS, PS, PSR ja; TS nein
- _Legende: Größenregel: Insert nur mit Baseplate gleicher Größe._

**Femur / Patella** (`T_tri_patella`, st1 S. 2)

- Jede Patella (asymmetrisch, symmetrisch, jeweils auch metal-backed) artikuliert mit jedem Femur (CR/PS/TS, zementiert/zementfrei)
- _Legende: gemeinsamer Radius über alle Größen_

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `stryker.triathlon.femur_cr_zem` | `stryker.triathlon.insert_cr` | **bedingt** | Größe ±1 zum Insert | st1 | S. 2 |
| `stryker.triathlon.femur_cr_zem` | `stryker.triathlon.insert_cs` | **bedingt** | Größe ±1 | st1 | S. 2 |
| `stryker.triathlon.femur_cr_zem` | `stryker.triathlon.insert_ps` | **nein** | laut Tabelle | st1 | S. 2 |
| `stryker.triathlon.femur_ps_zem` | `stryker.triathlon.insert_ps` | **bedingt** | Größe ±1 | st1 | S. 2 |
| `stryker.triathlon.femur_ps_zem` | `stryker.triathlon.insert_cs` | **bedingt** | Größe ±1 | st1 | S. 2 |
| `stryker.triathlon.femur_ps_zem` | `stryker.triathlon.insert_cr` | **nein** | laut Tabelle | st1 | S. 2 |
| `stryker.triathlon.femur_cr_zf` | `stryker.triathlon.insert_cr` | **bedingt** | Größe ±1; Femur nicht zementieren | st1 | S. 2 |
| `stryker.triathlon.femur_cr_zf` | `stryker.triathlon.insert_cs` | **bedingt** | Größe ±1 | st1 | S. 2 |
| `stryker.triathlon.femur_ps_zf` | `stryker.triathlon.insert_ps` | **bedingt** | Größe ±1 | st1 | S. 2 |
| `stryker.triathlon.femur_ps_zf` | `stryker.triathlon.insert_cs` | **nein** | laut Tabelle (CS nein bei PS Beaded PA) | st1 | S. 2 |
| `stryker.triathlon.insert_cr` | `stryker.triathlon.tibia_primary_zem` | **bedingt** | gleiche Größe | st1 | S. 2 |
| `stryker.triathlon.insert_ps` | `stryker.triathlon.tibia_primary_zem` | **bedingt** | gleiche Größe | st1 | S. 2 |
| `stryker.triathlon.insert_cs` | `stryker.triathlon.tibia_tritanium` | **bedingt** | gleiche Größe | st1 | S. 2 |
| `stryker.triathlon.patella_sym` | `stryker.triathlon.femur_cr_zem` | **ja** | alle Größen | st1 | S. 2 |
| `stryker.triathlon.patella_asym` | `stryker.triathlon.femur_ps_zem` | **ja** | alle Größen | st1 | S. 2 |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **insert** – insert.groesse == baseplate.groesse: Insert nur mit Baseplate gleicher Größe. (st1 S. 2)
- **femur** – |femur.groesse − insert.groesse| ≤ 1: Femur eine Größe auf oder ab zu Insert/Baseplate. (st1 S. 2)
- **insert** – REF endet auf -E: Kompatibilitätstabelle gilt für X3-Inserts mit REF-Endung E; andere beim Hersteller klären. (st1 S. 2)
- **femur** – zementfrei: Zementfreie Femurkomponenten nicht mit Zement verwenden. (st1 S. 2)
- **insert** – TS: TS-Insert nur mit Cemented Universal Baseplate (Revision, nicht Primärstandard). (st1 S. 2)

## Rückrufe / Sicherheitsinformationen
- keine im Lauf gefunden (nicht systematisch gesucht)

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.
- REF-Schema: X = Größe, NN = Höhe in mm; Endung -E bei X3 beachten.

## Offen
- Aktuelle EU-IFU nicht gelesen.
- Asymmetrische und metal-backed Patella: Implantat-REF nicht übernommen.
- PSR- und TS-Implantat-REF nicht übernommen (TS = Revision).
- Volle REF-Liste je Größe nicht als Tabelle übernommen – nur Schema mit X.

_Neuanlage 08.10.2026 aus Triathlon-Kompendium (Rev. 1, © 2021). verified: false._

