# kerlect-heike-wissen

Öffentliche Wissenspakete für **Heike** (Kerlect OP-Assistentin), Schwerpunkt **Springer-Vorbereitung**.

## Inhalt

| Ordner | Zweck |
| --- | --- |
| `pakete/` (`NNN-basis`) | Wissenspakete als `NNN-name.json` + `.md` (Entwürfe) |
| `pruefung/` | Gegenprüfung: `STATUS.json`, ggf. Berichte |
| `eingang/` | Neue Dateien (Grok-Prüfungen, Korrekturen) – werden nicht verändert |
| `aenderungen/` | Änderungsvorschläge von Claude zu Eingangsdateien, `INDEX.md` |

## Aktuelle Reihe

- **000-grundwissen** (`pakete/000-abschluss.md`, abgeschlossen v1.5) — gilt für jeden Eingriff: Sicherheit, Zählung, Sterilität, Lagerung, HF, Implantate, Präparate, Übergabe; 13 Situations-IDs.
- **001-hueft-tep** (`pakete/001-abschluss.md`, abgeschlossen v1.3, dazu `implantate/`: Stryker Accolade II, Aesculap Excia, S+N R3, Enovis twinSys) — Hüft-TEP primär, baut auf 000 auf; Chips mit Mengen, Naht, Varianten (Fixation/Zugang).
- 002 ff. folgen (z. B. Knie-TEP).

Ablauf (ab 07.10.2026). **Jede Datei bearbeitet nur ihr Ersteller – keiner verändert fremde Dateien.** Dateinamen ohne Versionsnummer.
1. **Claude** schreibt `pakete/NNN-basis.json` + `.md` (das Paket; Abschnitt „Zur Prüfung in dieser Runde“) und setzt in `pruefung/STATUS.json` `runde: grok`.
1b. Braucht es Implantat-Quellen, legt Claude zusätzlich `pakete/NNN-quellen-auftrag.md` an.
2. **Grok** schreibt `pruefung/NNN-grok.md` (Änderungsvorschläge; sucht die Quellen aus dem Quellen-Auftrag selbst, Nicht Gefundenes als „nicht gefunden“).
3. **Astra** liest alles, ändert nichts, schreibt `pruefung/NNN-astra.md` (Grok-Punkte, die Astra genauso übernehmen würde, bestätigt sie ausdrücklich, plus eigene). **Bis Paket 020 nur die Implantate** (Implantat-Suche und -Einbau); Läufe ohne Implantat-Bezug ohne Astra. Nach 020 prüft Astra in einem Gesamtlauf alles (000–020 + `implantate/`) → `pruefung/gesamt-astra.md`.
4. **Claude** liest alles (Basis, Grok, ggf. Astra), prüft kritisch mit und schickt Julian im Chat die **Änderungsliste: was Claude übernehmen würde, was nicht und warum** (`runde: julian`). Am Ende der Liste: **fertiger Perplexity-Prompt** für alles, was nicht gefunden wurde – Julian kopiert ihn zu Perplexity und das Ergebnis zurück in den Chat (`eingang/`).
5. **Julian** sagt ok bzw. korrigiert → Claude baut ein und macht daraus **eine Abschlussdatei** `pakete/NNN-abschluss.md` (oben lesbar, unten JSON für die App); die basis-Dateien verschwinden.
6. **Grok** und **Astra** löschen danach jeweils ihre eigene Datei → übrig bleibt nur `NNN-basis`. Nächstes Paket nur auf Julians Wort.

## Gegenprüfung

Siehe [PRUEFAUFTRAG.md](PRUEFAUFTRAG.md). Status: [pruefung/STATUS.json](pruefung/STATUS.json).

## Regeln (Kurz)

- **Rückfragen an Julian:** immer mit möglichst vielen Beispiel-Systemen/Produkten je Hersteller zur Auswahl (Schäfte, Pfannen, Inlays, Köpfe, Duoköpfe), damit er sie beim Lesen wiedererkennt.
- **Systeme nicht mischen:** Jede Implantat-Komponente nur mit dem, was der Hersteller im Dokument ausdrücklich dafür vorsieht – keine eigenen Kombinationen.
- **Zuordnung:** 000 = allgemeines OP-Wissen für jeden Eingriff. Eingriffspakete (001 …) enthalten nur Eingriffsspezifisches. Allgemeines wandert nach 000 und wird im Eingriffspaket gestrichen.

- Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.
- Nichts erfinden; Hausvorgaben, IFU und ärztliche Anordnung gehen immer vor.
- Quellen: AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-IFU/OP-Technik, öffentliche Klinik-SOPs — keine Foren/Shops.
- Keine Patientendaten.

## Lizenz / Nutzung

Entwürfe für Kerlect (Kerlwerk). Veröffentlichung zur Gegenprüfung durch KI/Fachpersonen; keine klinische Freigabe.
