# Lauf 001-implantate-luecken – Lücken der Hüft-Implantat-Dateien schließen

_Claude (Cloud), Start 07.10.2026 · Pipeline NEU · Perplexity-Quellen: `pruefung/001-implantate-luecken-perplexity.md` (Repo-Stand 9ad0cb1)_

Betrifft **nur `implantate/*`** (11 Systemdateien). Ziel: Werte, die bisher „offen“ sind, am **Original** übernehmen – mit Dokument, Kennung/Revision, Stand, **Seite** (gedruckt + PDF) und Markt. Perplexity-Funde sind nur Fundstellen.

**Regeln:** Original selbst öffnen · Werte wörtlich · Systeme nicht mischen · Nein-Zeilen/Fußnoten mitnehmen · nichts aus Fremdmarkt (US/JP/AU) als EU übernehmen, nur als „kein EU-Ersatz“ · nicht Lesbares markieren · keine PDFs/Bilder ins Repo.

## Zur Prüfung in diesem Lauf

### Stryker (`stryker-accolade-ii`)
1. **EU-eIFU** (labeling.stryker.com, Land DE): Accolade II QIN 4424, V40 CoCr QIN 4451, V40 Keramik QIN 4355, Trident II QIN 4450, X3 QIN 4351 – Ausgabe/Stand, Indikationen/Kontraindikationen, Kombinationsvorgaben.
2. **X3 26 mm**: laut Perplexity im DE-eIFU zwei 26-mm-X3-10°-Inserts gelistet – welche Schalen (Alpha)? Konflikt Tabelle 1 vs. Katalog auflösen.
3. **Accolade-II-Implantat-REF** aus Design Rationale ACCII-PG-3 Rev-1 (PDF-S. 12) – Markt prüfen.

### Smith+Nephew (`smith-nephew-r3`)
4. **POLARSTEM EU-OP-Technik** 01217-en V7 10/24 (CE 0123): Implantate PDF-S. 16, Dimensions PDF-S. 18–19 – Größen/REF/CCD/Kragen zementfrei + zementiert; ersetzt US-IFU.
5. **Matrix 04758 Ed. 05/26 V12 PDF-S. 1**: POLARSTEM-Spalten × Hausköpfe (OXINIUM, CoCr, BIOLOX delta) inkl. Nein-Zeilen.

### Medacta (`medacta-quadra-amistem`) – bisher nur Register
6. OP-Techniken Quadra-H (99.14HSClat.42), Quadra-P (99.14PS.42), Quadra/Quadra-C (99.14HSC.12), AMIStem-P (99.14ASTEMPS.42), AMIStem/-C (99.14ASTEM.12), Versafitcup CC Trio (99.16TRIO.42): Größen, REF, Konus, Liner/Kopf-Tabellen, max. Kopf-Ø je Pfanne.
7. **Kombinationstabelle** 99.99.COM rev. 12 (Kopf/Schaft, Kopf/Liner) und **IFU Hip Prosthesis** 75.09.017 rev. 26 (Kompatibilität S. 5 / DE S. 19).
8. **Bipolarkopf** (99.19.42) und **Endokopf** (99.18.12): Größen, Innenkopf, freigegebene Schäfte (AMIStem-C?).

### Zimmer Biomet (`zimmer-biomet`)
9. **Avenir (nicht Complete)** OP-Technik 4034.2-GLBL-en 2024-04: zementfrei/zementiert, was ist belegt (Größen?).
10. **Kopf-Tabellen je Schaft** 87-6204-051-00 Rev. 1 (Keramik 12/14) und 87-6204-951-00 Rev. 1 (CoCr/Freedom): Zeilen Avenir, CLS Spotorno, Alloclassic SL/SLL/SLO, Fitmore, MS-30 – Ø/Halslänge/REF.
11. **Flachprofil = Low Profile PE cup?** Tabelle C2 (rev. 2/15/2023): Zuordnung bestätigen, Größen/Kopf-Ø.
12. **Allofit/Allofit-S** Liner ↔ Kopf („Modular Liners and Cups“ rev. 05/03/2019), Schrauben C3.
13. **Bipolarkopf (AP) 1946/1989**: Innenkopf/Schaft laut Chart + Fußnoten.

### Mathys/Enovis (`enovis-optimys`, `enovis-twinsys`)
14. **optimys** OP-Technik 316.010.109 04-0920 (laut Versionsübersicht aktuell): Größen/REF S. 18, Dimensionen S. 24.
15. **RM Pressfit vitamys** OP-Technik 02-0522 (Nachfolger 316.010.164): Größen.
16. **Kopf-Kompatibilitäts-Chart** 316.010.157 01-1020: twinSys/optimys-Köpfe (ceramys, symarec, CoCr) inkl. Einschränkungsliste.
17. **Bipolar- und Hemikopf** 336.010.147 01-0719: Außen-/Innenkopf, freigegebene Schäfte (twinSys zementiert?).
18. **seleXys PC** 316.010.123 04-1019: PE-Einsatz standard/überhöht, Zuordnung S. 11–12/19.
Hinweis: Mathys-Download verlangt Fachkreis-Bestätigung – Zugang dokumentieren.

### DePuy Synthes (`depuy-corail-pinnacle`)
19. **PINNACLE** 142532-220805: PDF-S. 8 Schalen-Trial ↔ Liner-Trial (Abb. 13b) + Kopf-Ø-Farbcode; PDF-S. 18 Keramikliner – ergibt sich eine belegte Schale × Liner × Kopf-Zuordnung?
20. **ARTICUL/EZE-Köpfe** Bestellseite C-STEM AMT 143325-200907 S. 32: Ø/Offsets je Material; **CORAIL-REF** 198918 S. 24–26.
21. **TRILOC II, SELF-CENTERING Bipolar, Cathcart**: REF aus MRT-Broschüre 101721-221012 (S. 41/42/48) – nur REF, keine Freigaben; EU-Freigabe Self-Centering + CORAIL zementiert weiter suchen (e-ifu.com).

### Aesculap / Link (Dateien von Julian, erstmals prüfen)
22. **`aesculap-bicontact`, `aesculap-corehip`, `link-spii-lubinus`**: Werte, Seiten, Markt und Kombinationen am Original gegenprüfen (Schema v1.1).
23. **Aesculap Plasmafit Poly** UHMWPE/Vitelene-Liner PDF-S. 12, 18–19; Bipolar Cup × Excia T zementiert weiter suchen.

## Ergebnis-Format
- **Grok** (ganze Paketversion = alle 23 Punkte): `Nr · ok/Fehler/nicht gefunden · Befund · Wert/Tabelle wörtlich · Dokument + Kennung + Stand + Seite + Markt · Vorschlag` → `pruefung/001-implantate-luecken-grok.md`.
- **OpenAI** (nur Implantate: Herstellerangaben, Kompatibilitätstabellen, Indikationsgrenzen – keine Instrumente): liest Basis, Perplexity, Grok und `implantate/*`, ändert nichts; je Grok-Punkt bestätigt/korrigiert/abgelehnt + eigene Punkte; Ergebnis FREIGEGEBEN/ÄNDERN → `pruefung/001-implantate-luecken-openai.md`.
