# Zimmer Biomet · Persona The Personalized Knee (primär: CR, MC, UC, PS, CPS)

_Region Knie · Version 1.0 · Stand Extrakt 2026-10-08 · **verified: false** · gehört zu Paket 002 (Knie-TEP)_

Nur Daten aus Hersteller-Originalen mit Fundstelle. **Keine Bilder, keine PDF-Volltexte im Repo.** Systeme nicht mischen. Maschinenlesbar: `implantate/zimmer-biomet-persona-knie.json`.

## Quellen
- **zp1** – Persona The Personalized Knee – Surgical Technique · Stand: 3914.1-GLBL-en, Issue Date 2022-08 (MC258599) · Seiten: PDF-S. 4 Indikation/Fixation; S. 5 Kopplung; S. 6 Blutsperre; S. 31 Patella; S. 34/36 Standard/Narrow; S. 44 Insert-Höhen; S. 47–50 Implantation + REF-Beispiele; S. 70–72 Kompatibilität (gedruckt = PDF − 2) · Markt: global (englisch), Legal Manufacturer Zimmer Inc. USA; EU-IFU nicht gelesen · gelesen: Grok 08.10.2026; REF-Beispiele auch in pruefung/002-openai.md (OpenAI 07.10.2026) · https://assets.ctfassets.net/rc4arfpyhdpw/6R1FpGyC07WTfcszrO2MKP/710ce1e70eb68bda7a449e07909f4859/persona-the-personalized-knee-surgical-technique1.pdf

## Komponenten

| ID | Typ | Bezeichnung | Attribute | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `zb.persona.femur_cr` | femur | Persona CR Femurkomponente | kopplung: CR; groessen: 1–12; profile: Größe 1–2 nur narrow, 12 nur standard, 3–11 standard und narrow; seiten: links/rechts; fixation: zementiert; poröse Variante zementiert oder zementfrei (PDF-S. 4) | zp1 | belegt (Original, 1 Prüfer) |
| `zb.persona.femur_ps` | femur | Persona PS Femurkomponente | kopplung: PS; groessen: 1–12; profile: wie CR (PDF-S. 36); seiten: links/rechts; fixation: zementiert; poröse Variante zementiert oder zementfrei | zp1 | belegt (Original, 1 Prüfer) |
| `zb.persona.tibia` | tibia | Persona Tibiakomponente (u. a. Stemmed Cemented) | groessen: A, B, C, D, E, F, G, H, J (Farbcodes Orange/Gelb/Grün/Blau/Grau je Paar); seiten: links/rechts; fixation: nicht-poröse zementiert; poröse zementiert oder zementfrei | zp1 | belegt (Original, 1 Prüfer) |
| `zb.persona.insert_cr` | insert | Persona CR Tibial Articular Surface | kopplung: CR; hoehen_mm: 10–18 (15 nicht erhältlich); bezeichnung_groesse: Femurbereich/Tibiapaar, z. B. 3-11/EF | zp1 | belegt |
| `zb.persona.insert_mc` | insert | Persona MC (Medial Congruent) Tibial Articular Surface | kopplung: MC; hoehen_mm: 10–20 (15, 17, 19 nicht erhältlich); hkb: mit oder ohne HKB | zp1 | belegt |
| `zb.persona.insert_uc` | insert | Persona UC (Ultracongruent) Tibial Articular Surface | kopplung: UC; hoehen_mm: 10–20 (15, 17, 19 nicht erhältlich); hkb: nicht bei vorhandenem HKB; hinweis: nur In-vivo-Montage empfohlen (PDF-S. 49) | zp1 | belegt |
| `zb.persona.insert_ps` | insert | Persona PS Tibial Articular Surface | kopplung: PS; hoehen_mm: 10–20 (15, 17, 19 nicht erhältlich) | zp1 | belegt |
| `zb.persona.insert_cps` | insert | Persona CPS (Constrained Posterior Stabilized) Articular Surface *(nicht Primärstandard)* | kopplung: CPS; hinweis: nur mit zementierten nicht-porösen Femur- und Tibiakomponenten; eigene OP-Technik 97-5026-072-00 | zp1 | belegt (Regeltext); REF nicht gesehen |
| `zb.persona.patella` | patella | Persona All-Poly Patella (Standard) | groessen_mm: 26 × 7,5, 29 × 8,0, 32 × 8,5, 35 × 9,0, 38 × 9,5, 41 × 10,0; fixation: nur zementiert; inset: 26 mm immer inset; 29/32 mm inset bei PS-Femur 10–12 | zp1 | belegt |

## Größen und REF (nur wie im Original gesehen)

**Persona CR Femurkomponente** (`zb.persona.femur_cr`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 7 | rechts | 42-5026-062-02 | PDF-S. 48 |

**Persona PS Femurkomponente** (`zb.persona.femur_ps`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 7 | rechts | 42-5006-062-02 | PDF-S. 48 |

**Persona Tibiakomponente (u. a. Stemmed Cemented)** (`zb.persona.tibia`)

| groesse | seite | variante | ref | seite_quelle |
|---|---|---|---|---|
| F | rechts | Stemmed Cemented | 42-5320-075-02 | PDF-S. 47/49 |

**Persona CR Tibial Articular Surface** (`zb.persona.insert_cr`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 3-11/EF | rechts | 42-5210-005-10 | PDF-S. 49 |

**Persona MC (Medial Congruent) Tibial Articular Surface** (`zb.persona.insert_mc`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 6-7/EF | rechts | 42-5221-007-10 | PDF-S. 49 |

**Persona UC (Ultracongruent) Tibial Articular Surface** (`zb.persona.insert_uc`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 4-11/EF | rechts | 42-5212-005-10 | PDF-S. 49 |

**Persona PS Tibial Articular Surface** (`zb.persona.insert_ps`)

| groesse | seite | ref | seite_quelle |
|---|---|---|---|
| 6-9/EF | rechts | 42-5214-007-10 | PDF-S. 49 |

**Persona All-Poly Patella (Standard)** (`zb.persona.patella`)

| groesse | ref | seite_quelle |
|---|---|---|
| 32 mm | 42-5400-000-32 | PDF-S. 50 |

## Original-Tabellen

**CR-Femur / CR-Insert / Tibia** (`T_persona_cr`, zp1 PDF-S. 70)

- Tibia A–B: Femur 1–2 (Insert 1-2/AB), Femur 3–6 (3-6/AB)
- Tibia C–D: Femur 1–2 (1-2/CD), Femur 3–9 (3-9/CD)
- Tibia E–F: Femur 3–11 (3-11/EF)
- Tibia G–H: Femur 7–12 (7-12/GH)
- Tibia J: Femur 9–12 (9-12/J)
- _Legende: Aus PDF-Text extrahiert; vor App-Nutzung am Original gegenprüfen._

**CR-Femur / MC-Insert / Tibia** (`T_persona_mc`, zp1 PDF-S. 70)

- Tibia A–B: Femur 1–2, 3–4
- Tibia C–D: Femur 4–5, 6–7, 8–9
- Tibia E–F: Femur 4–5, 6–7, 8–11
- Tibia G–H: Femur 8–11, 12
- Tibia J: Femur 12
- _Legende: Aus PDF-Text extrahiert; Spaltenzuordnung am Original prüfen._

**CR-Femur / UC-Insert / Tibia** (`T_persona_uc`, zp1 PDF-S. 70)

- Tibia A–B: Femur 1–2, 3–4
- Tibia C–D: Femur 1–2, 3–7
- Tibia E–F: Femur 4–11
- Tibia G–H: Femur 7–12
- Tibia J: Femur 9–12
- _Legende: Aus PDF-Text extrahiert._

**PS-Femur / PS- bzw. CPS-Insert / Tibia (identisch)** (`T_persona_ps_cps`, zp1 PDF-S. 71)

- Tibia A–B: Femur 1–2, 3–5
- Tibia C–D: Femur 1–2, 3–5, 6–9
- Tibia E–F: Femur 3–5, 6–9, 10–11
- Tibia G–H: Femur 6–9, 10–12
- Tibia J: Femur 10–12
- _Legende: Aus PDF-Text extrahiert._

## Passt zu

| von | zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `zb.persona.femur_cr` | `zb.persona.insert_cr` | **bedingt** | HKB intakt; Größe laut T_persona_cr | zp1 | PDF-S. 5/70 |
| `zb.persona.femur_cr` | `zb.persona.insert_mc` | **bedingt** | mit oder ohne HKB; Größe laut T_persona_mc | zp1 | PDF-S. 5–6/70 |
| `zb.persona.femur_cr` | `zb.persona.insert_uc` | **bedingt** | nur bei reseziertem/insuffizientem HKB; Größe laut T_persona_uc | zp1 | PDF-S. 5–6/70 |
| `zb.persona.femur_cr` | `zb.persona.insert_ps` | **nein** | CR-Femur nicht mit PS- oder CPS-Insert | zp1 | PDF-S. 5 |
| `zb.persona.femur_cr` | `zb.persona.insert_cps` | **nein** | CR-Femur nicht mit PS- oder CPS-Insert | zp1 | PDF-S. 5 |
| `zb.persona.femur_ps` | `zb.persona.insert_ps` | **bedingt** | Größe laut T_persona_ps_cps | zp1 | PDF-S. 5/71 |
| `zb.persona.femur_ps` | `zb.persona.insert_cps` | **bedingt** | nur zementierte nicht-poröse Femur- und Tibiakomponenten | zp1 | PDF-S. 5/71 |
| `zb.persona.femur_ps` | `zb.persona.insert_cr` | **nein** | PS-Femur nicht mit CR-, MC- oder UC-Insert | zp1 | PDF-S. 5 |
| `zb.persona.femur_ps` | `zb.persona.insert_mc` | **nein** | PS-Femur nicht mit CR-, MC- oder UC-Insert | zp1 | PDF-S. 5 |
| `zb.persona.femur_ps` | `zb.persona.insert_uc` | **nein** | PS-Femur nicht mit CR-, MC- oder UC-Insert | zp1 | PDF-S. 5 |
| `zb.persona.patella` | `zb.persona.femur_ps` | **bedingt** | 29/32 mm bei PS-Femur 10–12 nur inset; 26 mm immer inset | zp1 | PDF-S. 31 |

_ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben._

## Regeln
- **insert** – femur.kopplung passt: PS-Femur nur mit PS/CPS; CR-Femur mit CR/MC/UC (UC nur ohne HKB). (zp1 PDF-S. 5)
- **insert** – hoehe in 10,11,12,13,14,16,18,20: CR maximal 18 mm; 15/17/19 mm nicht erhältlich. (zp1 PDF-S. 44)
- **insert** – nicht wiederverwenden: Insert nur einmal einsetzen, nie erneut auf eine Tibia setzen. (zp1 PDF-S. 48)
- **alle** – Kompatibilität vor Implantation: Vor dem Implantieren prüfen, dass alle Komponenten kompatibel sind. (zp1 PDF-S. 47)
- **reihenfolge** – femur.kopplung: CR-Femur: Tibia zuerst; PS-Femur: Femur zuerst (Technik-Empfehlung). (zp1 PDF-S. 49)
- **zement** – Portionen: Bei zementierten Komponenten zwei Zementportionen empfohlen; Zement nach Hersteller-IFU. (zp1 PDF-S. 47)

## Rückrufe / Sicherheitsinformationen
- keine im Lauf gefunden (nicht systematisch gesucht)

## Hinweise
- Vor dem Öffnen Komponente, Seite, Größe, Typ und Insert-Höhe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen – Registerbeobachtungen sind keine Freigabe.
- Nicht dokumentierte Kombinationen: offen – Operateur bzw. Hersteller fragen.

## Offen
- EU-IFU/Packungsbeilage nicht gelesen; nur globale OP-Technik 2022-08.
- Vollständige REF-Matrix (alle Größen/Seiten/Höhen) nicht übernommen – nur Beispiele aus der OP-Technik.
- Porous-/Trabecular-Metal-Varianten: Bezeichnungen und REF offen.
- Kreuzkompatibilität Persona-CR-Femur mit NexGen-Tibia/Inserts (PDF-S. 72) nicht übernommen.
- Personalized-Alignment-Technik laut Dokument in der EU nicht lizenziert (PDF-S. 4).

_Neuanlage 08.10.2026 aus Persona-OP-Technik 2022-08. verified: false. Tabellen aus PDF-Text extrahiert – am Original gegenprüfen._

