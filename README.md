# kerlect-heike-wissen

Öffentliche Wissenspakete für **Heike** (Kerlect OP-Assistentin), Schwerpunkt **Springer-Vorbereitung**.

## Inhalt

| Ordner | Zweck |
| --- | --- |
| `pakete/` | Wissenspakete als `NNN-name.json` + `.md` (Entwürfe) |
| `pruefung/` | Gegenprüfung: `STATUS.json`, ggf. Berichte |
| `eingang/` | Neue Dateien (Grok-Prüfungen, Korrekturen) – werden nicht verändert |
| `aenderungen/` | Änderungsvorschläge von Claude zu Eingangsdateien, `INDEX.md` |

## Aktuelle Reihe

- **000-grundwissen** — gilt für jeden Eingriff: Sicherheit, Zählung, Sterilität, Lagerung, HF, Implantate, Präparate, Übergabe; 13 Situations-IDs.
- **001-hueft-tep** — Hüft-TEP primär, baut auf 000 auf; Chips mit Mengen, Naht, Varianten (Fixation/Zugang).
- 002 ff. folgen (z. B. Knie-TEP).

Ablauf (ab 07.10.2026): Grok prüft offene Pakete → Ergebnis als Datei in `eingang/` → Claude prüft stündlich, legt einen Vorschlag in `aenderungen/` an und baut die „übernehmen“-Punkte **automatisch** als neue Paketversion ein (alte Version in `pakete/archiv/`) → **Astra prüft die neue Version vor der Integration** (`pruefung/STATUS.json`: `astra_vor_integration`) → Grok prüft die neue Version erneut. Punkte „Julian entscheidet“ (z. B. Implantat-Kombinationen) warten auf Julian.

## Gegenprüfung

Siehe [PRUEFAUFTRAG.md](PRUEFAUFTRAG.md). Status: [pruefung/STATUS.json](pruefung/STATUS.json).

## Regeln (Kurz)

- Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.
- Nichts erfinden; Hausvorgaben, IFU und ärztliche Anordnung gehen immer vor.
- Quellen: AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-IFU/OP-Technik, öffentliche Klinik-SOPs — keine Foren/Shops.
- Keine Patientendaten.

## Lizenz / Nutzung

Entwürfe für Kerlect (Kerlwerk). Veröffentlichung zur Gegenprüfung durch KI/Fachpersonen; keine klinische Freigabe.
