# Heike-Wissen 000 – Grundwissen für alle Eingriffe

_Version 1.4 · 07.10.2026 · nach Grok-Prüfung · Astra-Prüfung vor Integration offen · klinisches Review offen_

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
- Sterile Tische erst kurz vor Beginn (bis Schnitt steril abgedeckt; S. 462, Erläuterung S. 455) 📖 KRINKO
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
- Anästhesie vor Zement informieren (über jeden Zementierschritt; AMBOSS: vor Einbringen) — _nur Knochenzement geplant_ 📖 BCIS
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
- „Zement geplant? Anästhesie über jeden Zementierschritt informieren.“ 📖 BCIS
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

## Änderungen v1.4 (07.10.2026)
Grundlage: Lauf 000 (Grok + Astra, Julian ok).
- Anästhesie vor Zement informieren: Quelle AMBOSS → **BCIS** (AMBOSS-Hinweis bleibt)
- Heike-Satz „Zement geplant? …“: Quelle AMBOSS → **BCIS**
- KRINKO-Fundstellen: Inzisionsfolie/Türen **S. 461**, sterile Tische S. 462, Erläuterung **S. 455**

---

## Daten für die App (JSON)
_Maschinenlesbare Fassung desselben Pakets. Maßgeblich für den Import._

```json
{
 "paket": "heike-wissen-000",
 "typ": "grundwissen",
 "version": "1.4",
 "stand": "2026-10-07",
 "autor": "Claude (KI) – Entwurf, Gegenprüfung (Grok/Astra) + klinisches Review Julian offen",
 "gilt_fuer_eingriffe": "alle",
 "situationen": [
  {
   "id": "alle",
   "label": "alle Eingriffe"
  },
  {
   "id": "hf_mono",
   "label": "monopolare HF-Chirurgie"
  },
  {
   "id": "hf_bi",
   "label": "bipolare HF-Chirurgie"
  },
  {
   "id": "implantat",
   "label": "Implantat geplant"
  },
  {
   "id": "zement",
   "label": "Knochenzement geplant"
  },
  {
   "id": "bildwandler",
   "label": "Bildwandler/Röntgen geplant"
  },
  {
   "id": "praeparat",
   "label": "Präparat/Histologie angeordnet"
  },
  {
   "id": "blutsperre",
   "label": "Blutsperre/-leere geplant"
  },
  {
   "id": "seitenlage",
   "label": "Seitenlage"
  },
  {
   "id": "steinschnitt",
   "label": "Steinschnittlage"
  },
  {
   "id": "bauchlage",
   "label": "Bauchlage"
  },
  {
   "id": "laparoskopie",
   "label": "Laparoskopie"
  },
  {
   "id": "notfall",
   "label": "Notfalleingriff"
  }
 ],
 "regeln_fuer_heike": [
  "Erlaubt nur mit Quelle und Hinweis: Medikamente mit Dosierung („laut ärztlicher Anordnung/Fachinformation prüfen“), Zement-Mischzeiten („nur für genanntes Produkt laut IFU, temperaturabhängig“), HF-Leistungswerte („Herstellerempfehlung, Gerät/Gewebe abhängig“), Implantatgrößen und -kompatibilität („laut Herstellerdokument, Stand angeben“). Ohne Quelle: weglassen.",
  "Nichts als Hausstandard ausgeben; Vorschläge sind Vorschläge, gespeichert wird nur Angetipptes/Getipptes.",
  "Springer-Sicht: bereitstellen, anreichen, ansagen, dokumentieren – keine OP-Technik.",
  "Patientendaten nie verarbeiten oder speichern; Fotos ohne Personen/Identifikatoren.",
  "Sicherheitsregeln (Time-out, Zählung, Implantat auf Ansage) nie wegen Tempo weglassen.",
  "Bei Zähldifferenz, unklarer Seite oder unklarem Implantat: STOPP empfehlen, nie selbst entscheiden.",
  "Heike ist eine KI und behauptet keine eigene Berufserfahrung."
 ],
 "merge_regeln": [
  "Paket 000 gilt für jeden Eingriff; Eingriffspakete (001 ff.) ergänzen und präzisieren.",
  "Gleiche Bedeutung in 000 und Eingriffspaket: Eingriffspaket gewinnt, 000-Eintrag ausblenden.",
  "Situations-IDs (hf_mono, implantat, zement …) werden aus Eingriffspaket/Variante/Nutzerantwort abgeleitet; nur passende 000-Chips zeigen.",
  "000-Sicherheitspunkte (count, facts) erscheinen in jedem Standard als Vorschlag im passenden Abschnitt und im Abschluss-Check."
 ],
 "abschnitte": {
  "facts": [
   {
    "label": "Patientenidentität geprüft",
    "menge": null,
    "einheit": null,
    "spez": "Patient bestätigt Identität (WHO); Armband + aktive Rückfrage zusätzlich (KVWL/APS)",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_who",
    "hinweis": "Armband steht nicht in der WHO-Checkliste; Armband + Rückfrage laut q_kvwl."
   },
   {
    "label": "Eingriffsort markiert und sichtbar",
    "menge": null,
    "einheit": null,
    "spez": "Markierung nach Lagerung/Abdeckung prüfbar",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_kvwl"
   },
   {
    "label": "Sign-in",
    "menge": null,
    "einheit": null,
    "spez": "vor Narkoseeinleitung",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_who"
   },
   {
    "label": "Team-Time-out",
    "menge": null,
    "einheit": null,
    "spez": "vor dem Schnitt, hörbar, ganzes Team",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_who"
   },
   {
    "label": "Sign-out",
    "menge": null,
    "einheit": null,
    "spez": "vor Verlassen des Saals, inkl. Zählergebnis",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_who"
   },
   {
    "label": "Allergien/Unverträglichkeiten erfragt",
    "menge": null,
    "einheit": null,
    "spez": "produktbezogen (z. B. Desinfektion, Latex, Pflaster)",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Implantat laut Planung bestätigt",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   }
  ],
  "room": [
   {
    "label": "OP-Tisch + Zubehör für Lagerung",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "HF-Gerät funktionsgeprüft",
    "menge": null,
    "einheit": null,
    "spez": "Leistung nach Herstellerempfehlung/Operateur",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Neutralelektrode",
    "menge": 1,
    "einheit": "Stk",
    "spez": "nur bei monopolar",
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Bipolare Pinzette + Kabel",
    "menge": 1,
    "einheit": "Stk",
    "spez": null,
    "gilt_fuer": [
     "hf_bi"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Sauger funktionsgeprüft",
    "menge": 1,
    "einheit": "Stk",
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Wärmesystem",
    "menge": null,
    "einheit": null,
    "spez": "z. B. Warmluftdecke",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "OP-Licht ausgerichtet + Lichtgriffe",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   },
   {
    "label": "Bildwandler + Röntgenschürzen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "bildwandler"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Dosimeter/Strahlenschutz laut Haus",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "bildwandler"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Blutsperren-Gerät + Manschette",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "blutsperre"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Laparoskopie-Turm + CO₂ geprüft",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "laparoskopie"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Notfallausstattung erreichbar",
    "menge": null,
    "einheit": null,
    "spez": "laut Haus",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   }
  ],
  "position": [
   {
    "label": "Druckstellen gepolstert",
    "menge": null,
    "einheit": null,
    "spez": "Fersen, Sakrum, Ellenbogen, Knochenvorsprünge",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Arme gesichert, nicht überstreckt",
    "menge": null,
    "einheit": null,
    "spez": "Nervenschutz Plexus/Ulnaris",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Neutralelektrode-Ort",
    "menge": null,
    "einheit": null,
    "spez": "gut durchblutete Muskulatur, nicht über Knochen/Narbe/Metall, vollflächig",
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Kein Hautkontakt zu Metallteilen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Seitenstützen/Polster stabil",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "seitenlage"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Hüftbeugung >90° lange vermeiden",
    "menge": null,
    "einheit": null,
    "spez": "Steinschnitt, vaginale Eingriffe",
    "gilt_fuer": [
     "steinschnitt"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_lag"
   },
   {
    "label": "Gesicht/Augen/Brust geschützt",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "bauchlage"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Lagerung dokumentiert",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   }
  ],
  "draping": [
   {
    "label": "Sterile Tische erst kurz vor Beginn",
    "menge": null,
    "einheit": null,
    "spez": "bis Schnitt steril abgedeckt",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko",
    "hinweis": "KRINKO gedruckte S. 462 (PDF-S. 15), Abschnitt 4.1, Kat. II; Erläuterung S. 455 (PDF-S. 8), Instrumentarium (Medizinprodukte)."
   },
   {
    "label": "Hautdesinfektion laut Haus",
    "menge": null,
    "einheit": null,
    "spez": "Produkt + Einwirkzeit nach IFU",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Abdeckung flüssigkeitsdicht",
    "menge": null,
    "einheit": null,
    "spez": "Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko",
    "hinweis": "Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen."
   },
   {
    "label": "Keine nicht imprägnierte Inzisionsfolie",
    "menge": null,
    "einheit": null,
    "spez": "nicht antiseptisch imprägnierte Folien nicht verwenden (Kat. IB)",
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko"
   },
   {
    "label": "Türbewegungen/Saalverkehr gering",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko"
   }
  ],
  "count": [
   {
    "label": "Zählen vor Beginn",
    "menge": null,
    "einheit": null,
    "spez": "alle eingesetzten Materialien",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Ergänztes Material sofort zählen",
    "menge": null,
    "einheit": null,
    "spez": "Vier-Augen-Prinzip",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Zählen bei Teamwechsel",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Zählen vor Wund-/Höhlenverschluss",
    "menge": null,
    "einheit": null,
    "spez": "Zeitpunkte laut Haus-Zählplan",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": true,
    "quelle": "q_aps"
   },
   {
    "label": "Abschlusszählung + Entsorgungskontrolle",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Kompressen, Tupfer, Bauchtücher",
    "menge": null,
    "einheit": null,
    "spez": "röntgenkontrastgestreift",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Nadeln, Klingen, Clips, Drahtteile",
    "menge": null,
    "einheit": null,
    "spez": "Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Instrumente + Zusatzinstrumente",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Beabsichtigt belassenes Material doku",
    "menge": null,
    "einheit": null,
    "spez": "z. B. Tamponade, Drainage, Implantat",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Differenz: STOPP + sofort melden",
    "menge": null,
    "einheit": null,
    "spez": "weiteres Vorgehen laut Operateur/Haus",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": true,
    "quelle": "q_aps"
   },
   {
    "label": "Zählprotokoll dokumentiert",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   }
  ],
  "implants": [
   {
    "label": "Implantat erst auf Ansage öffnen",
    "menge": null,
    "einheit": null,
    "spez": "Typ, Seite, Größe laut wiederholen",
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Verpackung/Verfall prüfen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   },
   {
    "label": "Implantat-Etiketten in Doku",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Implantatpass laut Haus",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Anästhesie vor Zement informieren",
    "menge": null,
    "einheit": null,
    "spez": "Anästhesie über jeden Schritt des Zementiervorgangs informieren",
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_bcis",
    "hinweis": "AMBOSS: vor Einbringen; q_bcis: jeden Zementierschritt."
   },
   {
    "label": "Zement nach Hersteller-IFU",
    "menge": null,
    "einheit": null,
    "spez": "Mischzeit je Produkt laut IFU, temperaturabhängig",
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Medikamente am Tisch nur laut Anordnung",
    "menge": null,
    "einheit": null,
    "spez": "Dosis nur mit Quelle + „laut Anordnung prüfen“",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   }
  ],
  "workflow": [
   {
    "label": "Saal vorbereiten vor Einschleusen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Material nach Bedarf anreichen + ansagen",
    "menge": null,
    "einheit": null,
    "spez": "steril übergeben, mitzählen",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Instrumente/Material auf Ansage öffnen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Blutsperrenzeit ansagen + dokumentieren",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "blutsperre"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Präparat sofort beschriften",
    "menge": null,
    "einheit": null,
    "spez": "Patient, Lokalisation, Begleitschein",
    "gilt_fuer": [
     "praeparat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Fixierung laut Pathologie-Vorgabe",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "praeparat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Notfall: Zählung nach Haus-Regel",
    "menge": null,
    "einheit": null,
    "spez": "Aussetzen/Nachzählen festgelegt",
    "gilt_fuer": [
     "notfall"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": true,
    "quelle": "q_aps"
   }
  ],
  "dressing": [
   {
    "label": "Steriler Wundverband laut Haus",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Drainagen fixiert + beschriftet",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Neutralelektrode ab, Haut kontrolliert",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Lagerungsstellen kontrolliert",
    "menge": null,
    "einheit": null,
    "spez": "Hautbefund dokumentieren",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   },
   {
    "label": "Übergabe Aufwachraum",
    "menge": null,
    "einheit": null,
    "spez": "Eingriff, Drainagen, Besonderheiten, Anordnungen",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null
   }
  ],
  "pitfalls": [
   {
    "label": "Markierung unter Abdeckung verschwunden",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_kvwl"
   },
   {
    "label": "Zählung bei Teamwechsel vergessen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_aps"
   },
   {
    "label": "Implantat auf Verdacht geöffnet",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   },
   {
    "label": "Präparat unbeschriftet",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "praeparat"
    ],
    "optional": false,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   },
   {
    "label": "Tische zu früh offen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko"
   },
   {
    "label": "Neutralelektrode über Metall/Narbe",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   },
   {
    "label": "Zement ohne Anästhesie-Ansage",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_amboss"
   },
   {
    "label": "Keine Antiseptikum-Pfützen",
    "menge": null,
    "einheit": null,
    "spez": "Patient darf nicht in angesammeltem Hautantiseptikum liegen.",
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_krinko",
    "hinweis": "Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; besonders vor monopolarer HF."
   }
  ],
  "photos": [
   {
    "label": "Foto Tischaufbau ohne Patient",
    "menge": null,
    "einheit": null,
    "spez": "keine Personen, keine Identifikatoren",
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "üblich",
    "hausabhaengig": false,
    "quelle": null
   }
  ]
 },
 "heike_hinweise": [
  {
   "text": "Ist die Markierung nach dem Abdecken noch zu sehen?",
   "quelle": "q_kvwl"
  },
  {
   "text": "Ergänztes Material gleich mitzählen – vier Augen.",
   "quelle": "q_aps"
  },
  {
   "text": "Teamwechsel? Dann wird gezählt, bevor übergeben wird.",
   "quelle": "q_aps"
  },
  {
   "text": "Sterile Tische erst kurz vor Beginn öffnen und bis zum Schnitt abdecken.",
   "quelle": "q_krinko"
  },
  {
   "text": "Zement geplant? Anästhesie über jeden Zementierschritt informieren.",
   "quelle": "q_bcis"
  },
  {
   "text": "Implantat erst auf Ansage öffnen – Typ, Seite und Größe laut wiederholen.",
   "quelle": null
  }
 ],
 "typische_luecken": [
  "Zählung bei Teamwechsel",
  "Markierung nach Abdeckung prüfen",
  "Präparat-Begleitschein",
  "Implantat-Etiketten",
  "Neutralelektrode nach OP: Haut kontrollieren",
  "Lagerungsstellen nach OP kontrollieren"
 ],
 "quellen": [
  {
   "id": "q_who",
   "titel": "Implementation Manual WHO Surgical Safety Checklist 2009",
   "herausgeber": "World Health Organization",
   "url": "https://www.who.int/docs/default-source/patient-safety/9789241598590-eng.pdf",
   "abgerufen": "2026-10-06"
  },
  {
   "id": "q_aps",
   "titel": "Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“",
   "herausgeber": "Aktionsbündnis Patientensicherheit e. V.",
   "url": "https://www.aps-ev.de/wp-content/uploads/2024/06/flyer-JTZ.pdf",
   "abgerufen": "2026-10-06"
  },
  {
   "id": "q_krinko",
   "titel": "Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473",
   "herausgeber": "KRINKO am RKI",
   "url": "https://www.rki.de/DE/Themen/Infektionskrankheiten/Krankenhaushygiene/KRINKO/Empfehlungen-der-KRINKO/Device-assoziierte-postoperative-Infektionen/Downloads/Empf_postopWI.pdf?__blob=publicationFile&v=1",
   "abgerufen": "2026-10-06",
   "fundstelle": "Abschnitt 4.1: S. 461 (PDF-S. 14): Antiseptikum-Ansammlung (II), flüssigkeitsundurchlässige Abdeckung (IB), nicht antiseptisch imprägnierte Inzisionsfolie (IB), Türen/Fluktuation (II). S. 462 (PDF-S. 15): Abdeckung vorbereiteter steriler Tische (II). Erläuterung: S. 455 (PDF-S. 8), Instrumentarium (Medizinprodukte)."
  },
  {
   "id": "q_kvwl",
   "titel": "Handlungsempfehlung Vermeidung einer Eingriffsverwechslung, 2. Auflage 2024",
   "herausgeber": "APS / KVWL",
   "url": "https://www.kvwl.de/fileadmin/user_upload/pdf/Mitglieder/Qualitaetssicherung/Patientensicherheit/Vermeidung_einer_Eingriffsverwechslung.pdf",
   "abgerufen": "2026-10-06"
  },
  {
   "id": "q_lag",
   "titel": "S2k-Leitlinie Verhinderung lagerungsbedingter Schäden in der operativen Gynäkologie (AWMF 015-077)",
   "herausgeber": "AWMF / DGGG",
   "url": "https://register.awmf.org/assets/guidelines/015-077l_S2k_Verhinderung_Lagerungssch%C3%A4den_Operationen_Gyn%C3%A4kologie_2021-01.pdf",
   "abgerufen": "2026-10-06",
   "hinweis": "gyn-spezifisch; URL aus Lieferung 003 übernehmen"
  },
  {
   "id": "q_amboss",
   "titel": "Endoprothetik des Hüftgelenks (Zementhinweis)",
   "herausgeber": "AMBOSS GmbH",
   "url": "https://www.amboss.com/de/wissen/endoprothetik-des-huftgelenks",
   "abgerufen": "2026-10-06"
  },
  {
   "id": "q_bcis",
   "titel": "Factsheet Implantationssyndrom / BCIS",
   "herausgeber": "Heraeus Medical / PALACADEMY",
   "url": "https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf",
   "abgerufen": "2026-10-07",
   "fundstelle": "PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über jeden Schritt des Zementiervorgangs informieren."
  }
 ],
 "offen": [
  "Neutralelektrode: Ort/Anlage laut Hersteller-IFU des Hauses – keine Normquelle ausgewertet.",
  "Wärmemanagement: AWMF-S3 „Vermeidung perioperativer Hypothermie“ (001-018) nicht nachgelesen – deshalb ohne Quelle.",
  "Strahlenschutz: Strahlenschutzanweisung des Hauses maßgeblich; keine Rechtsquelle ausgewertet.",
  "Implantatpass/Dokumentationspflichten: rechtliche Grundlage (MPDG/MPBetreibV) nicht ausgewertet.",
  "Pathologie: keine deutsche Leitlinie gefunden; Haus-SOP verbindlich.",
  "Lagerungs-Leitlinie nur gynäkologisch (AWMF 015-077) – übertragbare Prinzipien, keine Orthopädie-Quelle."
 ],
 "julian_pruefen": [
  "Allergie-Abfrage-Formulierung",
  "Zählzeitpunkte laut eurem Zählplan",
  "Neutralelektrode-Regeln",
  "Was ihr bei Teamwechsel konkret macht",
  "Übergabe-Inhalte Aufwachraum"
 ],
 "aenderungsprotokoll": [
  {
   "version": "1.1",
   "datum": "2026-10-07",
   "was": "Regel geändert (Julian): Dosierungen, Zement-Mischzeiten, HF-Werte und Implantatgrößen mit Quelle und Hinweis erlaubt."
  },
  {
   "version": "1.2",
   "datum": "2026-10-07",
   "grundlage": "eingang/2026-10-07-000-grundwissen-v1.1-grok.md",
   "vorschlag": "aenderungen/2026-10-07-000-grundwissen-vorschlag.md",
   "was": "Grok Nr. 1–7, 11 eingebaut; KRINKO-Seiten nach Astra (S. 461); Nr. 8–10 bleiben offen."
  },
  {
   "version": "1.3",
   "datum": "2026-10-07",
   "grundlage": "eingang/2026-10-07-001-hueft-tep-v1.1-grok.md (KRINKO-Seitenklärung)",
   "was": "Sterile Tische: Fundstelle S. 461 → S. 462 (PDF-S. 15); q_krinko-Fundstellen bereinigt."
  },
  {
   "version": "1.4",
   "datum": "2026-10-07",
   "grundlage": "Lauf 000: 000-grok + 000-astra (Astra: ÄNDERN, Nr. 2/6/8/9), Julian ok 07.10.2026",
   "was": "Zement-Chip und Heike-Satz Quelle q_amboss → q_bcis; q_krinko-Fundstellen (S. 461/462/455); sterile Tische Erläuterung S. 455."
  }
 ]
}
```
