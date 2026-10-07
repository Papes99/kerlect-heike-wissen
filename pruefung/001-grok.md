# Prüfung 001-hueft-tep v1.2 – Grok – 07.10.2026

Scope: nur Delta v1.1→v1.2 (Nr 1–11) + Implantate-Umsetzung laut ASTRA.md (Nr 1–10). Quellen selbst geöffnet (pdftotext). Nichts erfunden.

## 001-hueft-tep (v1.1 → v1.2)

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| 1 | ok | umgesetzt wie beschrieben (nicht auszuschließen / Kat. IB; `hausabhaengig: false`) | – | KRINKO Prävention postop. WI 2018, gedr. S. 461 (PDF-S. 14), Abschn. 4.1 Kat. IB · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 2 | ok | umgesetzt wie beschrieben (hausabhängig, Rückmeldung Anästhesie; `quelle: null`) | – | keine (Praxis; stützt BCIS-Kommunikation, Zuständigkeit Haus-SOP) | – |
| 3 | ok | umgesetzt wie beschrieben (Stopper vs. Messhilfe; hausabhängig) | – | keine (Haus-Zählplan / Produkt-IFU; Bezug APS belassenes Material) | – |
| 4 | ok | umgesetzt wie beschrieben (nur Antiseptikum-Regel, Q_KRINKO; NE getrennt). `gilt_fuer: hf_mono` laut Astra belassen – allgemeine Regel steht in 000. | – | KRINKO 2018, S. 461 (PDF-S. 14), Abschn. 4.1 Kat. II · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf · Brandrisiko ergänzend HEBU GAHF113V004 Abschn. 6 | – |
| 5 | ok | umgesetzt wie beschrieben (HEBU Flüssigkeitsschutz; Haus-IFU maßgeblich) | – | HEBU medical, Einmal-Neutralelektroden GAHF113V004, 20.02.2026, Abschn. 5.2 (keine Flüssigkeitsberührung) und Abschn. 8 (kein Eindringen unter NE) · https://www.hebumedical.de/ga/GAHF113.pdf | – |
| 6 | ok | umgesetzt wie beschrieben (Mathys offen; Accolade-II-Hemi-Grenze; keine Cross-Hersteller-Kombi) | – | Accolade II Surgical Protocol ACCII-SP-1_Rev-4_34423 ©2022, S. 3/12 · https://cdn.stryker.com/SYKGCSDOC-2-45343 | – |
| 7 | ok | Alt-offen mit missverständlicher Duokopf-Formulierung gestrichen | – | – | – |
| 8 | ok | umgesetzt wie beschrieben (neutrale Rückfrage + Hemi-Warnung Accolade II) | – | ACCII-SP-1_Rev-4_34423 ©2022, S. 3/12 · https://cdn.stryker.com/SYKGCSDOC-2-45343 | – |
| 9 | ok | Alt-julian mit Accolade-II als Duokopf-Beispiel ohne Warnung gestrichen | – | – | – |
| 10 | ok | umgesetzt wie beschrieben (S. 461 / PDF-S. 14, Abschn. 4.1; Antiseptikum Kat. II + Abdeckung Kat. IB) | – | KRINKO Empf_postopWI.pdf selbst geprüft 07.10.2026 · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 11 | ok | umgesetzt wie beschrieben (ACCII-SP-1 Rev-4; S. 3/12; Dokumentcode S. 25) | – | Accolade II Femoral Hip System – Surgical protocol, ACCII-SP-1_Rev-4_34423 ©2022 · https://cdn.stryker.com/SYKGCSDOC-2-45343 | – |

**Sum 001:** 11× ok · 0× Fehler

## Implantate (stryker-accolade-ii, smith-nephew-polarstem)

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| 1 | ok | beide `verified: false` + Teilprüfung/Markt-Hinweis | – | Umsetzung ASTRA Implantat-Prüfung | – |
| 2 | ok | q1-Seiten: 3/12 EU-Grenze, 5 CCD, 12 Köpfe, 15/17 Hülsen | – | ACCII-SP-1_Rev-4_34423 ©2022, S. 5 (132°/127°), S. 3/12, 12, 15/17 · https://cdn.stryker.com/SYKGCSDOC-2-45343 | – |
| 3 | ok | UHR nur Japan-Katalogzuordnung; EU offen; Hemi-Sperre über q1 | – | Stryker Japan HE01-160_Rev1 03/2022 PDF-S. 2; EU-Sperre ACCII-SP-1 S. 3/12 | – |
| 4 | ok | Universal-Taper: Familie 6519-T-XX, keine Muster-REF; Hülse nach Offset/IFU | – | ACCII-SP-1 S. 12 (6519-T-XXX / konkrete Offsets 6519-T-025/100/204) | – |
| 5 | ok | Regel P1: Hülse zuerst auf Schaftkonus, nicht im Keramikkopf vormontieren | – | ACCII-SP-1 S. 15 Final reduction / Notes | – |
| 6 | ok | Quelle: Rev. 2, 06/2021, Markt USA (S. 1), S. 4/2/5 | – | POLARSTEM IFU 81098832 Rev. 2, 06/2021, S. 1 „US only“ · https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283 | – |
| 7 | ok | zementfrei als US-Daten; Standard/lateral auch mit Kragen; EU offen | – | POLARSTEM IFU S. 1/4 Device Description | – |
| 8 | ok | zementiert US-Daten; OXINIUM/BIOLOX delta; keine pauschale EU-Regel | – | POLARSTEM IFU S. 1/4/5 (Cemented stem only with OXINIUM or BIOLOX delta) | – |
| 9 | ok | Regel P2: gleicher Konus/Keramikmarke ≠ Kombinationsnachweis | – | POLARSTEM IFU S. 2/5 Combination restrictions | – |
| 10 | ok | offen: aktuelle EU-IFU POLARSTEM nachfordern | – | – | – |

**Sum Implantate:** 10× ok · 0× Fehler

## Zusatz (Praxis)
- PDF-Zuordnung KRINKO: PDF-S. 13=460 · 14=461 · 15=462. 001-Fundstelle S. 461 für Abdeckung/Antiseptikum korrekt; in **000** steht Inzisionsfolie/Türen fälschlich noch unter S. 460 (siehe `pruefung/000-grok.md` Nr 9).
- Zement-Kommunikation: 001 Chip + Heike korrekt `Q_BCIS`; 000 noch `q_amboss` bei BCIS-Wortlaut (Widerspruch Quellenfeld, Inhalt gleich).
- `Alkoholansammlungen` / `Keine Antiseptikum-Pfützen`: inhaltlich deckungsgleich; Scope-Trennung (001 `hf_mono` vs 000 `alle`) laut Astra gewollt – kein fachlicher Widerspruch.
