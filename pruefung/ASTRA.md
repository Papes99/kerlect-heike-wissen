# Astra – Prüfauftrag vor Integration

_Einzige Datei für Astra. Sie wird bei jeder neuen Paketversion **überschrieben** und enthält nur das, was Astra noch nicht geprüft hat. Bereits Freigegebenes taucht hier nicht mehr auf._

## Auftrag
Prüfe **nur die unten aufgeführten Änderungen** (ALT → NEU). Je Punkt: **ok** oder **Fehler** (mit Problem und Korrekturvorschlag). Prüfkriterien: Die Aussage stimmt fachlich. „belegt“ nur mit passender Quelle. Das Schema ist eingehalten (label ≤ 40 Zeichen, gilt_fuer, sicherheit, hausabhaengig, quelle). Nichts ist gefährlich oder widerspricht Paket 000.

**Antwort als neue Datei:** `eingang/<JJJJ-MM-TT>-<paket>-v<version>-astra.md`, erste Zeile `FREIGEGEBEN` oder `FEHLER`, darunter eine Tabelle | Nr | ok/Fehler | Problem | Vorschlag |. Bestehende Dateien bitte nicht ändern.

---

## 001-hueft-tep v1.0 → v1.1 (2026-10-07)
Grundlage: Grok-Prüfung `eingang/2026-10-07-001-hueft-tep-grok.md`. Claude konnte die Quellen nicht selbst öffnen (gesperrt), deshalb bitte die Quellenstellen besonders prüfen.

| Nr | Art | Abschnitt · Eintrag | ALT (nur geänderte Felder) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | position · **NE-Kontakt kontrollieren** | hinweis: Bei monopolarer Anwendung: geeignete Anlagefläche und vollständigen Hautkontakt gemäß Produkt-IFU prüfen; nach Umlagerung erneut kontrollieren. | hinweis: Bei monopolarer Anwendung: geeignete Anlagefläche und vollständigen Hautkontakt gemäß Produkt-IFU prüfen; nach Umlagerung erneut kontrollieren. HEBU GAHF113 ist nur ein Produktbeispiel; maßgeblich ist die IFU der im Haus verwendeten Neutralelektrode. | Q_HEBU – Einmal-Neutralelektroden Gebrauchsanweisung GAHF113 |
| 2 | geändert | draping · **Flüssigkeitsdichte Abdeckung** | spez: None; hausabhaengig: False | spez: Bei erwartetem Durchfeuchten flüssigkeitsundurchlässig (KRINKO Kat. IB); hausabhaengig: True | Q_KRINKO – Prävention postoperativer Wundinfektionen |
| 3 | geändert | workflow · **Anästhesie vor Zement informieren** | spez: None; hinweis: Zementierung rechtzeitig im Team ankündigen; BCIS-Vorsorge gemeinsam abstimmen. | spez: Anästhesie über jeden Schritt des Zementiervorgangs informieren; hinweis: Nicht nur einmal vor dem Einbringen: jeden Zementierschritt ansagen; BCIS-Vorsorge gemeinsam abstimmen. | Q_BCIS – Factsheet Implantationssyndrom / BCIS |
| 4 | neu | count · **Markraumstopper mitzählen** | – | spez: Implantierten/belassenen Markraumstopper in Zähl- und Implantatdokumentation; gilt_fuer: ['zementiert', 'hybrid']; optional: False; sicherheit: üblich; hausabhaengig: True; hinweis: Beabsichtigt belassenes Material gesondert dokumentieren; Haus-Zählplan maßgeblich. | keine (hausabhängig) |
| 5 | geändert | pitfalls · **Alkoholansammlungen vermeiden** | spez: None; hausabhaengig: False; quelle: Q_HEBU; hinweis: Brennbare Hautpräparate dürfen sich nicht ansammeln; vor HF-Anwendung ausreichende Trocknung sicherstellen, nach Produkt-IFU. | spez: Keine Flüssigkeitsansammlung des Hautantiseptikums; NE nicht unter Flüssigkeit; hausabhaengig: True; quelle: Q_KRINKO; hinweis: Vor HF-Anwendung Einwirkzeit/Abtrocknen laut Antiseptikum-IFU. Brandrisiko durch entzündliche Hautpräparate ergänzend laut NE-IFU (Q_HEBU). | Q_KRINKO – Prävention postoperativer Wundinfektionen |
| 6 | geändert | heike_hinweise | Zementiert? Sag der Anästhesie vor dem Einbringen Bescheid. | Zementiert? Anästhesie über jeden Zementierschritt informieren. | Q_BCIS – Factsheet BCIS |
| 7 | neu | offen | – | Implantate: Mathys-Werte offen (kein Herstellerdokument lesbar). Laut Grok (Accolade II Surgical Protocol ACCII-SP-1 Rev-4, S. 3/12) ist Accolade II in der EU nicht für Hemiarthroplastik indiziert – Haus-Kombi Stryker-Duokopf + Schaft klären. | – |
| 8 | neu | julian_pruefen | – | Stryker-Duokopf: auf welchem Schaft? z. B. Accolade II, Accolade TMZF, Exeter (zementiert) oder Hemi mit Mathys Bipolarkopf auf twinSys. | – |
| 9 | geändert | quellen · **Q_KRINKO** (Fundstelle) | 2018, S. 461, Abschnitt 4.2.4 Abdeckung | + Kat. II: keine Flüssigkeitsansammlung des Hautantiseptikums (laut Grok S. 460; Seite 460/461 am PDF bestätigen) | Q_KRINKO |

Quellenstellen: siehe `quellen` in `pakete/001-hueft-tep.json`. Was hier nicht steht, ist gegenüber v1.0 unverändert und muss nicht erneut geprüft werden.

---

## Implantat-Daten (neu): implantate/stryker-accolade-ii + implantate/smith-nephew-polarstem
Berichtigung von Claudes Websuche-Entwurf (`eingang/2026-10-07-implantate-*-extrakt`, verified:false) mit den Werten, die Grok im Herstellerdokument gelesen hat (`eingang/2026-10-07-001-hueft-tep-grok.md`, Abschnitt C). Claude konnte die Dokumente nicht öffnen.

| Nr | Art | Datei · Komponente | ALT (Entwurf) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | neu | stryker · Accolade II | Konus V40, zementfrei | + CCD 132° Standard / 127° High-Offset; **EU: nicht für Hemi indiziert** | ACCII-SP-1 Rev-4, S. 3, 4, 12 |
| 2 | geändert | stryker · V40 BIOLOX delta | 28/32/36, Offset −5 bis +7,5 pauschal | 28: −4/−2,7/0/+4 · 32: −4/0/+4 · 36: −5/−2,5/0/+2,5/+5/+7,5 | ACCII-SP-1 Rev-4, S. 12 |
| 3 | geändert | stryker · Universal Taper BIOLOX delta | Offset 0 | Offset −2,5/0/+4; nur mit Sleeve 6519-T-XX | ACCII-SP-1 Rev-4, S. 12 |
| 4 | geändert | stryker · Trident II | Schalen 42–72, Kopf 22–44 (Websuche) | Größen/Inlays/max. Kopf **offen** (keine OP-Technik gelesen) | Produktseite DE |
| 5 | geändert | stryker · UHR | Außen-Ø „u. a. 52“ | Außen-Ø 36–61, Innenkopf 22/26/28; **keine Freigabe mit Accolade II in EU** | UHR HE01-160 Rev1 (Japan) + ACCII-SP-1 |
| 6 | neu | smith-nephew · POLARSTEM zementfrei | Ti-6Al-4V, Konus offen | Konus 12/14; Ti mit Titanplasma/HA; CCD 135°/126°/145°, teils Kragen | IFU 81098832 Rev. 2 |
| 7 | neu | smith-nephew · POLARSTEM zementiert | – | Edelstahl; Konus 12/14; nur OXINIUM- oder BIOLOX-delta-Köpfe | IFU 81098832 Rev. 2 |
| 8 | neu | smith-nephew · R3 | – | im Haus (Julian); Größen/Inlays offen | Julian 07.10.2026 |

Mathys: keine Datei – kein Herstellerdokument lesbar, bleibt offen.
