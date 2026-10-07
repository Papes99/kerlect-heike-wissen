# 001 Hüfte – Prüfpaket für Grok (Gegenprüfung + Änderungsvorschläge)

_Stand 07.10.2026 · erstellt von Claude für Julian · alles zu Paket 001 Hüft-TEP in einer Datei_

## Auftrag an Grok
Du bist Gegenprüfer für **Paket 001 Hüft-TEP (primär), Version 1.0**. Es baut auf **Paket 000 Grundwissen v1.1** auf (unten mit abgedruckt). Zielgruppe: OP-Springer:innen bei der Vorbereitung.

Bitte:
1. **Belegte Zeilen prüfen** (📖): Die Aussage in der angegebenen Quelle nachlesen und als *bestätigt*, *zu weit gefasst* oder *nicht gefunden* einordnen.
2. **Fehler** finden: falsche, veraltete oder gefährliche Aussagen, jeweils mit Begründung und Quelle.
3. **Lücken** für die Springer-Vorbereitung finden: Geräte, Lagerung, Abdeckung, Siebe, Material mit Menge, Naht mit Stärke, Nadel und Schicht, Ablauf, Zählung.
4. **Implantate** (Abschnitt C): Für die Haus-Systeme nur Daten mit Herstellerdokument, Version/Stand, Seite und URL nennen. REF und Kompatibilität nur exakt wie gedruckt. Ohne Dokument: „offen“.
5. Daraus eine **Liste mit Änderungsvorschlägen** erstellen (Format unten).

**Regeln:** Nur seriöse Quellen (AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-OP-Techniken/IFU, öffentliche Klinik-SOPs, AMBOSS). Keine Foren, keine Shops. Nichts erfinden, ohne Quelle `quelle: null`. Dosierungen, Zement-Mischzeiten, HF-Werte und Implantatgrößen nur mit Quelle und Hinweis. Keine Patientendaten. Hausvorgaben, IFU und ärztliche Anordnung gehen immer vor.

## Gewünschtes Ausgabeformat
```
### PRÜFUNG 001-hueft-tep v1.0 – <Datum>

#### A. Prüfung der belegten Zeilen
| Abschnitt | Zeile | Quelle | Ergebnis (bestätigt / zu weit / nicht gefunden) | Bemerkung |

#### B. Änderungsvorschläge
| Nr | Abschnitt | Betroffener Eintrag (oder „neu“) | Art (Korrektur / Ergänzung / Streichung / Präzisierung) | Vorschlag (konkret, Schema-Felder) | Begründung | Quelle (Titel, Stand, Seite, URL) | Priorität (hoch = Sicherheit / mittel / niedrig) |

#### C. Implantate (Haus-Systeme)
| Hersteller | System | Angabe | Wert | Dokument / Stand / Seite / URL |
(nur exakt aus Herstellerdokumenten, sonst „offen“)

#### D. JSON
{"paket":"001-hueft-tep","version":"1.0","geprueft_am":"…","korrekturen":[…],"ergaenzungen":[…],"streichungen":[…],"quellen_neu":[…],"implantate":[…]}
```
Einträge in `korrekturen`/`ergaenzungen` haben die Felder des Paket-Schemas: `abschnitt`, `label` (≤ 40 Zeichen), `menge`, `einheit`, `spez`, `schicht`, `gilt_fuer`, `optional`, `sicherheit` (belegt/üblich/hausabhängig), `hausabhaengig`, `quelle`, `hinweis`.

**Ablage des Ergebnisses:** als `eingang/2026-10-07-001-hueft-tep-grok.md` (Julian legt die Datei ab). Claude macht daraus abends einen Vorschlag in `aenderungen/`. Paket 001 ändert sich erst nach Julians Freigabe.

## Maschinenlesbare Originale (für Details und Schema)
- Paket 001 JSON: https://raw.githubusercontent.com/Papes99/kerlect-heike-wissen/main/pakete/001-hueft-tep.json
- Paket 001 Text: https://github.com/Papes99/kerlect-heike-wissen/blob/main/pakete/001-hueft-tep.md
- Paket 000 JSON: https://raw.githubusercontent.com/Papes99/kerlect-heike-wissen/main/pakete/000-grundwissen.json
- Implantat-Schema: https://github.com/Papes99/kerlect-heike-wissen/blob/main/implantate/LIESMICH.md
- Prüfstatus: https://github.com/Papes99/kerlect-heike-wissen/blob/main/pruefung/STATUS.json

---

# A. Paket 001 – Hüft-TEP (primär), v1.0

_Version 1.0 · 06.10.2026 · baut auf Paket 000 auf · klinisches Review durch Julian offen_

Allgemeines (Time-out, Zählregeln, Markierung, Inzisionsfolie, Hautantiseptik, Heike-Regeln) steht in **Paket 000** und wird hier nicht wiederholt.

Legende: ⚠️ hausabhängig · *(optional)* · 📖 Quelle nachgelesen · _nur …_ = Variante/Situation · Mengen sind Vorschläge

**Fixation:** zementfrei · zementiert · Hybrid (= Schaft zementiert, Pfanne zementfrei)  
**Zugang:** DAA · anterolateral · lateral (Bauer) · posterolateral

## 1. Eckdaten `facts`
- **Primäre Hüft-TEP** 📖 AMBOSS
- **Fixation je Komponente klären** ⚠️
- **Zugang laut OP-Plan** ⚠️
- **OP-Dauer laut Hausplanung** *(optional)* ⚠️
- **Anästhesieverfahren laut Plan** ⚠️

## 2. Saal & Geräte `room`
- **OP-Tisch mit Hüftzubehör** ⚠️
- **DAA: Extensionstisch optional** — _nur daa_ *(optional)* ⚠️
- **HF-Gerät: Betriebsart prüfen** ⚠️
- 2 Systeme **Absaugsysteme** ⚠️
- **Pulslavage-Gerät** *(optional)* ⚠️
- **Antriebe und Ersatzakkus** ⚠️
- **Patientenwärmung** ⚠️
- **C-Bogen und Strahlenschutz** — _nur bildwandler_ *(optional)* ⚠️
- **Zementmischer: Anschlüsse prüfen** — _nur zementiert, hybrid_ ⚠️
- **Implantatvorrat bereitstellen** ⚠️
- **Implantat-Etikettenbogen bereit** ⚠️

## 3. Lagerung `position`
- **DAA: Rückenlage** — _nur daa_ 📖 AMBOSS
- **Anterolateral: Seite oder Rücken** — _nur anterolateral_ 📖 AMBOSS
- **Lateral: Rücken oder Schrägseite** — _nur lateral_ 📖 AMBOSS
- **Posterolateral: Seitenlage** — _nur posterolateral_ 📖 AMBOSS
- **Beckenstützen zugangsgerecht** ⚠️
- **DAA: kontralaterale Abstützung** — _nur daa_ *(optional)* ⚠️
- **Druckstellen und Arme schützen** ⚠️
- **Beinbeweglichkeit vorbereiten** ⚠️
- **NE-Kontakt kontrollieren** — _nur hf_mono_ 📖 HEBU
- **Mechanische Prophylaxe laut Plan** *(optional)* ⚠️

## 4. Desinfektion & Abdeckung `draping`
- **Hüft-/Extremitäten-Abdeckset** ⚠️
- **Beinschlauch oder Beinsack** ⚠️
- 1 Stück **Inzisionsfolie nur nach Hausplan** *(optional)* ⚠️
- **Flüssigkeitsdichte Abdeckung** 📖 KRINKO
- **Kabel und Schläuche sichern** ⚠️

## 5. Siebe & Zusatzinstrumente `trays`
- **Hüft-Grundsieb** ⚠️
- **Pfannenfräsen-Sieb** ⚠️
- **Schaft- und Probekomponenten-Sieb** ⚠️
- **Zugangsspezifische Zusatzinstrumente** *(optional)* ⚠️
- **DAA: LINK-Instrumentenbeispiel** — _nur daa_ *(optional)* 📖 LINK
- **Steriles Säge-/Antriebsset** ⚠️
- **Kopfzieher** ⚠️
- **Hüftkopf-Messhilfe optional** *(optional)* ⚠️
- **Zementierinstrumente** — _nur zementiert, hybrid_ ⚠️

## 6. Material `supplies`
- 1 Stück **Skalpellklinge Nr. 20** (Haut) ⚠️
- 1 Stück **Reserveklinge Nr. 10 oder 22** (eine Alternative wählen) *(optional)* ⚠️
- 20 Stück **Kompressen 10 × 10 cm** (röntgenkontrastgestreift) ⚠️
- 5 Stück **Bauchtücher** (röntgenkontrastgestreift) ⚠️
- 5 Stück **Stiel-/Präpariertupfer** (zählfähig) *(optional)* ⚠️
- 1 Stück **Oszillierendes Sägeblatt** (antriebskompatibel) ⚠️
- 1 Stück **Ersatz-Sägeblatt steril verpackt** (ungeöffnet bereithalten) *(optional)* ⚠️
- 2 Stück **Absaugschläuche** (passend zum Saugsystem) ⚠️
- 1 Stück **Yankauer-/chirurgischer Sauger** ⚠️
- 1 Stück **Monopolarer HF-Handgriff** — _nur hf_mono_ *(optional)* ⚠️
- 1 Stück **Neutralelektrode** (Anlage nach IFU) — _nur hf_mono_ *(optional)* ⚠️
- 1 Set **Bipolare Pinzette mit Kabel** — _nur hf_bi_ *(optional)* ⚠️
- 1 Set **Pulslavage-Set** (passend zum Gerät) *(optional)* ⚠️
- 3 Liter **NaCl 0,9 % als Spülvorrat** (Spülung, Erwärmung nach Hausverfahren) ⚠️
- 1 Stück **Blasenspritze 50 ml** *(optional)* ⚠️
- 1 Stück **Redon-Drainage optional** (Ch 10–12, nur wenn angeordnet) *(optional)* ⚠️
- 1 Stück **Passendes Drainage-Auffangsystem** (nur mit Drainage) *(optional)* ⚠️
- 2 Paare je sterile Person **Doppelhandschuhe pro sterile Person** (Größen je Person) ⚠️
- 1 Stück je sterile Person **Steriler OP-Kittel pro Person** ⚠️
- 2 Stück **Sterile Lichtgriffe** ⚠️
- **Knochenzement laut OP-Plan** (Produkt/Anzahl laut Plan) — _nur zementiert, hybrid_ ⚠️
- 1 Set **Zement-Mischset** (Vakuumsystem laut IFU) — _nur zementiert, hybrid_ ⚠️
- 1 Set **Zementspritze/Applikator** (passend zum System) — _nur zementiert, hybrid_ ⚠️
- 1 Stück **Markraumstopper** (Größe laut Operateur/Hersteller) — _nur zementiert, hybrid_ ⚠️
- 1 Stück **Hautklammergerät** (Alternative Hautverschluss) *(optional)* ⚠️
- 1 Stück **Hautkleber** (Alternative Hautverschluss) *(optional)* ⚠️
- **Hautantiseptik-/Waschset** (Hausprodukt) ⚠️
- 3 Stück **Sterile Schalen** ⚠️
- 1 Stück **Präparatgefäß Femurkopf** (nur bei Einsendung) — _nur praeparat_ *(optional)* ⚠️

## 7. Nahtmaterial `sutures`
- 2 Packungen **Refixation: Ethibond Nr. 2** (Nr. 2 · Nadel offen) – Muskel-/Kapselrefixation — _nur lateral, posterolateral_ *(optional)* ⚠️
- 2 Packungen **Refixation: FiberWire Nr. 2** (Nr. 2 · Nadel offen) – Muskel-/Kapselrefixation — _nur lateral, posterolateral_ *(optional)* ⚠️
- 2 Packungen **Faszie: Vicryl 1, CT-1** (1 · CT-1 (Artikel prüfen)) – Faszie ⚠️
- 1 Packung **Faszie: Widerhakennaht 1** (1 · Nadel offen) – Faszie *(optional)* ⚠️
- 2 Packungen **Subkutan: Vicryl 2-0** (2-0 · Nadel offen) – Subkutan ⚠️
- 1 Packung **Haut: Monocryl 3-0 oder 4-0** (3-0 oder 4-0 · Nadel offen) – Haut *(optional)* ⚠️
- 1 Packung **Halte-/Markierungsnaht** (Stärke/Nadel offen) – Kapsel/Muskelrefixation — _nur posterolateral_ *(optional)* ⚠️

## 8. Implantate `implants`
- **Acetabulum-Pfanne** ⚠️
- **Pfanneninlay bei modularem System** *(optional)* ⚠️
- **Femurschaft** ⚠️
- **Femurkopf** ⚠️
- **Pfannenschrauben nach Plan** — _nur zementfrei, hybrid_ *(optional)* ⚠️

## 9. Ablauf aus Springer-Sicht `workflow`
- **OP-Plan und Verfügbarkeit abgleichen** ⚠️
- **Anschlüsse vor Nutzung prüfen** ⚠️
- **Steriles Zubehör auf Ansage reichen** ⚠️
- **Zementvorbereitung abstimmen** — _nur zementiert, hybrid_ ⚠️
- **Anästhesie vor Zement informieren** — _nur zementiert, hybrid_ 📖 BCIS
- **Zementmischen nur auf Ansage** — _nur zementiert, hybrid_ ⚠️
- **Definitivimplantat bestätigt öffnen** ⚠️
- **Verschlussmaterial abstimmen** ⚠️
- **Implantatgrößen ansagen + wiederholen** ⚠️

## 10. Zählkontrolle & Dokumentation `count`
- **Probekomponenten zurückführen** ⚠️
- **Scharfe Teile und Teilebruch prüfen** ⚠️
- **Implantatstatus gesondert erfassen** ⚠️
- **Zementüberschuss gesondert prüfen** — _nur zementiert, hybrid_ ⚠️
- **Implantatetiketten dokumentieren** ⚠️
- **Zeit- und Bildgebungsdokumentation** — _nur zementiert, hybrid, bildwandler_ *(optional)* ⚠️

## 11. Verband & Ausleitung `dressing`
- **Steriler Wundverband** ⚠️
- **Drainageanschluss kontrollieren** *(optional)* ⚠️
- **Transfer und Bewegungsvorgaben** ⚠️
- **Präparat korrekt übergeben** — _nur praeparat_ *(optional)* ⚠️
- **Bildkontrolle nach Anordnung** *(optional)* ⚠️
- **Übergabe an AWR/Anästhesie** ⚠️

## 12. Besonderheiten & Fallstricke `pitfalls`
- **Keine unbestätigte Systemmischung** ⚠️
- **Fixation nicht aus Hybrid erraten** ⚠️
- **Konkrete Unverträglichkeiten klären** ⚠️
- **Alkoholansammlungen vermeiden** — _nur hf_mono_ 📖 HEBU
- **Größenvorrat vorab prüfen** ⚠️

## 13. Fotos `photos`
- **Foto: Lagerung ohne Patient** *(optional)* ⚠️
- **Foto: Abdeckaufbau am Modell** *(optional)* ⚠️
- **Foto: Instrumentiertisch** *(optional)* ⚠️
- **Foto: Prothesensiebe** *(optional)* ⚠️
- **Foto: Zementplatz** — _nur zementiert, hybrid_ *(optional)* ⚠️
- **Foto: Verband am Modell** *(optional)* ⚠️

## Heike darf sagen
- „Welcher Zugang und welche Fixation? Davon hängen Lagerung, Siebe und Zementmaterial ab.“ 📖 AMBOSS
- „Hybrid heißt hier: Schaft zementiert – Markraumstopper und Zementplatz trotzdem vorbereiten.“
- „Zementiert? Sag der Anästhesie vor dem Einbringen Bescheid.“ 📖 BCIS
- „Implantate erst auf Ansage öffnen – Komponente, Seite und Größe laut wiederholen.“
- „Probeköpfe und Probepfannen gehören in die Zählung, bevor die Faszie zu ist.“
- „Größenvorrat und Ersatzakkus vor dem Einschleusen prüfen.“

## Abschluss-Check
- Fixation je Komponente und Zugang
- Passende Siebe, Antriebe und Ersatzakkus
- Lavage-Zubehör nach Plan
- Zementierter Schaft auch bei Hybrid: Markraumstopper und Zementvorbereitung
- Strahlenschutz bei geplanter Bildgebung
- Nahtnadeln und Artikelnummern je Schicht
- Teambezogene Kittel-/Handschuhmengen
- Probekomponenten, Zähldifferenzen und Implantatdokumentation

## Quellen
- **AMBOSS** – Endoprothetik des Hüftgelenks. https://www.amboss.com/de/wissen/endoprothetik-des-huftgelenks
- **KRINKO** – Prävention postoperativer Wundinfektionen. https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf?isAllowed=y&sequence=1
- **LINK** – Direct Anterior Approach – Operationstechnik (herstellerspezifisch). https://www.link-ortho.com/fileadmin_atl/user_upload/Global_LINK_Website/Products/PDFs/DE/615_DAA_OP_de_2022-06_003_MAR-01209.pdf
- **BCIS** – Factsheet Implantationssyndrom / BCIS. https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf
- **HEBU** – Einmal-Neutralelektroden Gebrauchsanweisung GAHF113. https://www.hebumedical.de/ga/GAHF113.pdf

## Offen
- Status: redaktionell geprüftes Zusammenführungspaket, klinischer Entwurf; keine Freigabe durch Julian erfolgt.
- Keine Quelle belegt die konkreten Vorratsmengen oder die Nahtartikel dieser Lieferungen als allgemeinen Hüft-TEP-Standard.
- Alle nicht genannten Nadeln/Artikelnummern bleiben offen; keine Ergänzung aus Vermutung.
- Tatsächlich verwendete Zement-, Implantat-, Antriebs- und Tisch-IFUs liegen nicht vor. Die geprüfte HEBU-Anleitung ersetzt keine fremde Produkt-IFU.
- Mengen der Ausgangslieferungen unterscheiden sich; Entscheidungen und Ausschlüsse stehen in BEWERTUNG.md.
- Keine Bilder enthalten; Fotos benötigen separate Hausfreigabe und einen Aufbau ohne Patientendaten.
- Das C-Schema ist ein Wissensformat, kein nachgewiesener Direktimport für Heike. Es wurde kein App-Import durchgeführt.

## Julian bitte prüfen
- [ ] Eingriffsscope primäre Hüft-TEP bestätigen; keine Revision/Hemiendoprothese.
- [ ] Fixation von Pfanne und Schaft sowie Zugang bestätigen; Hybridbegriff und Reverse-Hybrid-Abgrenzung prüfen.
- [ ] Lagerung, Stützen, Tisch/Beinhalter und Bewegungsraum je Hauszugang freigeben.
- [ ] Hausgeräte/IFUs für HF, NE, Antriebe und Zement-/Mischsystem bestimmen.
- [ ] Siebnamen, vollständige Systemkompatibilität, AEMP-Prüfung und tatsächliche Bestandsverfügbarkeit bestätigen.
- [ ] Alle Vorratsmengen prüfen: insbesondere Klingen, 20 Kompressen, 5 Bauchtücher, 5 Tupfer und 3 Liter Spülvorrat.
- [ ] Handschuhe/Kittel nach tatsächlicher steriler Teamgröße und Wechselreserve berechnen.
- [ ] Naht je Schicht freigeben: Marke/Material, Stärke, Nadel, Länge und Anzahl. CT-1-Beispiel am konkreten Artikel prüfen; übrige Nadeln offen.
- [ ] Alternativen bei Refixation, Fasziennaht und Hautverschluss festlegen; optionale Artikel bleiben unselektiert.
- [ ] Knochenzement: Produkt, Packungsgröße/-anzahl und tatsächlich aktuelle Herstellerunterlagen; keine Dosier-/Mischangaben ergänzen.
- [ ] Redon ja/nein, Drainagegröße und passendes System; Bildgebung, Pathologie und Verband nach Hausplan.
- [ ] Zählumfang/-zeitpunkte inklusive Teamwechsel, Trial-Teilen, Teilebruch, Zähldifferenz und implantiertem Markraumstopper mit Haus-SOP abgleichen.
- [ ] Hygieneplan, Antiseptikum, Folienentscheidung und Flüssigkeitsmanagement prüfen.
- [ ] Transfer, Bewegungsvorgaben und Übergabeinhalte hausbezogen bestätigen.
- [ ] Vor späterem App-Einsatz Datenadapter prüfen: Mengen, Stärke, Nadel, Schicht, Variante, Herkunft und Auswahl müssen erhalten bleiben; nur explizit gewählte Inhalte speichern.

---

# B. Basis: Paket 000 – Grundwissen, v1.1

_Version 1.1 · 07.10.2026 · Entwurf Claude · Gegenprüfung und klinisches Review offen_

Paket 000 ist das gemeinsame Fundament: Es gilt bei **jedem** Eingriff. Die Eingriffspakete (001 Hüft-TEP …) ergänzen es.

Legende: ⚠️ hausabhängig · *(optional)* · 📖 Quelle nachgelesen · _nur …_ = gilt nur in dieser Situation

## Regeln für Heike
1. Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.
2. Nichts als Hausstandard ausgeben; Vorschläge sind Vorschläge, gespeichert wird nur Angetipptes/Getipptes.
3. Springer-Sicht: bereitstellen, anreichen, ansagen, dokumentieren – keine OP-Technik.
4. Patientendaten nie verarbeiten oder speichern; Fotos ohne Personen/Identifikatoren.
5. Sicherheitsregeln (Time-out, Zählung, Implantat auf Ansage) nie wegen Tempo weglassen.
6. Bei Zähldifferenz, unklarer Seite oder unklarem Implantat: STOPP empfehlen, nie selbst entscheiden.
7. Heike ist eine KI und behauptet keine eigene Berufserfahrung.

## Wie 000 mit Eingriffspaketen zusammenspielt
- Paket 000 gilt für jeden Eingriff; Eingriffspakete (001 ff.) ergänzen und präzisieren.
- Gleiche Bedeutung in 000 und Eingriffspaket: Eingriffspaket gewinnt, 000-Eintrag ausblenden.
- Situations-IDs (hf_mono, implantat, zement …) werden aus Eingriffspaket/Variante/Nutzerantwort abgeleitet; nur passende 000-Chips zeigen.
- 000-Sicherheitspunkte (count, facts) erscheinen in jedem Standard als Vorschlag im passenden Abschnitt und im Abschluss-Check.

## Situationen
- `alle` – alle Eingriffe
- `hf_mono` – monopolare HF-Chirurgie
- `hf_bi` – bipolare HF-Chirurgie
- `implantat` – Implantat geplant
- `zement` – Knochenzement geplant
- `bildwandler` – Bildwandler/Röntgen geplant
- `praeparat` – Präparat/Histologie angeordnet
- `blutsperre` – Blutsperre/-leere geplant
- `seitenlage` – Seitenlage
- `steinschnitt` – Steinschnittlage
- `bauchlage` – Bauchlage
- `laparoskopie` – Laparoskopie
- `notfall` – Notfalleingriff

## Eckdaten & Sicherheit `facts`
- Patientenidentität geprüft (Armband + Rückfrage) 📖 WHO
- Eingriffsort markiert und sichtbar (Markierung nach Lagerung/Abdeckung prüfbar) 📖 KVWL
- Sign-in (vor Narkoseeinleitung) 📖 WHO
- Team-Time-out (vor dem Schnitt, hörbar, ganzes Team) 📖 WHO
- Sign-out (vor Verlassen des Saals, inkl. Zählergebnis) 📖 WHO
- Allergien/Unverträglichkeiten erfragt (produktbezogen (z. B. Desinfektion, Latex, Pflaster)) ⚠️
- Implantat laut Planung bestätigt — _nur Implantat geplant_ ⚠️

## Saal & Geräte `room`
- OP-Tisch + Zubehör für Lagerung ⚠️
- HF-Gerät funktionsgeprüft (Leistung nach Herstellerempfehlung/Operateur) ⚠️
- 1× Neutralelektrode (nur bei monopolar) — _nur monopolare HF-Chirurgie_ ⚠️
- 1× Bipolare Pinzette + Kabel — _nur bipolare HF-Chirurgie_ *(optional)* ⚠️
- 1× Sauger funktionsgeprüft ⚠️
- Wärmesystem (z. B. Warmluftdecke) ⚠️
- OP-Licht ausgerichtet + Lichtgriffe
- Bildwandler + Röntgenschürzen — _nur Bildwandler/Röntgen geplant_ ⚠️
- Dosimeter/Strahlenschutz laut Haus — _nur Bildwandler/Röntgen geplant_ ⚠️
- Blutsperren-Gerät + Manschette — _nur Blutsperre/-leere geplant_ ⚠️
- Laparoskopie-Turm + CO₂ geprüft — _nur Laparoskopie_ ⚠️
- Notfallausstattung erreichbar (laut Haus) ⚠️

## Lagerung `position`
- Druckstellen gepolstert (Fersen, Sakrum, Ellenbogen, Knochenvorsprünge) ⚠️
- Arme gesichert, nicht überstreckt (Nervenschutz Plexus/Ulnaris) ⚠️
- Neutralelektrode-Ort (gut durchblutete Muskulatur, nicht über Knochen/Narbe/Metall, vollflächig) — _nur monopolare HF-Chirurgie_ ⚠️
- Kein Hautkontakt zu Metallteilen — _nur monopolare HF-Chirurgie_ ⚠️
- Seitenstützen/Polster stabil — _nur Seitenlage_ ⚠️
- Hüftbeugung >90° lange vermeiden (Steinschnitt, vaginale Eingriffe) — _nur Steinschnittlage_ 📖 LAG
- Gesicht/Augen/Brust geschützt — _nur Bauchlage_ ⚠️
- Lagerung dokumentiert ⚠️

## Desinfektion & Abdeckung `draping`
- Sterile Tische erst kurz vor Beginn (bis Schnitt steril abgedeckt) 📖 KRINKO
- Hautdesinfektion laut Haus (Produkt + Einwirkzeit nach IFU) ⚠️
- Abdeckung flüssigkeitsdicht (passend zum Eingriff) ⚠️
- Keine nicht imprägnierte Inzisionsfolie *(optional)* 📖 KRINKO
- Türbewegungen/Saalverkehr gering 📖 KRINKO

## Zählkontrolle & Dokumentation `count`
- Zählen vor Beginn (alle eingesetzten Materialien) 📖 APS
- Ergänztes Material sofort zählen (Vier-Augen-Prinzip) 📖 APS
- Zählen bei Teamwechsel 📖 APS
- Zählen vor Wund-/Höhlenverschluss (Zeitpunkte laut Haus-Zählplan) ⚠️ 📖 APS
- Abschlusszählung + Entsorgungskontrolle 📖 APS
- Kompressen, Tupfer, Bauchtücher (röntgenkontrastgestreift) 📖 APS
- Nadeln, Klingen, Clips, Drahtteile 📖 APS
- Instrumente + Zusatzinstrumente 📖 APS
- Beabsichtigt belassenes Material doku (z. B. Tamponade, Drainage, Implantat) 📖 APS
- Differenz: STOPP + sofort melden (weiteres Vorgehen laut Operateur/Haus) ⚠️ 📖 APS
- Zählprotokoll dokumentiert 📖 APS

## Implantate, Zement & Medikamente `implants`
- Implantat erst auf Ansage öffnen (Typ, Seite, Größe laut wiederholen) — _nur Implantat geplant_ ⚠️
- Verpackung/Verfall prüfen — _nur Implantat geplant_
- Implantat-Etiketten in Doku — _nur Implantat geplant_ ⚠️
- Implantatpass laut Haus — _nur Implantat geplant_ ⚠️
- Anästhesie vor Zement informieren — _nur Knochenzement geplant_ 📖 AMBOSS
- Zement nach Hersteller-IFU (Mischzeit je Produkt laut IFU, temperaturabhängig) — _nur Knochenzement geplant_ ⚠️
- Medikamente am Tisch nur laut Anordnung (Dosis nur mit Quelle + „laut Anordnung prüfen“) ⚠️

## Ablauf aus Springer-Sicht `workflow`
- Saal vorbereiten vor Einschleusen ⚠️
- Material nach Bedarf anreichen + ansagen (steril übergeben, mitzählen) 📖 APS
- Instrumente/Material auf Ansage öffnen ⚠️
- Blutsperrenzeit ansagen + dokumentieren — _nur Blutsperre/-leere geplant_ ⚠️
- Präparat sofort beschriften (Patient, Lokalisation, Begleitschein) — _nur Präparat/Histologie angeordnet_ ⚠️
- Fixierung laut Pathologie-Vorgabe — _nur Präparat/Histologie angeordnet_ ⚠️
- Notfall: Zählung nach Haus-Regel (Aussetzen/Nachzählen festgelegt) — _nur Notfalleingriff_ ⚠️ 📖 APS

## Verband & Ausleitung `dressing`
- Steriler Wundverband laut Haus ⚠️
- Drainagen fixiert + beschriftet *(optional)* ⚠️
- Neutralelektrode ab, Haut kontrolliert — _nur monopolare HF-Chirurgie_ ⚠️
- Lagerungsstellen kontrolliert (Hautbefund dokumentieren) ⚠️
- Übergabe Aufwachraum (Eingriff, Drainagen, Besonderheiten, Anordnungen) ⚠️

## Typische Fehler `pitfalls`
- Markierung unter Abdeckung verschwunden 📖 KVWL
- Zählung bei Teamwechsel vergessen 📖 APS
- Implantat auf Verdacht geöffnet — _nur Implantat geplant_
- Präparat unbeschriftet — _nur Präparat/Histologie angeordnet_
- Tische zu früh offen 📖 KRINKO
- Neutralelektrode über Metall/Narbe — _nur monopolare HF-Chirurgie_
- Zement ohne Anästhesie-Ansage — _nur Knochenzement geplant_ 📖 AMBOSS

## Fotos `photos`
- Foto Tischaufbau ohne Patient (keine Personen, keine Identifikatoren) *(optional)*

## Heike darf sagen
- „Ist die Markierung nach dem Abdecken noch zu sehen?“ 📖 KVWL
- „Ergänztes Material gleich mitzählen – vier Augen.“ 📖 APS
- „Teamwechsel? Dann wird gezählt, bevor übergeben wird.“ 📖 APS
- „Sterile Tische erst kurz vor Beginn öffnen und bis zum Schnitt abdecken.“ 📖 KRINKO
- „Zement geplant? Sag der Anästhesie vor dem Einbringen Bescheid.“ 📖 AMBOSS
- „Implantat erst auf Ansage öffnen – Typ, Seite und Größe laut wiederholen.“

## Abschluss-Check (typische Lücken)
- Zählung bei Teamwechsel
- Markierung nach Abdeckung prüfen
- Präparat-Begleitschein
- Implantat-Etiketten
- Neutralelektrode nach OP: Haut kontrollieren
- Lagerungsstellen nach OP kontrollieren

## Quellen
- **WHO** – Implementation Manual WHO Surgical Safety Checklist 2009, World Health Organization. https://www.who.int/docs/default-source/patient-safety/9789241598590-eng.pdf (abgerufen 2026-10-06)
- **APS** – Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“, Aktionsbündnis Patientensicherheit e. V.. https://www.aps-ev.de/wp-content/uploads/2024/06/flyer-JTZ.pdf (abgerufen 2026-10-06)
- **KRINKO** – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473, KRINKO am RKI. https://www.rki.de/DE/Themen/Infektionskrankheiten/Krankenhaushygiene/KRINKO/Empfehlungen-der-KRINKO/Device-assoziierte-postoperative-Infektionen/Downloads/Empf_postopWI.pdf?__blob=publicationFile&v=1 (abgerufen 2026-10-06)
- **KVWL** – Handlungsempfehlung Vermeidung einer Eingriffsverwechslung, 2. Auflage 2024, APS / KVWL. https://www.kvwl.de/fileadmin/user_upload/pdf/Mitglieder/Qualitaetssicherung/Patientensicherheit/Vermeidung_einer_Eingriffsverwechslung.pdf (abgerufen 2026-10-06)
- **LAG** – S2k-Leitlinie Verhinderung lagerungsbedingter Schäden in der operativen Gynäkologie (AWMF 015-077), AWMF / DGGG. https://register.awmf.org/assets/guidelines/015-077l_S2k_Verhinderung_Lagerungssch%C3%A4den_Operationen_Gyn%C3%A4kologie_2021-01.pdf (abgerufen 2026-10-06)
- **AMBOSS** – Endoprothetik des Hüftgelenks (Zementhinweis), AMBOSS GmbH. https://www.amboss.com/de/wissen/endoprothetik-des-huftgelenks (abgerufen 2026-10-06)

## Offen / nicht belegt
- Neutralelektrode: Ort/Anlage laut Hersteller-IFU des Hauses – keine Normquelle ausgewertet.
- Wärmemanagement: AWMF-S3 „Vermeidung perioperativer Hypothermie“ (001-018) nicht nachgelesen – deshalb ohne Quelle.
- Strahlenschutz: Strahlenschutzanweisung des Hauses maßgeblich; keine Rechtsquelle ausgewertet.
- Implantatpass/Dokumentationspflichten: rechtliche Grundlage (MPDG/MPBetreibV) nicht ausgewertet.
- Pathologie: keine deutsche Leitlinie gefunden; Haus-SOP verbindlich.
- Lagerungs-Leitlinie nur gynäkologisch (AWMF 015-077) – übertragbare Prinzipien, keine Orthopädie-Quelle.

## Julian bitte prüfen
- [ ] Allergie-Abfrage-Formulierung
- [ ] Zählzeitpunkte laut eurem Zählplan
- [ ] Neutralelektrode-Regeln
- [ ] Was ihr bei Teamwechsel konkret macht
- [ ] Übergabe-Inhalte Aufwachraum

---

# C. Implantate – Haus-Systeme und Stand der Herstellerdaten
## Systeme im Haus (Julian, 07.10.2026)
| Hersteller | Im Haus | Noch zu klären |
|---|---|---|
| **Stryker** | **nur zementfreie Hüfte**: Accolade-Schaft (Konus **V40**), zementfreie Pfanne, Duokopf (bipolar) | Accolade II oder Accolade TMZF (beide V40)? Name der Pfanne (z. B. Trident/Trident II)? Name des Duokopfs? |
| **Mathys** | **alles**: twinSys zementfrei + zementiert, Pfanne zementfrei + zementiert, Duokopf | Namen der Pfannen und des Duokopfs |
| **Smith & Nephew** | **alles**: Schaft zementfrei + zementiert, Pfanne zementfrei + zementiert, Duokopf | Systemnamen (Schaft, Pfannen, Duokopf) |

### Stand der Extraktion (07.10.2026)
Die Herstellerdokumente konnten noch nicht gelesen werden, weil der Netzwerkzugriff auf mathysmedical.com, stryker.com und smith-nephew.com gesperrt war. Bisher gibt es deshalb **keine geprüften REF-, Größen- oder Kompatibilitätsdaten**. Details stehen in `eingang/2026-10-07-implantate-UEBERSICHT.md`.

Bekannte Startdokumente (Mathys):
- OP-Technik twinSys, DE, V05: https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_twinSys_DE_V05.pdf
- Kompatibilitäts-Chart Hüftköpfe Mathys, DE, V01: https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Kompatibilitaets-Chart/Kompatibilit%C3%A4ts-Chart_OPT_Hipheads_Mathys_DE_V01.pdf

Fragen an Grok zu den Implantaten:
- Welche Herstellerdokumente (OP-Technik, Kompatibilitätstabelle, Katalog) gibt es öffentlich für jedes Haus-System? Bitte mit Titel, Version/Stand und URL.
- Welche Kopf-Ø und Halslängen sind laut Dokument pro Schaft/Konus zulässig? Welcher Inlay-Innen-Ø gehört zu welcher Pfannengröße? Welche Duokopf-Kombinationen sind zulässig? Jede Angabe bitte mit Seite.
- Herstellerübergreifende Kombinationen nur, wenn ein Dokument sie ausdrücklich erlaubt.
