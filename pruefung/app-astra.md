# Astra – App-Prüfung Hüft-Implantat-Auswahl

Stand: 07.10.2026. Geprüfter Branch: `main`, Commit `9af2f87e75e7d89f39e367d9c898f252b319d402`.

**Umsetzung/Abnahme blockiert: Ziel-App fehlt im angegebenen Repository.** Keine App implementiert, kein Build, kein UI-Lauf und kein Publish durchgeführt. Dieser Bericht ist keine klinische Freigabe.

## Gelesen und angesehen

- `README.md`, `pruefung/STATUS.json`, `PRUEFAUFTRAG.md`.
- `app/hueft-implantat-auswahl.md` vollständig; alle sieben PNG-Mockups einzeln visuell angesehen.
- `implantate/LIESMICH.md` und sämtliche vier Implantat-JSON-Dateien vollständig.
- `pakete/001-abschluss.md`: Fundstellen für den in der Vorgabe verlangten Zement-Schritt und `heike_hinweise` abgeglichen; nicht als zusätzliche App-Datenquelle verwendet.
- Vollständiger Git-Dateibaum: unter `app/` liegen ausschließlich die Vorgabe und die sieben Bilder. Kein App-Einstieg, Router, Quellcode, Buildmanifest oder Integrationspfad vorhanden. Kein `AGENTS.md` vorhanden.

## Rückfragen und Verbesserungsvorschläge

| Nr. | Priorität | Befund | Konkrete Rückfrage / Vorschlag |
| --- | --- | --- | --- |
| A1 | hoch | Die vorhandene Heike-App ist im angegebenen Repo nicht enthalten und nicht verlinkt. Die Mockups allein bestimmen weder Zielplattform noch Integration. | Wo liegt die zu bearbeitende Heike-App: GitHub-Repo + Branch + Heike-Einstiegsdatei oder konkrete Base44-App-ID? Falls hier eine neue eigenständige App entstehen soll, dies als Ziel festlegen. Ohne Zielzuordnung keine Änderungen in anderen Kerlect-Repos und keine behauptete App-Integration. |
| A2 | hoch | User-Auftrag erlaubt Daten ausschließlich aus `implantate/*.json` und `STATUS.haus_systeme`. Die Vorgabe verlangt gleichzeitig Texte aus Paket 001 und einen Zement-Schritt daraus. Diese Inhalte fehlen in den zugelassenen Datenquellen. | Soll Claude die benötigten Hinweise in eine zugelassene JSON-Datenstruktur aufnehmen, oder wird Paket 001 ausdrücklich als weitere Laufzeitquelle zugelassen? Bis dahin keine klinischen Texte aus dem Paket fest im Code hinterlegen. |
| A3 | hoch | `regeln.pruefe` enthält natürliche Sprache und uneinheitliche Ausdrücke; Hausprodukte sind teilweise kommaseparierte Sammeltexte. Eine Datei umfasst mehrere Produktfamilien. Gleiche Datei darf daher keine automatische Kombinationsfreigabe bedeuten. | Stabile Komponenten-IDs, explizite Hauszuordnung und maschinenlesbare Regeln mit Quelle vorsehen. Beispielsweise Plasmafit Poly → zulässiges Inlay-Material; R3/REFLECTION → jeweils zugeordnete Inlays; Kopf-Ø/Offset → konkrete Wertepaare. Freitextregeln anzeigen, nicht als Code ausführen. Fehlende Paarung bleibt „offen – Operateur fragen“. |
| A4 | hoch | Alle 36 Komponenten haben aktuell `ref:null` und `gtin:null`. Eine verlässliche Identifizierung aus einem unbekannten Barcode ist damit nicht möglich. | Namenssuche gegen die Daten ist möglich. Unbekannten REF-/UDI-Scan als „nicht hinterlegt – keine Zuordnung möglich“ behandeln; keine Hersteller- oder Systemzuordnung raten. Beispiel: Isodur CoCr ist anhand des Namens einer anderen Datei zuordenbar, ein unbekannter Zahlencode nicht. |
| A5 | mittel | Rückrufe sind Produkttexte ohne Komponenten-IDs. Der VITELENE-Hinweis ist vorhanden, VITELENE aber nicht als Hauskomponente; ausdrücklich „nicht BIOLOX delta“. | Hinweise vollständig samt Produkt, Kennung, Link und Einschränkung anzeigen. Für gezielte Komponentenanzeige Datenzuordnung ergänzen; VITELENE nicht dem BIOLOX-delta-Inlay als betroffen zuordnen und nicht als auswählbare Komponente erfinden. Keine pauschale Sperre/Freigabe. |
| A6 | mittel | Mockup 6 zeigt ein grünes „passt“, obwohl andere Kompatibilitätsmerkmale noch offen sein können. Mockup 7 zeigt Beispielwerte und eine Seite, die nicht als Auswahl übernommen werden dürfen. | Zugehörigkeit zum System und belegte Kombination getrennt anzeigen. Beispielwerte wie Pfanne 52, Kopf 36/0 und Seite rechts nicht vorbelegen; Auswahl oder manuelle Etiketteingabe erforderlich. „Nicht verifiziert“ aus den Daten auf jedem Teil erhalten. |

## Abnahme-Liste – jeder Punkt geprüft

„Blockiert“ bedeutet: Anforderung und Datenstand geprüft, tatsächliches App-Verhalten mangels Ziel-App nicht getestet. Kein Punkt wird als bestanden ausgegeben.

| Nr. | Abnahmepunkt aus der Vorgabe | Ergebnis | Nachweis / noch auszuführender Test |
| --- | --- | --- | --- |
| 1 | Alle 7 Screens wie Mockups; Daten nur aus Implantat-JSON + Hausauswahl | **Blockiert** | Alle sieben Referenzbilder vorhanden und angesehen; kein ausführbarer Screen vorhanden. Nach Integration jeden Screen visuell prüfen, Datenzugriffe kontrollieren; A1/A2 klären. |
| 2 | Kein fremder Hersteller/System wählbar; Isodur bei Stryker → Screen 6 | **Blockiert** | Isodur CoCr steht in Aesculap-Datei, Stryker in separater Datei. UI-Test aus laufender Stryker-Auswahl mit Suche „Isodur CoCr“ und Prüfung, dass keine Übernahme angeboten wird, noch offen. |
| 3 | Fehlende Werte „noch nicht hinterlegt“, keine erfundene Zahl/REF | **Blockiert** | Alle 36 REF und GTIN fehlen. Stryker-Kopf-Ø/Offsets stehen strukturiert in der JSON; viele andere Werte nur als offene Fundstellen. UI muss echte Werte, fehlende Werte und manuelle Etiketteingaben unterscheiden; keine Mockup-Werte übernehmen. |
| 4 | „Steril anreichen“ erst nach vollständigem Ansage-Check | **Blockiert** | Kein Button/State vorhanden. Alle sechs Haken einzeln testen; mit jeweils einem fehlenden Haken deaktiviert, mit allen aktiviert. Nach Änderung des Teils oder seiner Größe/Offset den zugehörigen Check zurücksetzen. |
| 5 | Rückruf-Hinweise bei LFIT/BIOLOX delta V40, R3 und VITELENE; nur Hinweis | **Blockiert** | Entsprechende Meldungen liegen in den JSON vor (Stryker 4, S+N 3, Aesculap 1; zusätzlich Enovis 1). Anzeige, Quellenlink, korrekte Produkteinschränkung und fehlende pauschale Sperre noch nicht im UI getestet; A5 beachten. |
| 6 | Ergänzte JSON-Werte erscheinen ohne Codeänderung | **Blockiert** | Kein Datenloader vorhanden. Nach Integration Test mit isolierten Testdaten: neuen Wert/REF ergänzen, Daten neu laden, Anzeige prüfen; Original-JSON dabei unverändert lassen. Keine fest codierten Herstellerlisten, Größen oder REF. |

## Tatsächlich ausgeführte technische Prüfungen

- Vier Implantat-JSON-Dateien und STATUS erfolgreich als JSON gelesen.
- 36 Komponenten gezählt: Aesculap 9, Enovis 10, Smith+Nephew 11, Stryker 6.
- Alle vier Hersteller-Schlüssel in `haus_systeme` vorhanden.
- Alle vier Dateien haben `verified:false`.
- Alle nichtleeren Komponenten-`quelle`-IDs innerhalb ihrer jeweiligen Datei auflösbar. Das ist ein Strukturtest, keine fachliche Bestätigung der Quellen.
- Sieben PNG-Dateien vorhanden und visuell geöffnet.
- Kein Build-/UI-Ergebnis behauptet; kein Zugriff auf Patientendaten.

## Wissens-Prüflauf

000 v1.5 und 001 v1.3 sind abgeschlossen. Alte 001-Astra-Datei bereits gelöscht. Extra-Lauf `001-implantate` steht auf `grok`, Laufstart `2026-10-07T03:55Z`; `pruefung/001-implantate-grok.md` fehlt am geprüften Commit. Deshalb noch keine fachliche Astra-Prüfung dieses Laufs.

Ausschließlich diese eigene Datei angelegt. Vorgabe, Mockups, Wissensdaten und fremde Prüfdateien unverändert.
