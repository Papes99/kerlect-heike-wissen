# Änderungsvorschlag 001 Hüft-TEP v1.0 → v1.1 (07.10.2026)

**Bezug:** `eingang/2026-10-07-001-hueft-tep-grok.md` (Grok-Gegenprüfung, Commits 6190984 + a3d8ece) · `eingang/2026-10-07-julian-implantate-bestaetigung.md` · Implantat-Entwürfe `eingang/2026-10-07-implantate-*`
**Paket:** `pakete/001-hueft-tep` v1.0 · **Status:** offen – Paket ändert sich erst nach Julians Freigabe.

**Nachprüfung durch Claude:** Ich wollte Groks Quellen stichprobenartig nachlesen (Accolade-II-OP-Technik, POLARSTEM-IFU, KRINKO). Alle drei Server sind in meiner Umgebung gesperrt. Die Bewertung unten stützt sich deshalb auf Groks Zitate mit Seitenangabe und nicht auf eigenes Nachlesen.

**Ergebnis:** 7 übernehmen · 0 ablehnen · 3 keine Änderung nötig (schon so im Paket) · 4 Julian entscheidet

## Das ändere ich in Paket 001 (v1.0 → v1.1)

**Ändere ich nach „f“:**
- pitfalls · Alkoholansammlungen vermeiden: Quelle HEBU → **KRINKO 2018** (HEBU nur ergänzend). Grund: HEBU belegt es nicht.
- workflow · Anästhesie vor Zement informieren: „vor Zement“ → **„über jeden Zementierschritt“**. Grund: BCIS-Factsheet verlangt mehr.
- Heike-Satz: „Sag der Anästhesie vor dem Einbringen Bescheid“ → **„Anästhesie über jeden Zementierschritt informieren“**. Grund: wie oben.
- draping · Flüssigkeitsdichte Abdeckung: + **„bei erwartetem Durchfeuchten flüssigkeitsundurchlässig (Kat. IB)“**. Grund: KRINKO genauer.
- position · NE-Kontakt kontrollieren: + Hinweis **„IFU der Haus-NE maßgeblich, HEBU nur Beispiel“**. Grund: Marken-IFU ist keine allgemeine Regel.
- count · **neu: „Markraumstopper mitzählen“** (zementiert/hybrid, hausabhängig). Grund: belassenes Material dokumentieren.
- implants · Mathys: alle Werte bleiben **„offen“**. Grund: kein Herstellerdokument lesbar.

**Ändere ich erst nach deiner Antwort:**
- implants · **neu: „EU: keine Hemi mit Accolade II“**. Frage: Auf welchen Schaft kommt der Stryker-Duokopf? Z. B. *Accolade II*, *Accolade TMZF*, *Exeter* (zementiert), oder Hemi mit *Mathys Bipolarkopf auf twinSys*?
- implants · Stryker-Daten → neue Datei `implantate/stryker-accolade-ii.json` (Konus V40, 132°/127°, Köpfe je ⌀ mit Offsets, UHR 36–61 mm). Frage: Werte so freigeben?
- implants · POLARSTEM → `implantate/smith-nephew-polarstem-r3.json`. Frage: Ist dein Schaft z. B. *POLARSTEM*, *SL-PLUS* oder *ANTHOLOGY*?
- implants · Trident II / R3 / TANDEM: Größen bleiben offen. Frage: Was steht auf dem Etikett, z. B. *Trident II Clusterhole + X3* oder *R3 + XLPE + OXINIUM 32 mm*?

**Abgelehnt:** nichts. **Keine Änderung nötig:** Naht, Materialmengen und LINK-DAA stehen schon so im Paket.

## A. Belegte Zeilen (Grok)
11 bestätigt · 1 zu weit gefasst (Alkoholansammlungen, Quelle HEBU → Nr. 1) · 0 nicht gefunden.
Kleine Abweichung: Grok nennt für die KRINKO-Abdeckung **S. 460**, im Paket steht **S. 461**. Beim Einbau bitte die Seite am PDF prüfen.

## B. Punkte
| Nr | Abschnitt | Eintrag | Groks Vorschlag | Entscheidung | Grund |
|---|---|---|---|---|---|
| 1 | pitfalls | Alkoholansammlungen vermeiden | Quelle auf KRINKO 2018 (Kat. II) umstellen, HEBU nur ergänzend für Brand/NE | **übernehmen** | Sicherheitsrelevant. HEBU allein belegt die Aussage nicht so, KRINKO schon. |
| 2 | workflow | Anästhesie vor Zement informieren | spez: über **jeden Schritt** des Zementierens informieren | **übernehmen** | Das BCIS-Factsheet verlangt mehr als einmal „vor dem Einbringen“. |
| 3 | Heike | „Zementiert? Sag der Anästhesie …“ | „Zementiert? Anästhesie über jeden Zementierschritt informieren.“ | **übernehmen** | Gleicher Grund wie Nr. 2. |
| 4 | draping | Flüssigkeitsdichte Abdeckung | spez: bei erwartetem Durchfeuchten flüssigkeits**undurchlässig** (Kat. IB) | **übernehmen** | Genauer und deckt sich mit KRINKO. |
| 5 | position | NE-Kontakt kontrollieren | hinweis: die IFU der Neutralelektrode im Haus ist maßgeblich, HEBU nur Beispiel | **übernehmen** | Eine Marken-IFU soll nicht wie eine allgemeine Regel klingen. |
| 6 | count | neu: Markraumstopper mitzählen | Ergänzung, sicherheit „üblich“, hausabhängig, quelle null | **übernehmen** | Steht schon in Julians Prüfliste. Das APS-Prinzip „belassenes Material dokumentieren“ passt dazu. |
| 7 | sutures | Nadel offen → hausabhängig | – | **keine Änderung nötig** | Im JSON sind alle Nahteinträge schon „hausabhängig“ ohne Quelle. |
| 8 | supplies | Mengen → hausabhängig | – | **keine Änderung nötig** | Im JSON sind alle Materialeinträge schon „hausabhängig“ ohne Quelle. |
| 9 | trays | LINK-DAA-Beispiel | Hinweis beibehalten | **keine Änderung nötig** | Ist schon als herstellerspezifisch und optional markiert. |
| 10 | implants | neu: EU: keine Hemi mit Accolade II | Ergänzung, belegt (ACCII-SP-1 Rev-4, S. 3 + 12) | **Julian entscheidet – hoch** | Grok zufolge ist Accolade II in der EU **nicht** für die Hemiprothese (Duokopf) zugelassen. Dann passt die Haus-Kombi „Accolade + Duokopf“ nicht. → Frage 1 unten. |
| 11 | implants | Stryker-Daten (Konus V40, 132°/127°, Köpfe, UHR 36–61 mm) | neu `implantate/stryker-accolade-ii.json` | **Julian entscheidet** | Grok hat das Herstellerdokument nach eigener Angabe gelesen, ich konnte es nicht gegenprüfen. Mein Entwurf hatte die Offsets falsch: „−5 bis +7,5“ gilt nur für 36 mm. Groks Werte ersetzen meinen Entwurf. |
| 12 | implants | Smith+Nephew POLARSTEM (12/14, Ti/HA zementfrei, Edelstahl zementiert, CCD 135/126/145°) | neu `implantate/smith-nephew-polarstem-r3.json` | **Julian entscheidet** | Quelle ist die IFU 81098832 Rev. 2, von Grok gelesen. Zuerst bestätigen, dass POLARSTEM wirklich im Haus ist. → Frage 3 |
| 13 | implants | Mathys (alles) | offen | **übernehmen (als offen)** | Kein Herstellerdokument lesbar, weder für Grok noch für mich. |
| 14 | implants | Trident II, R3, TANDEM, OXINIUM: Größen | offen | **Julian entscheidet** | Wir brauchen OP-Technik oder Größentabelle. → Frage 2 und 4 |

## Fragen an Julian (mit Beispielen)
1. **Stryker-Duokopf: Auf welchen Schaft kommt er bei euch?** Zum Beispiel *Accolade II* (in der EU laut Grok nicht für Hemi), *Accolade TMZF* oder ein zementierter Schaft wie *Exeter*. Oder macht ihr Hemi mit einem anderen Hersteller, z. B. *Mathys Bipolarkopf auf twinSys*?
2. **Stryker-Pfanne:** z. B. *Trident II Tritanium Clusterhole* oder *Multihole*? Inlay z. B. *X3-PE* oder *Keramik*? Ein Foto vom Etikett reicht.
3. **Smith+Nephew-Schaft:** z. B. *POLARSTEM* (zementfrei/zementiert), *SL-PLUS* oder *ANTHOLOGY*?
4. **R3:** welches Inlay, z. B. *XLPE* oder *Keramik*? Welcher Kopf, z. B. *OXINIUM 32 mm* oder *BIOLOX delta 36 mm*?
5. **Mathys:** die Pfannennamen vom Etikett, z. B. *RM Pressfit vitamys* oder *seleXys PC*.

## Wie es nach deiner Freigabe weitergeht
- Ich lege `pakete/001-hueft-tep` **v1.1** an mit Punkt 1–6 und dem, was du bei 10–14 freigibst. In `pruefung/STATUS.json` kommt 001 v1.1 auf „offen“ zur Kontrolle.
- Implantat-Daten kommen als neue Dateien nach `implantate/`, und zwar nur mit `verified: true`, wenn das Herstellerdokument mit Seite angegeben ist.
