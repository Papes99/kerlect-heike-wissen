# Umsetzung: Hüft-TEP – Implantat-Auswahl in der OP

_Anweisung für Astra (Umsetzung in der Heike-App) · Claude, 07.10.2026 · Mockups: `app/screens/hueft-implantat-1.png` … `-7.png`_

**Ziel:** Unerfahrene OP-Pflegekräfte sehen auf einen Blick, **was bei uns möglich ist**, und klicken sich während der OP **in der echten Reihenfolge** durch die Implantate. Bei jedem Schritt zeigt Heike **nur die passenden Teile desselben Systems** – mit Größe, Offset, REF und Bild. Heike entscheidet nichts: **Der Operateur sagt an, die Pflegekraft gleicht ab.**

## Datenquelle
- Nur `implantate/*.json` (Schema: `implantate/LIESMICH.md`) und Hausauswahl in `pruefung/STATUS.json` → `haus_systeme`. Nichts im App-Code fest eintragen.
- Werte fehlen noch (`"werte": "… noch nicht übernommen"`, `ref: null`): **nicht raten**, sondern Zustand „noch nicht hinterlegt“ zeigen (Screen 3) und Eintippen vom Etikett erlauben.
- `verified: false` → kleines Badge „nicht verifiziert“ an jedem Teil; Quelle (Dokument + Seite) per Tipp sichtbar.
- **Bilder:** keine Herstellerbilder kopieren. `bild.typ = "keins"` → neutrale Strichzeichnung je Typ (Pfanne/Inlay/Kopf/Schaft/Duokopf, wie in den Mockups). Liegt später ein Link mit Rechten vor, Bild per Link laden.

## Ablauf (Screens)
| # | Screen | Inhalt | Wichtig |
|---|---|---|---|
| 1 | **Was ist bei uns möglich?** | Matrix Haus-Systeme × zementfrei / zementiert / Duokopf: ✓ im Haus · – gibt es nicht · ? Herstellerfreigabe offen. Hybrid nur mit Freigabe. | Stryker: Duokopf „–“ (Accolade II EU nicht für Hemi). Regel „Systeme nie mischen“ immer sichtbar. |
| 2 | **System-Übersicht** | Schemazeichnung Hüfte mit nummerierten Teilen in OP-Reihenfolge + Liste der Hausprodukte je Schritt. Button „OP starten“. | Reihenfolge aus Variante (siehe unten). |
| 3 | **Schritt Pfanne** | Fortschrittsleiste; nur Pfannen dieses Systems; Größen-Chips aus Datei, sonst „noch nicht hinterlegt“ + Eintippfeld. | Andere Hersteller ausgeblendet. Heike: „Erst Probe, definitiv nur auf Ansage“. |
| 4 | **Schritt Kopf** (gleich für Inlay/Schaft) | Gefiltert nach vorher gewählten Teilen (z. B. Konus V40). Je Kopf-Ø die Offsets als große Chips (Stryker BIOLOX delta: 28/32/36 mm laut ACCII-SP-1 S. 12). | Fehlt eine Kompatibilitätsangabe (z. B. max. Kopf-Ø je Schale): Hinweis „Operateur fragen“, **nie** selbst ausschließen oder freigeben. |
| 5 | **Ansage-Check vor dem Öffnen** | Haken: angesagt + wiederholt · Probe passte · Hersteller/System auf Etikett · Größe/Offset gelesen · Verfall/Verpackung · zweite Person. Rückruf-Hinweis, wenn das Teil in `rueckrufe` steht. | „Steril anreichen“ erst aktiv, wenn alle Haken gesetzt sind. Rückruf nur als Hinweis „Chargen – MPB/Bestand geprüft?“, keine Sperre. |
| 6 | **Falsches Teil gesucht/gescannt** | Rote Karte „Nicht in diesem System“ mit Hersteller des Teils und der laufenden OP; darunter passende Teile. | Kein „trotzdem verwenden“-Button. Text: „Teil zurücklegen, Operateur informieren.“ |
| 7 | **Übersicht am Ende** | Alle gewählten Teile mit Größe, REF-Feld, „Etikett geklebt“; To-do: Probekomponenten zurück, Etiketten Doku/Implantatpass, Zählkontrolle. | Fehlendes Etikett rot. Daten lokal auf dem Gerät, keine Patientendaten. |

## Reihenfolge je Variante (Schritte)
- **zementfrei / zementiert (TEP):** 1 Pfanne → 2 Inlay (entfällt bei zementierter PE-Pfanne) → 3 Schaft (Raspel → Probe → definitiv) → 4 Probekopf → Kopf.
- **zementiert:** zusätzlich vor Schaft/Pfanne der Zement-Schritt aus Paket 001 (Zementansage, Mischen nur auf Ansage).
- **Duokopf (Hemi):** 1 Schaft zementiert → 2 Probe → 3 Duokopf. Nur anbieten, wo `haus_systeme` einen Duokopf nennt; solange die Herstellerfreigabe offen ist: Badge „Freigabe offen – Etikett/EU-IFU prüfen“.
- Hybrid: nur, wenn eine Implantat-Datei die Kombination mit Quelle ausdrücklich enthält.

## Filter-Logik (Pflicht)
1. Die erste Auswahl legt **Hersteller + System** fest. Danach nur Komponenten aus **derselben Datei**.
2. Weiter filtern nur mit Angaben aus der Datei (`attribute`, `regeln`): z. B. `konus`, `fixation`, Inlay-Material (Plasmafit Poly → nur PE), EU-Hinweise (X3 Eccentric 0° nicht CE).
3. Gibt es für eine Kombination **keine** Angabe: zeigen mit Badge „offen – Operateur fragen“. Nie selbst ableiten.
4. Gesuchtes/gescanntes Teil aus anderer Datei → Screen 6.

## Gestaltung für unerfahrene Kolleg:innen
- Große Tippflächen (≥ 48 px), Größen als Chips, eine Entscheidung pro Screen.
- Fortschrittsleiste oben, „zurück“ jederzeit, nichts geht verloren.
- Farben nur mit Text (✓/–/?/⛔), gut lesbar unter OP-Licht; Hell-Modus Standard.
- Heike-Satz in jedem Schritt: was jetzt passiert und worauf achten (Texte aus 001 `heike_hinweise`).
- Fachbegriffe kurz erklärt per Tipp (z. B. „Offset = Halslänge des Kopfes“).

## Abnahme (was fertig heißt)
- [ ] Alle 7 Screens wie Mockups, Daten nur aus `implantate/*.json` + `haus_systeme`.
- [ ] Kein Teil eines anderen Herstellers/Systems wählbar (Test: Isodur-CoCr-Kopf bei Stryker → Screen 6).
- [ ] Fehlende Werte erscheinen als „noch nicht hinterlegt“, nie als erfundene Zahl/REF.
- [ ] „Steril anreichen“ erst nach vollständigem Ansage-Check.
- [ ] Rückruf-Hinweis erscheint bei LFIT/BIOLOX delta V40 (Stryker), R3 (S+N), Vitelene (Aesculap) – nur als Hinweis.
- [ ] Neue Werte aus Lauf 001-implantate erscheinen ohne Codeänderung, sobald die JSON-Dateien ergänzt sind.

_Hinweis: Diese Datei gehört Claude. Astra legt Rückfragen/Vorschläge in `pruefung/app-astra.md` ab._
