# Heike-Wissen 000 – Grundwissen für alle Eingriffe

_Version 1.3 · 07.10.2026 · nach Grok-Prüfung · Astra-Prüfung vor Integration offen · klinisches Review offen_

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
- Patientenidentität geprüft (Patient bestätigt Identität; Armband + aktive Rückfrage zusätzlich laut KVWL) 📖 WHO · KVWL
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
- Sterile Tische erst kurz vor Beginn (bis Schnitt steril abgedeckt; S. 462) 📖 KRINKO
- Hautdesinfektion laut Haus (Produkt + Einwirkzeit nach IFU) ⚠️
- Abdeckung flüssigkeitsdicht (flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist, Kat. IB; Produkt laut Haus) 📖 KRINKO
- Keine nicht imprägnierte Inzisionsfolie (nicht antiseptisch imprägnierte Folien nicht verwenden, Kat. IB) *(optional)* 📖 KRINKO
- Türbewegungen/Saalverkehr gering 📖 KRINKO

## Zählkontrolle & Dokumentation `count`
- Zählen vor Beginn (alle eingesetzten Materialien) 📖 APS
- Ergänztes Material sofort zählen (Vier-Augen-Prinzip) 📖 APS
- Zählen bei Teamwechsel 📖 APS
- Zählen vor Wund-/Höhlenverschluss (Zeitpunkte laut Haus-Zählplan) ⚠️ 📖 APS
- Abschlusszählung + Entsorgungskontrolle 📖 APS
- Kompressen, Tupfer, Bauchtücher (röntgenkontrastgestreift) 📖 APS
- Nadeln, Klingen, Clips, Drahtteile (Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan) 📖 APS
- Instrumente + Zusatzinstrumente 📖 APS
- Beabsichtigt belassenes Material doku (z. B. Tamponade, Drainage, Implantat) 📖 APS
- Differenz: STOPP + sofort melden (weiteres Vorgehen laut Operateur/Haus) ⚠️ 📖 APS
- Zählprotokoll dokumentiert 📖 APS

## Implantate, Zement & Medikamente `implants`
- Implantat erst auf Ansage öffnen (Typ, Seite, Größe laut wiederholen) — _nur Implantat geplant_ ⚠️
- Verpackung/Verfall prüfen — _nur Implantat geplant_
- Implantat-Etiketten in Doku — _nur Implantat geplant_ ⚠️
- Implantatpass laut Haus — _nur Implantat geplant_ ⚠️
- Anästhesie vor Zement informieren (über jeden Zementierschritt) — _nur Knochenzement geplant_ 📖 AMBOSS · BCIS
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
- Keine Antiseptikum-Pfützen (Patient nicht in angesammeltem Hautantiseptikum) 📖 KRINKO

## Fotos `photos`
- Foto Tischaufbau ohne Patient (keine Personen, keine Identifikatoren) *(optional)*

## Heike darf sagen
- „Ist die Markierung nach dem Abdecken noch zu sehen?“ 📖 KVWL
- „Ergänztes Material gleich mitzählen – vier Augen.“ 📖 APS
- „Teamwechsel? Dann wird gezählt, bevor übergeben wird.“ 📖 APS
- „Sterile Tische erst kurz vor Beginn öffnen und bis zum Schnitt abdecken.“ 📖 KRINKO
- „Zement geplant? Anästhesie über jeden Zementierschritt informieren.“ 📖 AMBOSS · BCIS
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
- **BCIS** – Factsheet Implantationssyndrom / BCIS, Heraeus Medical / PALACADEMY, PDF S. 1. https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf (abgerufen 2026-10-07)
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

## Änderungen v1.2 (07.10.2026)
Grundlage: Grok-Prüfung 2026-10-07-000-grundwissen-v1.1-grok.md (Git-Verlauf). Alte Version: Git-Verlauf. KRINKO-Seiten nach Astra (S. 461, Abschnitt 4.1).
- Patientenidentität: WHO = Patientenbestätigung, Armband + Rückfrage laut KVWL
- Anästhesie über jeden Zementierschritt informieren (Chip + Heike-Satz), neue Quelle BCIS
- Abdeckung: jetzt belegt (KRINKO Kat. IB), flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen
- Neu: Keine Antiseptikum-Pfützen (KRINKO Kat. II)
- Sterile Tische: Seite 462 (v1.3); Inzisionsfolie: Text klarer; Zählung: Klingen laut Haus-Zählplan
- Wärme, NE-Ort, Strahlenschutz bleiben offen (Grok Nr. 8–10)

## Änderungen v1.3 (07.10.2026)
Grundlage: KRINKO-Seitenklärung in 2026-10-07-001-hueft-tep-v1.1-grok.md (Git-Verlauf). Alte Version: Git-Verlauf.
- Sterile Tische: Fundstelle S. 461 → **S. 462** (PDF-S. 15)

## Zur Prüfung in dieser Runde (Runde 2, 07.10.2026)

Regel (Julian): **000 = allgemeines OP-Wissen, nichts doppelt.** Allgemeines aus 001 wird hier in 000 aufgenommen und danach (Runde 001) in 001 gestrichen.

### Teil 1 – aus Runde 1, von Grok und Astra bereits bestätigt (nicht erneut prüfen, wird mit eingebaut)
| Nr | Abschnitt · Eintrag | ALT → NEU |
|---|---|---|
| R1-1 | implants · Anästhesie vor Zement informieren | quelle q_amboss → **q_bcis** (Hinweis AMBOSS bleibt) |
| R1-2 | heike_hinweise · „Zement geplant? …“ | quelle q_amboss → **q_bcis** |
| R1-3 | quellen · q_krinko fundstelle | Abschnitt 4.1: S. 461 (PDF-S. 14): Antiseptikum-Ansammlung (II), flüssigkeitsundurchlässige Abdeckung (IB), nicht antiseptisch imprägnierte Inzisionsfolie (IB), Türen/Fluktuation (II). S. 462 (PDF-S. 15): sterile Tische (II). Erläuterung: S. 455 (PDF-S. 8) |
| R1-4 | draping · Sterile Tische erst kurz vor Beginn | hinweis „Erläuterung S. 454“ → **„S. 455 (PDF-S. 8)“** |

### Teil 2 – Claude-Vorschläge (bitte prüfen)
| Nr | Abschnitt · Eintrag | ALT → NEU | Grund |
|---|---|---|---|
| C-A | count · Nadeln, Klingen, Clips, Drahtteile | label → **„Nadeln, Clips, Drahtteile zählen“** (belegt q_aps); neu **„Klingen laut Haus-Zählplan“** (hausabhängig, quelle null) | APS nennt Klingen nicht ausdrücklich |
| C-B | quellen · q_krinko url | rki.de-Link → **https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf** | Grok und Astra haben dieses Dokument geprüft |

### Teil 3 – Neuaufnahme: allgemeines Wissen aus 001 (bitte prüfen: wirklich allgemein? Formulierung? Quelle?)
| Nr | Abschnitt | Neuer Eintrag (Paket-Schema) | Herkunft |
|---|---|---|---|
| N1 | pitfalls | `{"label": "NE vor Flüssigkeit schützen", "menge": null, "einheit": null, "spez": "Flüssigkeitskontakt und Eindringen unter die NE vermeiden.", "gilt_fuer": ["hf_mono"], "optional": false, "sicherheit": "belegt", "hausabhaengig": false, "quelle": "q_hebu", "hinweis": "HEBU GAHF113V004 als Produktbeispiel; maßgeblich ist die IFU der tatsächlich verwendeten NE."}` | 001 pitfalls (Astra-Prüfung 001 v1.1, K5b); neue Quelle q_hebu = 001 Q_HEBU |
| N2 | draping | `{"label": "Kabel und Schläuche sichern", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Sterilfeld, Bewegungsraum und ggf. Bildgebung freihalten; keine Zugbelastung."}` | 001 draping |
| N3 | workflow | `{"label": "Anschlüsse vor Nutzung prüfen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "HF, Absaugung und Antriebe nach Bedarf funktionsgerecht anschließen; Springer stellt bereit, keine Instrumentier- oder Operationstechnik."}` | 001 workflow |
| N4 | count | `{"label": "Scharfe Teile und Teilebruch prüfen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Nadeln, Klingen, Sägeblätter sowie ablösbare Geräte-/Applikatorteile erfassen. Ungeöffnete Reserve nicht mit ans Sterilfeld gegebenem Material verwechseln."}` | 001 count |
| N5 | count | `{"label": "Probekomponenten zurückführen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["implantat"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Alle eingesetzten Trial-Teile nach Hausprotokoll auf Vollständigkeit prüfen; von Definitivimplantaten trennen."}` | 001 count (gilt_fuer alle → implantat) |
| N6 | implants | `{"label": "Größenvorrat vorab prüfen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["implantat"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Fehlende Größe mitten in der OP vermeiden – Lager/Leihset vorher mit der Planung abgleichen."}` | 001 pitfalls (gilt_fuer alle → implantat) |
| N7 | implants | `{"label": "Zementansage rückbestätigen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["zement"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Vorab festlegen, wer die Schritte ansagt. Beispiel: „Zement wird jetzt eingebracht“ – Rückmeldung der Anästhesie abwarten; bei fehlender Antwort unmittelbar klären. Konkrete Ansagen/Zuständigkeit laut Haus-SOP."}` | 001 workflow (Astra P1); zementiert/hybrid → zement |
| N8 | implants | `{"label": "Zementmischen nur auf Ansage", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["zement"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Start und Dokumentation nach Hausablauf; ausschließlich aktuelle Produkt-/Mischsystem-IFU verwenden. Keine Mischzeit oder Zusatzrezeptur."}` | 001 workflow; zementiert/hybrid → zement |
| N9 | count | `{"label": "Zementüberschuss gesondert prüfen", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["zement"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Kein pauschales Stückzählen von Zementresten. Operative Kontrolle auf unerwünschten Überschuss; beabsichtigte Zementfixation bleibt davon getrennt."}` | 001 count; zementiert/hybrid → zement |
| N10 | room | `{"label": "Doppelhandschuhe pro sterile Person", "menge": 2, "einheit": "Paare je sterile Person", "spez": "Größen je Person", "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Zwei Paare pro Person für doppelte Handschuhe; Größen, Material und Wechselreserve gesondert planen."}` | 001 supplies |
| N11 | room | `{"label": "Steriler OP-Kittel pro Person", "menge": 1, "einheit": "Stück je sterile Person", "spez": null, "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Ein Kittel je steril tätiger Person; Material/Schutzleistung und Reserven nach Hausplan."}` | 001 supplies |
| N12 | room | `{"label": "Antriebe und Ersatzakkus", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": true, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Nur wenn Antriebe geplant: funktionsbereit, Ersatzakkus geladen. Steriles Antriebskonzept gemäß jeweiliger IFU."}` | 001 room (Säge/Fräse-Bezug entfernt, optional) |
| N13 | position | `{"label": "Mechanische Prophylaxe laut Plan", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": true, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Nur falls angeordnet; System und vorgesehene Extremität bestätigen. Keine Medikamentenempfehlung."}` | 001 position |
| N14 | facts | `{"label": "Anästhesieverfahren laut Plan", "menge": null, "einheit": null, "spez": null, "gilt_fuer": ["alle"], "optional": false, "sicherheit": "hausabhängig", "hausabhaengig": true, "quelle": null, "hinweis": "Verfahren und organisatorische Besonderheiten mit Anästhesie abstimmen; keine Empfehlung für eine Narkoseart."}` | 001 facts |

Neue Quelle für N1: `q_hebu` = HEBU medical, Einmal-Neutralelektroden Gebrauchsanweisung GAHF113, GAHF113V004 vom 20.02.2026, https://www.hebumedical.de/ga/GAHF113.pdf (Produktbeispiel).

### Teil 4 – Doppelungen, die in Runde 001 aus 001 gestrichen werden (nur zur Info, 000 hat schon ein Gegenstück)
NE-Kontakt kontrollieren · Flüssigkeitsdichte Abdeckung · Alkoholansammlungen vermeiden · Druckstellen und Arme schützen · Anästhesie vor Zement informieren · Implantatetiketten dokumentieren · Steriler Wundverband · Übergabe an AWR/Anästhesie · Patientenwärmung · Bipolare Pinzette mit Kabel · Sterile Lichtgriffe · Konkrete Unverträglichkeiten klären · Inzisionsfolie nur nach Hausplan · C-Bogen und Strahlenschutz · Präparat korrekt übergeben · Hautantiseptik-/Waschset · HF-Gerät: Betriebsart prüfen · Absaugsysteme · Definitivimplantat bestätigt öffnen · Steriles Zubehör auf Ansage reichen · Drainageanschluss kontrollieren · Foto: Instrumentiertisch
Falls Grok/Astra hier ein Gegenstück in 000 für unpassend halten: bitte melden.
