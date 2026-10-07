# Umsetzung: Hüft-TEP – Implantat-Auswahl in der OP

_Anweisung für Astra (Umsetzung in Kerlect) · Claude, 07.10.2026_

**Astra programmiert, nur in Kerlect. Start freigegeben (Julian, 07.10.2026)** mit dem aktuellen Datenstand. Die Läufe 001-implantate und 001-implantate-dach liefern danach weitere Größen/REF/Regeln und Systeme – das Tablett muss sie ohne Codeänderung übernehmen (Daten aus dem Repo laden).

**Maßgeblich ist der klickbare Prototyp** `app/prototyp/hueft-implantat.html` (Live: https://claude.ai/artifact/TJH8LZJzkYndH88XUUjzpA) mit Screens `app/screens/prototyp-1.png` … `-9.png` und Video `app/screens/prototyp-ablauf.webm`. Die älteren Mockups `hueft-implantat-1…7.png` zeigen nur den Inhalt.

**Ziel:** Unerfahrene OP-Pflegekräfte sehen auf einen Blick, **was bei uns möglich ist**, und klicken sich während der OP **in der echten Reihenfolge** durch die Implantate. Bei jedem Schritt zeigt Heike **nur die passenden Teile desselben Systems** – mit Größe, Offset, REF und Bild. Heike entscheidet nichts: **Der Operateur sagt an, die Pflegekraft gleicht ab.**

## Ziel-App und Einbauort (Julian, 07.10.2026)
**Base44-App „Kerlect“, App-ID `6aa3f64b0b23cc244ce7686d`.** Kopien („Kerlect Copy“, „Kerlect (Copy)“) und „Kerlect Kliniken“ nicht anfassen. Vor Änderungen Checkpoint.

**Keine eigene Seite im Menü – das Implantat-Tablett erscheint in Kerlect bei den OP-Standards mit Implantaten:**
1. **Standard-Ansicht** `src/pages/OPKatalogClean.jsx` (`?module=…`): Erkennt die App den Eingriff über `app/implantat-eingriffe.json` → `erkennung` (Titel/Eckdaten, z. B. „Hüft-TEP“), zeigt sie
   - in der Aktionsleiste neben „OP-Modus“ und „Vorbereiten“ einen dritten Knopf **„Implantate“**,
   - im Abschnitt **„Implantate & Medikamente am Tisch“** (`CleanStandardView.jsx`, Abschnitt-ID `implants`) oben eine Karte „Implantate in OP-Reihenfolge wählen“.
   Beides öffnet das Tablett als Vollbild-Ebene, genauso wie `OPMode`/`PreparationList` (lazy geladen, `onClose`).
2. **OP-Modus** `src/components/onboarding/OPMode.jsx`: Beim Abschnitt Implantate bzw. als eigener Schritt „Implantate“ direkt erreichbar – dort wird es in der OP benutzt.
3. **System-Vorschlag:** Nennt der Abschnitt `implants` des Standards schon einen Hersteller/ein System (z. B. „Accolade“, „Excia“, „R3“, „twinSys“), steht dieses System beim Öffnen oben als Vorschlag – die Pflegekraft bestätigt es. Sonst wählt sie aus `haus_systeme`.
4. **Andere Standards ohne Implantat-Paket:** kein Knopf, keine Karte.
5. Generisch bauen (eine Komponente `ImplantTray`), gesteuert über `implantat-eingriffe.json` (Schritte je Variante) – Knie-TEP usw. kommen später nur als Daten dazu.

**Animation und Haptik mit dem, was Kerlect schon hat:** `src/lib/motion.js` (`springs.snappy/smooth/bouncy`, framer-motion) und `src/lib/feel.js` (`haptic`/`feedback`: `tap`, `toggle`, `success`, `complete`, `error`; respektiert die Vibrations-/Ton-Einstellung im Profil). Zuordnung: Teil rastet ein → `bouncy` + `success`; Rad-Tick → `toggle`; Schalter → `snappy`; Seiten → `smooth`; Halten fertig → `complete`; falsches Teil → Schütteln + `error`. `MotionConfig reducedMotion="user"` gilt bereits.

**Daten in Kerlect:** nicht im Code abtippen. Entweder per Backend-Funktion aus diesem Repo laden (`raw.githubusercontent.com/Papes99/kerlect-heike-wissen/main/…`) und mit Stand/Version zwischenspeichern (offline wie `offlineStandards.js`), oder als Base44-Entity importieren – mit Feld `stand` und Quelle. Keine Patientendaten speichern; die Auswahl im Tablett bleibt lokal bzw. am Standard-Lauf, nicht am Patienten.

## Datenquelle
- `implantate/*.json` (Schema: `implantate/LIESMICH.md`), Hausauswahl in `pruefung/STATUS.json` → `haus_systeme` **und (Julian, Antwort auf A2) der JSON-Block aus `pakete/001-abschluss.md`** für Heike-Sätze, Zement-Schritt und Hüft-Varianten. Nichts im App-Code fest eintragen.
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

## Antworten auf `pruefung/app-astra.md`
- **A1** → Ziel-App siehe oben. **A2** → Paket 001 ist zugelassene Datenquelle.
- **A3–A5** (stabile Komponenten-IDs, maschinenlesbare Regeln, Rückruf↔Komponente, Hauszuordnung) baut Claude im Lauf 001-implantate in die Implantat-Dateien ein; bis dahin Freitext-Regeln nur anzeigen.
- **A6** umgesetzt im Prototyp: Nichts vorbelegt: Pfanne, Schaft, Kopf-Ø und Offset sind leer, bis die Pflegekraft am Rad dreht bzw. antippt; „Übernehmen“ bis dahin gesperrt.
- Für Stryker gibt es nur „gehört zum System“, kein pauschales „passt“; fehlende Paarungsangaben bleiben „offen – Operateur fragen“.

## Bedienung und Animation (physikalisch, „satisfying“)
Alle Bewegungen laufen über **Federn** (Masse-Feder-Dämpfer, x'' = −k·(x−Ziel) − c·v), nicht über feste Zeitkurven. Werte aus dem Prototyp:

| Element | Verhalten | k / c |
|---|---|---|
| **Hüft-Bühne oben** | Jedes gewählte Teil fliegt an seinen Platz und rastet mit leichtem Überschwingen ein: Pfanne von links oben mit Drehung, Inlay fällt hinein, Schaft kommt von unten, Kopf fällt auf den Konus. Beim Einrasten: Ring-Welle + kurze Vibration. Die Hüfte baut sich so mit der OP mit auf. | 150 / 11 |
| **Kopfgröße** | Bei 28/32/36 mm wächst/schrumpft der Kopf in der Bühne federnd. | 260 / 16 |
| **Schritte wischen** | Seiten seitlich wischbar mit Schwung; am Rand gummiartiger Widerstand; vorwärts nur, wenn der Schritt erledigt ist. | 210 / 26 |
| **Größen-Rad** | Wie ein Drehrad: ziehen, loslassen mit Trägheit, rastet auf die nächste Zahl ein; Tick-Vibration pro Zahl; Zahlen kippen 3D weg. | 240 / 24 |
| **Schalter** (CCD, Material, Ø) | Der helle Knopf gleitet federnd unter die gewählte Option. | 300 / 24 |
| **Antippen** | Alles Tippbare gibt beim Drücken nach (Skalierung 0,95) und federt beim Loslassen zurück. | 420 / 20 |
| **Haken** | Kasten „ploppt“ (0,6 → 1 mit Überschwingen), Häkchen zeichnet sich. | 520 / 13 |
| **Steril anreichen** | **Gedrückt halten** (1,1 s), Balken füllt sich; früh loslassen → federt zurück. Verhindert versehentliches Bestätigen. | 200 / 22 |
| **Falsches Teil / gesperrter Schritt** | Karte bzw. Knopf schüttelt sich (gedämpfte Schwingung) + Doppel-Vibration. | 900 / 12 |

- Material-Optik als Wiedererkennung: **Titan** grau mit Poren-Struktur, **BIOLOX delta** rosa glänzend, **CoCr** spiegelnd silber, **PE** cremeweiß. Eigene Zeichnungen, keine Herstellerbilder.
- `prefers-reduced-motion`: alle Federn springen sofort ans Ziel, nichts fliegt.
- Vibration nur, wo das Gerät es kann; nie als einzige Rückmeldung.

## Gestaltung für unerfahrene Kolleg:innen
- Große Tippflächen (≥ 48 px), Größen als Chips, eine Entscheidung pro Screen.
- Fortschrittsleiste oben, „zurück“ jederzeit, nichts geht verloren.
- Farben nur mit Text (✓/–/?/⛔), gut lesbar unter OP-Licht; Hell-Modus Standard.
- Heike-Satz in jedem Schritt: was jetzt passiert und worauf achten (Texte aus 001 `heike_hinweise`).
- Fachbegriffe kurz erklärt per Tipp (z. B. „Offset = Halslänge des Kopfes“).

## Ergänzung Julian (07.10.2026): System im Standard, eigene Systeme
1. **Im Standard steht nie eine einzelne Implantatgröße** – die Größe ist bei jedem Patienten anders. Gespeichert wird nur das **System**: Hersteller, System, Fixation/Varianten, verfügbare Komponenten mit Größenbereichen, Konus, Probesets/Siebe, Quelle + Stand. Knopf im Abschnitt `implants`: **„System in Standard übernehmen“** (Auswahl aus `haus_systeme`/`implantate/*.json`). Das ist auch der System-Vorschlag beim Öffnen des Tabletts (Punkt 3 oben).
2. **Größenwahl = nur in der OP** (Tablett, Schritte 3–7): auf Ansage, lokal für den laufenden Lauf, **nie** im Standard gespeichert; nach Abschluss zurücksetzen.
3. **Eigene Systeme:** Nutzer können ein System selbst anlegen oder ergänzen (z. B. Lagerbestand, System, das Kerlect noch nicht kennt): Hersteller, System, Konus, Komponenten/Größen, REF, eigene Fotos (Rechte-Feld Pflicht). Immer sichtbar markiert **„eigene Angabe – nicht geprüft“**, privat oder für die eigene Gruppe teilbar (Rechte wie Standards, reader_ids nicht aufweichen). Geprüfte Kerlect-Daten bleiben schreibgeschützt; eigene Systeme werden nie mit geprüften gemischt (Filter-Logik gilt genauso: nur Teile derselben Quelle/Datei).
4. Vorlage für beides (erfundene Daten): https://claude.ai/artifact/35gHvTH2bBA4mWasYUEwNA

## Abnahme (was fertig heißt)
- [ ] Alle 7 Screens wie Mockups, Daten nur aus `implantate/*.json` + `haus_systeme`.
- [ ] Kein Teil eines anderen Herstellers/Systems wählbar (Test: Isodur-CoCr-Kopf bei Stryker → Screen 6).
- [ ] Fehlende Werte erscheinen als „noch nicht hinterlegt“, nie als erfundene Zahl/REF.
- [ ] „Steril anreichen“ erst nach vollständigem Ansage-Check.
- [ ] Rückruf-Hinweis erscheint bei LFIT/BIOLOX delta V40 (Stryker), R3 (S+N), Vitelene (Aesculap) – nur als Hinweis.
- [ ] Neue Werte aus Lauf 001-implantate erscheinen ohne Codeänderung, sobald die JSON-Dateien ergänzt sind.
- [ ] Standard speichert nur das System (keine Größe); Größen nur im Tablett, nicht persistent am Standard.
- [ ] Eigenes System anlegen/teilen funktioniert, Badge „eigene Angabe – nicht geprüft“, nie mit geprüften Daten gemischt.

_Hinweis: Diese Datei gehört Claude. Astra legt Rückfragen/Vorschläge in `pruefung/app-astra.md` ab._
