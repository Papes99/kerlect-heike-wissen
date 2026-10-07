# Lauf 001-implantate-dach – häufigste Hüft-TEP-Systeme in DACH (Extra-Lauf)

_Claude, Arbeit 1 · Start 07.10.2026 05:30Z · Auftrag Julian: „Implantate DACH los“_

**Ziel:** Die Implantat-Auswahl richtet sich nach der **Häufigkeit in Deutschland, Österreich und der Schweiz** (Register), nicht nach einer Klinik. Bisher vorhanden (v1.1, bleibt unverändert): Stryker Accolade II/Trident II, Aesculap Excia T/Plasmafit, S+N SL-PLUS MIA/SPECTRON EF/R3/TANDEM, Enovis twinSys/RM Classic/seleXys PC/ccB.
Neu hinzu nach Julians Wahl: **DePuy Synthes, Zimmer Biomet, weitere Mathys/Enovis-Systeme, weitere laut Register** (z. B. Lima, implantcast, Corin).

Ergebnis am Ende: je neues System eine Datei `implantate/<hersteller>-<system>.json + .md` im Schema v1.1 (`implantate/LIESMICH.md`: feste `id`, `groessen`, `tabellen`, `passt_zu` mit Bedingung/Quelle/Seite, `rueckrufe.betrifft`). Diese Basis-Datei wird danach entfernt.

**Regeln (wie immer)**
- Nur offizielle Hersteller-, Behörden- und Registerdokumente; Original selbst öffnen; jeder Wert mit Dokument, Kennung/Revision, Stand, **Seite** (gedruckt + PDF) und Markt.
- **Systeme nicht mischen**; Kombination nur, wenn der Hersteller sie ausdrücklich nennt. Nein-Zeilen und Fußnoten mit übernehmen.
- Nichts schätzen, nichts aus ähnlichen Systemen ableiten; nicht Lesbares als „nicht gefunden/nicht lesbar“ mit Grund.
- Keine PDFs, Volltexte oder Bilder ins Repo.
- Produktnamen unten sind **Kandidaten** – erst das Register-Ranking entscheidet, was aufgenommen wird.

## Zur Prüfung in diesem Lauf

### A. Ranking DACH (zuerst)
1. **EPRD Deutschland, Jahresbericht 2025** (+ Ergebnistabellen): häufigste **Schäfte** (zementfrei / zementiert), **Pfannen** (zementfrei / zementiert), **Schaft-Pfannen-Kombinationen** bei elektiver primärer Hüft-TEP – Top 15 mit Anzahl/Anteil, Tabellennummer, Seite. Zusätzlich häufigste **Hemi-/Duokopf-Systeme** bei Schenkelhalsfraktur, falls ausgewiesen.
2. **SIRIS Schweiz**, aktueller Jahresbericht: dasselbe (Top-Schäfte/Pfannen/Kombinationen).
3. **Österreich**: Register bzw. Bericht mit Implantat-Häufigkeiten (falls öffentlich); sonst „nicht gefunden“.
4. Daraus Vorschlag: welche Systeme (Hersteller + Schaft + Pfanne) die DACH-Auswahl bilden sollen – mit Rangplatz je Land. Bereits vorhandene vier Systeme mit einordnen (bleiben, rutschen raus?).

### B. DePuy Synthes (Kandidaten)
5. **Corail** (zementfrei; zementierte Variante?) – Größen, Kragen/ohne, Offset-Varianten, CCD, Konus; Kopf-Kombinationen.
6. **Actis** (zementfrei) – nur falls im Ranking relevant.
7. **Pinnacle** (zementfrei) – Schalengrößen, Liner (AltrX/Marathon, Keramik), **max. Kopf-Ø je Schale**.
8. Zementiert: Schaft (z. B. C-Stem AMT, Corail zementiert?) und zementierte Pfanne (z. B. Marathon/Elite Plus) – was ist DACH-relevant?
9. Köpfe: BIOLOX delta, CoCr (Articul/eze) – Ø/Offsets.
10. **Duokopf**: DePuy Self-Centering Bipolar (bzw. aktueller Name) + freigegebener zementierter Schaft.
11. Rückrufe/Sicherheitsmeldungen (BfArM) zu diesen Komponenten.

### C. Zimmer Biomet (Kandidaten)
12. **CLS Spotorno**, **Avenir Complete**, **Alloclassic Zweymüller**, **Fitmore** (zementfrei) – welche sind im Ranking oben?
13. Pfannen: **Allofit/Allofit-S**, **G7**, Continuum, Trilogy – Größen, Liner (Durasul, Longevity, Vivacit-E, Keramik), **max. Kopf-Ø je Schale**.
14. Zementiert: **Müller-Geradschaft (MS-30)**, Avenir zementiert, CPT; zementierte Pfanne (z. B. Müller Low Profile, ZCA).
15. Köpfe (BIOLOX delta, CoCr/Protasul) – Ø/Offsets je Konus (12/14 bzw. 8/10 bei Alloclassic beachten).
16. **Duokopf**: Zimmer-Biomet-Bipolarkopf + freigegebener zementierter Schaft.
17. Rückrufe (BfArM).

### D. Mathys/Enovis zusätzlich
18. **optimys** (Kurzschaft), **RM Pressfit vitamys**, seleXys TH+/TPS – Ranking v. a. Schweiz; Größen, Kombinationen.
19. Kopf-Kompatibilität (aktuelles Enovis-Chart) – auch für twinSys (offen aus Lauf 001-implantate).

### E. Weitere laut Ranking
20. Falls im Ranking unter den Top-Systemen: **Lima** (z. B. H-MAX, Delta TT), **implantcast**, **Corin** (MiniHip, Trinity), andere – nur Ranking-Fundstelle + Hauptdokumente; Details erst nach Julians Auswahl.

### F. Offenes aus Lauf 001-implantate (falls nebenbei auffindbar)
21. Aktuelle Enovis-Fassung seleXys PC (Original lesen: S. 11–12, 19), SL-PLUS MIA 31156-en V2 Längen, R-2020-04/R-2023-13 Schale oder Liner, X3 26 mm.

## Ergebnis-Format
- **Grok:** je Punkt `Nr · ok/nicht gefunden · Befund · Wert/Tabelle wörtlich · Dokument + Kennung + Stand + Seite + Markt · Vorschlag` – zuerst A (Ranking), dann B–F. Am Ende „Nicht gefunden“ und „Vorschlag DACH-Auswahl“ (Tabelle Land × Rang × System).
- **Astra (nur Implantate):** liest alles, ändert nichts; bestätigt/korrigiert Grok je Punkt am Original; eigene Punkte; Ergebnis FREIGEGEBEN/ÄNDERN.
- **Perplexity:** nur Fundstellen laut `pakete/001-implantate-dach-perplexity-auftrag.md`.
