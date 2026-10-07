ÄNDERN
OpenAI – Lauf 001-implantate-luecken, 2026-10-07 (STATUS-Laufstart 2026-10-07T18:45Z)

# Gegenprüfung der 23 Hüftimplantat-Lücken

Julian hat klargestellt: **002 = Knie-TEP**. Dieser Lauf gehört eigenständig zu 001. Geprüft wurden Herstellerangaben, Implantatgrößen, Kompatibilität und Indikationsgrenzen. Keine Instrumentenfreigabe, keine Änderung der Implantatdaten oder der App. Übergabe an Claude/Cloud für den letzten Check und Julians anschließende Entscheidung.

Grundlage: Basis-Blob `743ed37b5f26352cceee8a18de102477dcbb8341`, Grok-Blob `d39a86115238ce046a362556d3fa8d86295bf9ea`, Perplexity-Blob `f5a02fe893b45a7dfa80d1365ba99696dbca0524`; elf Implantat-JSONs des geprüften Repo-Stands. Perplexity wurde als Fundstellenliste verwendet. Hersteller-PDFs wurden heruntergeladen und gelesen; bei mehrspaltigen Freigaben wurden zusätzlich gerenderte Seiten geprüft. Nicht lesbare Volltexte werden ausdrücklich nicht bestätigt.

**Ergebnis:** Groks pauschale Übernahmeempfehlungen reichen nicht aus. Besonders zu korrigieren sind POLARSTEM-Nein-Zeilen, Medacta-Varianten/kleine Schäfte, ZB-Kopffamilien und Bipolar-Zuordnungen, CoreHip-Dysplasie-Längen sowie die Markt-/Versionsbindung bei LINK. Ein Katalogeintrag, eine technische Kompatibilität und eine aktuelle DE/EU-Freigabe sind getrennte Aussagen.

## 1. Entscheidung je Basis-/Grok-Punkt

„Bestätigt“ bestätigt hier das beschriebene Prüfergebnis, auch wenn dieses eine offene Lücke ist. „Korrigiert“ bedeutet, dass Groks Vorschlag nur mit den folgenden Änderungen verwendbar ist. Es gibt **23 Basis-Punkte**, keine überlappenden Erfolgszählungen.

| Nr. | Entscheidung zu Grok | Eigenständig festgestellter Befund / Konsequenz |
|---|---|---|
| 1 | Korrigiert; Volltexte offen | Stryker-DE-URLs liefern ein JS-Portal, keinen gelesenen IFU-Text. Auch QIN↔Produkt-Zuordnungen aus Perplexity nicht als unabhängig `belegt` markieren. |
| 2 | Bestätigt: offen | X3 26 mm weder freigeben noch endgültig ausschließen. Die behaupteten zwei eIFU-Produkte und ihre Alpha-Zuordnung sind nicht bestätigt. |
| 3 | Korrigiert / ergänzt | ACCII-PG-3 enthält **6720/132° und 6721/127°**, jeweils Größe 0–11. Grok lässt die zweite Serie aus. Markt nicht explizit EU. |
| 4 | Korrigiert | POLARSTEM zementiert: STD 0–8, LAT **1–8**. Zementfrei 145° nur ohne Kragen; „mit/ohne Kragen“ gilt nicht unterschiedslos für alle CCD. |
| 5 | Korrigiert / konkretisiert | CoCrMo-Zeilen sind für zementierten POLARSTEM negativ. Kleinste zementfreie STD-Größe **"01"** hat zusätzliche Ausschlüsse; 26-mm-Zeilen negativ. Details unten. |
| 6 | Korrigiert / ergänzt | Medacta-Implantatseiten und Varianten konkret extrahiert; kleine Schäfte mit Kopflängen-/Gewichtsgrenzen. Versafit: Material und Inlayform ändern die erlaubten Bohrungen. |
| 7 | Korrigiert | COM-Seite 3 ist **Liner×Schale**, nicht Versafit×Schaft. Rev.12 nennt Quadra-P/AMIStem-P nicht. IFU ersetzt die fehlende Familienzeile nicht. |
| 8 | Korrigiert | Bipolar-OP nennt Innenkopf 22/28 mm, liefert aber keine vollständige Außen-Ø×Innen-Ø×REF-Tabelle. Endo ist separat unipolar; dessen Katalogtabelle ist vorhanden. |
| 9 | Korrigiert / ergänzt | Avenir cemented: Total- oder Hemiarthroplastik; uncemented: im gelesenen Dokument **Totalarthroplastik**. Größen-/Bestelltabelle fehlt. Nicht mit Complete zusammenziehen. |
| 10 | Korrigiert | Charts enthalten Kopffamilien mit REF-Platzhaltern und Halslängengruppen, keinen vollständigen Ø×Einzel-REF-Katalog. Graue Zellen nicht übersehen; insbesondere CoCr +10,5/Freedom +9 nicht für alle Schäfte. |
| 11 | Korrigiert | Low Profile PE, DURASUL und METASUL sind getrennte Produkte. Die Identität der Hausbezeichnung „Flachprofil“ bleibt offen; Übersetzungsvermutung nicht als `üblich` abgesicherte Produktidentität ausgeben. C2 liefert keine Größen. |
| 12 | Korrigiert / konkretisiert | C1 belegt Liner×Schale, nicht automatisch Liner×Kopf. ALLOFIT und IT unterscheiden; STANDARD- sowie ALPHA-Liner beachten. C3 liefert konkrete Schraubenfamilien. |
| 13 | Korrigiert / konkretisiert | AP 1946/1989: Avenir Müller ✓, **Avenir Cemented und Avenir Complete grau/nein**. Innenkopf muss zusätzlich die Artikulations- UND Schafttabelle erfüllen. |
| 14 | Bestätigt: offen | optimys-Katalogvolltext hinter Fachkreis-Gate; keine neuen REF/Dimensionen bestätigt. |
| 15 | Bestätigt: offen | RM Pressfit vitamys: angefragte OP-Tabelle nicht gelesen; keine neuen Größen bestätigt. |
| 16 | Bestätigt: offen | Mathys-Kopf-Kompatibilitätschart nicht gelesen; keine pauschale Freigabe ceramys/symarec/CoCr mit optimys/twinSys. |
| 17 | Bestätigt: offen | Mathys Bipolar/Hemi: keine neue Außen-/Innenkopf- oder Schaftfreigabe. |
| 18 | Bestätigt: offen | seleXys-PC-Zuordnung bleibt offen; historische TH+/TPS-Aussagen nicht auf PC übertragen. |
| 19 | Korrigiert; Übernahme von Trialdaten abgelehnt | PINNACLE Trial-/Farbtabellen sind kein Implantatkatalog. Instrumentendaten gehören nicht in diesen Implantatlauf. Vollständige Implantatmatrix weiterhin offen. |
| 20 | Korrigiert / konkretisiert | CORAIL-Bestellseiten lesbar, Varianten getrennt unten. C-STEM-Kopfseite nicht gelesen; ARTICUL/EZE-Offsets deshalb offen. |
| 21 | Bestätigt: offen | MRT-Broschüre nicht lesbar erreichbar; US-Self-Centering kein EU-Ersatz. Weder REF aus Sekundärhinweisen noch Paarungsfreigabe erfinden. |
| 22 | Korrigiert | Bicontact-Katalogdaten grundsätzlich nachvollziehbar, historischer Stand. CoreHip enthält einen relevanten Längen-Sonderfall. LINK-US-Katalog ist keine allgemeine EU-Quelle; neuere globale EN-Dokumente geöffnet. |
| 23 | Korrigiert / konkretisiert | Plasmafit-Poly-Standard-UHMWPE ist deutlich enger als Vitelene. Tabellen unten schließen die Materiallücke. Bipolar Cup×Excia T zementiert weiterhin nicht ausdrücklich nachgewiesen. |

## 2. Stryker: REF ergänzen, eIFU-Lücken erhalten

Quelle **[8.6]**, PDF 12, unnummerierte Rückseite, ACCII-PG-3 Rev-1_22894, ©2020. Die vollständigen Implantat-REF-Zeilen lauten:

| Größe | 132° | 127° |
|---|---|---|
| 0 | 6720-0027 | 6721-0027 |
| 1 | 6720-0127 | 6721-0127 |
| 2 | 6720-0230 | 6721-0230 |
| 3 | 6720-0330 | 6721-0330 |
| 4 | 6720-0435 | 6721-0435 |
| 5 | 6720-0535 | 6721-0535 |
| 6 | 6720-0635 | 6721-0635 |
| 7 | 6720-0737 | 6721-0737 |
| 8 | 6720-0837 | 6721-0837 |
| 9 | 6720-0937 | 6721-0937 |
| 10 | 6720-1040 | 6721-1040 |
| 11 | 6720-1140 | 6721-1140 |

Diese Katalogdaten dürfen mit Kennung, Seite und „Markt im Dokument nicht eindeutig angegeben“ vorgeschlagen werden. Sie schließen weder die DE-eIFU-Frage noch den X3-26-mm-Konflikt. Der positive HTTP-Status der URLs [8.1–8.5] bestätigt nicht die Existenz des jeweils behaupteten QIN-Inhalts.

## 3. POLARSTEM: Varianten und negative Kombinationen

**[7.1]**, gedruckt 13–16 / PDF 16–19, 01217-en V7 10/24; EN-Ausgabe mit CE0123, keine reine US-Fassung. Konus jeweils 12/14; zementfrei Ti6Al4V, zementiert Edelstahl ISO5832-9. Die folgende verkürzte Schreibweise fasst tatsächlich vorhandene aufeinanderfolgende Tabellenzeilen zusammen; unregelmäßige Endpunkte sind separat angegeben. Größe **"01" als Zeichenfolge erhalten**, nicht in 1 umwandeln.

| Fixation / Variante | CCD | Größen | SAP-REF / Besonderheit |
|---|---:|---|---|
| Zf STD ohne Kragen | 135° | 01, 0, 1–11 | 01=75100462; 0=75100463; 1–10=75100464…75100473; 11=75100509 |
| Zf LAT ohne Kragen | 126° | 1–11 | 1–10=75100474…75100483; 11=75100510 |
| Zf VAL ohne Kragen | 145° | 0–7 | 75102072…75102079 |
| Zf STD mit Kragen | 135° | 01, 0, 1–11 | 01=75018399; 0–11=75018400…75018411 |
| Zf LAT mit Kragen | 126° | 1–11 | 1–8=75018412…75018419; 9–11=75102209…75102211 |
| Zementiert STD | 135° | 0–8 | SAP 75002111…75002119; Item 11000405…11000413 |
| Zementiert LAT | 126° | 1–8 | SAP 75002120…75002127; Item 11000414…11000421 |

Keinen VAL-Kragenschaft und keinen zementierten LAT Größe 0 erzeugen. Größe 01 trägt einen Nicht-US-Hinweis. Mit Stern markierte Varianten haben gesonderte Verfügbarkeit; Demo-REF aus benachbarten Zeilen nicht als Implantate übernehmen. PDF 18–19 enthält Dimensionen; CCD, Schaftoffset und Kopf-Halslänge sind unterschiedliche Felder.

**[7.2]**, 04758 Ed.05/26 V12, Seite/PDF 1: drei getrennte POLARSTEM-Spalten verwenden: zf STD01 (75100462/75018399), übrige zf, zementiert. „Ja“ bedeutet hier die technische Matrixaussage dieser Ausgabe, mit ihrem Marktvorbehalt.

| Kopfgruppe und Halslänge | Zf STD01 | Übrige zf | Zementiert |
|---|---|---|---|
| OXINIUM 22: +0/+4/+8/+12 | ja | ja | ja |
| OXINIUM 26, gelistete Zeilen | nein | nein | nein |
| OXINIUM 28/32: −3 oder +16 | nein | ja | ja |
| OXINIUM 28/32: +0/+4/+8/+12 | ja | ja | ja |
| OXINIUM 36: −3 | nein | ja | ja |
| OXINIUM 36: +0/+4/+8/+12 | ja | ja | ja |
| OXINIUM 40/44 mit erforderlicher Ti-Hülse: −4 | nein | ja | nein |
| OXINIUM 40/44 mit erforderlicher Ti-Hülse: +0/+4/+8 | ja | ja | nein |
| CoCrMo 22: +0/+4/+8/+12 | ja | ja | nein |
| CoCrMo 26, gelistete Zeilen | nein | nein | nein |
| CoCrMo 28/32: −3 oder +16 | nein | ja | nein |
| CoCrMo 28/32: +0/+4/+8/+12 | ja | ja | nein |
| CoCrMo 36: −3 | nein | ja | nein |
| CoCrMo 36: +0/+4/+8/+12 | ja | ja | nein |
| CoCrMo 40/44 mit erforderlicher Ti-Hülse: −4 | nein | ja | nein |
| CoCrMo 40/44 mit erforderlicher Ti-Hülse: +0/+4/+8 | ja | ja | nein |
| BIOLOX delta: die unten benannten REF-Gruppen | ja | ja | ja |

Die letzte Zeile umfasst ausschließlich: 32/+0,+4,+8 `765391-60/-61/-62`; 36/+0,+4,+8,+12 `765391-65/-66/-67/-53`; 40/+0,+4,+8 `713460-04/-05/-06`; 28/S,M,L `750074-51/-52/-53`; 32/S,M,L,XL `750074-60/-61/-62/-63`; 36/S,M,L,XL `750074-48/-49/-50/-47`. Keine freie Ø-/Halslängen-Interpolation.

BIOLOX OPTION ist separat mit Adapterhülse geführt: 28/32/36 S/M/L/XL positiv; 40 S/M/L positiv, **40 XL in allen drei Spalten negativ**. Edelstahlköpfe nicht mit CoCrMo zusammenfassen: die gelisteten 22/28/32-Edelstahlzeilen sind nur in der zementierten Spalte positiv, 26 negativ. Keine dieser Zeilen ist eine TANDEM-Bipolarfreigabe. Matrixgrafik und Legende lesen; das Text-Extraktzeichen „a“ ist kein belastbares Exportformat.

## 4. Medacta: Katalogfamilien und Kombinationen getrennt

### 4.1 Schäfte (Basis 6)

**[6.1]/[6.2]**, jeweils gedruckt/PDF 10: Quadra-H STD regulär 0–10 (`01.12.020…030`), LAT 1–7 (`01.12.031…037`). Short Neck STD 00SN (`01.12.98SN`, auf Anfrage), 0SN–3SN (`01.12.20SN…23SN`); LAT 1SN–3SN (`01.12.31SN…33SN`). **Quadra-C nur STD 0–7** (`01.12.040…047`), keine lateralisierte Zeile. Quadra-C Größe 0: **Körpermasse höchstens 65 kg**, nicht „BMI 65 kg“; EN-Fußnote [6.2] klärt den missverständlichen deutschen Wortlaut. Größe 10 Quadra-H ist als auf Anfrage markiert.

**[6.3]**, gedruckt/PDF 13: Quadra-P als eigene Familie auswerten:

| Variante | STD | LAT |
|---|---|---|
| Regulär | 00 `01.12.119` (Anfrage), 0–10 `01.12.120…130` | 0–10 `01.12.140…150` |
| Short Neck | 00SN `01.12.249` (Anfrage), 0SN–10SN `01.12.250…260` | 0SN–10SN `01.12.270…280` |
| Collared | 00 `01.12.159` (Anfrage), 0–10 `01.12.160…170` | 0–10 `01.12.180…190` |
| Cemented | 0–8 `01.12.210…218` | 0–8 `01.12.230…238` |

„Quadra-P Cemented“ nicht als zusätzliche Größen von Quadra-C ausgeben. Anfrage-/Verfügbarkeitsfußnoten bleiben bei der jeweiligen Variante; eine reguläre Nummernfolge beweist keine Lieferbarkeit.

**[6.4]**, gedruckt/PDF 15–16 (aktuellere Katalogquelle als [6.5]):

| Variante | STD | LAT |
|---|---|---|
| AMIStem-P regulär | 00 `01.18.399` (Anfrage), 0–9 `01.18.400…409` | 0–8 `01.18.410…418`; kein 9 |
| AMIStem-P SN | 00SN `01.18.459`, 0SN–9SN `01.18.460…469` | 0SN–8SN `01.18.470…478`; kein 9SN |
| AMIStem-P Collared | 00 `01.18.429` (Anfrage), 0–9 `01.18.430…439` | 0–8 `01.18.440…448` |
| AMIStem-C regulär | 00 `01.18.149`, 0–8 `01.18.150…158` | 0–8 `01.18.100…108` |
| AMIStem-C SN | 00SN `01.18.699`, 0SN–8SN `01.18.700…708` | 0SN–8SN `01.18.710…718` |

**Sicherheitsrelevante Fußnote:** AMIStem-P STD00SN und AMIStem-C STD00, STD00SN sowie STD0SN ausschließlich mit Kopfgrößen **S/M/L**. Nicht auf alle AMIStem-C-Größe-0-Varianten ausweiten; nicht durch eine allgemeine COM-Zeile überschreiben. Die hohen SN-Größen mit Fußnote III sind nur auf besondere Nachfrage mit Bestätigung erhältlich. [6.4] PDF 14 trennt Edelstahl, CoCr, CeramTec delta/OPTION und Mectacer delta/OPTION; OPTION-Systeme benötigen die passende Manschette und sind dort für Revision gekennzeichnet.

### 4.2 Versafitcup CC Trio (Basis 6)

**[6.6]**, gedruckt/PDF 12–13. Schalen: 40/42=AZ, 44=B, 46/48=C, 50/52/54=E, 56/58/60=F, 62/64=G. CC-Trio-NoHole beginnt in dieser Tabelle bei 44/B. Gleicher Code UND passende Bohrung UND freigegebene Materialpaarung sind erforderlich.

| Code | Standard-UHMWPE flach/überhöht | HIGHCROSS flach | HIGHCROSS überhöht | Keramik |
|---|---|---|---|---|
| AZ | 22 | 22 | 22 | — |
| B | 28 | 28 | 28 | 28 |
| C | 28 | 28,32 | 28 | 28,32 |
| E | 28,32 | 28,32,36 | 28,32 | 28,32,36 |
| F | 28,32 | 28,32,36 | 28,32 | 28,32,36,40 |
| G | 28,32 | 28,32,36 | 28,32 | 28,32,36,40 |

Zahlen sind konkrete Kopfbohrungen in mm, kein kontinuierlicher Bereich. Eine Regel `kopf_mm <= max_kopf_mm` wäre dafür unzureichend. Beispiele aus den gelesenen REF-Zellen: C/32/HIGHCROSS flach `01.26.3239HCT`; E/36/HIGHCROSS flach `01.26.3644HCT`; E/32/HIGHCROSS überhöht `01.26.3244HCAT`; F/40/Keramik `01.29.416`; G/40/Keramik `01.29.417`. **Kein 36-mm-HIGHCROSS-überhöht** aus dem Maximum der flachen Variante ableiten. Vollständige REF stehen in der bezeichneten Seite; hier sind nicht alle Einzel-REF erneut abgeschrieben.

### 4.3 COM, IFU, Bipolar und Endo (Basis 7–8)

**[6.11]**, 99.99.COM rev12, 10/2016: Seite 1 Kopf×Schaft, Seite 2 Kopf×Liner/Bipolar, Seite 3 Liner×Schale. Bei den benannten Quadra-C/H/S/R- und AMIStem-C/H-Familien sind die gelisteten Medacta-12/14-Kopfgruppen positiv; Native-10/12-Köpfe nicht. **Quadra-P und AMIStem-P fehlen namentlich.** Daher aus diesem älteren Chart keine vollständige neue P-Familienfreigabe konstruieren; neuere OP-Tabellen und deren Spezialgrenzen separat belegen.

COM Seite 2 führt die gelisteten Metall- UND Keramikkopfgruppen positiv zum **Medacta Bipolar Head**. Der Endo Head hat dort keine Liner-/Bipolar-Paarung. COM Seite 3 führt für CC Trio/NoHole die passenden CC-UHMWPE/HIGHCROSS- und Keramikliner, nicht beliebige Mpact- oder DM-Liner. Die Quelle belegt funktionale Kombinationen, nicht automatisch lokale regulatorische Zulässigkeit.

**[6.10]**: rev26, Last update 10/2020. Deutsch beginnt PDF/gedruckt 24, relevante Kombinations-/Warntexte PDF 26–27; EN PDF 5. Ein beim Download eingeblendetes „Valid on“-Datum ist keine neue Revision.

**[6.8]**, 99.19.42 rev00, 05/2022, PDF/gedruckt 4–6: Bipolar-Innenkopf **22 oder 28 mm**, Metall oder Keramik nach gültiger Kombination; außen Edelstahl, Innenlager UHMWPE. **Keine vollständige Außen-Ø/REF-Tabelle auf Seite 5–6.** Groks Übernahmevorschlag zu Außenmaßen ist deshalb nicht ausführbar; diese Felder bleiben offen. Das Dokument ist ausdrücklich nicht für den US-Markt bestimmt.

**[6.9]**, 99.18.12 rev03, PDF 1–2, ohne sichtbares Ausgabedatum: Endoköpfe außen **40,42,44,46,48,50,52,54,56 mm**, je S/M/L. Beispielsweise 40: `01.25.140S/M/L`, 56: `01.25.156S/M/L`. Das Dokument nennt Medacta-Schäfte mit 12/14-Konus; dies ist eine Hersteller-Systemaussage, keine freie Konuskompatibilitätsregel. Endo ist ein unipolarer Hemikopf und kein Innenkopf eines Bipolarsystems. Kleine-Schaft-Beschränkungen aus [6.4] bleiben zusätzlich wirksam.

## 5. Zimmer Biomet: drei verschiedene Kompatibilitätsebenen

### 5.1 Avenir und neue Kopffamilien (Basis 9–10)

**[4.1]**, 4034.2-GLBL-en 2024-04, PDF 2–3: Avenir cemented Protasul-S30/12/14 versus uncemented Protasul-64WF mit HA/12/14. Die Hemi-Indikation des cemented-Abschnitts nicht auf uncemented übertragen. Größen/Einzel-REF bleiben aus dieser OP-Technik unbelegt.

**[4.2]**, 87-6204-051-00 rev1, 7/1/2020, gedruckt=PDF 1–4: Die hier relevanten Alloclassic-SL-/SL-Offset-/SLL-, Avenir-Müller-/Cemented-, CLS-, Fitmore- und MS-30-Zeilen haben Häkchen in den vier benannten Keramikspalten. Diese heißen **80260xxxx** (−3,5 bis +3,5 bzw. +7) und **SELECT 80300xxxx + Adapter 8030000xx** (−6 bis +3,5 bzw. +7). Das sind REF-Familien/Platzhalter, keine fertigen Einzelbestellnummern. Sie nicht auf jeden vorhandenen „BIOLOX delta 12/14“-Datensatz übertragen; SELECT und OPTION ebenfalls nicht gleichsetzen.

**[4.3]**, 87-6204-951-00 rev1, gleicher Stand, PDF 1–4:

| Schaftzeilen | CoCr 80220xxxx −3,5…+3,5 | CoCr +7 | CoCr +10,5 | Freedom 80240xxxx −6…+3 | Freedom +6 | Freedom +9 |
|---|---|---|---|---|---|---|
| Alloclassic SL, SL Offset, SLL | ✓ | ✓ | grau | ✓ | ✓ | grau |
| Avenir Müller / Avenir Cemented | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| CLS Spotorno (genannte 125/135/145/HA-Zeilen) | ✓ | ✓ | grau | ✓ | ✓ | grau |
| Fitmore A/B/B Extended Offset/C | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| MS-30 STD/LAT | ✓ | ✓ | grau | ✓ | ✓ | grau |

Grau bedeutet nach dieser neueren Chart-Legende **nicht bewertet oder nicht funktional kompatibel**, also keine positive Freigabe; nicht als nachgewiesene mechanische Unverträglichkeit umformulieren. Die Kopf-Durchmesser und Einzel-REF werden dadurch noch nicht vollständig geliefert. Die Schaftzeile `01.00121.XXX Alloclassic SL Offset` ist exakt benennbar; keine zusätzliche SLO-Identität allein aus einem Kürzel erfinden. Marktstatus laut Fußzeile separat prüfen.

### 5.2 Low Profile, Allofit und Schrauben (Basis 11–12)

**[4.8] C2**, rev2/15/2023, Seite/PDF 1: Cup×Cage/Ring, keine Bestell-/Größentabelle. Produktidentität „Flachprofil“ weiter offen.

**[4.7] C1**, rev05/03/2019, Seite/PDF 1, visuell abgeglichen:

| Schale im Chart | Positive Linerfamilien |
|---|---|
| ALLOFIT Shell | ALPHA CERASUL, ALPHA DURASUL, ALPHA METASUL, ALPHA PE; außerdem STANDARD METASUL und STANDARD PE |
| ALLOFIT IT Acetabular Cup (8755) | BIOLOX Delta Taper Liner (8775), Longevity IT, Metasul Taper (8770), Vivacit-E |

Diese Zeilen bestätigen die **Schalenverriegelung**, nicht den Kopf. Kopf/Liner benötigt eine zusätzliche Artikulationsquelle. Keine IT↔Nicht-IT-Übertragung. Fußnote: 8775 in dieser Ausgabe nicht in den USA erhältlich. „ALLOFIT-S“ nicht ohne Artikelidentität mit jedem ALLOFIT-Eintrag gleichsetzen.

**[4.9] C3**, rev2/15/2023, Seite/PDF 1:

| Exakte Schalenzeile | Positive Schraubenfamilien |
|---|---|
| ALLOFIT-S IT Alloclassic Shell (8755) | `00-6250-065-xx` (6,5 mm); `4301-07-015/080` |
| ALLOFIT-S Alloclassic Shell | dieselben zwei; zusätzlich `02.06000.015/070` und `6301-07-015/080` |

Andere Spalten sind für diese Zeilen grau. Die Schrägstrich-/xx-Angaben so als Familienbezeichnung erhalten, keine nicht gelesenen Einzelgrößen interpolieren.

### 5.3 Bipolar AP 1946/1989 (Basis 13)

**[4.5]**, rev5/6/2019, beide Seiten visuell geprüft. Exakte AP-Spalte:

| Schaftzeile | AP 1946/1989 |
|---|---|
| Avenir Müller | ✓ |
| Avenir Cemented | **grau / laut Legende nicht freigegeben** |
| Avenir Complete | **grau / laut Legende nicht freigegeben** |
| ALLOCLASSIC SLA/SL-64, SLL-Revision, ALLOCLASSIC | ✓ |
| CLS SPOTORNO; Fitmore | ✓ |
| MS-30; Müller Straight PROTASUL-10/-S30 | ✓ |

Das ist kein Nachweis einer Hemi-Indikation jedes positiv markierten Schafts. Insbesondere bleibt die Avenir-Indikationsgrenze aus [4.1] bestehen. Fußnote 1 verlangt zusätzliche Artikulations- und Kopf/Schaft-Prüfung. Die bis-56-mm-Fußnote für bestimmte Alloclassic-Zeilen bezieht sich ausdrücklich auf **4404-/4405-22/26-XXX**, nicht pauschal auf AP1946/1989.

**[4.6] B1**, rev2/8/2023, Seite/PDF 2, liefert für AP beispielsweise positive CoCr/DURASUL-Zeilen **28/32/36/40** und **22/26**, aber die eigenständige **22,2-mm-Zeile ist grau**. Ebenso sind die VerSys-12/14-Spalten dort grau. Deshalb nicht „jeder CoCr-Kopf 12/14“ als Innenkopf freigeben. B1 ist keine Außen-Ø×Innen-Ø×REF-Bestellmatrix; konkrete Bipolargrößen bleiben zusätzlich zu belegen. Keramikköpfe werden durch diese Metall-/PE-Tabelle nicht entschieden.

## 6. Mathys/Enovis (Basis 14–18)

Die übermittelten Original-URLs [5.1–5.8] wurden versucht. In diesem Lauf erfolgte eine Weiterleitung auf `enovis-surgical.com/en/check.html`: HTTP200 mit Fachkreis-HTML statt PDF, **nicht derselbe HTTP415-Befund wie bei Grok**. [5.9] lieferte ebenfalls keinen gelesenen IFU-Volltext. Das Gate wurde nicht mit einer erfundenen beruflichen Bestätigung umgangen.

Die öffentliche optimys-Produktseite ist erreichbar und beschreibt das System; die dort geöffnete PDF zum Meißelsystem liefert keinen Ersatz für den angefragten Implantatkatalog. Daraus keine REF, Kopf/Schaft-Freigaben oder RM-/seleXys-Zuordnungen ableiten. Die fünf Lücken bleiben dokumentiert offen. Fundstellenversionen aus Perplexity nicht mit „am Original gelesen“ versehen.

## 7. DePuy (Basis 19–21)

**PINNACLE [DP-P]**, 142532-220805 EMEA ©2022: gedruckt 8/PDF10 zeigt Trialgrößen/-farben; gedruckt 9/PDF11 unterscheidet alternative Lager-Trials. Die Implantat-Linerkonfigurationen stehen gedruckt 10/PDF12. Keramik-Einsetz-/Größenbezug gedruckt 16/PDF18 ist keine vollständige Schale×Implantatliner×Kopf-Bestellmatrix. Groks Empfehlung, die Trialzuordnung in Implantatdaten zu übernehmen, wird **abgelehnt**. Die vollständige Matrix bleibt offen.

**CORAIL [DP-C]**, 198918-211214 UK ©2022, gedruckt 24–26/PDF25–27: Bestelltabellen sind lesbar. Version im PDF verwenden, nicht die abweichende Dateinummer der CDN-URL. Wichtige konkrete Zeilen und Grenzen:

| Variante | Größen | Gelesene REF-Zuordnung |
|---|---|---|
| STD135 collarless | 8,9,10,11,12,13,14,15,16,18,20 | 8=`3L92507` (unregelmäßig!), 9=`3L92509`, 10–16=`3L92510…16`, 18=`3L92518`, 20=`3L92520` |
| STD135 collared | dieselben | 8=`3L92498`, 9=`3L92499`, 10–16=`3L92500…06`, 18=`3L92508`, 20=`3L92521` |
| STD125 collarless | **8,9,10** | `L981208/L981209/L981210` |
| STD125 collared | 8–14 | `L971208…L971214` |
| Short Neck135 collarless | **8,9,10** | `L981308/L981309/L981310` |
| Short Neck135 collared | 8–14 | `L971308…L971314` |
| Cemented STD | 8–16,18,20 | `L96408…L96416`, `L96418`, `L96420` |
| Cemented HO | 9–16,18,20 | `L96509…L96516`, `L96518`, `L96520` |

HO135 hat Größe9–16,18,20, collarless `L20309…L20316/L20318/L20320`, collared `L971109…L971116/L971118/L971120`; KLA125 collared hat dieselben Größen mit `3L93709…3L93716/3L93718/3L93720` (PDF25). Nicht die STD-REF wiederverwenden. Dies ist ein UK/OUS-Katalognachweis, keine automatisch aktuelle DE-Freigabe. Kein Eintrag Größe17/19 aus einer Zahlenfolge erzeugen. Die Tabelle hier ersetzt keine zusätzliche Prüfung der Einzelkopf-/Schaftkombination.

**C-STEM 143325-200907 und MRT 101721-221012:** angefragte Volltexte in diesem Lauf nicht lesbar wiedergefunden. Die alten llnwd-Links schlugen fehl; nicht daraus schließen, dass das Produkt oder Dokument dauerhaft nicht existiert. ARTICUL/EZE-Einzel-REF/Offsets sowie TRILOC-II-/SELF-CENTERING-/Cathcart-REF aus diesen Fundstellen bleiben offen. Die gelesene CORAIL-OP und US-Self-Centering-Unterlagen sind kein Ersatz für eine ausdrückliche EU-Self-Centering×CORAIL-zementiert-Freigabe. Eine MRT-Broschüre würde ohnehin nur die tatsächlich gelisteten REF, keine mechanische Paarungsfreigabe liefern.

## 8. Neue Systemdateien (Basis 22)

### 8.1 Bicontact

**[BC]**, Herstellerbroschüre O10702 0113/1/1, historisch 2013, zugänglich über einen externen Dokumentenspiegel. Gedruckt=PDF34–35 und38: S/H zf, CCD135/128, 12/14 und die eingetragenen REF-Familien sind nachvollziehbar. S zf 10–19 und21; H entsprechende Größen. Zementiert S10/12/14/16/18, H12/14/16/18 in der eigentlichen Implantattabelle. **Nicht H10 ergänzen**, nur weil eine nachfolgende Centralizer-Zeile NK310K erwähnt. N-8/10- und N-12/14-Ausführungen getrennt halten; SD9/10 tragen eine IFU-Gewichtseinschränkung ohne hier bestätigten Zahlenwert.

Kopfkatalogdaten sind in dieser historischen Ausgabe belegt; daraus keine aktuelle Lieferbarkeit oder pauschale Plasmafit/All-POLY-Freigabe erklären. Die bisherigen offenen Pfannenpaarungen bleiben offen. Quelle als Herstellerdokument auf Fremdhost kennzeichnen, nicht als aktuellen DE-IFU-Download.

### 8.2 CoreHip – eigene Korrektur mit hoher Priorität

**[CH]**, Nr.4008487, Stand02/2024, DE; gedruckt32–35/PDF17–18, Fußnoten visuell geprüft.

Die gemeinsamen `schaftlaenge_mm`-Werte der Primary-zf-Zeilen (119,5…141,5) dürfen nicht unverändert für **Dysplasie** gelten. Der Hersteller definiert das Maß als Kopfmittelpunkt bis Schaftspitze und nennt DYS **10 mm kürzer**. Das ist mehr als nur die schon vorhandene Bemerkung zur Beinlänge. Vorschlag: Varianten trennen oder das gemeinsame Maß ausdrücklich als VLG/STD/VAR-Basis mit DYS-Abweichung −10 mm speichern. Abgeleitete Zahlen, etwa 109,5 für DYS0, als **berechnet aus Tabellenwert und Fußnote** kennzeichnen, nicht als separat gedruckte Tabellenzelle.

Die 60-kg-Grenze betrifft **Primary Größe0 aller vier Linien und ausschließlich DYS Größe1**. Für Größe1 die Grenze maschinenlesbar variantenspezifisch ergänzen; nicht alle Größe1-Varianten begrenzen. Primary-zementiert Größen1/3/5/7/9 samt K/Z-REF und Centralizer sowie Extended0–11 mit den vorhandenen REF-/Längenreihen stimmen mit der Übersicht überein. AS ist ein mehrlagiges CrN/CrCN/ZrN-System; nicht als bloßes ZrN-Material vereinfachen.

CCD VLG/DYS142°, STD132°, VAR122°: gedruckt16–17/PDF9; Offsetgruppen gedruckt24–25/PDF13. Isocer darf laut gedruckt35/PDF18 nur gegen PE/XLPE artikulieren; Keramik/Keramik ausdrücklich ausschließen, falls die Familie ergänzt wird. Plasmafit-/All-POLY-Schaftfreigabe bleibt weiterhin offen. Die bereits vorhandene vollständige Extended-Tabelle sollte nicht zugleich als „erst noch aus Broschüre nachzuziehen“ bezeichnet werden.

### 8.3 LINK – neue EN-Quelle und Versionskonflikt

**[LK-26]** wurde über die aktuelle LINK-Produktseite gefunden und geöffnet. Die URL enthält `6431_SPII_SurgTech_EN_2026-04_002_MAR-02619`, das tatsächliche PDF-Impressum jedoch **6430_SPII_SurgTech_EN_2026-04_009 B MAR-00799 15.0**. Beide Angaben dokumentieren; Identität/Revision niemals nur aus dem URL-Namen übernehmen. Globale EN-Fassung, aktuelle lokale Verfügbarkeit/IFU gesondert.

Gedruckt12–15/PDF14–17 bestätigt Standard EndoDur-CoCrMo/12/14, CCD117/126/135 und XL117/126. Die neue Standardtabelle umfasst auch 117°/170 mm (z.B. rechts R01 `127-710/17`), also nicht einfach die US2020-Matrix kopieren. Die drei bestehenden Standard-Beispiel-REF passen zur EN-Tabelle. XL ist +10,5 mm am Hals-/Konusabschnitt; die Beschränkung auf Köpfe bis **+4 mm Zusatzhalslänge** steht auf gedruckt15/PDF17 ausdrücklich für **XL Neck**.

Die bestehende globale +4-Regel für sämtliche SP-II-Standardvarianten stammt aus der **US2020**-Fassung [LK-US], gedruckt28/PDF30. Nicht als allgemeine DE/EU-Regel ausgeben. Gleichzeitig aus dem engeren Wortlaut der EN-XL-Seite **keine Erlaubnis längerer Köpfe für Standard** folgern: Standard-Kopfgrenzen bleiben bis zur passenden IFU variantenspezifisch zu klären. US-Nachweis als US-Nachweis erhalten.

**[LK-H]**, Prosthesis Heads, tatsächliches Impressum 9001_Prosthesis Heads_OP_EN_2026-06_007, MAR-01359 7.0, gedruckt4–6/PDF6–8, liefert inzwischen echte Kopf-REF statt Trialgrößen. CeraDur32: `198-792/01` −4, `/02`0, `/03`+4, `/04`**+7**; CeraDur36/40 XL jeweils +8. BIOLOX-delta ist eine andere REF-Familie (`128-79…`). CoCr-Beispiel: `128-828/04`=28/+10,5, aber `198-828/04`=28/+7; **Suffixe nicht familienübergreifend umdeuten**. CeraDur-Inlays nur mit CeraDur-Köpfen, BIOLOX-delta-Inlays nur mit entsprechenden delta-Köpfen laut Kataloghinweis. Das Kopfangebot ist keine pauschale Freigabe aller Köpfe für SP II.

Lubinus Cup bleibt auf Produktebene ausdrücklich mit SP II verbunden; diese Aussage ersetzt keine Größenpaarung. IP-/CombiCup-Paarungen bleiben offen; Registerbeobachtungen liefern keine Herstellerfreigabe.

## 9. Plasmafit Poly (Basis 23)

**[9.1]**, O45502 **0718/1/4** (vollständige Kennung), EN auf DE-Herstellerseite, gedruckt=PDF18–19; Materialdefinition PDF12/24. Schalen40–62 in 2-mm-Schritten, CodesB–M. Standard-UHMWPE hat REF **ohne E**; Vitelene ist vitamin-E-stabilisiertes hochvernetztes PE mit **E**-Suffix. Die vom Nutzer gewählte Standard-PE-Familie nicht durch Vitelene ersetzen.

| Poly-Schale / Code | Standard-UHMWPE symmetrisch 32 | Standard-UHMWPE mit Schulter 28 | Standard-UHMWPE mit Schulter 32 |
|---|---|---|---|
| 40/B | — | — | — |
| 42/C | — | NV289 | — |
| 44/D | — | NV290 | — |
| 46/E | NV201 | — | NV301 |
| 48/F | NV202 | — | NV302 |
| 50/G | NV203 | — | NV303 |
| 52/H | NV204 | — | NV304 |
| 54/I | NV205 | — | NV305 |
| 56/J | NV206 | — | NV306 |
| 58/K | NV207 | — | NV307 |
| 60/L | NV208 | — | NV308 |
| 62/M | NV209 | — | NV309 |

Keine Standard-UHMWPE-36-/40-mm-Zeilen aus Vitelene ableiten. Vitelene symmetrisch: 22,2 bei40/42; 28 bei42–54; 32 bei46–62; 36 bei50–62; 40 bei54–62. Posterior-wall-Vitelene hat keine 40-mm-Zeile. Asymmetrisches Vitelene: 22,2 bei40/42; 28 bei42/44/46; 32 bei46–62. Diese Varianten jeweils separat speichern; nicht nur ein Gesamtmaximum pro Schale.

Bipolar Cup×Excia T zementiert ist auch nach Abgleich der Excia-Unterlagen nicht ausdrücklich als Paarung belegt. Aktueller DE-Excia-Download [EX-DE] trägt **Nr.4008516, Stand01/2026**; die ältere EN-O56002-Quelle ist ein anderer Dokumentstand. Weder der gemeinsame Hersteller noch 12/14 noch ein Cup-Katalogeintrag schließen die Paarungslücke.

## 10. Nicht übernommen von Grok / Übergabe

Nicht übernommen werden die pauschalen Aussagen „Kernwerte behalten“ für CoreHip/LINK, die Gleichsetzung der ZB-Charts mit vollständigen Ø/REF-Katalogen, die vermeintliche Versafit×Schaft-Matrix, die nicht vorhandene Medacta-Bipolar-Außengrößentabelle und der Import von PINNACLE-Trialdaten in Implantatdaten. Groks Summenzeile zählt überlappende Punkte und ist keine belastbare Anzahl übernahmereifer Lücken.

Vorrang für den letzten Check: **POLARSTEM-negative Kombinationen; AMIStem-S/M/L- und Quadra-C-Gewichtsgrenzen; ZB-AP-Nein-Zeilen; CoreHip-DYS-Längenausnahme; LINK-Markt-/Variantenbindung; Plasmafit-Materialtrennung.** Die konkreten Ergänzungen dieses Berichts bleiben Änderungsvorschläge, keine Änderung der Datenbasis und keine klinische Freigabe.

Offen bleiben insbesondere Stryker-DE-eIFU/X3-26, Mathys14–18, vollständige PINNACLE-Implantatmatrix, C-STEM-/MRT-REF-Nachweise, mehrere explizite Hemi-/Pfannenpaarungen sowie nicht gelesene Einzelkataloge. `verified:false` nicht wegen dieses Teil-Lückenlaufs aufheben. Fehlende Produktidentität oder fehlende Freigabe ist keine Hausgewohnheit und wird nicht zu `üblich` oder `hausabhängig` umetikettiert.

## 11. Quellenprotokoll

Alle nachstehenden als gelesen bezeichneten Quellen wurden am **07.10.2026** in diesem Lauf geöffnet. Seitenangaben oben sind ausdrücklich gedruckt/PDF getrennt; „gleich“ meint identische Zählung. Die Nummern 4.x–9.x entsprechen den Perplexity-Fundstellen, deren Inhaltsbehauptungen hier unabhängig geprüft wurden. Links und Dokumentstände folgen unten.

| ID | Dokument / URL | Kennung / Stand | Fundstelle | Markt / Reichweite |
|---|---|---|---|---|
| 8.6 | [Accolade II Femoral Hip Stem – Design Rationale](https://www.stryker.com/content/dam/stryker/joint-replacement/products/accoladeii/resources/Accolade%20II%20Design%20Rationale%20ACCII-PG-3_Rev-1_22894.pdf) | ACCII-PG-3 Rev-1_22894 ©2020 | PDF12 (unnummeriert) | Markt nicht ausdrücklich EU |
| 7.1 | [Surgical Technique – POLARSTEM Cementless and Cemented Stem System](https://smith-nephew.stylelabs.cloud/api/public/content/d0db346865434eb18cfdd88134a43380?v=004c6504&download=true) | 01217-en V7 10/24 | Druck13–16/PDF16–19 | EN mit CE0123; lokale Verfügbarkeit |
| 7.2 | [Stem and Femoral Ball Head Combinations](https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de) | 04758 Ed.05/26 V12 | Seite/PDF1 | Global; Marktvorbehalt |
| 6.1 | [Quadra-H Operationstechnik](https://resources.medacta.com/downloadPdf?id=20125&nid=15168&lang=en&name=/Quadra-H%20Surgical%20Technique%20DE.pdf) | 99.14HSClat.42 rev00, 05/2016 | Seite/PDF10 | DE |
| 6.2 | [Quadra System Surgical Technique](https://resources.medacta.com/downloadPdf?id=3521&nid=2692&lang=en&name=/Quadra%20Surgical%20Technique%20EN.pdf) | 99.14HSC.12 rev07, 06/2012 | Seite/PDF10 | EN, historische Ausgabe |
| 6.3 | [Quadra-P System Operationstechnik](https://resources.medacta.com/downloadPdf?id=20368&nid=15307&lang=en&name=/Quadra-P%20System%20DE.pdf) | 99.14PS.42 rev00, 05/2021 | Seite/PDF13 | DE |
| 6.4 | [AMIStem-P System Operationstechnik (P-Instrumente)](https://resources.medacta.com/downloadPdf?id=21055&nid=15648&lang=en&name=/AMIStem-P%20Surgical%20Technique%20DE%20(P%20instruments).pdf) | 99.14ASTEMPS.42 rev00, 07/2022 | Seite/PDF14–16 | DE |
| 6.5 | [AMIStem System Surgical Technique](https://resources.medacta.com/downloadPdf?id=8530&nid=3025&lang=en&name=/AMIStem%20Surgical%20Technique%20EN.pdf) | 99.14ASTEM.12 rev09, 07/2014 | Seite/PDF12–13 | EN, ältere Ausgabe |
| 6.6 | [Versafitcup CC Trio Family Operationstechnik](https://resources.medacta.com/downloadPdf?id=20988&nid=15516&lang=en&name=/Versafitcup%20CC%20TRIO%20-%20Surgical%20Technique%20GER.pdf) | 99.16TRIO.42 rev01, 05/2022 | Seite/PDF9,12–13 | DE |
| 6.8 | [Bipolar Head Operationstechnik](https://resources.medacta.com/downloadPdf?id=20867&nid=15584&lang=en&name=/Bipolar%20Head%20Surgical%20Technique%20DE.pdf) | 99.19.42 rev00, 05/2022 | Seite/PDF4–6,8 | DE, ausdrücklich nicht US |
| 6.9 | [Medacta Endo Head – Implants/Instrumentation Nomenclature](https://resources.medacta.com/downloadPdf?id=3470&nid=1442&lang=en&name=/Endo%20Head%20Surgical%20Technique%20EN.pdf) | 99.18.12 rev03, Datum nicht sichtbar | PDF1–2 (Poster) | EN, Markt nicht eigens benannt |
| 6.10 | [IFU Hip Prosthesis](https://resources.medacta.com/downloadPdf?id=20370&nid=11761&lang=en&name=/IFU%20HIP%20PROSTHESIS.pdf) | 75.09.017 rev26, Last update10/2020 | EN PDF5; DE PDF24,26–27 | Mehrsprachig einschließlich DE |
| 6.11 | [Implant possible combinations](https://cms.medacta.com/uploads/media/99-99-com-rev12.pdf) | 99.99.COM rev12, 10/2016 | Seite/PDF1–3 | International; funktionale Kombination |
| 4.1 | [Avenir Hip System Surgical Technique](https://assets.ctfassets.net/rc4arfpyhdpw/3RKxcUBZ4YdWkinfK2ydhd/8c0dac0ead51dbd13fb56ead2bc99146/4034.2-GLBL-en_Avenir_SurgTech_A4_DIGITAL.pdf) | 4034.2-GLBL-en 2024-04, Lit.06.02448 | PDF2–3 | Global EN |
| 4.2 | [Head and Stem Combinations: Zimmer Biomet 12/14 Ceramic Femoral Heads](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/support/product-compatibility/87-6204-051-00-Rev1_01-Jul.pdf) | 87-6204-051-00 rev1, 7/1/2020 | Seite/PDF1–4 | Funktional; regulatorischer Status separat |
| 4.3 | [Head and Stem Combinations: Zimmer Biomet 12/14 CoCr Femoral Heads and Freedom Heads](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/support/product-compatibility/87-6204-951-00_Rev1_01-Jul.pdf) | 87-6204-951-00 rev1, 7/1/2020 | Seite/PDF1–4 | Funktional; regulatorischer Status separat |
| 4.5 | [Head and Stem Combinations: Unipolar and Bipolar Femoral Heads](https://assets.ctfassets.net/rc4arfpyhdpw/32LNW4qj9EF9gZTbsgW3XK/aff2b857d83db63fa9441c1d96e1237d/Unipolar_and_Bipolar_Femoral_Heads_NEW.pdf) | Revised5/6/2019 | Seite/PDF1–2 | Funktional; Marktstatus separat |
| 4.6 | [Articulating Combinations: Metal Femoral Heads and Polyethylene Articulation](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/support/product-compatibility/B1_Final_MFHPA.pdf) | B1, Revised2/8/2023 | Seite/PDF2 | Metall/PE; Marktstatus separat |
| 4.7 | [Modular Liners and Cups](https://assets.ctfassets.net/rc4arfpyhdpw/4cFuQfD9ptPL2LNaoqXCYj/f032b9a0ac0920a7c3e2b2b65949fa47/Liners_and_Cups_Final.pdf) | C1, Revised05/03/2019 | Seite/PDF1 | Marktvorbehalt; 8775 nicht US |
| 4.8 | [Acetabular Reconstruction: Polyethylene Liners/Cups and Metal Cages/Rings](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/support/product-compatibility/C2.pdf) | C2, Revised2/15/2023 | Seite/PDF1 | Cup/Cage; Marktstatus separat |
| 4.9 | [Acetabular Cups (Shells) – Bone Screw Combinations](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/support/product-compatibility/C3.pdf) | C3, Revised2/15/2023 | Seite/PDF1 | Schrauben/Schalen; Marktstatus separat |
| DP-P | [PINNACLE Hip Solutions Surgical Technique](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf) | 142532-220805 EMEA, ©2022 | Druck8–10,16/PDF10–12,18 | EMEA |
| DP-C | [CORAIL Total Hip System Surgical Technique](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf) | 198918-211214 UK, ©2022 | Druck24–26/PDF25–27 | UK/OUS; kein pauschaler aktueller DE-Nachweis |
| BC | [Aesculap Bicontact System – Hip Endoprosthesis System (OP-Technik / Implantatübersicht)](https://knoglemekanik.dk/Vejledninger/O10702%20Bicontact%202013.pdf) | O10702 0113/1/1, 2013 | Seite/PDF34–35,38 | EN-Herstellerdokument auf Fremdhost; historisch |
| CH | [AESCULAP CoreHip System (deutsche Broschüre)](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/corehip-broschuere.pdf) | Nr.4008487, Stand02/2024 | Druck16–17,24–25,32–35/PDF9,13,17–18 | DE |
| LK-US | [Lubinus SP II – Anatomically Adapted Cemented Hip System (Surgical Technique / Implants)](https://www.link-ortho.com/fileadmin/user_upload/Fuer_den_Arzt/Produkte/Downloads/US/6431_SP_II_OP-Impl-Instr_us_2020-05_001_MAR-01247_1.0_final.pdf) | 6431_SP_II_OP-Impl-Instr_us_2020-05_001, MAR-01247 1.0 | Druck12–15,28/PDF14–17,30 | US; kein EU-Ersatz |
| 9.1 | [AESCULAP Plasmafit Cementless Acetabular Cup System](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf) | O45502 0718/1/4, 07/2018 | Seite/PDF12,18–19,24,34 | EN auf DE-Herstellerseite |
| EX-DE | [AESCULAP Excia T – Hüftendoprothesensystem](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf) | Nr.4008516, Stand01/2026 | PDF1–13; Impressum13 | DE; explizite Bipolar-Paarung nicht gefunden |
| 9.2 | [AESCULAP Excia T Hip Endoprosthesis System](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-t.pdf) | O56002 0920/PDF/5, 09/2020 | Gesamtdokument geöffnet; kein positiver Paarungsbeleg | EN auf DE-Herstellerseite |
| LK-26 | [SPII Model Lubinus Surgical Technique](https://www.link-ortho.com/fileadmin_atl/user_upload/Global_LINK_Website/Products/PDFs/EN/6431_SPII_SurgTech_EN_2026-04_002_MAR-02619.pdf) | Tatsächliches Impressum: 6430_SPII_SurgTech_EN_2026-04_009 B, MAR-00799 15.0; 04/2026 | Druck12–15/PDF14–17; ImpressumPDF32 | Global EN; Dateiname/Impressum abweichend |
| LK-H | [Prosthesis Heads](https://www.link-ortho.com/fileadmin_atl/user_upload/Global_LINK_Website/Products/PDFs/EN/9001_Prosthesis_Heads_SurgTech_EN_2026-06_007_MAR-01359.pdf) | 9001_Prosthesis Heads_OP_EN_2026-06_007, MAR-01359 7.0; 06/2026 | Druck4–6/PDF6–8; ImpressumPDF12 | Global EN; Kopfangebot ist keine beliebige Schaftfreigabe |

COM [6.11] leitete auf `https://media.medacta.com/media/99-99-com-rev12.pdf` weiter; das gelesene PDF trägt rev12. Die neuen LINK-PDFs wurden über die [SP-II-Produktseite](https://www.link-ortho.com/products/hip/link-spii) gefunden. Die [Pfannenseite](https://www.link-ortho.com/products/hip/cemented-acetabular-cup-system) nennt die Lubinus-Paarung auf Produktebene. HTML hat keine Druck-/PDF-Seiten; Abrufdatum ist kein Revisionsdatum.

### Zugriffsversuche ohne bestätigten Volltext

Die folgenden Titel/Zielrevisionen stammen aus dem Suchauftrag; der jeweilige Dokumentinhalt wurde damit **nicht** bestätigt. Gate-/Portalantworten haben keine gelesene Dokumentseite.

| ID | Angefragte Quelle | Ergebnis |
|---|---|---|
| 8.1 | [Howmedica Osteonics ACCOLADE II FEMORAL STEMS](https://labeling.stryker.com/hcp/ORT/DE/ptort?keycode=04546540664433) | JS-Portal ohne IFU-Volltext |
| 8.2 | [Howmedica Osteonics V40 COBALT-CHROME (COCR) FEMORAL HEADS](https://labeling.stryker.com/hcp/ORT/DE/ptort?keycode=07613327032307) | JS-Portal ohne IFU-Volltext |
| 8.3 | [Trident Acetabular Component System MDR eIFU](https://labeling.stryker.com/hcp/ORT/DE/ptort?keycode=04546540608512) | JS-Portal ohne IFU-Volltext |
| 8.4 | [HOWMEDICA OSTEONICS TRIDENT POLYETHYLENE INSERTS](https://labeling.stryker.com/hcp/ORT/DE/ptort?keycode=07613327039689) | JS-Portal ohne IFU-Volltext |
| 8.5 | [TRIDENT II ACETABULAR COMPONENT SYSTEM](https://labeling.stryker.com/hcp/ORT/DE/ptort?keycode=07613327380859) | JS-Portal ohne IFU-Volltext |
| 5.1 | [Mathys IFUs – Surgical techniques (Overview)](https://www.mathysmedical.com/Storages/User/Dokumente_NEU/4_Unternehmen/Mathys_Overview_IFU_01.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.2 | [optimys Operationstechnik](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_optimys_DE_V04.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.3 | [RM Pressfit vitamys Operationstechnik](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/RM_Pressfit_vitamys/OP-Technik_RM_Pressfit_DE.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.4 | [RM Pressfit – Product Information](https://www.mathysmedical.com/Storages/User/Dokumente_NEU/1_Produkteinformationen/Hu%CC%88fte/produktinformation_rm-pressfit_en_v3.0.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.5 | [Kompatibilitätstabelle Mathys Femur-Hüftköpfe](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Kompatibilitaets-Chart/Kompatibilit%C3%A4ts-Chart_OPT_Hipheads_Mathys_DE_V01.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.6 | [Bipolar and Hemiheads](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Bipolar-Hemi/OP-Technik-Produktinfo_Bipolar-Hemikopf_EN_V01.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.7 | [twinSys Operationstechnik / Surgical technique](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_twinSys_DE_V05.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.8 | [seleXys PC Operationstechnik](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_seleXys_PC_DE_V04.pdf) | Fachkreis-HTML nach Weiterleitung, kein PDF |
| 5.9 | [eIFU – Mathys](https://ifu.mathysmedical.com) | eIFU-Portal ohne gelesenen Volltext |
| 1.2 | [Risks Associated with MRI of Patients with Hip and Knee Implants](https://synthes.vo.llnwd.net/o16/LLNWMB8/INT%20Mobile/Synthes%20International/Product%20Support%20Material/legacy_DePuy_PDFs/101721.pdf) | Alter Link nicht lesbar erreichbar |
| 2.1 | [C-STEM AMT InCement and Long Stem Revision Surgical Techniques](http://synthes.vo.llnwd.net/o16/LLNWMB8/INT%20Mobile/Synthes%20International/Product%20Support%20Material/legacy_Synthes_PDF/143325.pdf) | Alter Link nicht lesbar erreichbar |

Perplexity 3.1 verweist auf dieselbe MRT-Quelle wie 1.2. Zusätzliche Mathys-Recherche: [optimys-Produktseite](https://enovis-surgical.com/en/products/325/optimys.html) und dortige [Meißelsystem-PDF](https://enovis-surgical.com/repo/storage/4765/file/produktinformation_optimys-meisselsytem_en_v1.0.pdf) geöffnet. Keine Verwendung dieser Instrumenten-PDF als Implantatkatalog. Hersteller-Produktseiten ersetzen die gesperrten Tabellen nicht.

### Umfang der eigenen Änderung

Dieser Commit legt ausschließlich `pruefung/001-implantate-luecken-openai.md` an. Keine PDFs/Bilder, keine Änderungen an Implantatdaten, fremden Prüfdateien, STATUS oder Kerlect. STATUS wurde vor Abschluss erneut gelesen: `001-implantate-luecken` steht auf `openai`; `002-knie-tep` wartet auf „002 los“.

### Geprüfte Daten-Blobs

Diese elf SHA wurden unmittelbar vor dem Anlegen des Berichts mit `main` abgeglichen; alle unverändert gegenüber dem gelesenen Stand.

| Datei | Git-Blob-SHA |
|---|---|
| `implantate/stryker-accolade-ii.json` | `edc20d33e90d12557635c1e05aff9d7e51eee09a` |
| `implantate/smith-nephew-r3.json` | `ce395b360fd5d0f76b7463fb6764df1e4b136793` |
| `implantate/medacta-quadra-amistem.json` | `9f7c76c817da216be016e3d8fed5b834b6a13b15` |
| `implantate/zimmer-biomet.json` | `7aac1a040f77223ad2d84f8fe5d7e69cb8b86ef2` |
| `implantate/enovis-optimys.json` | `2ca4682ef91a586bff36686312ed34a4d77f0129` |
| `implantate/enovis-twinsys.json` | `a40654b88f9e1256c87fafd124ddda5ec2cf0911` |
| `implantate/depuy-corail-pinnacle.json` | `2782c610b274918f7b45b946d34f6905dfb73ad4` |
| `implantate/aesculap-bicontact.json` | `89bddf3b32a16a4f40033eb6f31e60ac7fafbdd9` |
| `implantate/aesculap-corehip.json` | `b0f500dac7b818640858d3ac6ffa6beda3873b8d` |
| `implantate/link-spii-lubinus.json` | `3460bb80a5cda28f65c5afdc4e80e557f5263120` |
| `implantate/aesculap-excia.json` | `f1e233d4b6f42d3826dac012a2a64d020c0cf4c9` |

