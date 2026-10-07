# Heike-Wissen 000 – Grundwissen für alle Eingriffe

_Version 1.5 · 2026-10-07 · abgeschlossen (Lauf 000 + Ergänzung aus Lauf 001) · klinisches Review durch Julian offen_

Paket 000 ist das gemeinsame Fundament: Es gilt bei **jedem** Eingriff und enthält alles allgemeine OP-Wissen. Die Eingriffspakete (001 Hüft-TEP …) enthalten nur Eingriffsspezifisches.

Legende: ⚠️ hausabhängig · *(optional)* · 📖 Quelle nachgelesen · _nur …_ = gilt nur in dieser Situation/Variante

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

## 1. Eckdaten & Sicherheit `facts`
- **Patientenidentität geprüft** (Patient bestätigt Identität (WHO); Armband + aktive Rückfrage zusätzlich (KVWL/APS)) 📖 WHO
  - Armband steht nicht in der WHO-Checkliste; Armband + Rückfrage laut q_kvwl.
- **Eingriffsort markiert und sichtbar** (Markierung nach Lagerung/Abdeckung prüfbar) 📖 KVWL
- **Sign-in** (vor Narkoseeinleitung) 📖 WHO
- **Team-Time-out** (vor dem Schnitt, hörbar, ganzes Team) 📖 WHO
- **Sign-out** (vor Verlassen des Saals, inkl. Zählergebnis) 📖 WHO
- **Allergien/Unverträglichkeiten erfragt** (konkrete Auslöser erfragen, z. B. Antiseptikum, Latex, Pflaster, Nickel/Metall, Knochenzement) ⚠️
- **Implantat laut Planung bestätigt** — _nur implantat_ ⚠️
- **Anästhesieverfahren laut Plan** ⚠️
  - Verfahren und organisatorische Besonderheiten mit Anästhesie abstimmen; keine Empfehlung für eine Narkoseart.

## 2. Saal & Geräte `room`
- **OP-Tisch + Zubehör für Lagerung** ⚠️
- **HF-Gerät funktionsgeprüft** (Leistung nach Herstellerempfehlung/Operateur) ⚠️
  - Geplante Betriebsart mono-/bipolar und zugehöriges Zubehör vor Nutzung klären; Geräte-/Zubehör-IFU und Hausablauf beachten.
- 1 Stk **Neutralelektrode** (nur bei monopolar) — _nur hf_mono_ ⚠️
- 1 Stk **Bipolare Pinzette + Kabel** — _nur hf_bi_ *(optional)* ⚠️
- **Sauger funktionsgeprüft** ⚠️
  - Anzahl und Konfiguration nach Eingriff und Hausplan festlegen; Funktion, Anschlüsse und erforderliche Reserve prüfen. Weder ein noch zwei Systeme als allgemeine Pflichtmenge setzen.
- **Wärmesystem** (z. B. Warmluftdecke) ⚠️
- **OP-Licht ausgerichtet + Lichtgriffe** ⚠️
- **Bildwandler + Röntgenschürzen** — _nur bildwandler_ ⚠️
- **Dosimeter/Strahlenschutz laut Haus** — _nur bildwandler_ ⚠️
- **Blutsperren-Gerät + Manschette** — _nur blutsperre_ ⚠️
- **Laparoskopie-Turm + CO₂ geprüft** — _nur laparoskopie_ ⚠️
- **Notfallausstattung erreichbar** (laut Haus) ⚠️
- 2 Paare je sterile Person **Doppelhandschuhe pro sterile Person** (Größen je Person) *(optional)* ⚠️
  - Nur wenn Doppelhandschuhe laut Risiko-/Hausplanung vorgesehen sind; Größen, Teamzahl und Wechselreserve festlegen. Keine allgemeine Zwei-Paar-Pflicht für jeden Eingriff.
- 1 Stück je sterile Person **Steriler OP-Kittel pro Person** ⚠️
  - Ein Kittel je steril tätiger Person; Material/Schutzleistung und Reserven nach Hausplan.
- **Antriebe und Ersatzakkus** *(optional)* ⚠️
  - Nur wenn Antriebe geplant; steriles Antriebskonzept und Ersatzakkus passend zu Gerät und IFU.

## 3. Lagerung `position`
- **Druckstellen gepolstert** (Fersen, Sakrum, Ellenbogen, Knochenvorsprünge) ⚠️
- **Arme gesichert, nicht überstreckt** (Nervenschutz Plexus/Ulnaris) ⚠️
- **Neutralelektrode-Ort** (gut durchblutete Muskulatur, nicht über Knochen/Narbe/Metall, vollflächig) — _nur hf_mono_ ⚠️
- **Kein Hautkontakt zu Metallteilen** — _nur hf_mono_ ⚠️
- **Seitenstützen/Polster stabil** — _nur seitenlage_ ⚠️
- **Hüftbeugung >90° lange vermeiden** (Steinschnitt, vaginale Eingriffe) — _nur steinschnitt_ 📖 LAG
- **Gesicht/Augen/Brust geschützt** — _nur bauchlage_ ⚠️
- **Lagerung dokumentiert** ⚠️
- **Mechanische Prophylaxe laut Plan** *(optional)* ⚠️
  - Nur falls angeordnet; System und vorgesehene Extremität bestätigen. Keine pauschale Gegenbein-Anordnung und keine Medikamentenempfehlung.
- **NE-Kontakt nach Umlagerung** — _nur hf_mono_ 📖 HEBU
  - HEBU verlangt erneute Kontrolle nach Änderung der Patientenlage. Produktbeispiel; tatsächliche NE-IFU maßgeblich.

## 4. Desinfektion & Abdeckung `draping`
- **Sterile Tische erst kurz vor Beginn** (bis Schnitt steril abgedeckt) 📖 KRINKO
  - KRINKO gedruckte S. 462 (PDF-S. 15), Abschnitt 4.1, Kat. II; Erläuterung S. 455 (PDF-S. 8), Instrumentarium (Medizinprodukte).
- **Hautdesinfektion laut Haus** (Produkt + Einwirkzeit nach IFU) ⚠️
- **Abdeckung flüssigkeitsdicht** (Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).) 📖 KRINKO
  - Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen.
- **Keine nicht imprägnierte Inzisionsfolie** (nicht antiseptisch imprägnierte Folien nicht verwenden (Kat. IB)) *(optional)* 📖 KRINKO
- **Türbewegungen/Saalverkehr gering** 📖 KRINKO
- **Kabel und Schläuche sichern** ⚠️
  - Sterilfeld, Bewegungsraum und ggf. Bildgebung freihalten; keine Zugbelastung.
- **Inzisionsfolie nur nach Hausplan** *(optional)* ⚠️
  - Nur antiseptisch imprägnierte Folie, falls laut Hausplan vorgesehen; keine allgemeine Folienpflicht. Separate KRINKO-Regel gegen nicht antiseptisch imprägnierte Inzisionsfolie bleibt bestehen.

## 5. Zählkontrolle & Dokumentation `count`
- **Zählen vor Beginn** (alle eingesetzten Materialien) 📖 APS
- **Ergänztes Material sofort zählen** (Vier-Augen-Prinzip) 📖 APS
- **Zählen bei Teamwechsel** 📖 APS
- **Zählen vor Wund-/Höhlenverschluss** (Zeitpunkte laut Haus-Zählplan) 📖 APS
- **Abschlusszählung + Entsorgungskontrolle** 📖 APS
- **Kompressen, Tupfer, Bauchtücher** (röntgenkontrastgestreift) 📖 APS
- **Nadeln, Klingen, Clips, Drahtteile** (Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan) 📖 APS
- **Instrumente + Zusatzinstrumente** 📖 APS
- **Beabsichtigt belassenes Material doku** (z. B. Tamponade, Drainage, Implantat) 📖 APS
- **Differenz: STOPP + sofort melden** (weiteres Vorgehen laut Operateur/Haus) 📖 APS
- **Zählprotokoll dokumentiert** 📖 APS
- **Scharfe Teile und Teilebruch prüfen** ⚠️
  - Nadeln, Klingen, Sägeblätter sowie ablösbare Geräte-/Applikatorteile erfassen. Ungeöffnete Reserve nicht mit ans Sterilfeld gegebenem Material verwechseln.
- **Probekomponenten zurückführen** — _nur implantat_ ⚠️
  - Alle eingesetzten Trial-Teile nach Hausprotokoll auf Vollständigkeit prüfen; von Definitivimplantaten trennen.
- **Zementüberschuss gesondert prüfen** — _nur zement_ ⚠️
  - Kein pauschales Stückzählen von Zementresten. Operative Kontrolle auf unerwünschten Überschuss; beabsichtigte Zementfixation bleibt davon getrennt.

## 6. Implantate, Zement & Medikamente `implants`
- **Implantat erst auf Ansage öffnen** (Typ, Seite, Größe laut wiederholen) — _nur implantat_ ⚠️
  - Vor Öffnen Komponente, gegebenenfalls Seite, System, Größe und ausdrücklich belegte Komponentenkompatibilität abgleichen; Ansage bestätigen lassen. Verpackung und Sterilität beachten. Offene Kompatibilität zuerst klären.
- **Verpackung/Verfall prüfen** — _nur implantat_ ⚠️
- **Implantat-Etiketten in Doku** — _nur implantat_ ⚠️
- **Implantatpass laut Haus** — _nur implantat_ ⚠️
- **Anästhesie vor Zement informieren** (Anästhesie über jeden Schritt des Zementiervorgangs informieren) — _nur zement_ 📖 BCIS
  - AMBOSS: vor Einbringen; q_bcis: jeden Zementierschritt.
- **Zement nach Hersteller-IFU** (Mischzeit je Produkt laut IFU, temperaturabhängig) — _nur zement_ ⚠️
- **Medikamente am Tisch nur laut Anordnung** (Dosis nur mit Quelle + „laut Anordnung prüfen“) ⚠️
- **Größenvorrat vorab prüfen** — _nur implantat_ ⚠️
  - Fehlende Größe mitten in der OP vermeiden – Lager/Leihset vorher mit der Planung abgleichen.
- **Zementansage rückbestätigen** — _nur zement_ ⚠️
  - Vorab festlegen, wer die Schritte ansagt. Beispiel: „Zement wird jetzt eingebracht“ – Rückmeldung der Anästhesie abwarten; bei fehlender Antwort unmittelbar klären. Konkrete Ansagen/Zuständigkeit laut Haus-SOP.
- **Zementmischen nur auf Ansage** — _nur zement_ ⚠️
  - Start und Dokumentation nach Hausablauf; ausschließlich aktuelle Produkt-/Mischsystem-IFU verwenden. Keine Mischzeit oder Zusatzrezeptur.

## 7. Ablauf aus Springer-Sicht `workflow`
- **Saal vorbereiten vor Einschleusen** ⚠️
- **Material nach Bedarf anreichen + ansagen** (steril übergeben, mitzählen) 📖 APS
- **Instrumente/Material auf Ansage öffnen** ⚠️
- **Blutsperrenzeit ansagen + dokumentieren** — _nur blutsperre_ ⚠️
- **Präparat sofort beschriften** (Patient, Lokalisation, Begleitschein) — _nur praeparat_ ⚠️
- **Fixierung laut Pathologie-Vorgabe** — _nur praeparat_ ⚠️
- **Notfall: Zählung nach Haus-Regel** (Aussetzen/Nachzählen festgelegt) — _nur notfall_ 📖 APS
- **Anschlüsse vor Nutzung prüfen** ⚠️
  - HF, Absaugung und Antriebe nach Bedarf funktionsgerecht anschließen; Springer stellt bereit, keine Instrumentier- oder Operationstechnik.

## 8. Verband & Ausleitung `dressing`
- **Steriler Wundverband laut Haus** ⚠️
- **Drainagen fixiert + beschriftet** *(optional)* ⚠️
  - Falls Drainage vorhanden: Fixierung/Beschriftung und passenden Anschluss zum Auffangsystem prüfen; Durchgängigkeit und Handhabung nach aktueller Produkt-IFU/Hausvorgabe kontrollieren.
- **Neutralelektrode ab, Haut kontrolliert** — _nur hf_mono_ ⚠️
- **Lagerungsstellen kontrolliert** (Hautbefund dokumentieren) ⚠️
- **Übergabe Aufwachraum** (Eingriff, Drainagen, Besonderheiten, Anordnungen) ⚠️
  - Zählstatus und offene Besonderheiten strukturiert übergeben; eingriffsspezifische Inhalte stehen im Eingriffspaket.

## 9. Typische Fehler & Fallstricke `pitfalls`
- **Markierung unter Abdeckung verschwunden** 📖 KVWL
- **Zählung bei Teamwechsel vergessen** 📖 APS
- **Implantat auf Verdacht geöffnet** — _nur implantat_ ⚠️
- **Präparat unbeschriftet** — _nur praeparat_ ⚠️
- **Tische zu früh offen** 📖 KRINKO
- **Neutralelektrode über Metall/Narbe** — _nur hf_mono_ ⚠️
- **Zement ohne Anästhesie-Ansage** — _nur zement_ 📖 AMBOSS
- **Keine Antiseptikum-Pfützen** (Patient darf nicht in angesammeltem Hautantiseptikum liegen.) 📖 KRINKO
  - Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; besonders vor monopolarer HF.
- **NE vor Flüssigkeit schützen** (Flüssigkeitskontakt und Eindringen unter die NE vermeiden.) — _nur hf_mono_ 📖 HEBU
  - HEBU GAHF113V004 als Produktbeispiel; maßgeblich ist die IFU der tatsächlich verwendeten NE.

## 10. Fotos `photos`
- **Foto Tischaufbau ohne Patient** (keine Personen, keine Identifikatoren) *(optional)* ⚠️

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
- **WHO** – Implementation Manual WHO Surgical Safety Checklist 2009, World Health Organization https://www.who.int/docs/default-source/patient-safety/9789241598590-eng.pdf
- **APS** – Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“, Aktionsbündnis Patientensicherheit e. V. https://www.aps-ev.de/wp-content/uploads/2024/06/flyer-JTZ.pdf
- **KRINKO** – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473, KRINKO am RKI. Abschnitt 4.1: S. 461 (PDF-S. 14): Antiseptikum-Ansammlung (II), flüssigkeitsundurchlässige Abdeckung (IB), nicht antiseptisch imprägnierte Inzisionsfolie (IB), Türen/Fluktuation (II). S. 462 (PDF-S. 15): Abdeckung vorbereiteter steriler Tische (II). Erläuterung: S. 455 (PDF-S. 8), Instrumentarium (Medizinprodukte). https://www.rki.de/DE/Themen/Infektionskrankheiten/Krankenhaushygiene/KRINKO/Empfehlungen-der-KRINKO/Device-assoziierte-postoperative-Infektionen/Downloads/Empf_postopWI.pdf?__blob=publicationFile&v=1
- **KVWL** – Handlungsempfehlung Vermeidung einer Eingriffsverwechslung, 2. Auflage 2024, APS / KVWL https://www.kvwl.de/fileadmin/user_upload/pdf/Mitglieder/Qualitaetssicherung/Patientensicherheit/Vermeidung_einer_Eingriffsverwechslung.pdf
- **LAG** – S2k-Leitlinie Verhinderung lagerungsbedingter Schäden in der operativen Gynäkologie (AWMF 015-077), AWMF / DGGG https://register.awmf.org/assets/guidelines/015-077l_S2k_Verhinderung_Lagerungssch%C3%A4den_Operationen_Gyn%C3%A4kologie_2021-01.pdf
- **AMBOSS** – Endoprothetik des Hüftgelenks (Zementhinweis), AMBOSS GmbH https://www.amboss.com/de/wissen/endoprothetik-des-huftgelenks
- **BCIS** – Factsheet Implantationssyndrom / BCIS, Heraeus Medical / PALACADEMY. PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über jeden Schritt des Zementiervorgangs informieren. https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf
- **HEBU** – Einmal-Neutralelektroden – Gebrauchsanweisung GAHF113, HEBU medical GmbH. GAHF113V004 vom 20.02.2026, S. 6 §5.2 (Kontakt, Kontrolle nach Lageänderung, kein Flüssigkeitskontakt); S. 8 §6 (Brandrisiko); S. 9 §8. Produktbeispiel – Haus-NE-IFU maßgeblich. https://www.hebumedical.de/ga/GAHF113.pdf

## Offen
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

## Änderungen
- **v1.1** (2026-10-07): Regel geändert (Julian): Dosierungen, Zement-Mischzeiten, HF-Werte und Implantatgrößen mit Quelle und Hinweis erlaubt.
- **v1.2** (2026-10-07): Grok Nr. 1–7, 11 eingebaut; KRINKO-Seiten nach Astra (S. 461); Nr. 8–10 bleiben offen.
- **v1.3** (2026-10-07): Sterile Tische: Fundstelle S. 461 → S. 462 (PDF-S. 15); q_krinko-Fundstellen bereinigt.
- **v1.4** (2026-10-07): Zement-Chip und Heike-Satz Quelle q_amboss → q_bcis; q_krinko-Fundstellen (S. 461/462/455); sterile Tische Erläuterung S. 455.
- **v1.5** (2026-10-07): Allgemeines aus 001 übernommen (14 Chips, u. a. Kabel sichern, Anschlüsse, scharfe Teile, Probekomponenten, Zementansage/-mischen/-überschuss, Kittel, Doppelhandschuhe optional, Antriebe, Prophylaxe, Anästhesieverfahren, NE vor Flüssigkeit, NE nach Umlagerung, Inzisionsfolie nach Hausplan); HF-Betriebsart, Sauger-Anzahl, Drainage, Implantat-Öffnen, Übergabe-Zählstatus und Allergie-Auslöser präzisiert; Quelle q_hebu neu.

---

## Daten für die App (JSON)
_Maschinenlesbare Fassung desselben Pakets. Maßgeblich für den Import._

```json
{
 "paket": "heike-wissen-000",
 "typ": "grundwissen",
 "version": "1.5",
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
    "spez": "konkrete Auslöser erfragen, z. B. Antiseptikum, Latex, Pflaster, Nickel/Metall, Knochenzement",
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
   },
   {
    "label": "Anästhesieverfahren laut Plan",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Verfahren und organisatorische Besonderheiten mit Anästhesie abstimmen; keine Empfehlung für eine Narkoseart."
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
    "quelle": null,
    "hinweis": "Geplante Betriebsart mono-/bipolar und zugehöriges Zubehör vor Nutzung klären; Geräte-/Zubehör-IFU und Hausablauf beachten."
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
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Anzahl und Konfiguration nach Eingriff und Hausplan festlegen; Funktion, Anschlüsse und erforderliche Reserve prüfen. Weder ein noch zwei Systeme als allgemeine Pflichtmenge setzen."
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
   },
   {
    "label": "Doppelhandschuhe pro sterile Person",
    "menge": 2,
    "einheit": "Paare je sterile Person",
    "spez": "Größen je Person",
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Nur wenn Doppelhandschuhe laut Risiko-/Hausplanung vorgesehen sind; Größen, Teamzahl und Wechselreserve festlegen. Keine allgemeine Zwei-Paar-Pflicht für jeden Eingriff."
   },
   {
    "label": "Steriler OP-Kittel pro Person",
    "menge": 1,
    "einheit": "Stück je sterile Person",
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Ein Kittel je steril tätiger Person; Material/Schutzleistung und Reserven nach Hausplan."
   },
   {
    "label": "Antriebe und Ersatzakkus",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Nur wenn Antriebe geplant; steriles Antriebskonzept und Ersatzakkus passend zu Gerät und IFU."
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
   },
   {
    "label": "Mechanische Prophylaxe laut Plan",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Nur falls angeordnet; System und vorgesehene Extremität bestätigen. Keine pauschale Gegenbein-Anordnung und keine Medikamentenempfehlung."
   },
   {
    "label": "NE-Kontakt nach Umlagerung",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_hebu",
    "hinweis": "HEBU verlangt erneute Kontrolle nach Änderung der Patientenlage. Produktbeispiel; tatsächliche NE-IFU maßgeblich."
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
   },
   {
    "label": "Kabel und Schläuche sichern",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Sterilfeld, Bewegungsraum und ggf. Bildgebung freihalten; keine Zugbelastung."
   },
   {
    "label": "Inzisionsfolie nur nach Hausplan",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": true,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Nur antiseptisch imprägnierte Folie, falls laut Hausplan vorgesehen; keine allgemeine Folienpflicht. Separate KRINKO-Regel gegen nicht antiseptisch imprägnierte Inzisionsfolie bleibt bestehen."
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
   },
   {
    "label": "Scharfe Teile und Teilebruch prüfen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Nadeln, Klingen, Sägeblätter sowie ablösbare Geräte-/Applikatorteile erfassen. Ungeöffnete Reserve nicht mit ans Sterilfeld gegebenem Material verwechseln."
   },
   {
    "label": "Probekomponenten zurückführen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Alle eingesetzten Trial-Teile nach Hausprotokoll auf Vollständigkeit prüfen; von Definitivimplantaten trennen."
   },
   {
    "label": "Zementüberschuss gesondert prüfen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Kein pauschales Stückzählen von Zementresten. Operative Kontrolle auf unerwünschten Überschuss; beabsichtigte Zementfixation bleibt davon getrennt."
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
    "quelle": null,
    "hinweis": "Vor Öffnen Komponente, gegebenenfalls Seite, System, Größe und ausdrücklich belegte Komponentenkompatibilität abgleichen; Ansage bestätigen lassen. Verpackung und Sterilität beachten. Offene Kompatibilität zuerst klären."
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
   },
   {
    "label": "Größenvorrat vorab prüfen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "implantat"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Fehlende Größe mitten in der OP vermeiden – Lager/Leihset vorher mit der Planung abgleichen."
   },
   {
    "label": "Zementansage rückbestätigen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Vorab festlegen, wer die Schritte ansagt. Beispiel: „Zement wird jetzt eingebracht“ – Rückmeldung der Anästhesie abwarten; bei fehlender Antwort unmittelbar klären. Konkrete Ansagen/Zuständigkeit laut Haus-SOP."
   },
   {
    "label": "Zementmischen nur auf Ansage",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "zement"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "Start und Dokumentation nach Hausablauf; ausschließlich aktuelle Produkt-/Mischsystem-IFU verwenden. Keine Mischzeit oder Zusatzrezeptur."
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
   },
   {
    "label": "Anschlüsse vor Nutzung prüfen",
    "menge": null,
    "einheit": null,
    "spez": null,
    "gilt_fuer": [
     "alle"
    ],
    "optional": false,
    "sicherheit": "hausabhängig",
    "hausabhaengig": true,
    "quelle": null,
    "hinweis": "HF, Absaugung und Antriebe nach Bedarf funktionsgerecht anschließen; Springer stellt bereit, keine Instrumentier- oder Operationstechnik."
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
    "quelle": null,
    "hinweis": "Falls Drainage vorhanden: Fixierung/Beschriftung und passenden Anschluss zum Auffangsystem prüfen; Durchgängigkeit und Handhabung nach aktueller Produkt-IFU/Hausvorgabe kontrollieren."
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
    "quelle": null,
    "hinweis": "Zählstatus und offene Besonderheiten strukturiert übergeben; eingriffsspezifische Inhalte stehen im Eingriffspaket."
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
   },
   {
    "label": "NE vor Flüssigkeit schützen",
    "menge": null,
    "einheit": null,
    "spez": "Flüssigkeitskontakt und Eindringen unter die NE vermeiden.",
    "gilt_fuer": [
     "hf_mono"
    ],
    "optional": false,
    "sicherheit": "belegt",
    "hausabhaengig": false,
    "quelle": "q_hebu",
    "hinweis": "HEBU GAHF113V004 als Produktbeispiel; maßgeblich ist die IFU der tatsächlich verwendeten NE."
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
  },
  {
   "id": "q_hebu",
   "titel": "Einmal-Neutralelektroden – Gebrauchsanweisung GAHF113",
   "herausgeber": "HEBU medical GmbH",
   "url": "https://www.hebumedical.de/ga/GAHF113.pdf",
   "abgerufen": "2026-10-07",
   "fundstelle": "GAHF113V004 vom 20.02.2026, S. 6 §5.2 (Kontakt, Kontrolle nach Lageänderung, kein Flüssigkeitskontakt); S. 8 §6 (Brandrisiko); S. 9 §8. Produktbeispiel – Haus-NE-IFU maßgeblich."
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
  },
  {
   "version": "1.5",
   "datum": "2026-10-07",
   "grundlage": "Lauf 001 (Grok + Astra, Julian-Abnahme 07.10.2026)",
   "was": "Allgemeines aus 001 übernommen (14 Chips, u. a. Kabel sichern, Anschlüsse, scharfe Teile, Probekomponenten, Zementansage/-mischen/-überschuss, Kittel, Doppelhandschuhe optional, Antriebe, Prophylaxe, Anästhesieverfahren, NE vor Flüssigkeit, NE nach Umlagerung, Inzisionsfolie nach Hausplan); HF-Betriebsart, Sauger-Anzahl, Drainage, Implantat-Öffnen, Übergabe-Zählstatus und Allergie-Auslöser präzisiert; Quelle q_hebu neu."
  }
 ]
}
```
