# Heike-Wissen 002 – Knie-TEP (primär)

_Version 1.0 · 2026-10-08 · Neuanlage (Grok im Auftrag von Julian) · baut auf Paket 000 auf · Prüfrunde und klinisches Review durch Julian offen_

Allgemeines OP-Wissen (Time-out, Zählung, Abdeckung, HF/NE, Blutsperren-Grundregeln, Implantat- und Zement-Kommunikation, Übergabe …) steht in **Paket 000** und wird hier nicht wiederholt. Implantat-Daten: `implantate/*-knie` (Aesculap Columbus, Zimmer Biomet Persona, Smith+Nephew LEGION/GENESIS II, Stryker Triathlon, DePuy Synthes ATTUNE, Medacta GMK Sphere). Maschinenlesbare Fassung: `pakete/002-basis.json`.

**Fixation:** zementiert · zementfrei · Hybrid (Komponenten unterschiedlich fixiert – je Komponente klären)  
**Kopplung:** CR · PS · UC/CS · MP/MC  
**Plattform:** fest · mobil  
**Patella:** mit · ohne Rückflächenersatz  
**Technik:** konventionell · Navigation · PSI · Roboter

Legende: ⚠️ hausabhängig · *(optional)* · 📖 Quelle nachgelesen · _nur …_ = gilt nur in dieser Situation/Variante · Herstellerbeispiele gelten nur für das genannte Produkt

## Varianten
- `zementiert` – zementiert
- `zementfrei` – zementfrei
- `hybrid` – Hybrid: Komponenten unterschiedlich fixiert
- `cr` – CR – kreuzbanderhaltend
- `ps` – PS – posterior stabilisiert
- `uc` – UC/CS – ultrakongruent
- `mp` – MP/MC – medial pivot/medial congruent
- `plattform_fest` – feste Plattform
- `plattform_mobil` – mobile Plattform
- `mit_patella` – mit Patellarückflächenersatz
- `ohne_patella` – ohne Patellarückflächenersatz
- `konventionell` – konventionelle Instrumente
- `navigation` – Navigation
- `psi` – PSI (patientenspezifische Schablonen)
- `roboter` – Roboter-Assistenz

Situationen aus 000: immer `implantat`; bei zementiert/hybrid `zement`; typisch `hf_mono`; bei Bedarf `blutsperre`, `hf_bi`, `bildwandler`.

## 1. Eckdaten & Sicherheit `facts`
- **Primäre Knie-TEP (bikondylärer Oberflächenersatz)** 📖 EMED
  - Ersatz der femoralen und tibialen Gelenkfläche, mit oder ohne Patellarückflächenersatz. Unikondylärer Schlitten, teil-/vollgekoppelte Revisions- und Tumorprothesen sind nicht Inhalt dieses Pakets.
- **Zementiert ist in DE der Regelfall** 📖 EPRD
  - EPRD-Jahresbericht 2025, Datenjahr 2024: 96,5 % der Knie-TEP zementiert, 1,9 % hybrid, 1,5 % zementfrei (Tab. 31). In der Schweiz 2024: 75,7 % vollzementiert (SIRIS S. 136). Registerzahl ist keine Vorgabe für den einzelnen Fall.
- **Fixation je Komponente klären** ⚠️ 📖 GON_K
  - Leitlinie: (teil-)zementierte und zementfreie Versorgung möglich, vergleichbare Ergebnisse (Empf. 76, ⇔). Hybrid heißt hier: Komponenten unterschiedlich fixiert – welche Komponente zementiert wird, ausdrücklich nachfragen. Heike leitet die Fixation nicht aus Alter oder Knochenqualität ab.
- **Kopplungsgrad / Insert-Typ laut OP-Plan** ⚠️ 📖 GON_K
  - CR (kreuzbanderhaltend), PS (posterior stabilisiert), UC/CS (ultrakongruent), MP/MC (medial pivot/medial congruent). Leitlinie: kreuzbanderhaltende und -resezierende Prothesen möglich (Empf. 75, ⇔). EPRD 2024 Standardprothesen: CR 40,6 %, PS 25,5 %, CR/CS 12,1 %, CS 10,8 %, Pivot 6,7 % (Tab. 30).
- **Patellarückflächenersatz ja/nein klären** ⚠️ 📖 GON_K
  - Leitlinie: Retropatellarersatz kann erfolgen (Empf. 77, ⇔). EPRD 2024: 11,0 % mit Retropatellarersatz (Tab. 35); SIRIS 2024: 43,2 % (S. 136). Entscheidung trifft der Operateur – Patella-Instrumente und -Implantat nur dann vorbereiten bzw. bereithalten.
- **Plattform fest oder mobil** ⚠️ 📖 EPRD
  - EPRD 2024: feste Plattform 92,9 %, mobile Plattform 7,1 % (Tab. 33). SIRIS 2024: mobile PE 16,4 % (S. 136). Systemabhängig – nicht jedes System bietet beides.
- **Navigation, PSI, Roboter nur als Variante** ⚠️ 📖 GON_K
  - Leitlinie: Navigation (Empf. 59), PSI (Empf. 60) und Roboter-Assistenz (Empf. 78) können verwendet werden (⇔). SIRIS 2019–2024: konventionell 67,2 %, PSI 18,1 %, Navigation 9,3 %, Roboter 6,0 % (Tab. 5.1, S. 135). Standard dieses Pakets ist konventionell.
- **Metallallergie abfragen** ⚠️ 📖 EMED
  - CoCrMo enthält geringe Anteile Nickel – Allergie präoperativ abfragen (Q_EMED). Leitlinie Empf. 61 (EK ⇑⇑): bei bestätigter Metallallergie Aufklärung und Abwägung; Standardimplantat mit Einverständnis möglich. Beschichtete Implantate (z. B. TiN, TiNbN, OxZr, ZrN) nur nach ärztlicher Entscheidung.
- **Tranexamsäure: ärztliche Entscheidung** ⚠️ 📖 GON_K
  - Leitlinie empfiehlt TXA ohne Kontraindikation (Empf. 74, ⇑⇑). Anordnung, Applikationsweg und Dosis ausschließlich ärztlich – Heike nennt keine Dosis.
- **Blutsperre: Entscheidung des Operateurs** — _nur blutsperre_ ⚠️ 📖 GON_K
  - Leitlinie: Blutsperre kann nach Nutzen-Risiko-Abwägung benutzt werden (Empf. 58a, ⇔); Dauer so kurz wie möglich (58b, ⇑). Für den Manschettendruck gibt die Literatur laut Leitlinie keine Empfehlung her (Langfassung S. 221).
- **OP-Dauer laut Hausplanung** *(optional)* ⚠️
  - Zeitbedarf aus lokaler Planung übernehmen; keine allgemeine Zeitgarantie.

## 2. Saal & Geräte `room`
- **OP-Tisch mit Knie-Lagerungszubehör** ⚠️
  - Seitenstütze, Fußstütze/Keil oder Beinhalter laut Hausausstattung und Tisch-IFU bereithalten; Details unter position.
- **Blutsperre: Oberschenkelmanschette passender Größe** — _nur blutsperre_ ⚠️ 📖 VBM
  - Manschettengröße passend zur Extremität wählen; vor Gebrauch Sicht- und Funktionskontrolle mit dem Blutsperregerät (Beispiel VBM Tourniquet Wipe Cuff, PDF-S. 5–6). Allgemeines zu Gerät und Manschette in 000; tatsächliche Geräte-/Manschetten-IFU des Hauses maßgeblich.
- **Jet-Lavage-Gerät** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Bei zementierten Komponenten wird vor dem Zementieren mit Jet-Lavage gereinigt (Q_EMED). Gerät, Akku/Energieversorgung und passendes Einmalset prüfen.
- **Vakuum-Zementmischsystem: Vakuumquelle prüfen** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Zwei-Komponenten-PMMA wird im Vakuumsystem angemischt, um Lufteinschlüsse zu vermeiden (Q_EMED). Anschluss/Pumpe passend zum Hausprodukt; Einmalset unter supplies.
- **Bildwandler nach Anordnung** *(optional)* ⚠️ 📖 EMED
  - Q_EMED beschreibt eine intraoperative Kontrolle und Dokumentation der Implantatlage mittels Bildwandler. Ob und wann: Operateur/Hausstandard. Strahlenschutz laut 000.
- **Navigationssystem: Kamera und Tower** — _nur navigation_ ⚠️
  - Gerät, Software-Fall, sterile Tracker und Zubehör laut Hersteller und Haus. Aufstellung im Saal mit Operateur und Hersteller-Einweisung abstimmen.
- **Robotersystem: Gerät, Kamera, sterile Abdeckungen** — _nur roboter_ ⚠️
  - Mako, ROSA, VELYS oder anderes System nur nach OP-Plan (Systemnamen laut Q_EMED). Planungsdaten, Einweisung, sterile Drapes und systemeigene Einmalartikel laut Hersteller-IFU und Haus.
- **Implantatvorrat bereitstellen** ⚠️
  - Femur, Tibia, Insert und ggf. Patella des geplanten Systems mit Größenreserve außerhalb des Sterilfelds. Femurkomponenten sind in den Implantat-Dateien links/rechts geführt – Seite am Etikett prüfen. Sterilverpackungen bis zur Anforderung geschlossen (Regel aus 000).
- **Systemsiebe/Leihsiebe rechtzeitig** ⚠️
  - Bei Leih- oder Systemsieben Lieferung, Vollständigkeit und Aufbereitung vor OP-Tag mit AEMP klären.

## 3. Lagerung `position`
- **Rückenlage** 📖 EMED
  - Standard für die primäre Knie-TEP mit medialem parapatellarem Zugang (Q_EMED). Abweichungen laut OP-Plan.
- **Seitenstütze und Keil/Fußstütze für ca. 90° Beugung** ⚠️ 📖 EMED
  - Wegen häufigem Wechsel zwischen Streckung und Beugung hat sich laut Q_EMED eine Seitenstütze plus Keil zur Aufstellung des Knies in 90°-Beugung bewährt. Konkretes Zubehör und Position laut Tisch-IFU und Operateur.
- **Beinhalter als Alternative** *(optional)* ⚠️
  - Statt Keil/Fußstütze ein Beinhalter-System, falls im Haus verwendet; Kompatibilität mit Tisch prüfen.
- **Bein frei zwischen Streckung und Beugung** ⚠️
  - Abdeckung und Lagerung so, dass das Bein intraoperativ voll gestreckt und gebeugt werden kann.
- **Blutsperrenmanschette proximal am Oberschenkel** — _nur blutsperre_ ⚠️ 📖 VBM
  - Dünn unterpolstern, Schlauch nach proximal (nicht ins OP-Feld), eng ohne Kraft anlegen – zwei Finger sollen zwischen Bein und Manschette passen (Beispiel VBM, PDF-S. 6). Persona-OP-Technik nennt eine proximale Oberschenkel-Blutsperre (Q_PERSONA, PDF-S. 6). Haus-IFU maßgeblich.
- **Gegenbein und Druckstellen** ⚠️
  - Polsterung und Druckstellenkontrolle laut 000; Seitenstütze nicht auf Druckstellen.

## 4. Desinfektion & Abdeckung `draping`
- **Extremitäten-Abdeckset Knie** ⚠️
  - Konkretes Set laut Haus; Bein beweglich lassen.
- **Fuß/Unterschenkel steril einpacken** ⚠️
  - Beinschlauch/Stockinette oder Fußsack laut Hausset; integrierte Bestandteile nicht doppelt als Material zählen.
- **Unterschenkelachse beurteilbar lassen** ⚠️ 📖 EMED
  - Bei extramedullärer Tibia-Ausrichtung so abdecken, dass die Unterschenkelachse beurteilt werden kann (Q_EMED).
- **Keine Flüssigkeit unter die Manschette** — _nur blutsperre_ 📖 VBM
  - Um chemische Verbrennung zu vermeiden, darf keine Flüssigkeit unter die Manschette gelangen (Q_VBM, PDF-S. 7). KRINKO: Ansammlungen von Hautantiseptikum vermeiden (Q_KRINKO). Manschette vor dem Abwaschen schützen, z. B. abkleben laut Haus.
- **Flüssigkeitsdichte Abdeckung bei Lavage** 📖 KRINKO
  - Wenn Durchfeuchten nicht auszuschließen ist (z. B. Jet-Lavage), flüssigkeitsundurchlässig abdecken (KRINKO Kat. IB).
- **Sterile Abdeckung für Navigation/Roboter** — _nur navigation, roboter_ ⚠️
  - Systemeigene sterile Drapes für Kamera-/Roboterarm laut Hersteller-IFU.

## 5. Siebe & Zusatzinstrumente `trays`
- **Knie-Grundsieb** ⚠️
  - Basisinstrumente, Haken/Hohmann-Hebel nach lokaler Siebliste; Bezeichnung mit AEMP abgleichen.
- **System-Instrumentarium des geplanten Implantats** ⚠️
  - Ausrichtung (intra-/extramedullär), Schnittblöcke, Größenlehren laut Hersteller-Siebliste. Nur Instrumente des geplanten Systems – Systeme nicht mischen.
- **Probekomponenten-Sieb** ⚠️
  - Probefemur, Probetibia, Probeinserts (Höhen/Typen) und ggf. Probepatella des geplanten Systems. Persona z. B. mit TASP-Probeaufbau aus Shims (Q_PERSONA, PDF-S. 44) – alle Shims mitzählen.
- **Patella-Instrumente** — _nur mit_patella_ ⚠️
  - Patella-Resektions-/Bohrlehre und Zementierzange laut System.
- **Säge-/Antriebsset** ⚠️
  - Oszillierende Säge und Bohrmaschine; Aufbereitung, Funktion, Ersatzakkus (000).
- **Zementierinstrumente** — _nur zementiert, hybrid_ ⚠️
  - Laut System und Hausstandard; Einmalartikel unter supplies.
- **Navigations-/Roboter-Instrumente** — _nur navigation, roboter_ ⚠️
  - Tracker, Pins, Pointer, systemeigene Schneidführungen laut System.
- **PSI-Schablonen** — _nur psi_ ⚠️
  - Patientenspezifische Schnittblöcke: Name, Geburtsdatum, Seite und Lieferung vor OP-Beginn prüfen; Aufbereitung/Sterilität laut Hersteller.
- **Höher gekoppeltes Insert / Stiel nach Absprache** *(optional)* ⚠️
  - Ob ein stärker gekoppeltes Insert (z. B. PS statt CR) oder ein Stiel in Reserve bereitliegt, entscheidet der Operateur. Persona: Operateur beurteilt, ob ein stärker gekoppeltes System nötig ist (Q_PERSONA, PDF-S. 5).

## 6. Material `supplies`
- 1 Stück **Skalpellklinge Haut** (Haut) ⚠️
  - Hautklinge als Vorschlag; Halterkompatibilität lokal bestätigen.
- 1 Stück **Reserveklinge** (Größe laut Haus) *(optional)* ⚠️
  - Eine passende Alternative wählen; nicht automatisch öffnen.
- Menge offen (Stück) – **Kompressen röntgenkontrastgestreift** (röntgenkontrastfähig) ⚠️
  - Zählmaterial; Menge laut Haus-Zählplan.
- Menge offen (Stück) – **Bauchtücher röntgenkontrastgestreift** (röntgenkontrastfähig) ⚠️
  - Zählmaterial; Menge laut Haus.
- Menge offen (Stück) – **Sägeblätter passend zu Schnittblock und Antrieb** (systemkompatibel) ⚠️ 📖 LEGION
  - Blattdicke/-breite systemabhängig – Hersteller führen Blattdicken für ihre Schnittblöcke (z. B. LEGION Spezifikation „Sawblade/Tibial Stylus Thickness“, Q_LEGION S. 12). Haus- und Systemartikel prüfen.
- 1 Stück **Ersatz-Sägeblatt steril verpackt** *(optional)* ⚠️
  - Ungeöffnet bereithalten.
- 1 Set **Absaugschlauch und Sauger** ⚠️
  - Laut Haus.
- 1 Stück **HF-Handgriff monopolar** ⚠️
  - Allgemeines zu HF/NE in 000.
- 1 Set **Jet-Lavage-Einmalset** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Vor dem Zementieren Jet-Lavage (Q_EMED); auch Persona-OP-Technik nennt Pulslavage vor dem Zementieren (Q_PERSONA, PDF-S. 47). Set passend zum Gerät.
- Menge offen (Liter) – **Spülflüssigkeit** ⚠️
  - Art und Menge laut Haus/Operateur.
- Menge offen (Set) – **Vakuum-Zementmischsystem** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Einmal-Mischset passend zum Zement und zur Vakuumquelle (Q_EMED). Anzahl laut Zementmenge.
- Menge offen (Stück) – **Zementapplikator/-spritze** — _nur zementiert, hybrid_ *(optional)* ⚠️
  - Nur falls laut Haus verwendet.
- **Blutsperre: Unterpolsterung** — _nur blutsperre_ ⚠️ 📖 VBM
  - Dünne Unterpolsterung unter der Manschette gegen Druckstellen und Hautverletzungen (Beispiel VBM, PDF-S. 6). Material laut Haus.
- **Blutsperre: Auswickelbinde** — _nur blutsperre_ *(optional)* ⚠️ 📖 VBM
  - Laut VBM-IFU muss vor dem Belüften die Blutentleerung der Extremität erfolgen (PDF-S. 6); Methode laut Operateur/Haus.
- 1 Stück **Redon-Drainage nur auf Anforderung** *(optional)* ⚠️ 📖 GON_K
  - Leitlinie empfiehlt, auf eine Drainage zu verzichten (Empf. 57, ⇓⇓); in begründeten Fällen kann eine Drainage gelegt werden (Langfassung S. 216). Nicht standardmäßig öffnen.
- 1 Stück **Drainage-Auffangsystem** *(optional)* ⚠️
  - Nur zusammen mit angeforderter Drainage.
- Menge offen (Stück) – **Spritzen/Kanülen für LIA** *(optional)* ⚠️
  - Nur wenn LIA angeordnet; Spritzengröße/Kanülen laut Haus. Medikamente unter implants.
- 1 Stück **Hautklammergerät** *(optional)* ⚠️
  - Alternative zum Nahtverschluss; eine Variante wählen.
- 1 Stück **Hautkleber** *(optional)* ⚠️
  - Optional laut Haus.
- Menge offen (Stück) – **Sterile Schalen** ⚠️
  - Für Spülung, Zement-Zubehör, Probeteile; Anzahl laut Haus.
- Menge offen (Stück) – **Elastische Binde zum Wickeln** ⚠️ 📖 EMED
  - Q_EMED nennt das Wickeln des Beins nach Hautnaht (Blutsperre-Öffnung danach möglich). Material laut Haus.

## 7. Nahtmaterial `sutures`
- Menge offen (Packungen) – **Kapsel/Retinakulum: Einzelknopfnähte** (Stärke/Nadel offen) ⚠️ 📖 EMED · Schicht: Kapsel/Retinakulum
  - Q_EMED beschreibt den Kapselverschluss in Einzelknopftechnik. Material, Stärke, Nadel und Anzahl offen – Hausartikel und Operateur.
- Menge offen (Packungen) – **Kapsel: zusätzliche fortlaufende Naht bei intraartikulärer LIA** (Stärke/Nadel offen) *(optional)* ⚠️ 📖 EMED · Schicht: Kapsel/Retinakulum
  - Laut Q_EMED soll bei intraartikulärer LIA zusätzlich fortlaufend verschlossen werden. Material/Stärke offen.
- Menge offen (Packungen) – **Kapsel: Widerhakennaht** (Stärke/Nadel offen) *(optional)* ⚠️ · Schicht: Kapsel/Retinakulum
  - Produktabhängige Alternative; nur nach Operateur.
- Menge offen (Packungen) – **Subkutan** (Stärke/Nadel offen) ⚠️ · Schicht: Subkutan
  - Stärke und Nadel laut Haus.
- Menge offen (Packungen) – **Haut: intrakutan oder Einzelknopf** (Stärke/Nadel offen) *(optional)* ⚠️ · Schicht: Haut
  - Eine Variante auswählen; Alternative Klammern (supplies).
- Menge offen (Packungen) – **Drainage-Fixationsnaht** (Stärke/Nadel offen) *(optional)* ⚠️ · Schicht: Haut
  - Nur bei angeforderter Drainage.

## 8. Implantate, Zement & Medikamente `implants`
- **Femurkomponente** ⚠️
  - System, Typ (CR/PS …), Fixation, Seite (L/R) und bestätigte Größe laut OP-Plan. Keine Standardgröße.
- **Tibiakomponente (Tibiaplateau)** ⚠️
  - Fixation, Plattform (fest/mobil) und Größe laut OP-Plan; manche Systeme mit Stiel-Option.
- **Tibia-Insert (PE-Gleitfläche)** ⚠️
  - Typ passend zur Femurkomponente (CR/PS/UC/MP), Größe und Höhe nach Probephase. Kombination laut Kompatibilitätstabelle des Systems (implantate/*-knie). Persona: ein Insert nur einmal einsetzen, nie erneut auf eine Tibia setzen (Q_PERSONA, PDF-S. 48).
- **Patellakomponente** — _nur mit_patella_ ⚠️
  - Nur bei Patellarückflächenersatz; Größe nach Probe. Größenfreigabe systemabhängig (z. B. ATTUNE: 29 mm nur Femur 1–3, Q_ATTUNE PDF-S. 132).
- **Probe- vs. Originalimplantat trennen** ⚠️
  - Probeteile nicht implantieren; Original erst nach Probephase auf Ansage öffnen (000). Probeinsert und Originalinsert: Typ, Größe und Höhe abgleichen.
- **Knochenzement (PMMA) laut OP-Plan** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Produkt, Antibiotikazusatz und Packungszahl ärztlich/hausabhängig; dem Zement können Antibiotika beigemengt sein (Q_EMED). Menge systemabhängig – Persona-OP-Technik empfiehlt bei zementierten Komponenten zwei Zementportionen (Q_PERSONA, PDF-S. 47). Keine Mischzeiten von Heike; Hersteller-IFU des Zements.
- **Zement auch für Patella** — _nur mit_patella_ *(optional)* ⚠️ 📖 PERSONA
  - Bei zementierter Patella (z. B. Persona All-Poly-Patella nur zementiert, Q_PERSONA PDF-S. 4) Zementbedarf mit einplanen.
- **Stiel/Verlängerung nach Plan** *(optional)* ⚠️
  - Nur wenn vorgesehen (z. B. Persona Stemmed Tibia, GMK Stem Extension); Größe/Länge offen.
- **Tranexamsäure nach ärztlicher Anordnung** *(optional)* ⚠️ 📖 GON_K
  - Leitlinie Empf. 74 (⇑⇑). Applikation (i.v./topisch), Zeitpunkt und Dosis nur ärztlich; Heike nennt keine Dosis. Bei topischer Gabe Bereitstellung laut Anordnung.
- **LIA-Medikamente nach ärztlicher Anordnung** *(optional)* ⚠️ 📖 GON_K
  - Leitlinie empfiehlt LIA als Teil des Narkosekonzepts (Empf. 55/56, ⇑⇑). Mischung und Dosis nur ärztlich/Haus-SOP; Heike nennt keine Rezeptur.

## 9. Ablauf aus Springer-Sicht `workflow`
- **OP-Plan abgleichen** ⚠️
  - Seite, System, Fixation je Komponente, Kopplung (CR/PS/UC/MP), Plattform, Patella ja/nein, Technik (konventionell/Navigation/PSI/Roboter), Größenvorrat, Leihsiebe.
- **Blutsperre: Anlage und Belüften auf Ansage** — _nur blutsperre_ ⚠️ 📖 VBM
  - Ob Blutsperre, Druck und Zeitpunkt entscheidet der Operateur (Empf. 58). VBM-Beispiel: Platzierung prüfen, Blutentleerung vor Belüften, niedrigst notwendiger Druck, arterieller Fluss gestoppt (PDF-S. 6–7). Persona-Beispiel: Belüften bei hyperflektiertem Knie (Q_PERSONA PDF-S. 6). Heike nennt keine Druckwerte.
- **Blutsperre: Zeit im Blick** — _nur blutsperre_ ⚠️ 📖 GON_K
  - Dauer so kurz wie möglich (Empf. 58b). Herstellerbeispiel VBM: Dauer im Ermessen des Arztes, üblicherweise max. 2 Stunden empfohlen (produktspezifisch, PDF-S. 6). Ansage und Dokumentation der Zeit laut 000.
- **Blutsperre öffnen: Zeitpunkt erfragen** — _nur blutsperre_ ⚠️ 📖 EMED
  - Laut Q_EMED entweder vor vollständigem Kapselverschluss (Blutungskontrolle) oder nach Hautnaht und Wickeln. Öffnungszeit dokumentieren.
- **Probephase begleiten** ⚠️
  - Probeteile in Typ/Größe/Höhe bereithalten und nach Gebrauch zurückführen (000). Gewählte Probegrößen für alle Komponenten notieren.
- **Kompatibilität vor dem Öffnen prüfen** ⚠️ 📖 PERSONA
  - Persona: vor dem Implantieren prüfen, dass alle Komponenten kompatibel sind (Q_PERSONA PDF-S. 47). Tabellen je System in implantate/*-knie.json.
- **Implantat-Anreichen im Vier-Augen-Prinzip** ⚠️
  - Vor dem Öffnen Komponente, Seite, Größe, Typ (CR/PS …), Insert-Höhe, Fixation und Verfall laut ansagen und vom Operateur am Etikett bestätigen lassen. Grundregel in 000.
- **Jet-Lavage vor dem Zementieren** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Laut Q_EMED vor dem Zementieren und erneut nach Entfernen des Zementüberschusses. Lavage-Set rechtzeitig bereit.
- **Zement im Vakuumsystem auf Ansage anmischen** — _nur zementiert, hybrid_ ⚠️ 📖 EMED
  - Vakuummischung gegen Lufteinschlüsse (Q_EMED). Anmischen nur auf Ansage, Zeiten nach Zement-IFU (000). Anästhesie vor Zement informieren (000; Q_BCIS).
- **Reihenfolge der Komponenten erfragen** ⚠️ 📖 PERSONA
  - Systemabhängig (z. B. Persona: bei CR-Femur Tibia zuerst, bei PS-Femur Femur zuerst, Q_PERSONA PDF-S. 49). Reihenfolge beim Operateur erfragen und Komponenten in dieser Reihenfolge bereithalten.
- **Bildwandlerkontrolle nach Anordnung** *(optional)* ⚠️ 📖 EMED
  - Optionale intraoperative Kontrolle der Implantatlage (Q_EMED).
- **Etiketten aller Komponenten sichern** ⚠️
  - Femur, Tibia, Insert, ggf. Patella, Zement: Etiketten in OP-Doku/Implantatpass laut 000 und Haus.
- **Navigation/Roboter: Ablauf mit Team** — _nur navigation, roboter_ ⚠️
  - Hochfahren, Registrierung, Tracker-Pins und Zubehör laut Hersteller und Operateur; Springer-Aufgaben vorab klären.
- **Verschlussmaterial abstimmen** ⚠️
  - Naht/Klammern, Drainage ja/nein, Verband nach Anforderung bereitstellen.

## 10. Zählkontrolle & Dokumentation `count`
- **Probekomponenten vollständig zurück** ⚠️
  - Probefemur, -tibia, -inserts, Shims/Spacer, Probepatella: Anzahl vor Kapselverschluss prüfen. Grundregel in 000.
- **Pins und Bohrdrähte zählen** ⚠️
  - Schnittblock-Pins und ggf. Tracker-Pins: Anzahl ein/aus laut Haus-Zählplan.
- **Sägeblätter auf Vollständigkeit prüfen** ⚠️
  - Blätter nach Gebrauch auf Bruchstücke prüfen.
- **Implantatstatus gesondert erfassen** ⚠️
  - Implantierte Komponenten (inkl. Patella, Zement) dokumentieren; nicht als zurückzuholendes Material behandeln.
- **Blutsperre dokumentieren** — _nur blutsperre_ ⚠️
  - Zeiten (Anlage/Öffnen) laut 000; Druck und Manschettenlage laut Hausformular.

## 11. Verband & Ausleitung `dressing`
- **Blutsperre vollständig ablassen und entfernen** — _nur blutsperre_ 📖 VBM
  - Manschette nach Anwendung vollständig entlüften und mit Unterpolsterung sofort entfernen – Risiko venöser Stauung (Q_VBM PDF-S. 7).
- **Steriler Wundverband** ⚠️ 📖 EMED
  - Erster Verbandwechsel laut Q_EMED (mit Bezug auf KRINKO 2018) nach 48 h, sofern keine Komplikation früher erfordert. Verbandprodukt laut Haus.
- **Wickeln des Beins** *(optional)* ⚠️
  - Elastische Wickelung laut Haus/Operateur (Q_EMED erwähnt Wickeln).
- **Drainage: Klemmstatus übergeben** *(optional)* ⚠️ 📖 EMED
  - Bei LIA laut Q_EMED Drainage 1–2 h geschlossen lassen, danach öffnen. Nur bei angeforderter Drainage.
- **Knie-bezogene Übergabe** ⚠️
  - Blutsperrenzeit, Drainage ja/nein (Klemmstatus), LIA ja/nein, TXA laut Anästhesie-Doku, Patella ja/nein, implantiertes System. Allgemeine Übergabe in 000.
- **Lagerung/Schiene nach Anordnung** *(optional)* ⚠️
  - Keine allgemeinen Winkel- oder Lagerungsvorgaben von Heike.

## 12. Typische Fehler & Fallstricke `pitfalls`
- **Desinfektionsmittel unter der Manschette** — _nur blutsperre_ 📖 VBM
  - Flüssigkeit unter der Manschette kann zu chemischer Verbrennung führen (Q_VBM PDF-S. 7); Antiseptikum-Ansammlungen vermeiden (Q_KRINKO).
- **CR- und PS-Komponenten verwechseln** 📖 PERSONA
  - Persona: PS-Femur nicht mit CR-, MC- oder UC-Insert; CR-Femur nicht mit PS- oder CPS-Insert (Q_PERSONA PDF-S. 5). Triathlon: CR-Femur nicht mit PS-/PSR-/TS-Insert (Q_TRIATHLON S. 2). Typ am Etikett prüfen.
- **Systeme nicht mischen** 📖 ATTUNE
  - ATTUNE: Implantate und Probeteile anderer Hersteller/Systeme nie zusammen verwenden (Q_ATTUNE PDF-S. 132). Registerbefunde zu Mischkombinationen (EPRD S. 60) sind keine Freigabe.
- **REF-Suffix beachten** 📖 TRIATHLON
  - Triathlon: Kompatibilitätstabelle gilt für X3-Inserts mit REF-Endung „E“ (Q_TRIATHLON S. 2). Andere Inserts beim Hersteller klären.
- **Zementfreie Komponente nicht zementieren** 📖 TRIATHLON
  - Triathlon: zementfreie Femurkomponenten nicht mit Zement verwenden (Q_TRIATHLON S. 2). Fixationsfreigabe je System im Etikett/IFU prüfen.
- **Insert nicht wiederverwenden** ⚠️ 📖 PERSONA
  - Persona: ein Insert nur einmal einsetzen (Q_PERSONA PDF-S. 48). Herausgenommenes Original-Insert nicht erneut verwenden; Ersatz klären.
- **Seite der Femurkomponente** ⚠️
  - Femurkomponenten der ausgewählten Systeme sind seitenspezifisch (L/R) geführt; Seite am Etikett mit OP-Seite abgleichen.
- **PSI-Schablone falscher Patient/Seite** — _nur psi_ ⚠️
  - Patientendaten und Seite der Schablone vor Gebrauch prüfen.
- **Keine Dosen und Gerätewerte von Heike** ⚠️
  - TXA, LIA, Antibiotika, Blutsperrendruck und Zement-Mischzeiten nur nach ärztlicher Anordnung bzw. Produkt-IFU.

## 13. Fotos `photos`
- **Foto: Lagerung mit Seitenstütze/Fußstütze ohne Patient** *(optional)* ⚠️
  - Aufbau am leeren Tisch. Nur freigegebene eigene Bilder ohne Personen/Identifikatoren; Platzhalter, kein Bild enthalten.
- **Foto: Blutsperrenmanschette am Modell** — _nur blutsperre_ *(optional)* ⚠️
  - Lage, Unterpolsterung, Schlauchrichtung. Nur eigene freigegebene Bilder; Platzhalter.
- **Foto: Abdeckaufbau am Modell** *(optional)* ⚠️
  - Hausset am Modell. Nur eigene freigegebene Bilder; Platzhalter.
- **Foto: Systemsiebe** *(optional)* ⚠️
  - Haus-/Systembezeichnung; keine Herstellerbilder übernehmen. Platzhalter.
- **Foto: Ablage Probe- vs. Originalimplantate** *(optional)* ⚠️
  - Eigene Fotos ohne Patientendaten; keine Herstellerbilder. Platzhalter.
- **Foto: Zementplatz mit Vakuummischsystem** — _nur zementiert, hybrid_ *(optional)* ⚠️
  - Nur nach Hausregeln. Platzhalter.
- **Foto: Verband am Modell** *(optional)* ⚠️
  - Optionaler Hausaufbau ohne Patient. Platzhalter.

## Heike darf sagen
- „Welche Fixation, welcher Insert-Typ und Patella ja oder nein? Davon hängen Siebe, Implantate und Zement ab.“ 📖 GON_K
- „Blutsperre? Manschette dünn unterpolstern, Schlauch nach oben – und keine Desinfektionslösung drunterlaufen lassen.“ 📖 VBM
- „Seitenstütze und Fußkeil für die 90°-Beugung bereit?“ 📖 EMED
- „Zementiert? Jet-Lavage und Vakuummischer vorbereiten, Anästhesie vor dem Zement informieren.“ 📖 EMED
- „CR und PS nicht verwechseln – Femur und Insert müssen laut Tabelle zusammenpassen.“ 📖 PERSONA
- „Implantat erst auf Ansage öffnen: Komponente, Seite, Größe, Typ, Höhe laut wiederholen.“
- „Drainage nur, wenn der Operateur sie ausdrücklich will.“ 📖 GON_K
- „Tranexamsäure und LIA: ärztliche Anordnung – ich nenne keine Dosis.“
- „Probeteile, Shims und Pins vor dem Kapselverschluss vollständig?“

## Abschluss-Check (typische Lücken)
- Fixation je Komponente, Kopplung und Patella ja/nein
- Passende System- und Leihsiebe, Antriebe, Ersatzakkus
- Seitenstütze/Fußstütze bzw. Beinhalter
- Blutsperre: Manschettengröße, Unterpolsterung, Schutz vor Flüssigkeit
- Jet-Lavage und Vakuum-Zementmischsystem
- Insert-Höhen und Probeteile vollständig
- Implantat-Etiketten aller Komponenten
- Drainage ja/nein und LIA ja/nein

## Regeln für die App
- Ich bin Heike, eine KI-Assistentin für OP-Vorbereitung. Ich habe keine eigene klinische Berufserfahrung.
- Diese Einträge sind auswählbare Vorschläge; weder optional=false noch belegt bedeutet automatische Auswahl oder klinische Freigabe.
- Zuerst Fixation, Kopplung, Patella und Technik klären. gilt_fuer enthält kanonische Varianten-IDs oder Situations-IDs aus 000 (z. B. blutsperre); mehrere IDs bedeuten ODER. alle steht allein.
- Belegt kennzeichnet die konkrete Quellenstütze, nicht die Freigabe für jedes Haus. Herstellerbeispiele gelten nur für das genannte Produkt.
- Eigene bestätigte Angaben haben Vorrang bei Hausdetails. Widersprüche zu Sicherheitsinformationen sichtbar klären, nicht still überschreiben.
- Keine Dosen (TXA, LIA, Antibiotika), keine Blutsperrendrücke, keine Zement-Mischzeiten und keine Implantatgrößen vorschlagen.
- Implantat-Kompatibilität nur aus implantate/*-knie.json des jeweiligen Systems; keine transitiven Freigaben, keine Systemmischung.

## Aus 000 übernommen (hier nicht wiederholt)
- Sign-in/Time-out/Sign-out
- Zählumfang, Zeitpunkte, Vier-Augen, Differenz-Stopp
- Seitenmarkierung sichtbar
- Inzisionsfolie, Hautantiseptik
- Blutsperren-Gerät + Manschette; Blutsperrenzeit ansagen + dokumentieren
- Implantat erst auf Ansage öffnen; Verpackung/Verfall prüfen; Etiketten in Doku; Implantatpass laut Haus
- Größenvorrat vorab prüfen; Probekomponenten zurückführen
- Zement: Anästhesie informieren, Zement nach IFU, Ansage rückbestätigen, Mischen nur auf Ansage, Überschuss prüfen
- Druckstellen gepolstert, NE-Ort, Antriebe und Ersatzakkus, Doppelhandschuhe
- Regeln: keine Dosen/Mischzeiten/HF-Werte/Implantatgrößen

## Julian bitte prüfen
- [ ] Scope primäre bikondyläre Knie-TEP bestätigen (keine Schlitten-/Revisionsprothesen).
- [ ] Hausstandard Blutsperre: Gerät, Manschette, Dokumentation, wer belüftet/öffnet.
- [ ] Lagerungszubehör (Seitenstütze, Fußstütze/Keil, Beinhalter) und Abdeckset benennen.
- [ ] Haus-Systeme Knie (welche der sechs Dateien; weitere wie SIGMA, Vanguard, NexGen, balanSys?).
- [ ] Zement: Produkt, Antibiotikazusatz, Packungszahl, Vakuummischsystem und Jet-Lavage-Set.
- [ ] Naht je Schicht (Kapsel, Subkutan, Haut): Material, Stärke, Nadel, Anzahl.
- [ ] Drainage-, LIA- und TXA-Praxis im Haus (nur Ablauf, keine Dosen in Heike).
- [ ] Navigation/Roboter/PSI im Haus vorhanden? Welche Systeme?
- [ ] Zählplan: Probeteile, Shims, Pins, Sägeblätter.

## Änderungen
- **v1.0** (2026-10-08): Neuanlage 002 mit 13 Abschnitten; Neue Implantat-Dateien für 6 Knie-Systeme. Grundlage: Auftrag Julian („Erstelle Datei für knie tep also 002 ausführlich“); eigene Recherche Grok; Struktur nach 001 v1.3. Cloud-/Julian-Prüfung ausstehend.

## Offene Punkte / nicht belegt
_Stand der Einträge: 119 Einträge in 13 Abschnitten · belegt 50 · üblich 0 · hausabhängig 69. „Belegt“ heißt: Aussage im Original nachgelesen – nicht: für jedes Haus freigegeben._

- Status: Neuanlage, klinischer Entwurf; keine Freigabe durch Julian, keine Cloud-Prüfrunde.
- Keine Quelle belegt Vorratsmengen, Nahtmaterial (Stärke/Nadel) oder Sieb-Inhalte als allgemeinen Knie-TEP-Standard – alles hausabhängig.
- Keine Geräte-IFU für das Blutsperregerät, keine Zement-IFU und keine Jet-Lavage-IFU des Hauses gelesen. VBM-Manschette nur als Produktbeispiel.
- Blutsperrendruck: laut Leitlinie keine Empfehlung aus Literatur ableitbar – bewusst offen.
- BCIS-Bezug nur allgemein (Heraeus-Factsheet); keine knie-spezifische Quelle gelesen.
- Navigation/Roboter: keine Hersteller-IFU von Mako, ROSA oder VELYS gelesen; nur Systemnamen aus Q_EMED.
- Österreich: kein aktuelles Implantat-Ranking gefunden (nur BMSGPK-Bericht 2018).
- Implantat-Originale teils US-Fassungen bzw. alt (ATTUNE US Rev. K 2022, LEGION US 2015) oder Drittanbieter-Kopie (Columbus 2014); EU-IFUs nicht gelesen.
- Keine Bilder enthalten.
- **Nicht belegt (bewusst hausabhängig):** alle Mengen, Siebnamen, Nahtmaterial (Stärke/Nadel/Anzahl), Verbandprodukte, Lagerungszubehör-Produkte, Navigations-/Roboter-Abläufe, PSI-Abläufe, Zählplan-Details.
- **Bewusst nicht aufgenommen:** Dosen (TXA, LIA, Antibiotika), Blutsperrendruck, Zement-Misch-/Aushärtezeiten, Implantatgrößen-Vorschläge, OP-Technik-Schritte des Operateurs.

## Quellenliste
- **GON_K** – S3-Leitlinie Prävention und Therapie der Gonarthrose – Kurzfassung (AWMF-Reg.-Nr. 187-050), Version 5.0, DGOU/DGOOC u. a. (AWMF). Überarbeitung 2024/07/12. S. 14–15: Empf. 55/56 (Narkose + LIA ⇑⇑), 57 (Drainage verzichten ⇓⇓), 58 (Blutsperre a ⇔, b Dauer kurz ⇑); S. 16: Empf. 59 Navigation, 60 PSI, 61 Metallallergie; S. 18: Empf. 74 TXA ⇑⇑ (Dosisangaben im Original bewusst nicht übernommen); S. 19: Empf. 75 CR/PS, 76 zementiert/zementfrei, 77 Retropatellarersatz, 78 Roboter (alle ⇔). https://register.awmf.org/assets/guidelines/187-050k_S3_Gonarthrose_2025-05.pdf (abgerufen 2026-10-07; PDF heruntergeladen, Empfehlungstexte im Original gelesen am 2026-10-07/08 (Grok).)
- **GON_L** – S3-Leitlinie Prävention und Therapie der Gonarthrose – Langfassung (187-050), Version 5.0, DGOU/DGOOC u. a. (AWMF). S. 215–216 Drainage („In begründeten Fällen kann eine Drainage gelegt werden“); S. 219–221 Blutsperre (Höhe: keine Empfehlung aus Literatur ableitbar, S. 221). https://register.awmf.org/assets/guidelines/187-050l_S3_Gonarthrose_2025-05.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-07.)
- **EMED** – Knieendoprothetik (eMedpedia Orthopädie und Unfallchirurgie), Springer Medizin; Goedecke E, Engelhardt M, Haaker R. Publiziert 08.07.2024. Abschnitte: Versorgungsmöglichkeiten; Zugangsweg (medial parapatellar); Lagerung und Blutsperre (Seitenstütze + Keil 90°, Blutsperre Operateursentscheidung, Abdeckung Unterschenkelachse); OP-Schritte (Jet-Lavage, Einzelknopf-Kapselnaht, fortlaufend bei LIA, Öffnen der Blutsperre); Materialien (Nickel abfragen, Beschichtungen); Zementiert oder zementfrei (Vakuummischung, Jet-Lavage, Antibiotika im Zement); Nachbehandlung (Bildwandler intraoperativ, Drainage bei LIA 1–2 h geschlossen, erster Verbandwechsel nach 48 h mit Bezug KRINKO 2018). https://www.springermedizin.de/emedpedia/detail/orthopaedie-und-unfallchirurgie/knieendoprothetik?epediaDoi=10.1007%2F978-3-642-54673-0_321 (abgerufen 2026-10-08; Volltext online gelesen am 2026-10-08 (Grok).)
- **VBM** – Tourniquet Wipe Cuff – Gebrauchsanweisung 004-01-0349, VBM Medizintechnik GmbH. Rev. 02/2024-05, deutscher Teil PDF-S. 5–7: Manschettengröße, Sicht-/Funktionskontrolle, Dauer im Ermessen des Arztes (üblicherweise max. 2 h empfohlen), dünn unterpolstern, Schlauch nach proximal, zwei Finger, Blutentleerung vor Belüften, niedrigst notwendiger Druck, keine Flüssigkeit unter die Manschette, nach Gebrauch vollständig entlüften und sofort entfernen. Produktspezifisch – ersetzt nicht die Haus-IFU. https://ifu.vbm-medical.de/ifudocs/004-01-0349%20Tourniquet%20Wipe%20Cuff%2002_2024-05_online.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-07/08.)
- **KRINKO** – Prävention postoperativer Wundinfektionen, KRINKO am RKI. 2018, Bundesgesundheitsblatt 61:448–473, gedruckte S. 461 (PDF-S. 14), Abschnitt 4.1: Hautantiseptikum-Ansammlungen (Kat. II); flüssigkeitsundurchlässige Abdeckung bei nicht ausschließbarem Durchfeuchten (Kat. IB). https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf?isAllowed=y&sequence=1 (abgerufen 2026-10-07; Aus Paket 001 übernommen (dort von Astra am 07.10.2026 geprüft).)
- **BCIS** – Factsheet Implantationssyndrom / BCIS, Heraeus Medical (PALACADEMY). PDF S. 1: Kommunikation und chirurgische Vorsorge. Nicht knie-spezifisch; kein Beleg für Mischzeiten oder Packungszahl. https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf (abgerufen 2026-10-06; Aus Paket 001 übernommen.)
- **EPRD** – EPRD Jahresbericht 2025, EPRD Deutsche Endoprothesenregister gGmbH. Status 5, 2025-10-28. Datenjahr 2024, gedruckte S. 48–50: Tab. 30 Kopplung, Tab. 31 Fixation, Tab. 33 Plattform, Tab. 35 Retropatellarersatz, Tab. 36/37 Material/Insert; S. 60 Mischkombinationen (Tab. 47/49). https://www.eprd.de/fileadmin/user_upload/Dateien/Publikationen/Berichte/Jahresbericht2025-Status5_2025-10-28_F.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-07.)
- **EPRD_XLSX** – EPRD Implantatergebnisse Knieversorgungen 2025 (Tabelle), EPRD. Kumulative Analysepopulation je Femur-/Tibia-System (kein Jahres-Marktanteil). Grundlage der Systemauswahl. https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Knieversorgungen.xlsx (abgerufen 2026-10-07; Datei ausgewertet (Grok) 2026-10-07.)
- **SIRIS** – SIRIS Report Hip and Knee 2025, SIRIS / ANQ / Stiftung SIRIS. Tab. 5.1 S. 135 (Technik, Kopplung 2019–2024); S. 136 (Fixation, Patella, mobile PE 2024); Tab. 5.8 S. 157 (häufigste TKA-Systeme 2024). https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-07. ANQ-Link mit JS-Sperre nicht abrufbar.)
- **PERSONA** – Persona The Personalized Knee – Surgical Technique, Zimmer Biomet. 3914.1-GLBL-en, Issue Date 2022-08. PDF-S. 4 Fixation; S. 5 Kopplungsregeln; S. 6 Blutsperre; S. 44 Insert-Höhen; S. 47–49 Implantation (Zement, Lavage, Reihenfolge, Insert einmalig); S. 70–71 Kompatibilität. Englisch, global. https://assets.ctfassets.net/rc4arfpyhdpw/6R1FpGyC07WTfcszrO2MKP/710ce1e70eb68bda7a449e07909f4859/persona-the-personalized-knee-surgical-technique1.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-08.)
- **TRIATHLON** – Triathlon Knee System – Surgical protocol compendium, Stryker. TRIATH-SP-30_Rev-1_29865, © 2021. S. 2 Kompatibilität; S. 57–58 Implantat-REF (Schema mit X). https://www.stryker.com/content/dam/stryker/joint-replacement/training-and-education/orthopaedic-fellows-summit/resources/1--knees/3.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-08.)
- **ATTUNE** – ATTUNE Knee System – INTUITION Instruments Surgical Technique, DePuy Synthes. DSUS/JRC/0316/1437 Rev. K, © 2022 (US-Fassung). PDF-S. 2 Konfigurationen; S. 130 Kompatibilität; S. 132 Essential Product Information. https://p1.aprimocdn.net/jjamp/en/depuy-synthes/surgical-technique-guide/attune-knee-system-intuition-instruments-dsusjrc03161437.pdf (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-08. US-Dokument – kein EU-Ersatz.)
- **LEGION** – LEGION Total Knee System – Specification Guide and Product Catalog, Smith & Nephew. 02861 V1 02/15 (US). S. 12 Sägeblatt-/Stylusdicke, S. 21–25 Kompatibilität, S. 40–48 Katalog. https://smith-nephew.stylelabs.cloud/api/public/content/9b60b8ccb8d34736b556c9582336e376?download=true&v=e3edc939 (abgerufen 2026-10-07; PDF gelesen (Grok) 2026-10-08. US-Katalog 2015 – kein EU-Ersatz.)
- Implantat-Quellen je System: siehe `implantate/*-knie.json` (Feld `quellen`).
