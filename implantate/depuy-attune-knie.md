# DePuy Synthes (J&J MedTech) · ATTUNE Knee System (PS FB, PS RP, CR FB, CR RP, MS FB)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/depuy-attune-knie.json`.

## Quellen
- **da1** – ATTUNE Knee System – INTUITION Instruments Surgical Technique · Stand: DSUS/JRC/0316/1437 Rev. K, © 2022 · Seiten: PDF-S. 2 Konfigurationen; S. 43 Narrow-Größen; S. 68 Patella-Optionen; S. 130 Kompatibilität; S. 132 Essential Product Information · Markt: US-Fassung – kein EU-Ersatz · gelesen: Grok 08.10.2026; OpenAI 07.10.2026 (S. 130) · https://p1.aprimocdn.net/jjamp/en/depuy-synthes/surgical-technique-guide/attune-knee-system-intuition-instruments-dsusjrc03161437.pdf
- **da_fsca** – Swissmedic FSCA – Dringende Sicherheitsinformation ATTUNE zementfreier CR-Femur (falsche Größe, 1 Lot) · Stand: DePuy Ireland, Schreiben 18.08.2023; DPS-Referenz 2293230 · Seiten: S. 1 · Markt: CH · gelesen: Grok 08.10.2026 (Hinweis aus OpenAI 07.10.2026) · https://fsca.swissmedic.ch/mep/api/publications/Vk_20230814_04/documents/1

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `depuy.attune.femur_cr` | femur | ATTUNE CR Femoral Component | kopplung: CR (auch für CS-Anwendung); groessen: 1, 2, 3/3N, 4/4N, 5/5N, 6/6N, 7, 8, 9, 10; narrow: 3–6; fixation: zementiert; zementfreie poröse CR-Variante existiert laut FSCA (mit oder ohne Zement) | da1 | belegt |
| `depuy.attune.femur_ps` | femur | ATTUNE PS Femoral Component | kopplung: PS; groessen: 1, 2, 3/3N, 4/4N, 5/5N, 6/6N, 7, 8, 9, 10 | da1 | belegt |
| `depuy.attune.tibia_fb` | tibia | ATTUNE FB Tibial Base (Fixed Bearing) | groessen: 1–10; plattform: fest | da1 | belegt |
| `depuy.attune.tibia_rp` | tibia | ATTUNE RP Tibial Base (Rotating Platform) | groessen: 1–10; plattform: mobil | da1 | belegt |
| `depuy.attune.insert_fb` | insert | ATTUNE CR, PS und Medial Stabilized FB Tibial Insert | kopplung: CR / PS / MS; groessen: 1–10 (= Femurgröße); hoehen: offen (Original nicht ausgewertet) | da1 | belegt (Größen); Höhen offen |
| `depuy.attune.insert_rp` | insert | ATTUNE CR und PS RP Tibial Insert | kopplung: CR / PS; groessen: 1–10 | da1 | belegt |
| `depuy.attune.allpoly` | tibia | ATTUNE CR und PS All Poly Tibial Component *(nicht Primärstandard)* | fixation: zementiert (laut Kompatibilitätstabelle ±1 Größe) | da1 | belegt |
| `depuy.attune.patella` | patella | ATTUNE Medialized Anatomic / Medialized Dome Patella | groessen_mm: 29, 32, 35, 38, 41; hinweis: Aufteilung der Größen auf Anatomic/Dome laut Tabelle S. 130 am Original prüfen | da1 | belegt (Größenregel) |

## Größen und REF (nur wie im Original gesehen)

**ATTUNE CR Femoral Component** (`depuy.attune.femur_cr`)

| variante | ref | gtin | seite_quelle |
|---|---|---|---|
| zementfrei Porocoat, rechts, Größe 4 | 1504-01-204 | 10603295041474 | da_fsca S. 1 (Rückruf-Lot!) |

## Original-Tabellen

**Femur = Insert-Größe; Tibia-Basis FB/RP; Patella** (`T_attune_modular`, da1 PDF-S. 130)

- F1: Basis 1–3; Patella 29–41
- F2: Basis 1–4; Patella 29–41
- F3/3N: Basis 1–5; Patella 29–41
- F4/4N: Basis 2–6; Patella 32–41
- F5/5N: Basis 3–7; Patella 32–41
- F6/6N: Basis 4–8; Patella 32–41
- F7: Basis 5–9; Patella 35–41
- F8: Basis 6–10; Patella 35–41
- F9: Basis 7–10; Patella 38–41
- F10: Basis 8–10; Patella 38–41
- _Legende: Insert-Größe = Femurgröße; Insert ±2 Größen zur Basis (Ref. Number 103262475)._

**Femur / All-Poly-Tibia** (`T_attune_allpoly`, da1 PDF-S. 130)

- F1: 1–2
- F2: 1–3
- F3/3N: 2–4
- F4/4N: 3–5
- F5/5N: 4–6
- F6/6N: 5–7
- F7: 6–8
- F8: 7–9
- F9: 8–10
- F10: 9–10
- _Legende: ±1 Größe_

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `depuy.attune.femur_cr` | `depuy.attune.insert_fb` | **bedingt** | CR-Insert gleiche Größe wie CR-Femur; Insert ±2 Größen zur Basis | da1 | PDF-S. 132/130 |
| `depuy.attune.femur_ps` | `depuy.attune.insert_fb` | **bedingt** | PS-Insert gleiche Größe wie PS-Femur; ±2 zur Basis | da1 | PDF-S. 132/130 |
| `depuy.attune.femur_cr` | `depuy.attune.insert_rp` | **bedingt** | CR-RP-Insert, Größe laut Tabelle | da1 | PDF-S. 130 |
| `depuy.attune.insert_fb` | `depuy.attune.tibia_fb` | **bedingt** | ±2 Größen | da1 | PDF-S. 132/130 |
| `depuy.attune.insert_rp` | `depuy.attune.tibia_rp` | **bedingt** | ±2 Größen | da1 | PDF-S. 130 |
| `depuy.attune.allpoly` | `depuy.attune.femur_cr` | **bedingt** | ±1 Größe | da1 | PDF-S. 132/130 |
| `depuy.attune.patella` | `depuy.attune.femur_cr` | **bedingt** | 38/41 mm alle Femurgrößen; 29 mm nur F1–3; 32 mm nur F1–6; 35 mm nur F1–8 | da1 | PDF-S. 132 |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **insert** – insert.groesse == femur.groesse: CR/PS-Insert gleiche Größe wie Femur; innerhalb 2 Größen der Basis. (da1 PDF-S. 132)
- **patella** – femur.groesse: 29 mm nur F1–3, 32 mm nur F1–6, 35 mm nur F1–8, 38/41 mm alle. (da1 PDF-S. 132)
- **fremd** – nicht mischen: Implantate und Probeteile anderer Hersteller/Systeme nie zusammen verwenden. (da1 PDF-S. 132)

## Rückrufe / Sicherheitsinformationen
- depuy.attune.femur_cr · CH (Swissmedic FSCA, DePuy Ireland 18.08.2023) · lot-spezifisch: REF 1504-01-204, Lot 3883327 (zementfreier CR-Femur rechts Gr. 4, Maße einer Gr. 5) – keine allgemeine Sperre

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.

## Offen
- Nur US-Dokument (Rev. K 2022) gelesen – EU-IFU/Katalog offen.
- REF der zementierten Standardkomponenten nicht gesehen.
- Insert-Höhen nicht ausgewertet.
- Zementfreie ATTUNE-Komponenten (außer FSCA-Beispiel) offen.

_Neuanlage 08.10.2026 aus ATTUNE INTUITION ST Rev. K (US) und Swissmedic-FSCA. verified: false._

