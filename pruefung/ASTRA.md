# Astra – Prüfauftrag vor Integration

_Einzige Datei für Astra. Sie wird bei jeder neuen Version **überschrieben** und enthält nur, was Astra noch nicht geprüft hat. Freigegebenes taucht hier nicht mehr auf._

## Auftrag
Prüfe **nur die unten aufgeführten Änderungen** (ALT → NEU), je Abschnitt getrennt. Je Punkt: **ok** oder **Fehler** (Problem + Korrekturvorschlag). Kriterien: fachlich richtig; „belegt“ nur mit passender Quelle; Schema (label ≤ 40, gilt_fuer, sicherheit, hausabhaengig, quelle); nichts Gefährliches; kein Widerspruch zwischen 000 und 001.

**Antwort je Abschnitt als neue Datei:** `eingang/<JJJJ-MM-TT>-<paket>-v<version>-astra.md` (für Implantate: `eingang/<JJJJ-MM-TT>-implantate-astra.md`), erste Zeile `FREIGEGEBEN` oder `FEHLER`, darunter | Nr | ok/Fehler | Problem | Vorschlag | Quelle | Priorität |, optional „Zusatz (Praxis)“. Bestehende Dateien nicht ändern.

---

## 001-hueft-tep v1.1 → v1.2
Grundlage: deine Prüfung `eingang/2026-10-07-001-hueft-tep-v1.1-astra.md` (FEHLER) – K2, K5a/b, K8, K9, Q_STRYKER_ACCII, P1, P2 1:1 eingebaut. Bitte nur prüfen, ob richtig umgesetzt. Deine ok-Punkte 1, 3, 4, 6, 7 sind unverändert.

| Nr | Art | Abschnitt · Eintrag | ALT (nur geänderte Felder) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | draping · **Flüssigkeitsdichte Abdeckung** | spez: Bei erwartetem Durchfeuchten flüssigkeitsundurchlässig (KRINKO Kat. IB); hausabhaengig: True; hinweis: Bei erwartetem Durchfeuchten flüssigkeitsdichte Abdeckung einsetzen. | spez: Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).; hausabhaengig: False; hinweis: Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen. | Q_KRINKO – Prävention postoperativer Wundinfektionen |
| 2 | neu | workflow · **Zementansage rückbestätigen** | – | gilt_fuer: ['zementiert', 'hybrid']; optional: False; sicherheit: hausabhängig; hausabhaengig: True; hinweis: Vorab festlegen, wer die Schritte ansagt. Beispiel: „Zement wird jetzt eingebracht“ – Rückmeldung der Anästhesie abwarten; bei fehlender Antwort unmittelbar klären. Konkrete Ansagen/Zuständigkeit laut Haus-SOP. | keine (hausabhängig) |
| 3 | neu | count · **Stopper und Messhilfe unterscheiden** | – | gilt_fuer: ['zementiert', 'hybrid']; optional: False; sicherheit: hausabhängig; hausabhaengig: True; hinweis: Implantierter Stopper und temporäre Mess-/Einführteile getrennt führen. Beispiel: Stopper absichtlich im Markraum, Messhilfe wieder außerhalb. Eine dokumentierte Implantation erklärt keinen fehlenden Trial oder Instrumententeil; Haus-Zählplan und Produkt-IFU prüfen. | keine (hausabhängig) |
| 4 | geändert | pitfalls · **Alkoholansammlungen vermeiden** | spez: Keine Flüssigkeitsansammlung des Hautantiseptikums; NE nicht unter Flüssigkeit; hausabhaengig: True; hinweis: Vor HF-Anwendung Einwirkzeit/Abtrocknen laut Antiseptikum-IFU. Brandrisiko durch entzündliche Hautpräparate ergänzend laut NE-IFU (Q_HEBU). | spez: Patient darf nicht in angesammeltem Hautantiseptikum liegen.; hausabhaengig: False; hinweis: Einwirkzeit und anschließende Trocknung laut IFU des verwendeten Antiseptikums prüfen; HF-Brandrisiko ergänzend Q_HEBU, Abschnitt 6. NE-Flüssigkeitsschutz getrennt belegen. | Q_KRINKO – Prävention postoperativer Wundinfektionen |
| 5 | neu | pitfalls · **NE vor Flüssigkeit schützen** | – | spez: Flüssigkeitskontakt und Eindringen unter die NE vermeiden.; gilt_fuer: ['hf_mono']; optional: False; sicherheit: belegt; hausabhaengig: False; quelle: Q_HEBU; hinweis: HEBU GAHF113V004 als Produktbeispiel; maßgeblich ist die IFU der tatsächlich verwendeten NE. | Q_HEBU – Einmal-Neutralelektroden Gebrauchsanweisung GAHF113 |
| 6 | neu | offen | – | Implantate: Mathys-Werte offen (kein Herstellerdokument lesbar). Accolade II ist laut Q_STRYKER_ACCII (Rev-4, 2022, S. 3/12) in der EU nicht für Hemiarthroplastik indiziert; keine Kopf-Schaft-Kombination über Hersteller hinweg ableiten. | keine (hausabhängig) |
| 7 | gestrichen | offen | Implantate: Mathys-Werte offen (kein Herstellerdokument lesbar). Laut Grok (Accolade II Surgical Protocol ACCII-SP-1 Rev-4, S. 3/12) ist Accolade II in der EU nicht für Hemiarthroplastik indiziert – Haus-Kombi Stryker-Duokopf + Schaft klären. | – | keine (hausabhängig) |
| 8 | neu | julian_pruefen | – | Nur Rückfrage außerhalb des Primär-TEP-Scope: Wie heißen Duokopf, Innenkopf und Schaft genau? Bitte Hersteller, Produktlinie, REF und aktuelle EU-IFU nennen. Zur Identifikation: Steht auf der Schaftpackung Accolade II, Accolade TMZF, Exeter oder twinSys? Dies sind keine freigegebenen Kombinationsvorschläge. Accolade II ist laut Q_STRYKER_ACCII (Rev-4, 2022, S. 3/12) in der EU nicht für Hemiarthroplastik indiziert. Auch eine Mathys-Bipolarkopf/twinSys-Kombination bleibt ohne konkreten Herstellerbeleg offen; keine Kombination über Hersteller hinweg ableiten. | keine (hausabhängig) |
| 9 | gestrichen | julian_pruefen | Stryker-Duokopf: auf welchem Schaft? z. B. Accolade II, Accolade TMZF, Exeter (zementiert) oder Hemi mit Mathys Bipolarkopf auf twinSys. | – | keine (hausabhängig) |
| 10 | geändert | quellen · **Q_KRINKO** | 2018, Bundesgesundheitsblatt 61:448–473, S. 461, Abschnitt 4.2.4 Abdeckung. Keine generelle Positivempfehlung für imprägnierte Folie. Zusätzlich Kat. II: keine Flüssigkeitsansammlung des Hautantiseptikums (laut Grok-Prüfung 07.10.2026 S. 460; Seite 460/461 am PDF bestätigen). | 2018, Bundesgesundheitsblatt 61:448–473, gedruckte S. 461 (PDF-S. 14), Abschnitt 4.1 Präoperativ und intraoperativ: Hautantiseptikum-Ansammlungen (Kat. II); flüssigkeitsundurchlässige Abdeckung bei nicht ausschließbarem Durchfeuchten (Kat. IB). | Q_KRINKO – Prävention postoperativer Wundinfektionen |
| 11 | neu | quellen · **Q_STRYKER_ACCII** | – | Accolade II Femoral Hip System – Surgical protocol – ACCII-SP-1_Rev-4_34423, © 2022; S. 3: EU-Indikationen; S. 12: Ausschluss Hemiarthroplastik in EU; Dokumentcode S. 25. | Q_STRYKER_ACCII – Accolade II Femoral Hip System – Surgical protocol |

---

## 000-grundwissen v1.1 → v1.2
Grundlage: Grok-Prüfung `eingang/2026-10-07-000-grundwissen-v1.1-grok.md` (Grok Nr. 1–7, 11; Nr. 8–10 bleiben offen). KRINKO-Seiten nach deiner 001-Prüfung (S. 461, Abschnitt 4.1) statt Groks S. 460. Erstmals bei Astra – nur diese Änderungen prüfen.

| Nr | Art | Abschnitt · Eintrag | ALT (nur geänderte Felder) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | facts · **Patientenidentität geprüft** | spez: Armband + Rückfrage; hinweis: None | spez: Patient bestätigt Identität (WHO); Armband + aktive Rückfrage zusätzlich (KVWL/APS); hinweis: Armband steht nicht in der WHO-Checkliste; Armband + Rückfrage laut q_kvwl. | q_who – Implementation Manual WHO Surgical Safety Checklist 2009 |
| 2 | geändert | draping · **Sterile Tische erst kurz vor Beginn** | hinweis: None | hinweis: KRINKO S. 461 Kat. II; Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 3 | geändert | draping · **Abdeckung flüssigkeitsdicht** | spez: passend zum Eingriff; sicherheit: hausabhängig; hausabhaengig: True; quelle: None; hinweis: None | spez: Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 4 | geändert | draping · **Keine nicht imprägnierte Inzisionsfolie** | spez: None | spez: nicht antiseptisch imprägnierte Folien nicht verwenden (Kat. IB) | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 5 | geändert | count · **Nadeln, Klingen, Clips, Drahtteile** | spez: None | spez: Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan | q_aps – Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“ |
| 6 | geändert | implants · **Anästhesie vor Zement informieren** | spez: None; hinweis: None | spez: Anästhesie über jeden Schritt des Zementiervorgangs informieren; hinweis: AMBOSS: vor Einbringen; q_bcis: jeden Zementierschritt. | q_amboss – Endoprothetik des Hüftgelenks (Zementhinweis) |
| 7 | neu | pitfalls · **Keine Antiseptikum-Pfützen** | – | spez: Patient darf nicht in angesammeltem Hautantiseptikum liegen.; gilt_fuer: ['alle']; optional: False; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; besonders vor monopolarer HF. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 8 | geändert | heike_hinweise | Zement geplant? Sag der Anästhesie vor dem Einbringen Bescheid. | Zement geplant? Anästhesie über jeden Zementierschritt informieren. | keine (hausabhängig) |
| 9 | geändert | quellen · **q_krinko** | – | S. 460 Kat. IB (keine nicht imprägnierte Inzisionsfolie), S. 460 Kat. II (Türen/Fluktuation), S. 461 Abschnitt 4.1 (Antiseptikum-Ansammlung Kat. II; flüssigkeitsundurchlässige Abdeckung Kat. IB; sterile Tische Kat. II), Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 10 | neu | quellen · **q_bcis** | – | Factsheet Implantationssyndrom / BCIS – PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über jeden Schritt des Zementiervorgangs informieren. | q_bcis – Factsheet Implantationssyndrom / BCIS |

---

## Implantat-Daten (neu): implantate/stryker-accolade-ii + implantate/smith-nephew-polarstem
Berichtigung von Claudes Websuche-Entwurf (`eingang/2026-10-07-implantate-*-extrakt`, verified:false) mit den Werten, die Grok im Herstellerdokument gelesen hat (`eingang/2026-10-07-001-hueft-tep-grok.md`, Abschnitt C). Claude konnte die Dokumente nicht öffnen.

| Nr | Art | Datei · Komponente | ALT (Entwurf) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | neu | stryker · Accolade II | Konus V40, zementfrei | + CCD 132° Standard / 127° High-Offset; **EU: nicht für Hemi indiziert** (von Astra in 001-Prüfung bestätigt) | ACCII-SP-1_Rev-4_34423, S. 3, 4, 12 · https://cdn.stryker.com/SYKGCSDOC-2-45343 |
| 2 | geändert | stryker · V40 BIOLOX delta | 28/32/36, Offset −5 bis +7,5 pauschal | 28: −4/−2,7/0/+4 · 32: −4/0/+4 · 36: −5/−2,5/0/+2,5/+5/+7,5 | ACCII-SP-1 Rev-4, S. 12 |
| 3 | geändert | stryker · Universal Taper BIOLOX delta | Offset 0 | Offset −2,5/0/+4; nur mit Sleeve 6519-T-XX | ACCII-SP-1 Rev-4, S. 12 |
| 4 | geändert | stryker · Trident II | Schalen 42–72, Kopf 22–44 (Websuche) | Größen/Inlays/max. Kopf **offen** (keine OP-Technik gelesen) | Produktseite DE |
| 5 | geändert | stryker · UHR | Außen-Ø „u. a. 52“ | Außen-Ø 36–61, Innenkopf 22/26/28; **keine Freigabe mit Accolade II in EU** | UHR HE01-160 Rev1 (Japan) + ACCII-SP-1 |
| 6 | neu | smith-nephew · POLARSTEM zementfrei | Ti-6Al-4V, Konus offen | Konus 12/14; Ti mit Titanplasma/HA; CCD 135°/126°/145°, teils Kragen | IFU 81098832 Rev. 2 |
| 7 | neu | smith-nephew · POLARSTEM zementiert | – | Edelstahl; Konus 12/14; nur OXINIUM- oder BIOLOX-delta-Köpfe | IFU 81098832 Rev. 2 |
| 8 | neu | smith-nephew · R3 | – | im Haus (Julian); Größen/Inlays offen | Julian 07.10.2026 |

Mathys: keine Datei – kein Herstellerdokument lesbar, bleibt offen.
