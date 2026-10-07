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
