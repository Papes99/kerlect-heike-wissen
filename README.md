# kerlect-heike-wissen

Öffentliche Wissenspakete für **Heike** (Kerlect OP-Assistentin), Schwerpunkt **Springer-Vorbereitung**.

## Inhalt

| Ordner | Zweck |
| --- | --- |
| `pakete/` (`NNN-basis`) | Wissenspakete als `NNN-name.json` + `.md` (Entwürfe) |
| `pruefung/` | Gegenprüfung: `STATUS.json`, ggf. Berichte |
| `eingang/` | Neue Dateien (Grok-Prüfungen, Korrekturen) – werden nicht verändert |
| `aenderungen/` | Änderungsvorschläge von Claude zu Eingangsdateien, `INDEX.md` |

## App (Kerlect)

**Astra programmiert – nur in Kerlect** (Base44-App „Kerlect“, ID `6aa3f64b0b23cc244ce7686d`). Claude schreibt keinen App-Code, sondern liefert Daten, Vorgaben (`app/`) und Prototypen.

## Auswahl der Implantat-Systeme

Nach Häufigkeit in DACH (Register EPRD, SIRIS, Österreich) – nicht nach einer einzelnen Klinik. Jede Klinik gleicht ihren Bestand selbst am Etikett ab.

## Aktuelle Reihe

- **000-grundwissen** (`pakete/000-abschluss.md`, abgeschlossen v1.5) — gilt für jeden Eingriff: Sicherheit, Zählung, Sterilität, Lagerung, HF, Implantate, Präparate, Übergabe; 13 Situations-IDs.
- **001-hueft-tep** (`pakete/001-abschluss.md`, abgeschlossen v1.3, dazu `implantate/`: 11 Systemdateien häufiger DACH-Systeme, Ranking `implantate/auswahl-dach.md`) — Hüft-TEP primär, baut auf 000 auf; Chips mit Mengen, Naht, Varianten (Fixation/Zugang).
- **002-knie-tep** folgt (Start auf „002 los“); danach 003 ff.

Ablauf – **Prüf-Pipeline NEU** (Julian, 07.10.2026; Details `pruefung/PIPELINE-NEU.md`, `pruefung/runde-schema-v2.json`). **Jede Datei bearbeitet nur ihr Ersteller – keiner verändert fremde Dateien.** Dateinamen ohne Versionsnummer. „Cloud“ = Claude.
1. **Julian** nennt das Paket (z. B. „003 los“).
2. **Claude** recherchiert die Quellen selbst und liest sie am Original (Hersteller, Behörden, Register, Leitlinien – mit Seite), legt `pakete/NNN-basis` (+ „Zur Prüfung in diesem Lauf“) und ggf. `implantate/*` an → `runde: grok`. *(Perplexity entfällt seit 07.10.2026.)*
3. **Grok** prüft die ganze Paketversion gründlich → `pruefung/NNN-grok.md`.
4. **Nur bei Implantaten: OpenAI** prüft ausschließlich Implantate (Herstellerangaben, Kompatibilitätstabellen, Indikationsgrenzen – keine Instrumente) → `pruefung/NNN-openai.md` → zurück an Claude.
5. **Claude** macht den letzten Check, denkt kritisch mit und schickt Julian die Änderungsliste (✅/❌/✏️/❓ als Multiple Choice, 🔎 Perplexity-Prompt) → `runde: julian`.
6. **Julian** gibt das Okay → Claude baut die Daten ein (`pakete/NNN-abschluss.md` bzw. `implantate/*`) → `runde: astra-bau`.
7. **Astra implementiert** in Kerlect (nur dort) → `runde: abgeschlossen`.
8. **Grok, OpenAI und Astra** löschen danach nur ihre eigenen Prüfdateien.

`runde`-Kette: `wartet → cloud → grok → (openai nur Implantate) → cloud-final → julian → astra-bau → abgeschlossen`. Ereignisgesteuert über GitHub-Action (`pruefung/github-action-pruef-pipeline.yml`, einmalig nach `.github/workflows/` kopieren).

## Gegenprüfung

Siehe [PRUEFAUFTRAG.md](PRUEFAUFTRAG.md). Status: [pruefung/STATUS.json](pruefung/STATUS.json).

## Regeln (Kurz)

- **Prompts für Astra:** immer mit empfohlenem **Aufwand** (niedrig / mittel / hoch / sehr hoch) und kurzem Grund.
- **Rückfragen an Julian:** immer mit möglichst vielen Beispiel-Systemen/Produkten je Hersteller zur Auswahl (Schäfte, Pfannen, Inlays, Köpfe, Duoköpfe), damit er sie beim Lesen wiedererkennt.
- **Systeme nicht mischen:** Jede Implantat-Komponente nur mit dem, was der Hersteller im Dokument ausdrücklich dafür vorsieht – keine eigenen Kombinationen.
- **Zuordnung:** 000 = allgemeines OP-Wissen für jeden Eingriff. Eingriffspakete (001 …) enthalten nur Eingriffsspezifisches. Allgemeines wandert nach 000 und wird im Eingriffspaket gestrichen.

- Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.
- Nichts erfinden; Hausvorgaben, IFU und ärztliche Anordnung gehen immer vor.
- Quellen: AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-IFU/OP-Technik, öffentliche Klinik-SOPs — keine Foren/Shops.
- Keine Patientendaten.

## Lizenz / Nutzung

Entwürfe für Kerlect (Kerlwerk). Veröffentlichung zur Gegenprüfung durch KI/Fachpersonen; keine klinische Freigabe.
