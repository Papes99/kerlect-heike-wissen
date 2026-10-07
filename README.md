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

- **000-grundwissen** (`pakete/000-basis`) — gilt für jeden Eingriff: Sicherheit, Zählung, Sterilität, Lagerung, HF, Implantate, Präparate, Übergabe; 13 Situations-IDs.
- **001-hueft-tep** (`pakete/001-basis`, dazu `implantate/`) — Hüft-TEP primär, baut auf 000 auf; Chips mit Mengen, Naht, Varianten (Fixation/Zugang).
- 002 ff. folgen (z. B. Knie-TEP).

Ablauf (ab 07.10.2026). **Jede Datei bearbeitet nur ihr Ersteller – keiner verändert fremde Dateien.** Dateinamen ohne Versionsnummer.
1. **Claude** schreibt `pakete/NNN-basis.json` + `.md` (das Paket; Abschnitt „Zur Prüfung in dieser Runde“) und setzt in `pruefung/STATUS.json` `runde: grok`.
2. **Grok** schreibt `pruefung/NNN-grok.md` (Änderungsvorschläge).
3. **Astra** liest alles, ändert nichts, schreibt `pruefung/NNN-astra.md` (Änderungsvorschläge wie Grok; Grok-Punkte, die Astra genauso übernehmen würde, bestätigt sie ausdrücklich, plus eigene).
4. **Claude** liest alle drei (Basis, Grok, Astra), prüft kritisch mit und schickt Julian im Chat die **Änderungsliste: was Claude übernehmen würde, was nicht und warum** (`runde: julian`).
5. **Julian** sagt ok bzw. korrigiert → Claude baut ein und setzt `runde: eingebaut`.
6. **Grok** und **Astra** löschen danach jeweils ihre eigene Datei → übrig bleibt nur `NNN-basis`. Nächstes Paket nur auf Julians Wort.

## Gegenprüfung

Siehe [PRUEFAUFTRAG.md](PRUEFAUFTRAG.md). Status: [pruefung/STATUS.json](pruefung/STATUS.json).

## Regeln (Kurz)

- Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.
- Nichts erfinden; Hausvorgaben, IFU und ärztliche Anordnung gehen immer vor.
- Quellen: AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-IFU/OP-Technik, öffentliche Klinik-SOPs — keine Foren/Shops.
- Keine Patientendaten.

## Lizenz / Nutzung

Entwürfe für Kerlect (Kerlwerk). Veröffentlichung zur Gegenprüfung durch KI/Fachpersonen; keine klinische Freigabe.
