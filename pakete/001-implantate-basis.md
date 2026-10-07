# Lauf 001-implantate – Implantat-Dateien der Hüft-TEP (Extra-Lauf)

_Claude, Arbeit 1 · Start 07.10.2026 03:55Z · Grundlage: `implantate/*.json` (Stand nach 001 v1.3) + `eingang/001-perplexity-2.md`_

Dieser Lauf betrifft **nur die vier Implantat-Dateien** der Haussysteme. Paket 001 (`pakete/001-abschluss.md`) und 000 bleiben unverändert.

| Datei | System im Haus |
|---|---|
| `implantate/stryker-accolade-ii.json` | Accolade II (zementfrei), Trident II Tritanium, X3, V40 BIOLOX delta + V40 CoCr (LFIT) |
| `implantate/aesculap-excia.json` | Excia T, Excia T zementiert, Plasmafit Plus/Poly, PE-Pfanne zementiert, BIOLOX delta Inlay, BIOLOX delta + Isodur CoCr, Bipolar Cup |
| `implantate/smith-nephew-r3.json` | SL-PLUS MIA, SPECTRON EF, R3, REFLECTION (zementfrei/All-Poly), Müller-PE-Pfanne, R3 XLPE, OXINIUM/BIOLOX delta/CoCr, Bi-Polar Head |
| `implantate/enovis-twinsys.json` | twinSys zementfrei/zementiert, RM Classic, seleXys PC, ccB-Pfanne, PE-Inlay, ceramys/symarec/CoCr, Mathys Bipolarkopf |

**Regeln für diesen Lauf**
- Nur offizielle Herstellerdokumente und Behörden; Original selbst öffnen. Jeder Wert mit Dokument, Kennung/Revision, Stand und **Seite** (gedruckt und PDF-Seite).
- Markt immer angeben (EU/US/JP/BR …). Fremdmarkt ersetzt keine EU-IFU.
- **Systeme nicht mischen:** Kombination nur, wenn der Hersteller sie ausdrücklich für genau diese Komponenten nennt. Gleicher Konus oder gleiche Keramikmarke ist kein Nachweis.
- Nichts schätzen, nichts aus ähnlichen Systemen oder älteren Ausgaben ableiten. Was nicht lesbar ist: **„nicht gefunden“** bzw. **„nicht lesbar“** mit Grund.
- Keine PDFs, Volltexte oder Bilder ins Repo – nur Links, Seiten und die übernommenen Werte.
- Größen/Werte als Tabelle so, wie sie im Dokument stehen (Größenbezeichnung, ggf. REF, Seite). REF nur, wenn im Dokument lesbar.

## Zur Prüfung in diesem Lauf

### A. Stryker – `stryker-accolade-ii`
1. **Accolade II Größenreihe** (Größen, CCD-Varianten 127°/132°) aus ACCII-SP-1_Rev-4_34423 – Seite angeben.
2. **V40 CoCr (LFIT):** Ø und Offsets laut ACCII-SP-1 S. 12 übernehmen; prüfen, ob die vorhandenen BIOLOX-delta-Offsets (28: −4/−2,7/0/+4; 32: −4/0/+4; 36: −5/−2,5/0/+2,5/+5/+7,5) stimmen.
3. **Trident II Tritanium:** Schalengrößen, passende X3-Inlays und **max. Kopf-Ø je Schale** aus TRITRI-SP-3_Rev-6_29553 Tabelle 1 (S. 4) und Katalog (S. 21). X3-Varianten mit EU-Status (X3 Eccentric 0° laut Tabelle nicht CE).
4. **EU-IFUs** Accolade II, V40-Köpfe, Trident X3 (QIN 4351): Perplexity fand nur BR-Fassung (ifu.stryker.com.br/documentos/download/44) – EU-Fassung auf ifu.stryker.com suchen.
5. **Rückrufe – neuer Stand laut Perplexity:**
   - LFIT CoCr: FDA Z-2299-2018 (Event 80059) **terminated 08.05.2020** – nur US; EU-Abschluss zu RA2018-1757583 suchen.
   - BIOLOX delta V40: FDA Z-0842-2022 (Event 89592, PFA 2902313) „Open, Classified“ – ist das dieselbe Maßnahme wie EU RA2022-2911584? Nur übernehmen, wenn das Dokument die Zuordnung zeigt.
6. **ACCII-TL-1 Tray Layout (q2):** Stand und Seiten offen – lesen oder als „nicht lesbar“ markieren.

### B. Aesculap – `aesculap-excia`
7. **Excia T zementfrei und Excia T zementiert:** Größenreihe aus Nr. 4008516 01/2026 (Implantatübersicht gedr. S. 18–19 / PDF 10; laut Perplexity zementierte Implantation S. 16–17, Übersicht S. 19).
8. **Plasmafit Plus / Poly:** Größen und Liner-Optionen aus O45502 S. 5–7; Köpfe/ISODUR F PDF 24.
9. **Neu (Perplexity): Excia 12/14 zementiert, O90301 (11/2019), S. 14/16 inkl. ISODUR-F-Köpfe.** Bitte nur klären: Ist das ein **anderer Schaft** als Excia T zementiert? Nichts daraus auf Excia T übertragen.
10. **Bipolar Cup:** B. Braun-Seite „Zementierte Hüftprothese“ (bbraun.de …/zementierte-hueftprothese.html, Abschnitt Operationstechniken) – was steht dort genau zu Bipolar Cup + Excia T zementiert? Gibt es eine verlinkte OP-Technik/IFU mit ausdrücklicher Freigabe?
11. **Zementierte PE-Pfanne:** genaue Produktbezeichnung und Dokument (Katalog PRID00002464 „Cemented Polyethylene Cups“).

### C. Smith+Nephew – `smith-nephew-r3`
12. **Matrix 04758 neu: Ed. 10/24, V12, alle 7 Seiten** (smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de) ersetzt die bisherige Einzelseite V11. Bitte für die **Hausköpfe (OXINIUM, BIOLOX delta, CoCr)** die Zeilen zu **SL-PLUS MIA (S. 2)** und **SPECTRON (S. 6)** wörtlich übernehmen (Kopf-Ø, Halslängen, zulässig ja/nein, Seite). Länder-/Gültigkeitsvermerke mit angeben.
13. **SL-PLUS MIA Größenreihe** aus 00884-en V4 01/15 (Seiten offen).
14. **SPECTRON EF Größenreihe** aus 21885 V3 REVB 03/23.
15. **R3:** Schalen-/Inlay-Zuordnung aus 7138-1560-de REVB (PDF 13) und XLPE-Katalog (PDF 17–18); EU-IFU über ifu.smith-nephew.com (braucht REF/IFU-Nr.).
16. **REFLECTION zementfrei / All-Poly, Müller-PE-Pfanne:** EU-Dokument suchen. Perplexity fand nur JP-Dokument (…/77555ee941a84e2fa059dbeeeed99636) – kein EU-Ersatz.
17. **Bi-Polar Head:** TANDEM Bipolar/Unipolar INTL Surgical Technique (smith-nephew.com …/tandem) – Heißt das Hausprodukt „Bi-Polar Head“ oder „TANDEM Bipolar“? Steht SPECTRON EF ausdrücklich als freigegebener Schaft drin?
18. **Rückrufe R-2023-13 und R-2020-04:** Abschlussmeldung vorhanden?

### D. Enovis – `enovis-twinsys`
19. **Aktuelle Enovis-Seiten** (enovis-surgical.com/en/products/327 twinSys uncemented, /328 cemented, /321 RM Classic, /332 Ceramic, /333 Metal, /335 Bipolar; /resources.html: twinSys-Flyer EN, CCB–CCE Surgical Technique EN): Was ist ohne Login lesbar? Größen/Kombinationen nur aus PDF mit Seite.
20. **seleXys PC und „PE-Inlay Standard“:** Dokument und genaue Bezeichnung (welche Pfanne?).
21. **Mathys Bipolarkopf + twinSys zementiert:** ausdrückliche Freigabe vorhanden?

## Ergebnis-Format (Grok und Astra)
Je Punkt: **Nr. · Befund · Wert/Tabelle · Dokument + Kennung + Stand + Seite + Markt · Vorschlag (übernehmen / nicht / offen lassen)**. Am Ende Abschnitt „Nicht gefunden“.
