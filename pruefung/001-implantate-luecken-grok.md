Grok – Lauf 2026-10-07T18:30Z

# Grok-Prüfung – 001-implantate-luecken (ganze Paketversion, 23 Punkte)

_Rolle: OP-Fachkraft 20+ Jahre Unfallchirurgie/Orthopädie Endoprothetik, Praxisanleitung, Hygiene; KRINKO/AWMF/IFU._  
_Grundlage: `pakete/001-implantate-luecken-basis.md`, `pruefung/001-implantate-luecken-perplexity.md`, betroffene `implantate/*.json` (Stand main). STATUS-Hinweis „wartet/002“ bewusst übergangen – Julian 07.10.2026: „001 lücken füllen“._  
_Methode: Perplexity = Fundstellenliste. Werte nur am Original (IFU/OP-Technik/Register) bestätigt. Streng: **belegt** / **üblich** / **hausabhängig**. Systeme nicht gemischt. Keine PDFs ins Repo._

## Stichprobe Links (Original geöffnet)

| Nr | Quelle | Status | Hinweis |
|---|---|---|---|
| 7.1 | S+N POLARSTEM 01217-en V7 10/24 | **ok** | PDF lesbar, CE 0123, Hersteller Zug |
| 7.2 | S+N Matrix 04758 Ed. 05/26 V12 | **ok** | PDF lesbar, Markt-Caveat im Text |
| 8.6 | Accolade II ACCII-PG-3 Rev-1 | **ok** | PDF-S. 12 Implantat-REF |
| 8.1–8.5 | Stryker labeling.stryker.com DE | **Portal** | HTML-Gerüst ohne IFU-Volltext (JS); Existenz der Keycodes bestätigt, Inhalt nicht am PDF gelesen |
| 4.1 | ZB Avenir 4034.2-GLBL-en 2024-04 | **ok** | 13 S., keine Bestelltabelle |
| 4.2/4.3 | 87-6204-051-00 / 951-00 Rev.1 | **ok** | Keramik-/CoCr-Charts |
| 4.5/4.7/4.8/4.9 | Bipolar / Liners / C2 / C3 | **ok** | PDFs lesbar |
| 6.1–6.11 | Medacta resources/cms | **ok** | OP-Techniken + COM + IFU lesbar |
| 1.1 / 2.3 | PINNACLE/CORAIL via aprimocdn / jnjmedtech | **ok** | Mirror; **synthes.vo.llnwd.net tot** (HTTP 000) |
| 2.1 / 1.2 / 3.1 | C-STEM 143325, MRI 101721 | **tot/nicht gelesen** | llnwd-Spiegel nicht erreichbar |
| 5.x | Mathys mathysmedical.com OP-PDFs | **Gate** | HTTP 415 / Fachkreis-Bestätigung – Werte **nicht** am Original gelesen |
| 9.1/9.2 | Aesculap Plasmafit / Excia T | **ok** | bbraun.de PDFs |
| Bicontact / CoreHip / SP II | O10702 / CoreHip / 6431 SP II | **ok** | PDFs lesbar |

---

## Punkte 1–23

### Stryker (`stryker-accolade-ii`)

**1 · EU-eIFU Accolade II / V40 / Trident II / X3 · teilweise / nicht gefunden (Inhalt)**  
- **Befund:** Perplexity-Keycodes für DE-eIFU (QIN 4424, 4451, 4355, 4450, 4351) führen auf labeling.stryker.com. Portal antwortet, liefert aber ohne interaktive Session keinen IFU-Volltext (nur HTML-Gerüst). Indikationen/Kontraindikationen/Kombinationsvorgaben daher **am Original-IFU-PDF nicht bestätigt**.  
- **Dokument:** Stryker eIFU DE · laufend · Markt DE · Portal.  
- **Vorschlag:** Claude/OpenAI: IFU-PDFs aus dem Portal speichern (nicht ins Repo) und Indikationen/Kombi wörtlich übernehmen. Bis dahin `eu_eifu`-Felder offen lassen. QIN 4350 (alt) vs. 4355 (Keramik unter Trident-MDR) als **belegt nur als Portal-Zuordnung Perplexity**, nicht als Inhalt.

**2 · X3 26 mm · nicht gefunden (am eIFU-PDF)**  
- **Befund:** Konflikt Tabelle 1 (ohne 26 mm) vs. Katalog 26C–26J bleibt. Perplexity: zwei 26-mm-X3-10°-Inserts im DE-eIFU gelistet – **nicht am IFU-PDF verifiziert** (Portal).  
- **Vorschlag:** 26 mm weiter **offen – Hersteller/Etikett klären**; nicht als EU-Standard übernehmen.

**3 · Accolade-II-Implantat-REF ACCII-PG-3 · ok (REF), Markt offen**  
- **Befund:** Design Rationale ACCII-PG-3 Rev-1_22894 ©2020, **PDF-S. 12** „Accolade II Implant catalog numbers“: Part number `6720-0027` … `6720-1140`, Size 0–11, Neck angle **132°**.  
- **Markt:** im Dokument **nicht** als EU ausgewiesen → REF nur mit Vermerk „Markt im Dokument nicht angegeben / kein EU-Nachweis aus diesem PDF“.  
- **Vorschlag:** REF-Liste in `komponenten[0].attribute.implantat_ref` übernehmen mit Quelle ACCII-PG-3 PDF-S.12 + Markt-Hinweis; EU-eIFU parallel nachziehen.

### Smith+Nephew (`smith-nephew-r3`)

**4 · POLARSTEM EU-OP-Technik 01217-en V7 10/24 · ok**  
- **Befund:** Original gelesen. Hersteller Smith & Nephew Orthopaedics AG Zug, **CE 0123**, `01217-en V7 10/24`.  
  - Cementless: Ti-6Al-4V ISO 5832-3, Konus **12/14**, CCD **135° / 126° / 145°**, mit/ohne Collar; SAP-/Size-Tabellen (PDF-S. **16**, gedruckt ca. 13).  
  - Cemented: Stainless steel ISO 5832-9, Konus 12/14, Standard 135° / Lateral 126°, Size 0–8 mit SAP/Item-No. (PDF-S. **17**, gedruckt 14).  
  - Dimensions PDF-S. **18–19**.  
- **Ersetzt** die bisherige nur-US-IFU als Größen-/REF-Quelle für EU.  
- **Vorschlag:** In `POLARSTEM zementfrei/zementiert` Größen/REF/CCD/Collar/Material aus 01217 übernehmen; US-IFU 81098832 als „kein EU-Ersatz“ belassen.

**5 · Matrix 04758 Ed. 05/26 V12 · ok (mit Caveat)**  
- **Befund:** „Stem and Femoral Ball Head Combinations“, Lit. No. **04758 Ed. 05/26 V12**, PDF-S. **1** POLARSTEM-Spalten (Cementless inkl. Collar / Cemented). OXINIUM-/CoCr-/BIOLOX-Zeilen mit a/= (approved / not). Text: Kombinationen **may not be approved in all markets**; IFU vor Ort gilt.  
- **Vorschlag:** Hausköpfe (OXINIUM, CoCr, BIOLOX delta) × POLARSTEM nur Zeilen mit **a** übernehmen; Nein-Zeilen explizit; Markt-Caveat in `regeln`/`hinweise`.

### Medacta (`medacta-quadra-amistem`)

**6 · OP-Techniken Quadra/AMIStem/Versafit · ok (Dokumente), Seitenkorrektur**  
- **Befund:** Alle genannten Medacta-Links (6.1–6.6) **lesbar**.  
  - Quadra-H 99.14HSClat.42: TOC S.3; Implantate/Nomenklatur eher **S. 8–10** (nicht „S. 3 Implantate“ wie Perplexity).  
  - Versafitcup CC Trio 99.16TRIO.42: Inlay/Kopf/Größen **S. 3–4, 9–13** bestätigt (Inhalt vorhanden).  
  - AMIStem/Quadra-C/-P: Dokumente da; Größen/REF am Original für Claude/OpenAI Zellenweise zu übernehmen.  
- **Vorschlag:** Größen/REF/Konus/Liner-Kopf aus den OP-Techniken in die JSON; Perplexity-Seitenangabe Quadra-H S.3 korrigieren.

**7 · Kombinationstabelle 99.99.COM rev.12 + IFU 75.09.017 rev.26 · ok / korrigiert**  
- **Befund:**  
  - **99.99.COM rev. 12** (10/2016): lesbar; P/O-Matrix Kopf/Schaft und Kopf/Liner; Versafitcup CC Trio-Zeilen mit P/O je Schaftfamilie.  
  - **IFU 75.09.017 rev. 26**: EN-Kompatibilitätshinweise (Stem-Head-Fit, Warnungen) um PDF-S. **5**; **Deutsch ab gedruckt S. 24** (nicht „DE ab S. 17 / Kompatibilität S. 19“ – das war NL/andere Sprache). Detaillierte Freigabematrix steht in **COM**, nicht als große Tabelle in der IFU.  
- **Vorschlag:** `passt_zu` aus COM P-Zellen; IFU nur für Warnungen/Indikationen; Seitenangabe DE korrigieren.

**8 · Bipolarkopf 99.19.42 + Endokopf 99.18.12 · ok (Doc), Freigabe aus COM/OP**  
- **Befund:** Bipolar-OP DE lesbar (Indikationen Hemi, Konzept Außenschale + UHMWPE-Innenlager). Größen/Köpfe S. 5–6 laut Aufbau; Schaftfreigaben **nur** laut Kompatibilitätsseite der OP + COM/IFU – nicht raten. Endokopf-PDF Fundstelle ok.  
- **Vorschlag:** Außen-/Innenkopf-Größen aus OP; freigegebene Schäfte (z. B. AMIStem-C) **nur** wenn in OP/COM mit P markiert.

### Zimmer Biomet (`zimmer-biomet`)

**9 · Avenir (nicht Complete) 4034.2-GLBL-en 2024-04 · ok (Beschreibung), Größen offen**  
- **Befund:** Avenir Müller **Cemented** (Protasul-S30, 12/14, cemented only) + **Uncemented** (Ti-Legierung) beschrieben; Indikationen/Kontraindikationen; Verweis auf labeling.zimmerbiomet.com. **13 PDF-Seiten, keine Bestell-/Größentabelle.**  
- **Vorschlag:** Beschreibung/Indikationen/Konus 12/14 übernehmen; Größen/REF weiter **offen** (anderes Dokument/eIFU).

**10 · Kopf-Tabellen 87-6204-051-00 / 951-00 Rev.1 · ok**  
- **Befund:** Beide Charts 2020-07-01 lesbar. Zeilen u. a. **Avenir Müller**, **CLS Spotorno**, **Alloclassic**, **Fitmore**, **MS-30** vorhanden (Keramik PDF-S. 2–4; CoCr analog). Exact Ø/Halslänge/REF = Zelleninhalt → OpenAI/Claude wörtlich extrahieren.  
- **Vorschlag:** Je Schaftfamilie nur Chart-Zeilen mit ✓; BIOLOX OPTION getrennt halten (wie bisherige Regel).

**11 · Flachprofil = Low Profile PE cup? · üblich / nicht wörtlich belegt**  
- **Befund:** C2 rev. 2/15/2023 listet **Low Profile PE / DURASUL / METASUL cup** und **Full Profile PE cup** – **nicht** das Wort „Flachprofil“. Deutsche Hausbezeichnung „Flachprofil“ ↔ Low Profile ist **üblich**, aber in diesem EN-Chart **nicht wörtlich**.  
- **Vorschlag:** In JSON: engl. Produktname aus C2 + Hinweis „DE-Etikett/IFU: Flachprofil? hausabhängig“; Größen/Kopf-Ø aus C2 allein **nicht** ablesbar (nur Cage-Kombi).

**12 · Allofit/Allofit-S Liner ↔ Kopf + Schrauben C3 · ok (Docs)**  
- **Befund:** „Modular Liners and Cups“ rev. 05/03/2019 enthält Allofit-Zeilen; C3 Bone Screw Combinations rev. 2/15/2023 lesbar. Zellenweise Freigaben für Claude/OpenAI.  
- **Vorschlag:** Allofit / Allofit-S / Allofit IT getrennt; nur ✓-Kombinationen; Schrauben aus C3.

**13 · Bipolarkopf (AP) 1946/1989 · ok**  
- **Befund:** Unipolar and Bipolar Femoral Heads Chart rev. **5/6/2019**, Spalte Bipolar Head (AP) (1946/1989), Fußnoten S. 2.  
- **Vorschlag:** Innenkopf/Schaft nur laut Chart+Fußnoten; SIRIS-Beobachtungen ≠ Freigabe.

### Mathys/Enovis (`enovis-optimys`, `enovis-twinsys`)

**14–18 · optimys / RM Pressfit / Kopf-Chart / Bipolar / seleXys · nicht gefunden (am Original)**  
- **Befund:** Perplexity-Links auf mathysmedical.com liefern **Fachkreis-Gate** (kein PDF-Inhalt). Overview-IFU-Liste ebenfalls geblockt. Damit **keine** Größen/REF/Kombi am Original bestätigt.  
- **Vorschlag:** Fundstellen in Quellen belassen; Werte **nicht** einbauen, bis Julian/Claude mit Fachkreis-Zugang PDFs liest. seleXys TH+/TPS-Warnung (historisch AU) weiter getrennt von seleXys PC halten.

### DePuy Synthes (`depuy-corail-pinnacle`)

**19 · PINNACLE 142532-220805 · ok (Teil), Matrix unvollständig**  
- **Befund:** EMEA-OP-Technik via jnjmedtech/aprimocdn gelesen (llnwd-Spiegel **tot**).  
  - Abb. 13a/13b **gedruckte S. 8 = PDF-Viewer-S. 10** (Perplexity „PDF-S. 8“ = Druckseite; Viewer-Offset +2). Neutral / +4 Neutral / +4 10° / Lipped; Farbcode Kopf-Ø (28 green, 32 blue, 36 orange, …); Cup-Trial ↔ Liner-Trial-Größen.  
  - Keramikliner-Einführung PDF-S. **18** (gedruckt 16): Size Selection Pusher=Head / Gripper=Shell – **keine** vollständige Schale×Liner×max.Kopf-Bestellmatrix.  
- **Vorschlag:** Liner-Konfigurationen + Trial-Zuordnung + Farbcode übernehmen; „aktuelle EMEA-Matrix Schale×Liner×max.Kopf“ weiter **offen** (Perplexity „Nicht gefunden“ bestätigt).

**20 · ARTICUL/EZE + CORAIL-REF · ok (CORAIL), C-STEM nicht gelesen**  
- **Befund:** CORAIL 198918-211214 UK ©2022: Size Offerings + **Ordering Information** PDF-S. **25–27** (TOC „24“; Perplexity S. 24–26 nahe). REF z. B. STD 135° KS/KA, 125°, SN, Cemented L964xx/L965xx.  
  - C-STEM 143325 (Köpfe S. 32): **llnwd tot** – Bestellseite Köpfe **diese Runde nicht am Original**.  
- **Vorschlag:** CORAIL-REF aus 198918 übernehmen; ARTICUL/EZE Ø/Offsets erst nach lesbarem EMEA-Dokument (eCatalog/e-ifu oder neuer Mirror).

**21 · TRILOC II / SELF-CENTERING / Cathcart · teilweise**  
- **Befund:** MRI-Broschüre 101721 **nicht erreichbar** (llnwd). Self-Centering OP nur **US** (Perplexity 3.2) – **kein EU-Ersatz**, Freigabe CORAIL zementiert weiter **offen**.  
- **Vorschlag:** Nur REF, falls später aus erreichbarer EMEA-Quelle; keine Schaftfreigabe erfinden. e-ifu.com per REF suchen.

### Aesculap / Link (Neudateien + Excia)

**22 · bicontact / corehip / link-spii-lubinus · ok (Kernwerte), Freigaben offen**  
- **Befund:**  
  - **Bicontact** O10702: CCD 135° (S) / 128° (H), Plasmapore/Isodur, Köpfe BIOLOX delta/forte + Isodur, Konus **12/14** (und 8/10 Option) – Kernaussagen am Original bestätigt. Plasmafit/All POLY **ohne** Freigabetabelle in diesem Doc → Status **offen** korrekt.  
  - **CoreHip** Broschüren: Primary/Extended, Valgus/Standard/Varus, Köpfe 12/14 – vorhanden; Plasmafit/All POLY Freigabe **offen**.  
  - **SP II** 6431_…_2020-05: zementiert, anatomisch, Konus **12/14**, CCD-Schablonen 117/126/135°; Lubinus Cup auf Produktseite mit SP II; IP/CombiCup Freigabe **offen** wie in JSON.  
- **Vorschlag:** Bereits eingetragene Kernwerte behalten; offene Pfannen-Freigaben nicht schließen ohne IFU-Tabelle.

**23 · Plasmafit Poly UHMWPE/Vitelene + Bipolar×Excia · ok (Liner), Freigabe Duokopf offen**  
- **Befund:** O45502 0718/1: Vitelene-Beschreibung PDF-S. **12**; Plasmafit Poly Implantate Schale↔Liner **PDF-S. 18–19** (Cup 40–62, Liner B–M, Vitelene + UHMWPE-Zeilen, REF NV…). Excia T O56002 lesbar. Bipolar Cup Katalogseite: **keine** Schaftfreigabe × Excia T zementiert.  
- **Vorschlag:** Plasmafit-Poly-Tabelle (Vitelene/UHMWPE) in `aesculap-excia` (und Kontext Bicontact nur mit Freigabe-Hinweis) übernehmen; Bipolar×Excia weiter **offen – Operateur/Hersteller**.

---

## Was in die Implantat-Dateien darf (für Claude / nach OpenAI)

| Priorität | Datei | Übernehmen (belegt) | Nicht übernehmen |
|---|---|---|---|
| Hoch | `smith-nephew-r3` | POLARSTEM EU Größen/REF/CCD/Collar/Material aus 01217; Matrix 04758 a/Nein für Hausköpfe | US-IFU als EU-Werte |
| Hoch | `depuy-corail-pinnacle` | CORAIL Ordering-REF 198918; PINNACLE Liner-Konfigs + Trial/Farbcode | erfundene Schale×Kopf-Max-Matrix; US Self-Centering-Freigabe |
| Hoch | `stryker-accolade-ii` | ACCII-PG-3 REF 6720-… mit Markt-Hinweis | 26 mm als geklärt; eIFU-Indikationen ohne PDF |
| Hoch | `medacta-quadra-amistem` | OP-Technik Größen/REF; COM P-Zellen; Bipolar-Größen aus OP | Perplexity-Seitenfehler; Register als Freigabe |
| Mittel | `zimmer-biomet` | Kopf-Charts Zeilen; Bipolar-Chart; Allofit/C3 ✓; Avenir Beschr. | Flachprofil=Low Profile als bewiesen; Größen aus 4034.2 |
| Mittel | `aesculap-excia` (+ ggf. Kontext) | Plasmafit Poly S.18–19 | Bipolar×Excia Freigabe |
| Niedrig | Bicontact/CoreHip/Link | nur Korrekturen falls Abweichung; Freigaben offen lassen | Register-Kombis als Freigabe |
| Stop | `enovis-optimys` / twinSys-Köpfe/Bipolar | — bis Mathys-PDFs lesbar | Werte aus Perplexity-Fundstellen |

---

## Offene Lücken (nach dieser Prüfung)

1. Stryker DE-eIFU-Volltexte (Indikationen, 26 mm X3).  
2. Mathys/Enovis OP-Techniken hinter Fachkreis-Gate (Punkte 14–18 komplett).  
3. DePuy: PINNACLE Bestellmatrix Schale×Liner×max.Kopf; ARTICUL/EZE Bestellseite; EU Self-Centering/Cathcart/TRILOC II Docs (llnwd tot).  
4. ZB: Avenir Größen/REF; CLS/Alloclassic/Allofit/M.E.M./Flachprofil EU-OP/Katalog; Namensklärung Flachprofil.  
5. Aesculap: Bipolar Cup × Excia T Freigabetabelle; Plasmafit/All POLY × Bicontact/CoreHip Freigabe.  
6. Link: IP/CombiCup × SP II explizite Freigabetabelle.  
7. Medacta: Zellenweise REF aus OP + COM (Arbeit für OpenAI/Claude, Docs ok).

---

## Kurzfazit

| Status | Anzahl (von 23) | Punkte |
|---|---|---|
| **ok** (am Original bestätigt, Übernahme möglich) | **11** | 3 (teilw.), 4, 5, 6, 7, 8, 10, 12, 13, 19 (teilw.), 20 (CORAIL), 22 (Kern), 23 (Liner) |
| **teilweise / korrigiert** | **5** | 1, 9, 11, 19, 20–21 |
| **nicht gefunden / Gate / tot** | **7** | 2, 14–18, Teile 1/21, C-STEM |

Genau gezählt nach Basis-Nummern: **belegt übernahmereif ~10–12**, **teilweise ~5**, **offen/Gate ~6–8**.

**Ergebnis Grok:** **ÄNDERN** – viele Fundstellen tragen, aber JSON noch nicht gefüllt; Mathys und mehrere DePuy/Stryker-eIFU-Lücken bleiben.

## Nächster Schritt

1. **OpenAI** (`pruefung/001-implantate-luecken-openai.md`): Herstellerangaben/Kompatibilität/Indikationsgrenzen zu den **ok**-Punkten gegenlesen, Zellen aus Charts/OP-Techniken vorschlagen.  
2. **Claude/Cloud:** letzter Check + Änderungsliste Multiple Choice an Julian.  
3. **Julian:** okay zu den Übernahmen.  
4. Danach Einbau in `implantate/*.json` (+0.1); Mathys erst nach lesbaren PDFs.  
5. STATUS zieht Cloud – Grok ändert STATUS nicht.
