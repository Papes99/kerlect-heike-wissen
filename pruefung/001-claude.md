# 001 – Claude

_Arbeitsdatei Runde 001 (001-hueft-tep + implantate/stryker-accolade-ii, implantate/smith-nephew-polarstem). Wird bei jeder Runde **überschrieben**. Nach Astras Urteil baut Claude ein und **löscht 001-claude, 001-grok und 001-astra** – übrig bleibt nur das Paket._

## Ablauf dieser Runde
1. **Grok** prüft diese Datei → schreibt `pruefung/001-grok.md`.
2. **Astra** prüft diese Datei **und** `pruefung/001-grok.md` (Grok-Datei unverändert lassen) → schreibt `pruefung/001-astra.md`. Erste Zeile `FREIGEGEBEN` oder `ÄNDERN`. Bei `ÄNDERN`: Tabelle | Nr | Quelle des Punkts (Claude/Grok/Astra) | Entscheidung | Endgültiger Text im Paket-Schema | Quelle (Titel, Stand, Seite, URL) |. Astra entscheidet abschließend, auch zwischen Claude und Grok.
3. **Claude** baut Astras Entscheidung 1:1 ein, schickt Julian die Auflistung und löscht die drei Arbeitsdateien.

## Was Claude geändert hat (noch nicht abschließend geprüft)
Die Änderungen stehen schon im Paket (`pakete/`). Geprüft wird nur, was hier steht. Alles andere ist unverändert.

### 001-hueft-tep (v1.1 → v1.2)
Grundlage: deine Prüfung 2026-10-07-001-hueft-tep-v1.1-astra.md (im Repo unter eingang/) (FEHLER) – K2, K5a/b, K8, K9, Q_STRYKER_ACCII, P1, P2 1:1 eingebaut. Bitte nur prüfen, ob richtig umgesetzt. Deine ok-Punkte 1, 3, 4, 6, 7 sind unverändert. Groks Nachprüfung von v1.1 (2026-10-07-001-hueft-tep-v1.1-grok.md (im Repo unter eingang/)) bestätigt K2/K5/K8/K9/P1/P2; Groks Abweichung „Alkoholansammlungen gilt_fuer alle“ nicht übernommen (deine K5a: hf_mono; allgemeine Regel steht in 000 „Keine Antiseptikum-Pfützen“).

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

### Implantate zu 001: Umsetzung von Astras Implantat-Prüfung (stryker-accolade-ii, smith-nephew-polarstem)
Grundlage: 2026-10-07-implantate-vstand-2026-10-07-astra.md (im Repo unter eingang/) (FEHLER) – K5, K6, K7, P1, P2 1:1 umgesetzt. Bitte nur die Umsetzung prüfen; deine ok-Punkte 1–4, 8 sind unverändert (nur Seitenergänzung S. 5).

| Nr | Art | Datei · Komponente | ALT | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | beide · verified | true | **false** + „Teilprüfung: Markt-/EU-Anwendbarkeit teilweise offen“ | dein Bericht |
| 2 | geändert | stryker · Quelle q1 Seiten | 3, 4, 12 | 3/12 EU-Grenze, **5 CCD**, 12 Kopfwerte, 15/17 Hülsen | ACCII-SP-1_Rev-4_34423 |
| 3 | geändert | stryker · UHR (K5) | Außen-Ø 36–61, Innenkopf 22/26/28 | **nur Japan-Katalogdaten**: 36/38/40→22; 41/42/43→26; 44–56 (1-mm), 58, 61→28; EU-Größen/REF offen; Hemi-Sperre über q1, nicht q3 | HE01-160_Rev1, 03/2022, PDF-S. 2 |
| 4 | geändert | stryker · Universal-Taper-Kopf | Sleeve 6519-T-XX | Familie 6519-T-XX, **keine bestellfähige REF**; Hülse nach Offset/IFU | ACCII-SP-1 S. 12 |
| 5 | neu | stryker · Regel (P1) | – | Universal-Taper-Hülse zuerst auf den Schaftkonus, dann Kopf; nicht im Keramikkopf vormontieren | ACCII-SP-1 S. 15 |
| 6 | geändert | polarstem · Quelle (K6/K7) | IFU 81098832 Rev. 2 | + 06/2021, **Markt USA** (S. 1), S. 4/2/5 | US-IFU |
| 7 | geändert | polarstem · zementfrei (K6) | „teils Kragen“ | **US-Daten**; Standard und lateral auch mit Kragen; EU-Varianten offen | US-IFU S. 1/4 |
| 8 | geändert | polarstem · zementiert (K7) | nur OXINIUM/BIOLOX delta | **US-Daten**; keine pauschale EU-Kombinationsregel – konkreten S+N-Kopf mit EU-Freigabe prüfen | US-IFU S. 1/4/5 |
| 9 | neu | polarstem · Regel (P2) | – | Gleicher Konus/gleiche Keramikmarke ist kein Kombinationsnachweis | US-IFU S. 2/5 |
| 10 | neu | polarstem · offen | – | Aktuelle EU-IFU POLARSTEM nachfordern | – |

**Wartet auf Julian (nicht prüfen):** Schaft des Duokopfs (z. B. Accolade II / Accolade TMZF / Exeter / twinSys) · S+N-Schaft (z. B. POLARSTEM / SL-PLUS / ANTHOLOGY) und EU-IFU.
