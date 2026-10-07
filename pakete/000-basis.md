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
Grundlage: Grok-Prüfung `eingang/2026-10-07-000-grundwissen-v1.1-grok.md`. Alte Version: `pakete/archiv/000-grundwissen-v1.1.*`. KRINKO-Seiten nach Astra (S. 461, Abschnitt 4.1).
- Patientenidentität: WHO = Patientenbestätigung, Armband + Rückfrage laut KVWL
- Anästhesie über jeden Zementierschritt informieren (Chip + Heike-Satz), neue Quelle BCIS
- Abdeckung: jetzt belegt (KRINKO Kat. IB), flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen
- Neu: Keine Antiseptikum-Pfützen (KRINKO Kat. II)
- Sterile Tische: Seite 462 (v1.3); Inzisionsfolie: Text klarer; Zählung: Klingen laut Haus-Zählplan
- Wärme, NE-Ort, Strahlenschutz bleiben offen (Grok Nr. 8–10)

## Änderungen v1.3 (07.10.2026)
Grundlage: KRINKO-Seitenklärung in `eingang/2026-10-07-001-hueft-tep-v1.1-grok.md`. Alte Version: `pakete/archiv/000-grundwissen-v1.2.*`.
- Sterile Tische: Fundstelle S. 461 → **S. 462** (PDF-S. 15)

## Zur Prüfung in dieser Runde (07.10.2026)
Grok und Astra prüfen in dieser Runde nur diese Punkte, alles andere ist unverändert. Claude ersetzt diesen Abschnitt in jeder Runde.

#### 000-grundwissen (v1.1 → v1.3)
Grundlage: Grok-Prüfung 2026-10-07-000-grundwissen-v1.1-grok.md (im Repo unter eingang/) (Grok Nr. 1–7, 11; Nr. 8–10 bleiben offen) = v1.2; KRINKO-Seitenklärung aus 2026-10-07-001-hueft-tep-v1.1-grok.md (im Repo unter eingang/) (sterile Tische S. 462) = v1.3. Abdeckung/Antiseptikum nach deiner 001-Prüfung (S. 461, Abschnitt 4.1). Erstmals bei Astra – nur diese Änderungen prüfen.

| Nr | Art | Abschnitt · Eintrag | ALT (nur geänderte Felder) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | facts · **Patientenidentität geprüft** | spez: Armband + Rückfrage; hinweis: None | spez: Patient bestätigt Identität (WHO); Armband + aktive Rückfrage zusätzlich (KVWL/APS); hinweis: Armband steht nicht in der WHO-Checkliste; Armband + Rückfrage laut q_kvwl. | q_who – Implementation Manual WHO Surgical Safety Checklist 2009 |
| 2 | geändert | draping · **Sterile Tische erst kurz vor Beginn** | hinweis: None | hinweis: KRINKO gedruckte S. 462 (PDF-S. 15) Kat. II; Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 3 | geändert | draping · **Abdeckung flüssigkeitsdicht** | spez: passend zum Eingriff; sicherheit: hausabhängig; hausabhaengig: True; quelle: None; hinweis: None | spez: Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 4 | geändert | draping · **Keine nicht imprägnierte Inzisionsfolie** | spez: None | spez: nicht antiseptisch imprägnierte Folien nicht verwenden (Kat. IB) | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 5 | geändert | count · **Nadeln, Klingen, Clips, Drahtteile** | spez: None | spez: Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan | q_aps – Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“ |
| 6 | geändert | implants · **Anästhesie vor Zement informieren** | spez: None; hinweis: None | spez: Anästhesie über jeden Schritt des Zementiervorgangs informieren; hinweis: AMBOSS: vor Einbringen; q_bcis: jeden Zementierschritt. | q_amboss – Endoprothetik des Hüftgelenks (Zementhinweis) |
| 7 | neu | pitfalls · **Keine Antiseptikum-Pfützen** | – | spez: Patient darf nicht in angesammeltem Hautantiseptikum liegen.; gilt_fuer: ['alle']; optional: False; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; besonders vor monopolarer HF. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 8 | geändert | heike_hinweise | Zement geplant? Sag der Anästhesie vor dem Einbringen Bescheid. | Zement geplant? Anästhesie über jeden Zementierschritt informieren. | keine (hausabhängig) |
| 9 | geändert | quellen · **q_krinko** | – | Gedruckte S. 461 (PDF-S. 14), Abschnitt 4.1: Antiseptikum-Ansammlung Kat. II, flüssigkeitsundurchlässige Abdeckung bei nicht ausschließbarem Durchfeuchten Kat. IB; S. 460: nicht imprägnierte Inzisionsfolie Kat. IB, Türen/Fluktuation Kat. II; S. 462 (PDF-S. 15): sterile Tische bis OP-Beginn abdecken Kat. II; Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 10 | neu | quellen · **q_bcis** | – | Factsheet Implantationssyndrom / BCIS – PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über jeden Schritt des Zementiervorgangs informieren. | q_bcis – Factsheet Implantationssyndrom / BCIS |
