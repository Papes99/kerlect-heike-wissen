ÄNDERN
Astra – Lauf 2026-10-07T05:30Z

# 001-implantate-dach – Gegenprüfung

34 Prüfpunkte. Alle 21 Nummern des benannten Prüfumfangs einschließlich Grok-Nachtrag geprüft; offene Teilfragen bleiben ausdrücklich offen. Perspektive: OP-Pflege/OTA, Schwerpunkt Endoprothetik. Keine persönlichen Berufsqualifikationen und keine klinische Freigabe. Ranking-Auswahl ist nicht Hausbestand, technische Kompatibilität oder eine Versorgungsempfehlung.

## Lauf- und Quellenabgrenzung

Gelesen: README, STATUS, Basis-MD, Quellen-Auftrag, Grok einschließlich Nachtrag, Perplexity sowie die zu 001 gehörenden Implantatdaten und deren Schema. Eine `pakete/001-implantate-dach-basis.json` ist in diesem Lauf nicht vorhanden; keine Werte daraus angenommen. Eingriffsspezifische Befunde gehören zu 001/Implantaten, nicht nach 000.

Fälligkeit: lauf_start `2026-10-07T05:30Z`; Grok-Datei mit passender Laufkennung, letzter Datei-Commit `535768f1f89d26239c21a7582939c75e98ba5e7c`, Author/Committer `2026-10-07T06:16:12Z`. Astra-Datei zu Prüfungsbeginn und unmittelbar vor Schreiben nicht vorhanden, GitHub-Dateiverlauf leer. Eingabe-Blobs vor Schreiben erneut unverändert geprüft. STATUS-Blob `01466956c365eaab135e887d1da2e19bfa6c2b34`; Grok-Blob `6ed9e9f1e9458905b42e183312623085efcfd8bf`. Abgeschlossene Pakete 000, 001, 001-implantate: keine eigene Astra-Datei zum Löschen vorhanden.

Die Tabelle enthält direkt verwendbare Chiptexte. Quellen-IDs sind auf die am Ende vollständig ausgeschriebenen Originale aufgelöst; `quelle:null` kennzeichnet die jeweils fehlende Detailfreigabe, nicht das Fehlen jeder Hintergrundquelle. Implantatfelder wie `tabellen`, `groessen`, `passt_zu` und `rueckrufe.betrifft` sind in `spez` ausdrücklich zugeordnet. Mengen werden nicht aus Registerhäufigkeiten zu Stücklisten umgedeutet.

## Prüfung – Sicherheitsrelevantes zuerst

| Nr | Von (Grok bestätigt / Astra) | ok/Fehler | Problem | Endgültiger Text im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|---|
| 1 (Grok 17) | Astra | Fehler | Grok nennt 52/III und 54/III; Original benennt andere Größen. | `{"abschnitt":"Implantate","label":"Allofit-S Rückruf exakt","menge":null,"einheit":null,"spez":"rueckrufe: Allofit-S Alloclassic shell with polar screw plug: Größe 52/II, REF 4265, Lot 2984922; Größe 54/JJ, REF 4266, Lots 2984958 und 2984959. Kennung ZFA2019-00187. betrifft ausschließlich diese Schalen/Chargen; keine pauschale Allofit-Sperre und kein Abschlussnachweis.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fallofit"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fallofit](#quelle-fallofit): Zimmer Biomet ZFA2019-00187 / BfArM 10144-19, Allofit-S Alloclassic; 30.07.2019; PDF 1, Produkttabelle; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2019/10144-19_kundeninfo_en.pdf?__blob=publicationFile) | hoch |
| 2 (Grok 5,9) | Astra | Fehler | Die 13-mm-Grenze wird unzulässig auf alle CORAIL-Varianten übertragen. | `{"abschnitt":"Implantate","label":"Corail Kopfgrenze zuordnen","menge":null,"einheit":null,"spez":"Die Kopf-Offsetgrenze maximal 13 mm gehört in dieser EMEA-Technik zum Dysplasia-Schaft Größe 6; dort auch Hemiarthroplastik und Patientengewicht über 60 kg ausgeschlossen. DePuy-Synthes-12/14-Kopf gemäß konkreter Produktfreigabe verwenden. Keine allgemeine CORAIL-Grenze 13 mm und keine markenübergreifende Freigabe aus 12/14 ableiten. Vollständige Kopf-Ø/Offset-Matrix bleibt offen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["corail"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [corail](#quelle-corail): CORAIL Total Hip System Surgical Technique, 198918-211214 UK; ©2022; EMEA; S. 11,13,15,20–26/PDF 12,14,16,21–27; [Original](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf) | hoch |
| 3 (Grok 13) | Astra | Fehler | Ein einziges max_kopf_mm pro Schale ist falsch; +5-mm-Liner weicht ab. | `{"abschnitt":"Implantate","label":"G7 Liner bestimmt Kopfgröße","menge":null,"einheit":null,"spez":"tabellen: G7_PE_Matrix gemäß Anhang G7. Für 48/C mit +5-Lateralized kein 36-mm-Kopf, 52/E mit +5 kein 40-mm-Kopf, 58/60 G mit +5 kein 44-mm-Kopf in der Thickness-Tabelle belegt. Übersicht S. 3 ist hierfür zu grob. Kombination nur nach Schalen-Alpha, exaktem Liner, Kopfart, Ø und Herstellerfreigabe; Keramik, Freedom und Dual Mobility getrennt.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["g7"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [g7](#quelle-g7): G7 Acetabular System Surgical Technique, 2336.6-GLBL-en; 2026-09-09; S. 3–5/PDF 6–8; Keramik S. 7/PDF 10; [Original](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/g7-acetabular-system/2336.6-GLBL-en%20G7%20Acetabular%20System%20Surgical%20Technique.pdf) | hoch |
| 4 (Grok 15) | Astra | Fehler | 8/10 pauschal bei Alloclassic sowie EU-Freigabe allein aus Chart nicht belegt. | `{"abschnitt":"Implantate","label":"ZB Konus und Freigabe trennen","menge":null,"einheit":null,"spez":"passt_zu nur je genauer Zeile: Im Ceramic-Chart sind die dort benannten Alloclassic-Zeilen sowie Avenir/CLS/Fitmore bei BIOLOX delta 12/14 und OPTION 12/14 markiert, OPTION 8/10 dort nicht. Das ist keine Freigabe jedes Kopf-Ø/Offsets. Charts warnen ausdrücklich: funktionelle Kompatibilität bedeutet nicht zwingend regulatorische Zulassung. Markt/IFU und vollständige Artikelpaarung separat prüfen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["ceramic","cocr"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [ceramic](#quelle-ceramic): Head and Stem Combinations: Ceramic Femoral Heads; Revised 5/6/2019 (Originalschreibweise); PDF 1–3; insbesondere Zeilen Alloclassic/Avenir/CLS/Fitmore auf PDF 1 und Fußnoten; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/6LuflsxnuxzS6yod8Wbg5c/75d5c277cb99658423118798f590191e/Ceramic_Femoral_Heads_NEW.pdf)<br>[cocr](#quelle-cocr): Head and Stem Combinations: CoCr Femoral Heads; Revised 7/15/2020; PDF 1–3, produktspezifische Spalten und Fußnoten; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/iV1BfgVRHhLqYPmt2Zt2G/bc7ac72e2ad60e1eed7f7d9f5628fa51/CoCr-Femoral-Heads_NEW.pdf) | hoch |
| 5 (Grok 16) | Astra | Fehler | Chart ist keine pauschale regulatorische Schaft-Duokopf-Freigabe. | `{"abschnitt":"Implantate","label":"ZB Bipolar nicht transitiv","menge":null,"einheit":null,"spez":"MS-30-Zeile im Uni/Bipolar-Chart: AP 1946/1989 markiert; Multipolar nicht markiert. Fußnote 1 fordert zusätzlich Artikulations- und Kopf/Schaft-Tabellen. Diese Teilinformation als bedingt führen; innere Kopfgröße, Kopf-Schaft-Paar und EU-IFU vor Auswahl ergänzen. Fehlende Bestätigung bleibt offen, nicht automatisch verboten. Vollständige Duokopf-Kombination noch nicht freigegeben.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["bipolar"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [bipolar](#quelle-bipolar): Head and Stem Combinations: Unipolar and Bipolar Femoral Heads; Revised 5/6/2019 (Originalschreibweise); PDF 1–2, Zeile MS-30 auf PDF 2 und Fußnote 1; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/32LNW4qj9EF9gZTbsgW3XK/aff2b857d83db63fa9441c1d96e1237d/Unipolar_and_Bipolar_Femoral_Heads_NEW.pdf) | hoch |
| 6 (Grok 12) | Astra | Fehler | B Extended Größe 12 hat innerhalb derselben Originalausgabe zwei Offsetwerte. | `{"abschnitt":"Implantate","label":"Fitmore Offset widersprüchlich","menge":null,"einheit":null,"spez":"groessen: Fitmore B Extended Offset Größe 12, REF 01.00551.312: horizontaler Offset 50,0 mm in Sizing S. 14/PDF 16, 50,75 mm in Ordering S. 16/PDF 18. attribute.offset=null, sicherheit=offen; beide Fundstellen dokumentieren und Herstellerklärung verlangen. Keine selbst gewählte Rundung.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fitmore](#quelle-fitmore): Fitmore Hip Stem Surgical Technique, 1013.3-GLBL-en; 2025-04; S. 12–16/PDF 14–18; Bestelltabellen S. 16 ff.; [Original](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/fitmore/1013.3-GLBL-en%20Fitmore%20Hip%20Stem%20Surg%20Tech%20A4%20DIGITAL.pdf) | hoch |
| 7 (Grok 21) | Astra | Fehler | Offene Zuordnung im bestehenden Paket enthält eine falsche Liner-Angabe. | `{"abschnitt":"Implantate","label":"R3 Rückruf 2023: Schale","menge":null,"einheit":null,"spez":"rueckrufe R-2023-13: betrifft=[sn.r3.schale], nicht sn.r3.xlpe. R3 0 HOLE ACET SHELL 54MM, REF 71331854, Lot 23HM03659; Verpackung enthält irrtümlich eine 3-HOLE-Schale 54 mm. Betroffene Ware laut FSN lokalisieren/quarantänisieren/zurücksenden. Kein behördlicher Abschluss belegt.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fr2023"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fr2023](#quelle-fr2023): Smith+Nephew Dringender Sicherheitshinweis, R-2023-13 / BfArM 35762-23; 20.11.2023; PDF 1–2; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 8 (Grok 21) | Astra | Fehler | Schale/Liner-Zuordnung trotz verfügbarem Original offen gelassen. | `{"abschnitt":"Implantate","label":"R3 Rückruf 2020: Schale","menge":null,"einheit":null,"spez":"rueckrufe R-2020-04: betrifft=[sn.r3.schale]. Das EN-Arztschreiben bezeichnet R3 Acetabular Shells, bestimmte Chargen; Verriegelungsfehler kann PE-/Keramikliner betreffen, macht diese aber nicht zum rückgerufenen Produkt. Hersteller beschreibt betroffene Ware als bereits abgewickelt/zurückgenommen; das ist kein behördlicher Abschluss. REF-/Lot-Liste aus diesem Update nicht vollständig ableitbar: offen lassen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fr2020"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fr2020](#quelle-fr2020): Smith+Nephew Physician Communication, R-2020-04 / BfArM 05608-20; 2020; undatiertes Update im geöffneten PDF; PDF 1, Affected Product/Background/Actions; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2020/05608-20_kundeninfo_en.pdf?__blob=publicationFile&v=1) | hoch |
| 9 (Grok 11) | Grok bestätigt | ok | Grok-Nachtrag: exakte betroffene Ausführung selbst bestätigt. | `{"abschnitt":"Implantate","label":"Corail Rückruf 2018","menge":null,"einheit":null,"spez":"rueckrufe PIE-1104627: CORAIL cementless HA 12/14 AMT 135° Standard No Collar Size 12, REF 3L92512, Lot 5300693. Tatsächliche Größe 11, als 12 gekennzeichnet; nicht auf alle CORAIL-Schäfte ausweiten.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fcorail18"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fcorail18](#quelle-fcorail18): DePuy Urgent Field Safety Notice PIE-1104627 / BfArM 02257-18; Februar 2018; PDF 1–3; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2018/02257-18_kundeninfo_en.pdf?__blob=publicationFile) | hoch |
| 10 (Grok 11) | Astra | Fehler | Zwei einschlägige BfArM-Meldungen im 10-Jahresfenster fehlen. | `{"abschnitt":"Implantate","label":"Corail weitere Sicherheitsmeldungen","menge":null,"einheit":null,"spez":"rueckrufe PIE-863755 (2017): KLA collared 9 REF 3L93709/Lot 5291990 und HO collarless 14 REF L20314/Lot 5292130 vertauscht. PIE-1125109 (2018): CORAIL AMT Probehälse L94003–L94007, alle Chargen, Dichtungsringpartikel; Instrumentenkorrektur, kein Schaft-Rückruf. betrifft getrennt für Implantate und Probehals-Instrumente führen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fcorail17","ftrial"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fcorail17](#quelle-fcorail17): DePuy Sicherheitsinformation PIE-863755 / BfArM 07375-17; Juli 2017; PDF 1–3; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07375-17_kundeninfo_de.pdf?__blob=publicationFile)<br>[ftrial](#quelle-ftrial): DePuy Sicherheitsinformation PIE-1125109 / BfArM 06669-18; Mai 2018; PDF 1–2; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/06/2018/06669-18_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 11 (Grok 11) | Astra | Fehler | Nachtrag nennt FSN, aber die Reichweite muss in den Daten stehen. | `{"abschnitt":"Implantate","label":"Pinnacle FSN präzisieren","menge":null,"einheit":null,"spez":"rueckrufe Ref. 1896433: aktualisierte FSN 18.02.2021 ersetzt 17.12.2020; Gewindeproblem am Apex-Loch bestimmter PINNACLE-Pfannen. Aktualisierte Anweisung betrifft alle gelisteten betroffenen Pfannen unabhängig von geplanter optionaler Apex-Schraube. Produkt-/Lot-Liste aus Anhang erforderlich; keine unbelegte Komplettliste erzeugen. Kein Abschluss belegt.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fpinnacle"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fpinnacle](#quelle-fpinnacle): DePuy aktualisierte Sicherheitsinformation PINNACLE, Ref. 1896433 / BfArM 22108-20; 18.02.2021; PDF 1–4; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2021/22108-20_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 12 (Grok 17) | Grok bestätigt | ok | Grok-Nachtrag zur Größenverwechslung bestätigt. | `{"abschnitt":"Implantate","label":"Avenir Müller Rückruf","menge":null,"einheit":null,"spez":"rueckrufe ZFA2018-00572/FA2018-06: Avenir Müller Größe 1, REF 01.06010.001, Lot 2955599, enthält Größe 2 (REF 01.06010.002, Lot 2956599). Nicht pauschal Avenir Complete oder alle Avenir-Produkte als betroffen markieren.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["favenir"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [favenir](#quelle-favenir): Zimmer Biomet ZFA2018-00572, FA2018-06 / BfArM 13742-18; 31.10.2018; PDF 1; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/13742-18_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 13 (Grok 17) | Astra | Fehler | Nachtrag enthält relevante Warnung; Protasul-S30 nicht als CoCr einordnen. | `{"abschnitt":"Implantate","label":"Metallkopf nach Keramikbruch","menge":null,"einheit":null,"spez":"rueckrufe/hinweise FA2016-10: nach Keramikbruch keine der betroffenen Metallkopf-Gleitpaarungen verwenden; Hersteller nennt Keramik/Keramik oder Keramik/PE als Alternative. CoCr modular, Protasul-S30 und Metasul getrennt führen; Protasul-S30 ist in diesem Schreiben Edelstahl. Aufgelistete Pfannensysteme nicht mit einer generellen Schaft-Freigabe verwechseln.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fmetal"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fmetal](#quelle-fmetal): Zimmer Biomet FA 2016-10, ZFA 2016-150 / BfArM 01461-17; 13.02.2017; PDF 1–2; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/01461-17_Kundeninfo_de.pdf?__blob=publicationFile&v=1) | hoch |
| 14 (Grok 14,17) | Astra | Fehler | Relevante CPT-Meldung fehlt trotz Kandidat im Prüfumfang. | `{"abschnitt":"Implantate","label":"CPT Sicherheitskorrektur","menge":null,"einheit":null,"spez":"rueckrufe/hinweise ZFA2024-00121: CPT-Schaft, Sicherheitskorrektur zu erhöhtem Risiko periprothetischer Femurfraktur; Schreiben 01.07.2024. Angekündigtes Auslaufen bis Dezember 2024 nicht als Beleg aktueller Marktverfügbarkeit oder behördlichen Abschlusses verwenden. CPT nicht allein aufgrund historischen Katalogs neu zur Auswahl freigeben.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fcpt"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fcpt](#quelle-fcpt): Zimmer Biomet ZFA2024-00121 / BfArM 21393-24, CPT; 01.07.2024; PDF 1–2; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/21393-24_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 15 (Grok 18) | Astra | Fehler | Nur Portaltitel und Portaldatum erfasst. | `{"abschnitt":"Implantate","label":"optimys Rückruf chargengenau","menge":null,"einheit":null,"spez":"rueckrufe FSCA 17/02: optimys lateral TAV Größe 7 unzementiert, REF 52.34.0207, Lot 2240248. Fehlende Siegelnaht am zweiten Klarsichtbeutel laut Schreiben 18.07.2017. Kein Rückruf aller optimys-Schäfte; kein Abschluss belegt.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["foptimys"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [foptimys](#quelle-foptimys): Mathys FSCA 17/02 / BfArM 07038-17, optimys; 18.07.2017 (Schreiben; Portal 20.07.2017); PDF 1; [Original](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07038-17_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 16 (Grok 18) | Astra | Fehler | TH+/TPS ohne historische Sicherheitsabgrenzung als Kandidat ungeeignet. | `{"abschnitt":"Implantate","label":"seleXys TH+/TPS getrennt","menge":null,"einheit":null,"spez":"Historischer AU-Hinweis 16.09.2015 außerhalb des 10-Jahresfensters: TGA-Warnung erhöhte Revisionen seleXys TH+/TPS; Lieferende AU TH+ April 2013/TPS Juni 2014, ARTG-Einträge gelöscht. seleXys PC ausdrücklich nicht Gegenstand dieser Warnung. Daraus weder heutigen EU-Status noch EU-Freigabe ableiten; TH+/TPS als neue DACH-Auswahl ohne aktuelle EU-Originale offen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["tga"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [tga](#quelle-tga): TGA: SeleXys TH+ and TPS acetabular shells used in hip replacements; 16.09.2015; historisch, Australien; Hazard alert; Lieferende/ARTG und Abgrenzung PC; [Original](https://www.tga.gov.au/safety/recalls-and-other-market-actions/market-actions/selexys-th-and-tps-acetabular-shells-used-hip-replacements) | hoch |
| 17 (Grok 1) | Astra | Fehler | Anteile und komplette Top-15-Kategorien fehlen; Häufigkeit ist keine Kompatibilität. | `{"abschnitt":"Implantate","label":"DE Ranking korrekt einordnen","menge":null,"einheit":null,"spez":"auswahl_dach: EPRD-Anhang dieses Berichts nutzen: Top 15 je Fixationskategorie für Schäfte, Pfannen und vier Versorgungstypen; Anzahl und berechneter Anteil an jeweiliger GESAMT-Zeile. Kumulierte Analysepopulation, kein OP-Jahr-2024-Marktanteil; unterschiedliche Beobachtungszeiten und Mindestfallzahlen. Auch beobachtete Hersteller-Mischkombinationen nicht in passt_zu=ja umwandeln. Keine Markenrangliste Hemi aus diesen HTEP-Tabellen ableiten.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["eprd","es","ep","ek"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [eprd](#quelle-eprd): EPRD Jahresbericht 2025, Status 5; 28.10.2025 (Dateistand); Tab. 53 S. 94–111/PDF 54–62; Tab. 77 S. 204–213/PDF 113–117; Tab. 78 S. 214–221/PDF 118–121; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Publikationen/Berichte/Jahresbericht2025-Status5_2025-10-28_F.pdf)<br>[es](#quelle-es): EPRD Implantatergebnisse Hüftschäfte; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx)<br>[ep](#quelle-ep): EPRD Implantatergebnisse Hüftpfannen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftpfannen.xlsx)<br>[ek](#quelle-ek): EPRD Implantatergebnisse Hüftversorgungen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftversorgungen.xlsx) | mittel |
| 18 (Grok 2) | Astra | Fehler | 2.466/12.580 ist Gesamt inklusive other combinations, nicht nur Top-75%-Liste. | `{"abschnitt":"Implantate","label":"CH Bezugsgrößen korrigieren","menge":null,"einheit":null,"spez":"auswahl_dach: SIRIS Tab. 4.16 S. 95 und 4.19 S. 103 enthalten ausgewählte Schaft/Pfannen-Kombinationen mit 2024- und 2019–2024-Zahlen. Tab. 4.19 Gesamt 2.466/12.580 inklusive übriger Kombinationen. Kein separates vollständiges Schaft-/Pfannen-Top-15 aus diesen Ausschnitten konstruieren. Rangfolge im Anhang ist eigene Sortierung der ausgewiesenen Kombinationen nach 2024, nicht landesweites Marktanteilsranking.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["siris"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [siris](#quelle-siris): SIRIS Report Hip & Knee 2025, Annual Report 2012–2024; Dezember 2025; Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.; [Original](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf) | mittel |
| 19 (Grok 2) | Grok bestätigt | ok | Grok-Nachtrag ersetzt frühere Aussage ohne Markenliste. | `{"abschnitt":"Implantate","label":"CH Hemi-Nachtrag bestätigt","menge":null,"einheit":null,"spez":"auswahl_dach: SIRIS Tab. 4.34 S./PDF 129 enthält produktbezogene Schaft/Kopf-Kombinationen bei Hemi-Versorgung. Alle im Anhang wiedergegebenen 2024-/2019–2024-Zahlen des Nachtrags stimmen. Gesamt 2.299/12.645 einschließlich other combinations. Unipolar und Bipolar getrennt; keine IFU-Kompatibilität aus Häufigkeit ableiten.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["siris"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [siris](#quelle-siris): SIRIS Report Hip & Knee 2025, Annual Report 2012–2024; Dezember 2025; Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.; [Original](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf) | mittel |
| 20 (Grok 3) | Astra | Fehler | Pauschales Fehlen öffentlich zugänglicher Produkt-Häufigkeiten ist unvollständig. | `{"abschnitt":"Implantate","label":"Österreich regional ergänzen","menge":null,"einheit":null,"spez":"auswahl_dach: Öffentlicher Euregio-Bericht enthält Tiroler Produkt-Häufigkeiten, Tab. 62–67 S. 117–119. Historischer regionaler Befund, kein aktuelles Österreich-Ranking; Südtirol/Trentino gehören nicht zur AT-Stichprobe. Berichtszeitraum 2013–2017; Bezugsjahr der einzelnen Anhangstabelle hier nicht eindeutig bestätigt, daher keine Jahreszahl für diese Produktzahlen ergänzen. Aktuelles bundesweites öffentliches Markenranking weiterhin nicht gefunden.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["tirol","at"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [tirol](#quelle-tirol): Hüftendoprothetik in der Europaregion Tirol-Südtirol-Trentino der Operationsjahre 2013 bis 2017; Februar 2021; Anhang Tirol, Tab. 62–67, S. 117–119/PDF 123–125; [Original](https://www.iet.at/data.cfm?vpath=publikationen210/prt/euregio-bericht_2013-17_deu)<br>[at](#quelle-at): Hüft- und Knie-Endoprothetik in Österreich; 27.07.2018; Abschnitt 4.2, S. 31; [Original](https://www.sozialministerium.gv.at/dam/jcr:a32545b2-d40c-43f2-ac1f-7c6ce97804a8/endoprothetik-bericht_27.07.18_final.pdf) | mittel |
| 21 (Grok 4,12,14) | Astra | Fehler | Avenir ≠ Avenir Complete; M.E.M. ≠ MS-30; Trident ≠ Trident II. | `{"abschnitt":"Implantate","label":"DACH Auswahl ohne Systemtransfer","menge":null,"einheit":null,"spez":"auswahl_dach: DePuy CORAIL/PINNACLE, ZB Avenir/Fitmore/CLS/Allofit, Enovis optimys/RM Pressfit vitamys und Medacta Quadra/Amistem/Versafit priorisieren. EPRD Avenir n=40.890 belegt nicht Avenir Complete (eigene Zeile Avenir Complete Collarless n=4.820). M.E.M. und MS-30 separat. Bestehende vier Systemdateien bleiben laut Auftrag; historische Varianten und Registerpaarungen begründen keine neue Freigabe ihrer aktuellen Komponenten. Länder-/Variantenzuordnung siehe Auswahlanhang.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["es","ep","ek","siris","tirol","avenir"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [es](#quelle-es): EPRD Implantatergebnisse Hüftschäfte; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx)<br>[ep](#quelle-ep): EPRD Implantatergebnisse Hüftpfannen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftpfannen.xlsx)<br>[ek](#quelle-ek): EPRD Implantatergebnisse Hüftversorgungen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftversorgungen.xlsx)<br>[siris](#quelle-siris): SIRIS Report Hip & Knee 2025, Annual Report 2012–2024; Dezember 2025; Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.; [Original](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf)<br>[tirol](#quelle-tirol): Hüftendoprothetik in der Europaregion Tirol-Südtirol-Trentino der Operationsjahre 2013 bis 2017; Februar 2021; Anhang Tirol, Tab. 62–67, S. 117–119/PDF 123–125; [Original](https://www.iet.at/data.cfm?vpath=publikationen210/prt/euregio-bericht_2013-17_deu)<br>[avenir](#quelle-avenir): Avenir Complete Surgical Technique, 1624.4-GLBL-en; 2021-11-10; S./PDF 7,9; Ausgabe insgesamt 12 PDF-Seiten; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/4PulT0mR4JdEX4f5n00BxC/88cc646adbb9dbc5309025ed0769cd3e/1624.4-GLBL-en_Avenir_SurgTech.pdf) | mittel |
| 22 (Grok 5) | Astra | Fehler | Aktuellere EMEA-Originalquelle gefunden; HO collared fehlt bei Grok. | `{"abschnitt":"Implantate","label":"Corail EMEA-Größen","menge":null,"einheit":null,"spez":"groessen: STD 135° collarless/collared: 8,9,10,11,12,13,14,15,16,18,20. HO 135° collarless und collared sowie KLA 125° collared: 9,10,11,12,13,14,15,16,18,20. Dysplasia 6A/6S separat. Zementierte STD-Größen 8–16,18,20; HO 9–16,18,20. HA-beschichtete Ausführungen nicht zementieren. STD125/SN135 nicht aus den anderen Familien ableiten; Katalog-/Sizing-Abgleich für deren vollständige Bestellzeilen bleibt offen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["corail"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [corail](#quelle-corail): CORAIL Total Hip System Surgical Technique, 198918-211214 UK; ©2022; EMEA; S. 11,13,15,20–26/PDF 12,14,16,21–27; [Original](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf) | hoch |
| 23 (Grok 6) | Astra | Fehler | AU/NZ-Technik darf keine EU-Detailfreigabe ersetzen. | `{"abschnitt":"Implantate","label":"Actis marktbezogen offen","menge":null,"einheit":null,"spez":"Ranking: EPRD ACTIS zementfrei n=3.993; SIRIS Actis/Pinnacle 2024 n=606. AU/NZ-Technik existiert, enthält Warnung Size 0 nicht mit Kopf-Offset >+13 mm. EU-Größen-/REF-/Kopf-Freigabematrix weiterhin nicht belegt; diese Detaildaten bleiben quelle:null und passt_zu=offen statt AU/NZ-Werte als EU-Auswahl zu importieren.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [es](#quelle-es): EPRD Implantatergebnisse Hüftschäfte; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx)<br>[siris](#quelle-siris): SIRIS Report Hip & Knee 2025, Annual Report 2012–2024; Dezember 2025; Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.; [Original](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf)<br>[actis](#quelle-actis): ACTIS Total Hip System Surgical Technique, 190156-210922 NZ / AU-Ausgabe; September 2021 NZ; AU 2020; Warnung S. 8/PDF 10; Technical Specifications S. 12/PDF 14; [Original](https://www.jnjmedtech.com/system/files/pdf/190156.210922%20NZ_134763.200315AU%20ACTIS%20Surgical%20Technique%20FINAL.pdf) | hoch |
| 24 (Grok 7) | Grok bestätigt | ok | Nur den im Nachtrag exakt belegten Teil übernehmen. | `{"abschnitt":"Implantate","label":"Pinnacle Liner-Typen bestätigt","menge":null,"einheit":null,"spez":"Liner-Konfigurationen in EMEA-Technik: Neutral, +4 Neutral, +4 10° Face-Changing, Lipped. Diese Angaben belegen die Konfigurationen, nicht jede Schalen-/Kopf-/Materialkombination. Quelle ersetzt hierfür den älteren Spiegel.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["pinnacle"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [pinnacle](#quelle-pinnacle): PINNACLE Hip Solutions Surgical Technique, 142532-220805 EMEA; ©2022; S. 8–10/PDF 10–12; S. 16/PDF 18; [Original](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf) | hoch |
| 25 (Grok 7,9,10) | Astra | Fehler | Probeliner/ROM-Tabellen liefern keine vollständige Implantatmatrix. | `{"abschnitt":"Implantate","label":"DePuy Detailmatrizen offen","menge":null,"einheit":null,"spez":"offen: aktuelle PINNACLE-Schalen-Ø × konkreter AltrX/Marathon/Keramikliner × max. Kopf-Ø, Articul/eze/BIOLOX-delta-Ø/Offsets sowie Self-Centering-Bipolar mit genau freigegebenem zementiertem EU-Schaft. Trial-Liner 28–44 mm/+2 mm sind keine pauschale Implantatfreigabe. Alte 38–66/28–48-Angaben nicht als heutige vollständige EMEA-Matrix übernehmen. quelle:null für fehlende Einzelkombinationen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [pinnacle](#quelle-pinnacle): PINNACLE Hip Solutions Surgical Technique, 142532-220805 EMEA; ©2022; S. 8–10/PDF 10–12; S. 16/PDF 18; [Original](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf)<br>[corail](#quelle-corail): CORAIL Total Hip System Surgical Technique, 198918-211214 UK; ©2022; EMEA; S. 11,13,15,20–26/PDF 12,14,16,21–27; [Original](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf) | hoch |
| 26 (Grok 8) | Astra | Fehler | Registerpriorität stimmt, ist jedoch noch keine technische Freigabe. | `{"abschnitt":"Implantate","label":"DePuy zementiert priorisieren","menge":null,"einheit":null,"spez":"auswahl_dach: CORAIL zementiert ohne Kragen n=11.830; Hybrid CORAIL/PINNACLE n=9.351; CORAIL/TRILOC II-PE zementiert n=1.072. Als getrennte Kandidaten führen. C-STEM AMT sekundär; Elite Plus/Marathon-zementiert nicht aus PINNACLE-Dokument ableiten. passt_zu für konkrete Köpfe/Pfannen ausschließlich nach eigener Produktfreigabe.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["es","ek"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [es](#quelle-es): EPRD Implantatergebnisse Hüftschäfte; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx)<br>[ek](#quelle-ek): EPRD Implantatergebnisse Hüftversorgungen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftversorgungen.xlsx) | mittel |
| 27 (Grok 12) | Astra | Fehler | Grok-Nachtrag lässt A-Größenspanne unvollständig. | `{"abschnitt":"Implantate","label":"Fitmore Familien vollständig","menge":null,"einheit":null,"spez":"groessen: Fitmore A, B, B Extended Offset und C jeweils Größen 1–14 laut Originaltabellen; CCD 140°/137°/129°/127°, Konus 12/14, Protasul-64, zementfrei. A Größe 1 nicht USA; 13/14 auf Anfrage laut Quelle, keine globale Lieferzusage. Widersprüchlichen B-Extended-12-Offset separat offen halten. Vollständige CLS-/Alloclassic-EU-Größen nicht durch JP- oder US-Ausgabe ersetzen.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fitmore"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [fitmore](#quelle-fitmore): Fitmore Hip Stem Surgical Technique, 1013.3-GLBL-en; 2025-04; S. 12–16/PDF 14–18; Bestelltabellen S. 16 ff.; [Original](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/fitmore/1013.3-GLBL-en%20Fitmore%20Hip%20Stem%20Surg%20Tech%20A4%20DIGITAL.pdf) | hoch |
| 28 (Grok 13) | Astra | Fehler | Allofit-Häufigkeit ersetzt weder Allofit-S-Matrix noch G7-Freigabe. | `{"abschnitt":"Implantate","label":"ZB Pfannenlücken benennen","menge":null,"einheit":null,"spez":"offen: Allofit/Allofit-S/Allofit IT, Continuum und Trilogy mit je eigener Größe/Liner/Kopf-Ø-/REF-Matrix und EU-Quelle. Nicht zwischen Produktnamen zusammenführen. EPRD Allofit 195.023, Allofit IT 12.969, Trilogy 7.677 sind Auswahlbelege, keine Kompatibilitätstabellen. G7 ist separat anhand Anhang belegt, nicht auf die anderen Pfannen übertragbar.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [ep](#quelle-ep): EPRD Implantatergebnisse Hüftpfannen; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftpfannen.xlsx)<br>[g7](#quelle-g7): G7 Acetabular System Surgical Technique, 2336.6-GLBL-en; 2026-09-09; S. 3–5/PDF 6–8; Keramik S. 7/PDF 10; [Original](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/g7-acetabular-system/2336.6-GLBL-en%20G7%20Acetabular%20System%20Surgical%20Technique.pdf) | hoch |
| 29 (Grok 14) | Grok bestätigt | ok | Größen/Varianten des Nachtrags am Herstelleroriginal bestätigt. | `{"abschnitt":"Implantate","label":"MS-30 Nachtrag bestätigt","menge":null,"einheit":null,"spez":"groessen: MS-30 zementiert, Konus 12/14; Standard und Lateral je 6,8,10,12,14,16. Standard CCD 130–135°, Offset 37,7–43,3 mm; Lateral CCD 124,3–128°, Offset 42,2–48,4 mm. Einzeltabelle im Anhang. M.E.M.-Registerzahlen nicht hierfür verwenden.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["ms30"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [ms30](#quelle-ms30): MS-30 Cemented Hip Stem Surgical Technique, 5087.1-GLBL-en; 2025-12; S./PDF 25–26,29–30; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/141dC8Nk3O5X6zFJkF1ba2/11cb417e096fc3f917a1cebfee73a33b/5087.1-GLBL-en_MS-30_Cemented_Hip_Stem_Upgraded_Instruments_Surg_Tech_A4_DIGITAL.pdf) | hoch |
| 30 (Grok 15) | Astra | Fehler | Gefundene Chartspalten noch keine vollständige Kopfgrößen-/Offsetliste. | `{"abschnitt":"Implantate","label":"ZB Kopfdetails weiter offen","menge":null,"einheit":null,"spez":"offen: exakte BIOLOX delta/OPTION-, CoCr-, Protasul- und ggf. 8/10-REF-Zeilen je Schaft, Durchmesser, Halslänge und Markt. Keine kartesische Kombination aller Ø/Offsets aus mehreren Charts. Passung nur über tatsächlich markierte Schnittstelle plus Fußnoten/IFU; bloß gleiche 12/14-Bezeichnung genügt nicht.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [ceramic](#quelle-ceramic): Head and Stem Combinations: Ceramic Femoral Heads; Revised 5/6/2019 (Originalschreibweise); PDF 1–3; insbesondere Zeilen Alloclassic/Avenir/CLS/Fitmore auf PDF 1 und Fußnoten; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/6LuflsxnuxzS6yod8Wbg5c/75d5c277cb99658423118798f590191e/Ceramic_Femoral_Heads_NEW.pdf)<br>[cocr](#quelle-cocr): Head and Stem Combinations: CoCr Femoral Heads; Revised 7/15/2020; PDF 1–3, produktspezifische Spalten und Fußnoten; [Original](https://assets.ctfassets.net/rc4arfpyhdpw/iV1BfgVRHhLqYPmt2Zt2G/bc7ac72e2ad60e1eed7f7d9f5628fa51/CoCr-Femoral-Heads_NEW.pdf) | hoch |
| 31 (Grok 18,19) | Astra | Fehler | Produktseiten und Broschüren sind öffentlich lesbar; vollständige Charts bleiben offen. | `{"abschnitt":"Implantate","label":"Enovis Dokumentlage korrigieren","menge":null,"einheit":null,"spez":"optimys-Produktseite nennt 12 Größen und Standard/Lateral; RM Pressfit vitamys ist Monoblock, kein separates modulares Inlay. Öffentlich geöffnete Keramikbroschüre belegt Materialien/Gleitpaarungen, aber keine vollständige named-stem-REF-Matrix. Vollständige optimys-/RM-Größentabelle und Kopf-Freigaben, insbesondere twinSys und Bipolar, weiter offen; alte PDF-Links liefern Gate/Umleitung. Keine Freigabe per gleichem Konzern oder transitiv über RM ableiten.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["optimys","rm","heads"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [optimys](#quelle-optimys): Enovis optimys – Produktseite; undatiert, Abruf 07.10.2026; Product details/Bone Preservation; [Original](https://enovis-surgical.com/en/products/325/optimys.html)<br>[rm](#quelle-rm): RM Pressfit vitamys Product Information, 336.010.121 03-0123-01; 2023-01; PDF 2–5, Monoblockkonzept; [Original](https://enovis-surgical.com/repo/storage/4724/file/produktinformation_rm-pressfit_en_v3.0.pdf)<br>[heads](#quelle-heads): Mathys Ceramic Product Information, 336.010.127 03-0319-01; 2019-03; PDF 2–3, ceramys/symarec und Gleitpaarung; [Original](https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf) | hoch |
| 32 (Grok 20) | Astra | Fehler | Außerhalb DE-Top-15 bedeutet nicht außerhalb jeder regionalen AT-Liste. | `{"abschnitt":"Implantate","label":"Weitere Kandidaten differenzieren","menge":null,"einheit":null,"spez":"auswahl_dach: Medacta priorisieren (DE QUADRA-H #13; CH Quadra-P/Versafit und Amistem-P/Versafit). Tirol historisch: Lima MINIMA-S #9 (57), Corin MiniHip #12 (30); Corin Trinity bei Pfannen geteilter Rang 7 (30). Das belegt weder Lima H-Max noch aktuelle nationale Verbreitung. Implantcast nach Register separat/sekundär; keine Detailfreigabe. Aktuelle EU-Hauptdokumente für zusätzlich gewählte Lima-/Corin-/Implantcast-Systeme noch offen; Fundstellenauftrag unvollständig erfüllt.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["es","siris","tirol"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [es](#quelle-es): EPRD Implantatergebnisse Hüftschäfte; Jahresbericht 2025; Abruf 07.10.2026; Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang; [Original](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx)<br>[siris](#quelle-siris): SIRIS Report Hip & Knee 2025, Annual Report 2012–2024; Dezember 2025; Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.; [Original](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf)<br>[tirol](#quelle-tirol): Hüftendoprothetik in der Europaregion Tirol-Südtirol-Trentino der Operationsjahre 2013 bis 2017; Februar 2021; Anhang Tirol, Tab. 62–67, S. 117–119/PDF 123–125; [Original](https://www.iet.at/data.cfm?vpath=publikationen210/prt/euregio-bericht_2013-17_deu) | mittel |
| 33 (Grok 21) | Astra | Fehler | 31156-en V2 nun selbst geöffnet; alte Längenlücke kann geschlossen werden. | `{"abschnitt":"Implantate","label":"SL-PLUS MIA Längen geklärt","menge":null,"einheit":null,"spez":"tabellen: SLPLUS_MIA_Laengen laut Anhang, getrennt Stem length I und II, S. 17/PDF 20; Definition Zeichnung S. 18/PDF 21. Für Größe 1/2/6 Länge I 137/141/159 mm. Alte abweichende 136/140/158-Werte nicht übernehmen. Standard 01,0,1–12 und Lateral 1–12 getrennt halten; Angaben der Geometrietabelle sind keine Kopf-Kompatibilitätsfreigabe.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["slmia"],"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | [slmia](#quelle-slmia): SL-PLUS MIA Surgical Technique, 31156-en V2; 11/2024; S. 17–18/PDF 20–21; Warnungen S. 2/PDF 5; [Original](https://smith-nephew.stylelabs.cloud/api/public/content/c38ee11595e14dfdbdd7ade71a170ac9?v=3e0dbffa&download=true) | hoch |
| 34 (Grok 21) | Astra | Fehler | Nicht selbst erneut geprüfte Detailquellen dürfen nicht als belegt gelten. | `{"abschnitt":"Implantate","label":"Restpunkte ausdrücklich offen","menge":null,"einheit":null,"spez":"offen: seleXys PC aktuelle Originalseiten 11–12,19 weiterhin nicht lesbar über den alten Link; X3 26 mm in diesem Lauf nicht erneut aus produktspezifischer Originaltabelle bestätigt. Betroffene max_kopf_mm-/REF-/Kombinationswerte quelle:null und passt_zu=offen belassen. Kein Rückschluss aus Trident statt Trident II oder aus anderem Liner.","gilt_fuer":["001 Hüftendoprothetik","001-implantate-dach"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Datenprüfung aus OP-Pflege/OTA-Perspektive; keine klinische Freigabe. Lokaler Bestand und Verfügbarkeit sind hausabhängig."}` | Keine produktspezifische Originalquelle für die offene Angabe. | hoch |

## Anhang: EPRD – Anzahl und Anteil

Selbst aus den drei Original-XLSX nach `Anzahl` absteigend sortiert. Prozent = Anzahl / GESAMT derselben Kategorie × 100, auf zwei Dezimalen gerundet. Gleiche Anzahl erhält gleichen Rang. Es werden höchstens 15 Produktzeilen gezeigt. Zähler und Nenner sind kumulierte Analysezahlen; weder Jahresmarktanteile noch länderübergreifend addierbar. `⚠` bedeutet verschiedene Hersteller in einer beobachteten Registerpaarung; keine Freigabe zur Kombination.

### zementfreie Schaftverankerung
Quelle es; GESAMT 495.462.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen | 45321 | 9.15 | 28 |
| 2 | Zimmer Biomet: Avenir | 40890 | 8.25 | 19 |
| 3 | Zimmer Biomet: Fitmore | 38591 | 7.79 | 39 |
| 4 | Mathys: optimys | 37801 | 7.63 | 51 |
| 5 | Zimmer Biomet: CLS Spotorno | 31461 | 6.35 | 26 |
| 6 | Aesculap: BICONTACT | 21080 | 4.25 | 21 |
| 7 | Smith & Nephew: Polarschaft | 20743 | 4.19 | 53 |
| 8 | Johnson & Johnson: CORAIL AMT-Hüftschaft mit Kragen | 19425 | 3.92 | 27 |
| 9 | ARTIQO: A2 Kurzschaft | 15853 | 3.20 | 5 |
| 10 | Aesculap: COREHIP | 15809 | 3.19 | 29 |
| 11 | Aesculap: EXCIA | 15564 | 3.14 | 38 |
| 12 | Stryker: Accolade II | 15445 | 3.12 | 7 |
| 13 | Medacta Ortho: QUADRA-H | 15013 | 3.03 | 60 |
| 14 | Zimmer Biomet: Alloclassic | 12493 | 2.52 | 10 |
| 15 | Aesculap: METHA | 9548 | 1.93 | 46 |

### zementierte Schaftverankerung
Quelle es; GESAMT 135.607.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: M.E.M. Geradschaft | 37967 | 28.00 | 102 |
| 2 | Waldemar Link: SPII Model Lubinus | 17624 | 13.00 | 113 |
| 3 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen | 11830 | 8.72 | 91 |
| 4 | Zimmer Biomet: Avenir | 9362 | 6.90 | 85 |
| 5 | Aesculap: EXCIA | 6990 | 5.15 | 97 |
| 6 | Zimmer Biomet: MS-30 | 4842 | 3.57 | 104 |
| 7 | Aesculap: BICONTACT | 4731 | 3.49 | 88 |
| 8 | Smith & Nephew: Polarschaft | 4515 | 3.33 | 108 |
| 9 | Medacta Ortho: QUADRA-C | 3400 | 2.51 | 111 |
| 10 | Aesculap: COREHIP | 2968 | 2.19 | 92 |
| 11 | Mathys: twinSys | 2841 | 2.10 | 118 |
| 12 | Zimmer Biomet: METABLOC | 2299 | 1.70 | 103 |
| 13 | Zimmer Biomet: Taperloc | 2291 | 1.69 | 116 |
| 14 | OHST Medizintechnik: Müller Geradschaft | 2187 | 1.61 | 106 |
| 15 | Mathys: CCA | 1965 | 1.45 | 90 |

### zementfreie Pfannenverankerung
Quelle ep; GESAMT 597.485.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: Allofit | 195023 | 32.64 | 7 |
| 2 | Johnson & Johnson: PINNACLE Press Fit | 81222 | 13.59 | 40 |
| 3 | Aesculap: PLASMAFIT | 72818 | 12.19 | 43 |
| 4 | Smith & Nephew: R3 | 28491 | 4.77 | 48 |
| 5 | Mathys: RM Pressfit vitamys | 28001 | 4.69 | 52 |
| 6 | Medacta Ortho: VERSAFITCUP CC TRIO | 20423 | 3.42 | 67 |
| 7 | Zimmer Biomet: Allofit IT | 12969 | 2.17 | 8 |
| 8 | ARTIQO: ANA.NOVA Hybrid | 12288 | 2.06 | 10 |
| 9 | Stryker: Trident | 11644 | 1.95 | 58 |
| 10 | Aesculap: PLASMACUP | 10419 | 1.74 | 42 |
| 11 | ARTIQO: ANA.NOVA Alpha | 10231 | 1.71 | 9 |
| 12 | Mathys: aneXys Flex | 9091 | 1.52 | 12 |
| 13 | Zimmer Biomet: Trilogy | 7677 | 1.28 | 62 |
| 14 | Smith & Nephew: HI Lubricer Schale | 6401 | 1.07 | 36 |
| 15 | Waldemar Link: CombiCup | 5656 | 0.95 | 22 |

### zementierte Pfannenverankerung
Quelle ep; GESAMT 33.321.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: Flachprofil | 10672 | 32.03 | 77 |
| 2 | Aesculap: All POLY | 4960 | 14.89 | 70 |
| 3 | OHST Medizintechnik: Müller II | 3075 | 9.23 | 81 |
| 4 | Zimmer Biomet: AVANTAGE | 1757 | 5.27 | 72 |
| 5 | Waldemar Link: IP | 1560 | 4.68 | 78 |
| 5 | Johnson & Johnson: TRILOC II-PE | 1560 | 4.68 | 84 |
| 7 | Mathys: CCB | 1377 | 4.13 | 74 |
| 8 | Waldemar Link: Lubinus | 1319 | 3.96 | 79 |
| 9 | Waldemar Link: Endo-Model | 614 | 1.84 | 76 |
| 10 | Implantcast: Mueller II | 607 | 1.82 | 80 |
| 11 | Smith & Nephew: POLARCUP | 528 | 1.58 | 82 |
| 12 | Implantcast: EcoFit 2M | 499 | 1.50 | 75 |
| 13 | MicroPort: PROCOTYL C | 448 | 1.34 | 83 |
| 14 | Waldemar Link: BiMobile Dual Mobility System | 444 | 1.33 | 73 |
| 15 | Medacta Ortho: APRICOT | 385 | 1.16 | 71 |

### Hybride Verankerung
Quelle ek; GESAMT 108.536.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: M.E.M. Geradschaft + Zimmer Biomet: Allofit | 27085 | 24.95 | 27 |
| 2 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen + Johnson & Johnson: PINNACLE Press Fit | 9351 | 8.62 | 18 |
| 3 | Waldemar Link: SPII Model Lubinus + Zimmer Biomet: Allofit ⚠ | 7308 | 6.73 | 38 |
| 4 | Zimmer Biomet: Avenir + Zimmer Biomet: Allofit | 6410 | 5.91 | 8 |
| 5 | Aesculap: EXCIA + Aesculap: PLASMAFIT | 4852 | 4.47 | 22 |
| 6 | Zimmer Biomet: MS-30 + Zimmer Biomet: Allofit | 4177 | 3.85 | 32 |
| 7 | Medacta Ortho: QUADRA-C + Medacta Ortho: VERSAFITCUP CC TRIO | 2746 | 2.53 | 36 |
| 8 | Smith & Nephew: Polarschaft + Smith & Nephew: R3 | 2542 | 2.34 | 34 |
| 9 | Aesculap: BICONTACT + Aesculap: PLASMAFIT | 2237 | 2.06 | 12 |
| 10 | Aesculap: COREHIP + Aesculap: PLASMAFIT | 2025 | 1.87 | 20 |
| 11 | Waldemar Link: SPII Model Lubinus + Waldemar Link: Mobile Link, Porous Surface | 1809 | 1.67 | 42 |
| 12 | Zimmer Biomet: M.E.M. Geradschaft + Zimmer Biomet: Trilogy | 1737 | 1.60 | 29 |
| 13 | Zimmer Biomet: METABLOC + Zimmer Biomet: Allofit | 1513 | 1.39 | 31 |
| 14 | Waldemar Link: SPII Model Lubinus + Waldemar Link: CombiCup | 1405 | 1.29 | 40 |
| 15 | Mathys: twinSys + Mathys: RM Pressfit vitamys | 1275 | 1.17 | 49 |

### Revers-hybride Verankerung
Quelle ek; GESAMT 6.337.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: Avenir + Zimmer Biomet: Flachprofil | 455 | 7.18 | 51 |
| 2 | Aesculap: BICONTACT + Aesculap: All POLY | 435 | 6.86 | 52 |
| 3 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen + Johnson & Johnson: TRILOC II-PE | 323 | 5.10 | 53 |

### Zementfreie Verankerung
Quelle ek; GESAMT 488.949.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen + Johnson & Johnson: PINNACLE Press Fit | 40946 | 8.37 | 100 |
| 2 | Zimmer Biomet: Avenir + Zimmer Biomet: Allofit | 35664 | 7.29 | 80 |
| 3 | Zimmer Biomet: Fitmore + Zimmer Biomet: Allofit | 30373 | 6.21 | 111 |
| 4 | Zimmer Biomet: CLS Spotorno + Zimmer Biomet: Allofit | 26782 | 5.48 | 91 |
| 5 | Mathys: optimys + Mathys: RM Pressfit vitamys | 21771 | 4.45 | 140 |
| 6 | Johnson & Johnson: CORAIL AMT-Hüftschaft mit Kragen + Johnson & Johnson: PINNACLE Press Fit | 18707 | 3.83 | 96 |
| 7 | Aesculap: EXCIA + Aesculap: PLASMAFIT | 14593 | 2.98 | 109 |
| 8 | Smith & Nephew: Polarschaft + Smith & Nephew: R3 | 14298 | 2.92 | 143 |
| 9 | Aesculap: BICONTACT + Aesculap: PLASMAFIT | 14016 | 2.87 | 86 |
| 10 | Medacta Ortho: QUADRA-H + Medacta Ortho: VERSAFITCUP CC TRIO | 13812 | 2.82 | 152 |
| 11 | Aesculap: COREHIP + Aesculap: PLASMAFIT | 12954 | 2.65 | 103 |
| 12 | Zimmer Biomet: Alloclassic + Zimmer Biomet: Allofit | 10226 | 2.09 | 68 |
| 13 | Stryker: Accolade II + Stryker: Trident | 9152 | 1.87 | 58 |
| 14 | ARTIQO: A2 Kurzschaft + ARTIQO: ANA.NOVA Alpha | 7595 | 1.55 | 55 |
| 15 | ARTIQO: A2 Kurzschaft + ARTIQO: ANA.NOVA Hybrid | 7481 | 1.53 | 56 |

### Zementierte Verankerung
Quelle ek; GESAMT 26.984.

| Rang | Hersteller / Produkt | Anzahl | Anteil % | XLSX-Zeile |
|---|---|---|---|---|
| 1 | Zimmer Biomet: M.E.M. Geradschaft + Zimmer Biomet: Flachprofil | 5797 | 21.48 | 199 |
| 2 | Aesculap: BICONTACT + Aesculap: All POLY | 1676 | 6.21 | 192 |
| 3 | Zimmer Biomet: Avenir + Zimmer Biomet: Flachprofil | 1403 | 5.20 | 191 |
| 4 | Waldemar Link: SPII Model Lubinus + Waldemar Link: IP | 1346 | 4.99 | 204 |
| 5 | Aesculap: EXCIA + Aesculap: All POLY | 1331 | 4.93 | 197 |
| 6 | Johnson & Johnson: CORAIL AMT-Hüftschaft ohne Kragen + Johnson & Johnson: TRILOC II-PE | 1072 | 3.97 | 194 |
| 7 | Waldemar Link: SPII Model Lubinus + Waldemar Link: Lubinus | 1046 | 3.88 | 205 |
| 8 | Smith & Nephew: Polarschaft + OHST Medizintechnik: Müller II ⚠ | 709 | 2.63 | 202 |
| 9 | Mathys: twinSys + Mathys: CCB | 645 | 2.39 | 206 |
| 10 | Zimmer Biomet: MS-30 + Zimmer Biomet: Flachprofil | 512 | 1.90 | 201 |
| 11 | Waldemar Link: SPII Model Lubinus + Waldemar Link: Endo-Model | 502 | 1.86 | 203 |
| 12 | Smith & Nephew: CS PLUS + OHST Medizintechnik: Müller II ⚠ | 487 | 1.80 | 196 |
| 13 | Zimmer Biomet: METABLOC + Zimmer Biomet: Flachprofil | 422 | 1.56 | 200 |
| 14 | Zimmer Biomet: Avenir + Zimmer Biomet: AVANTAGE | 399 | 1.48 | 190 |
| 15 | Aesculap: COREHIP + Aesculap: All POLY | 357 | 1.32 | 195 |

## Anhang: Schweiz

Quelle siris. Eigene Sortierung der einzeln ausgewiesenen Kombinationen nach 2024. Die Sammelzeile other combinations hat keinen Produktrang. Kein vollständiges nationales Schaft-/Pfannen-Ranking.

### Unzementiert, primäre Arthrose – Tabelle 4.16

| Rang innerhalb der ausgewiesenen Produkte | Schaft / Pfanne | 2024 | 2019–2024 | Anteil am Tabellen-Gesamt 2024 % |
|---|---|---|---|---|
| 1 | Optimys / RM pressfit vitamys | 3780 | 16709 | 21.35 |
| 2 | Corail collared / Pinnacle | 2421 | 12093 | 13.68 |
| 3 | Polarstem / R3 | 1237 | 5440 | 6.99 |
| 4 | Quadra-P / Versafitcup trio/ccl. | 1179 | 3971 | 6.66 |
| 5 | Fitmore / Allofit | 1097 | 4333 | 6.20 |
| 6 | Amistem-P / Versafitcup trio/ccl. | 1032 | 6189 | 5.83 |
| 7 | Corail / Pinnacle | 638 | 5937 | 3.60 |
| 8 | Actis / Pinnacle | 606 | 2076 | 3.42 |
| 9 | Avenir / Allofit | 542 | 4576 | 3.06 |
| 10 | Corail collared / Novae TH-Bi-Mentum | 521 | 1882 | 2.94 |
| 11 | Twinsys / RM pressfit vitamys | 492 | 2596 | 2.78 |
| 12 | Fitmore / Fitmore | 230 | 3221 | 1.30 |
| 13 | Polarstem / Polarcup | 196 | 1189 | 1.11 |
| 14 | Quadra-H / Versafitcup trio/ccl. | 0 | 2415 | 0.00 |
| – | other combinations | 3732 | 23208 | 21.08 |
| – | Gesamt | 17703 | 95835 | 100 |

Hybrid Tab. 4.19: Twinsys cem/RM 526; Corail cem/Pinnacle 232; MS-30/Allofit 215; Avenir cem/Allofit 197; Amistem-C/Versafit 183. Tabellen-Gesamt 2024: 2.466 einschließlich 692 other combinations. Das sind keine addierbaren Einzelkomponenten-Marktanteile.

### Hemi – Tabelle 4.34

| Schaft / Kopf | 2024 | 2019–2024 |
|---|---|---|
| Amistem-C / Medacta bipolar | 221 | 944 |
| Amistem-C / Medacta endohead | 345 | 2128 |
| Avenir cem / ZB bipolar | 151 | 616 |
| Avenir cem / ZB unipolar | 77 | 359 |
| CCA / Hemihead SS | 166 | 1827 |
| Centris / Hemihead SS | 0 | 325 |
| Corail cem / J&J Cathcart | 300 | 1210 |
| Twinsys cem / Hemihead SS | 293 | 1206 |
| Twinsys cem / Mathys bipolar steel | 91 | 327 |
| Weber / ZB unipolar | 69 | 857 |
| other combinations | 586 | 2846 |
| Gesamt | 2299 | 12645 |

## Anhang: Auswahlentscheidung DACH

Priorisierung zur späteren Entscheidung, keine eigenständige Aufnahme oder technische Freigabe. Ränge DE = EPRD-Analysehäufigkeit; CH = Rang innerhalb ausgewiesener 2024-Kombinationen; AT = ausschließlich historischer Tirol-Anhang, kein nationaler Rang.

| Kandidat | DE | CH | AT/Tirol historisch | Konsequenz |
|---|---|---|---|---|
| CORAIL / PINNACLE | zf-Kombi ohne Kragen #1; mit Kragen #6 | collared/Pinnacle #2 | Corail-Schaft #5; Pinnacle-Pfanne #4 | priorisieren, Varianten getrennt |
| Avenir / Allofit | zf-Kombi #2 | #9 | Avenir Standard-Schaft #8; Allofit-Pfanne #2 | nicht Avenir Complete gleichsetzen |
| Fitmore / Allofit | zf-Kombi #3 | #5 | keine Ableitung aus anderer ZB-Variante | priorisieren; Offsetkonflikt offen |
| CLS / Allofit | zf-Kombi #4 | keine neue Top-15-Behauptung | CLS-Schaft #2 | priorisieren, EU-Detaildaten nachziehen |
| optimys / RM Pressfit vitamys | zf-Kombi #5 | #1 | hier kein aktueller Beleg | priorisieren; RM Monoblock |
| Medacta Quadra / Amistem / Versafit | QUADRA-H-Schaft #13; Kombi #10 | Quadra-P #4, Amistem-P #6 | Quadra-Schaft #1; Amistem #4 | H/P/C nicht zusammenlegen |
| ZB M.E.M. / MS-30 / Avenir cem | zementierte Schäfte #1 / #6 / #4 | MS-30/Allofit 215, Avenir/Allofit 197 | Müller-Zimmer ist keine eindeutige MS-30-Zuordnung | getrennte Kandidaten |
| Bestehend: Accolade II / Trident II | Accolade-II-Schaft #12; Kombi #13 nennt Trident | kein Transfer von Trident | Accolade-II-Schaft #3; Trident PSL-Pfanne #3 | behalten laut Auftrag; aktuelle Pfannenvariante separat |
| Bestehend: Excia T / Plasmafit | EXCIA #11 Schaft, PLASMAFIT #3 Pfanne; Kombi #7 | kein zusätzlicher Rang belegt | kein zusätzlicher Rang belegt | behalten; Handelsnamen/Untervarianten prüfen |
| Bestehend: SL-PLUS MIA / SPECTRON EF / R3 | R3-Pfanne #4; Polar/R3 belegt nicht SL-MIA | SL-MIA/R3 historische Revisionszeile N=2024, kein Jahresrang | SL-MIA-Schaft #13 | behalten; verschiedene Schäfte nicht gleichsetzen |
| Bestehend: twinSys / RM Classic / seleXys PC / ccB | twinSys cem #11; CCB cem-Pfanne #7 | Twinsys/RM vitamys #11, hybrid 526 | historische CCA-Daten nicht twinSys | behalten; RM vitamys ≠ RM Classic |
| Lima / Corin / Implantcast | nicht pauschal Top 15 | H-Max S/Delta TT N=531 ist Revisionskohorte | MINIMA-S #9; MiniHip #12; Trinity Pfanne geteilt #7 | nur benannte Varianten weiter recherchieren |

Tirol Tab. 66: zf-Schäfte N=1.938; QUADRA 508 (26,2%), CLS 359 (18,5%), Accolade II 195 (10,1%), AMISTEM 181 (9,3%), CORAIL 161 (8,3%), MONOCON MIS 150 (7,7%), PPF 98 (5,1%), Avenir Standard 65 (3,4%), MINIMA-S 57 (2,9%), CBC und Alloclassic je 34 (je 1,8%), MiniHip 30 (1,5%), SL-PLUS MIA 24 (1,2%), GTS 12 (0,6%), ANA.NOVA Solitär 7 (0,4%). Bei gleichem n ist der Rang gleich; MiniHip bleibt wegen zweier gleichrangiger Vorgänger Position 12. Quelle tirol.

## Anhang: G7-Matrix

Quelle g7, Thickness Guide S. 4–5/PDF 7–8. Angaben in mm; nur zu den dort ausgewiesenen PE-Linern. Keine Übertragung auf Ceramic, Freedom oder Dual Mobility. Probeliner-Farbe/Alpha ersetzt keine REF-Prüfung.

| Schalen-Ø / Alpha | PE Neutral, High Wall, 10°: Kopf-Ø | +5 Lateralized: Kopf-Ø |
|---|---|---|
| 42,44 / A | 28 | 28 |
| 46 / B | 28,32 | 28,32 |
| 48 / C | 28,32,36 | 28,32 |
| 50 / D | 28,32,36 | 28,32,36 |
| 52 / E | 28,32,36,40 | 28,32,36 |
| 54,56 / F | 28,32,36,40 | 28,32,36,40 |
| 58,60 / G | 28,32,36,40,44 | 28,32,36,40 |
| 62,64 / H | 32,36,40,44 | 32,36,40,44 |
| 66,68,70*,72* / I | 36,40,44 | 36,40,44 |
| 74*,76*,78*,80* / J | 36,40,44 | 36,40,44 |

*70/72 und J laut Tabelle nur OsseoTi Multi Hole; lokale Marktverfügbarkeit prüfen. Keramik-Tabelle S. 7/PDF 10: A/J kein Eintrag; B 28; C/D 32; E/F 32,36; G/H/I 32,36,40. Keine Ableitung des Keramik-Maximums aus PE.

## Anhang: MS-30

Quelle ms30 S./PDF 29; Größen 6,8,10,12,14,16. Länge/Offset in mm, CCD in Grad.

| Größe | Standard REF | Länge | Offset | CCD | Lateral REF | Länge | Offset | CCD |
|---|---|---|---|---|---|---|---|---|
| 6 | 30.00.49-060 | 115 | 37.7 | 130 | 01.00351.001 | 116 | 42.2 | 124.3 |
| 8 | 30.00.49-080 | 132 | 38.9 | 131 | 01.00351.002 | 133 | 43.6 | 125.3 |
| 10 | 30.00.49-100 | 136 | 40.1 | 132 | 01.00351.003 | 137 | 44.9 | 126.3 |
| 12 | 30.00.49-120 | 140.5 | 41.3 | 133 | 01.00351.004 | 140.5 | 46.2 | 127.3 |
| 14 | 30.00.49-140 | 146 | 42.3 | 134 | 01.00351.005 | 146 | 47.3 | 127.7 |
| 16 | 30.00.49-160 | 152.5 | 43.3 | 135 | 01.00351.006 | 152.5 | 48.4 | 128 |

## Anhang: SL-PLUS MIA Längen

Quelle slmia, S. 17–18/PDF 20–21. Getrennte Originalmaße I und II, jeweils mm; keine „einzige Schaftlänge“ aus den beiden Spalten erzeugen. Standard alle aufgeführten Größen, Lateral erst ab Größe 1.

| Größe | Stem length I | Stem length II |
|---|---|---|
| 01 | 128 | 109 |
| 0 | 132 | 113 |
| 1 | 137 | 117 |
| 2 | 141 | 121 |
| 3 | 145 | 124 |
| 4 | 150 | 128 |
| 5 | 154 | 132 |
| 6 | 159 | 136 |
| 7 | 163 | 140 |
| 8 | 168 | 144 |
| 9 | 173 | 148 |
| 10 | 178 | 152 |
| 11 | 183 | 157 |
| 12 | 188 | 162 |

## Nicht übernommen von Grok

- **Grok 1:** Nur Teilabdeckung: Anteile und vollständige Kategorien ergänzt. Häufigkeitsdaten belegen keine zulässigen Paarungen. Gleichstände nicht willkürlich auseinanderziehen.
- **Grok 2:** Ursprüngliches „keine Markenliste Hemi“ wird durch den zutreffenden Nachtrag ersetzt. 2.466/12.580 enthält other combinations; kein reines Top-75%-Subtotal. Tab. 4.16 steht auf S. 95.
- **Grok 3:** Öffentliche regionale Tiroler Produktlisten existieren. Bundesweit/aktuell weiterhin nicht gefunden, aber pauschale AT-Negativaussage zu weit.
- **Grok 4:** Auswahl nur komponenten- und variantengenau; bestehende vier bleiben laut Basis. Ein Ranking verwandter Produkte belegt nicht exakt die gespeicherten Varianten.
- **Grok 5:** Aktuellere EMEA-Quelle vorhanden; HO auch collared; Dysplasia-13-mm-Grenze nicht auf alle CORAIL übertragen.
- **Grok 6:** AU/NZ-Original nicht als EU-Größen-/Kompatibilitätsfreigabe übernehmen. Rankingbefund separat brauchbar.
- **Grok 7:** EMEA-Liner-Konfigurationen bestätigt; alte Größen und Trial-/ROM-Werte nicht als aktuelle vollständige Implantatmatrix übernehmen.
- **Grok 8:** Zementierte Kandidaten durch Register gestützt, konkrete Kopf-/Pfannenfreigaben bleiben zusätzliche Anforderung.
- **Grok 9:** Keine pauschale 13-mm-Regel für sämtliche CORAIL-Köpfe; vollständige Ø-/Offsetmatrix fehlt.
- **Grok 10:** Kein positiver Self-Centering-Befund möglich; bleibt ausdrücklich offen, kein Ersatz durch Cathcart-Unipolar-Häufigkeit.
- **Grok 11:** Grok-Nachtrag zum CORAIL-2018-Rückruf bestätigt; weitere 2017/2018-Meldungen und Umfang der PINNACLE-Aktualisierung ergänzen. „Kein Treffer“ ist keine Rückruffreiheit.
- **Grok 12:** Avenir-Rang nicht Avenir Complete zuschreiben; Fitmore alle vier Familien 1–14 und interner Offsetwiderspruch ergänzen. JP-/US-Unterlagen keine EU-Ersatzfreigabe.
- **Grok 13:** G7 linerabhängig; +5 hat Einschränkungen. Register-Allofit nicht ungeprüft Allofit-S/IT zuordnen; andere Pfannenmatrizen offen.
- **Grok 14:** MS-30-Nachtrag bestätigt; M.E.M./Müller-Bezeichnungen nicht gleichsetzen. CPT-Sicherheitskorrektur ergänzt.
- **Grok 15:** Keine pauschale Alloclassic-8/10-Zuordnung oder regulatorische EU-Freigabe aus funktionellen Charts. Vollständige Einzelkopf-Matrix offen.
- **Grok 16:** Bipolar-Chartfußnote verlangt weitere Kopf-/Artikulationsprüfung; keine transitive Freigabe.
- **Grok 17:** Allofit-Größen 52/II und 54/JJ korrigieren. Protasul-S30 als Edelstahl differenzieren. CPT ergänzen; Avenir-Rückruf-Nachtrag bestätigt.
- **Grok 18:** Öffentliche Enovis-Produktdokumente lesbar; Detailtabellen dennoch offen. optimys-FSN exakt, seleXys-TH+/TPS-AU-Historie getrennt von PC ergänzen.
- **Grok 19:** Keramikbroschüre ersetzt das fehlende named-stem-Kopf-Chart nicht; twinSys-Paarungen bleiben offen.
- **Grok 20:** Historische Tirol-Top-Liste enthält Lima MINIMA-S/Corin MiniHip/Trinity. Nicht auf H-Max oder heutiges AT-Ranking übertragen; angeforderte aktuelle Hauptdokumente noch offen.
- **Grok 21:** SL-MIA-Längen sowie R-2020-04/R-2023-13-Zuordnung geklärt. seleXys-PC-Seiten und X3-26-mm-Matrix in diesem Lauf weiterhin nicht belegt.

## Prüfdatum und selbst geöffnete Quellen

Prüfdatum: **07.10.2026 (UTC)**. Hersteller-PDFs, Behörden-FSNs und Registertabellen wurden selbst geöffnet; Perplexity und Grok dienten nicht als Beleg. Standangaben nennen den Dokumentstand, nicht eine behauptete aktuelle Zulassung. Rückrufprüfung ist eine dokumentierte Recherche im Fenster 07.10.2016–07.10.2026, kein Vollständigkeits- oder Entwarnungsnachweis. Der TGA-Hinweis von 2015 ist ausdrücklich historische Zusatzinformation zum beauftragten Kandidaten. Keine PDF-Volltexte, Herstellerbilder oder Patientendaten übernommen.

### Quelle eprd
EPRD Jahresbericht 2025, Status 5. Stand: 28.10.2025 (Dateistand). Fundstelle: Tab. 53 S. 94–111/PDF 54–62; Tab. 77 S. 204–213/PDF 113–117; Tab. 78 S. 214–221/PDF 118–121. URL: [https://www.eprd.de/fileadmin/user_upload/Dateien/Publikationen/Berichte/Jahresbericht2025-Status5_2025-10-28_F.pdf](https://www.eprd.de/fileadmin/user_upload/Dateien/Publikationen/Berichte/Jahresbericht2025-Status5_2025-10-28_F.pdf).

### Quelle es
EPRD Implantatergebnisse Hüftschäfte. Stand: Jahresbericht 2025; Abruf 07.10.2026. Fundstelle: Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang. URL: [https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftschaefte.xlsx).

### Quelle ep
EPRD Implantatergebnisse Hüftpfannen. Stand: Jahresbericht 2025; Abruf 07.10.2026. Fundstelle: Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang. URL: [https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftpfannen.xlsx](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftpfannen.xlsx).

### Quelle ek
EPRD Implantatergebnisse Hüftversorgungen. Stand: Jahresbericht 2025; Abruf 07.10.2026. Fundstelle: Blatt Tabelle, Kategorie/Trademark/Anzahl; Einzelzeilen im Anhang. URL: [https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftversorgungen.xlsx](https://www.eprd.de/fileadmin/user_upload/Dateien/Tabellen/2025/Implantatergebnisse_Hueftversorgungen.xlsx).

### Quelle siris
SIRIS Report Hip & Knee 2025, Annual Report 2012–2024. Stand: Dezember 2025. Fundstelle: Tab. 4.16 S./PDF 95; 4.19 S./PDF 103; 4.34 S./PDF 129; 4.17 S. 96 ff.. URL: [https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf](https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf).

### Quelle tirol
Hüftendoprothetik in der Europaregion Tirol-Südtirol-Trentino der Operationsjahre 2013 bis 2017. Stand: Februar 2021. Fundstelle: Anhang Tirol, Tab. 62–67, S. 117–119/PDF 123–125. URL: [https://www.iet.at/data.cfm?vpath=publikationen210/prt/euregio-bericht_2013-17_deu](https://www.iet.at/data.cfm?vpath=publikationen210/prt/euregio-bericht_2013-17_deu).

### Quelle at
Hüft- und Knie-Endoprothetik in Österreich. Stand: 27.07.2018. Fundstelle: Abschnitt 4.2, S. 31. URL: [https://www.sozialministerium.gv.at/dam/jcr:a32545b2-d40c-43f2-ac1f-7c6ce97804a8/endoprothetik-bericht_27.07.18_final.pdf](https://www.sozialministerium.gv.at/dam/jcr:a32545b2-d40c-43f2-ac1f-7c6ce97804a8/endoprothetik-bericht_27.07.18_final.pdf).

### Quelle corail
CORAIL Total Hip System Surgical Technique, 198918-211214 UK. Stand: ©2022; EMEA. Fundstelle: S. 11,13,15,20–26/PDF 12,14,16,21–27. URL: [https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf).

### Quelle pinnacle
PINNACLE Hip Solutions Surgical Technique, 142532-220805 EMEA. Stand: ©2022. Fundstelle: S. 8–10/PDF 10–12; S. 16/PDF 18. URL: [https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf](https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf).

### Quelle actis
ACTIS Total Hip System Surgical Technique, 190156-210922 NZ / AU-Ausgabe. Stand: September 2021 NZ; AU 2020. Fundstelle: Warnung S. 8/PDF 10; Technical Specifications S. 12/PDF 14. URL: [https://www.jnjmedtech.com/system/files/pdf/190156.210922%20NZ_134763.200315AU%20ACTIS%20Surgical%20Technique%20FINAL.pdf](https://www.jnjmedtech.com/system/files/pdf/190156.210922%20NZ_134763.200315AU%20ACTIS%20Surgical%20Technique%20FINAL.pdf).

### Quelle fitmore
Fitmore Hip Stem Surgical Technique, 1013.3-GLBL-en. Stand: 2025-04. Fundstelle: S. 12–16/PDF 14–18; Bestelltabellen S. 16 ff.. URL: [https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/fitmore/1013.3-GLBL-en%20Fitmore%20Hip%20Stem%20Surg%20Tech%20A4%20DIGITAL.pdf](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/fitmore/1013.3-GLBL-en%20Fitmore%20Hip%20Stem%20Surg%20Tech%20A4%20DIGITAL.pdf).

### Quelle ms30
MS-30 Cemented Hip Stem Surgical Technique, 5087.1-GLBL-en. Stand: 2025-12. Fundstelle: S./PDF 25–26,29–30. URL: [https://assets.ctfassets.net/rc4arfpyhdpw/141dC8Nk3O5X6zFJkF1ba2/11cb417e096fc3f917a1cebfee73a33b/5087.1-GLBL-en_MS-30_Cemented_Hip_Stem_Upgraded_Instruments_Surg_Tech_A4_DIGITAL.pdf](https://assets.ctfassets.net/rc4arfpyhdpw/141dC8Nk3O5X6zFJkF1ba2/11cb417e096fc3f917a1cebfee73a33b/5087.1-GLBL-en_MS-30_Cemented_Hip_Stem_Upgraded_Instruments_Surg_Tech_A4_DIGITAL.pdf).

### Quelle avenir
Avenir Complete Surgical Technique, 1624.4-GLBL-en. Stand: 2021-11-10. Fundstelle: S./PDF 7,9; Ausgabe insgesamt 12 PDF-Seiten. URL: [https://assets.ctfassets.net/rc4arfpyhdpw/4PulT0mR4JdEX4f5n00BxC/88cc646adbb9dbc5309025ed0769cd3e/1624.4-GLBL-en_Avenir_SurgTech.pdf](https://assets.ctfassets.net/rc4arfpyhdpw/4PulT0mR4JdEX4f5n00BxC/88cc646adbb9dbc5309025ed0769cd3e/1624.4-GLBL-en_Avenir_SurgTech.pdf).

### Quelle ceramic
Head and Stem Combinations: Ceramic Femoral Heads. Stand: Revised 5/6/2019 (Originalschreibweise). Fundstelle: PDF 1–3; insbesondere Zeilen Alloclassic/Avenir/CLS/Fitmore auf PDF 1 und Fußnoten. URL: [https://assets.ctfassets.net/rc4arfpyhdpw/6LuflsxnuxzS6yod8Wbg5c/75d5c277cb99658423118798f590191e/Ceramic_Femoral_Heads_NEW.pdf](https://assets.ctfassets.net/rc4arfpyhdpw/6LuflsxnuxzS6yod8Wbg5c/75d5c277cb99658423118798f590191e/Ceramic_Femoral_Heads_NEW.pdf).

### Quelle cocr
Head and Stem Combinations: CoCr Femoral Heads. Stand: Revised 7/15/2020. Fundstelle: PDF 1–3, produktspezifische Spalten und Fußnoten. URL: [https://assets.ctfassets.net/rc4arfpyhdpw/iV1BfgVRHhLqYPmt2Zt2G/bc7ac72e2ad60e1eed7f7d9f5628fa51/CoCr-Femoral-Heads_NEW.pdf](https://assets.ctfassets.net/rc4arfpyhdpw/iV1BfgVRHhLqYPmt2Zt2G/bc7ac72e2ad60e1eed7f7d9f5628fa51/CoCr-Femoral-Heads_NEW.pdf).

### Quelle bipolar
Head and Stem Combinations: Unipolar and Bipolar Femoral Heads. Stand: Revised 5/6/2019 (Originalschreibweise). Fundstelle: PDF 1–2, Zeile MS-30 auf PDF 2 und Fußnote 1. URL: [https://assets.ctfassets.net/rc4arfpyhdpw/32LNW4qj9EF9gZTbsgW3XK/aff2b857d83db63fa9441c1d96e1237d/Unipolar_and_Bipolar_Femoral_Heads_NEW.pdf](https://assets.ctfassets.net/rc4arfpyhdpw/32LNW4qj9EF9gZTbsgW3XK/aff2b857d83db63fa9441c1d96e1237d/Unipolar_and_Bipolar_Femoral_Heads_NEW.pdf).

### Quelle g7
G7 Acetabular System Surgical Technique, 2336.6-GLBL-en. Stand: 2026-09-09. Fundstelle: S. 3–5/PDF 6–8; Keramik S. 7/PDF 10. URL: [https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/g7-acetabular-system/2336.6-GLBL-en%20G7%20Acetabular%20System%20Surgical%20Technique.pdf](https://www.zimmerbiomet.com/content/dam/zb-corporate/en/education-resources/surgical-techniques/specialties/hip/g7-acetabular-system/2336.6-GLBL-en%20G7%20Acetabular%20System%20Surgical%20Technique.pdf).

### Quelle fcorail18
DePuy Urgent Field Safety Notice PIE-1104627 / BfArM 02257-18. Stand: Februar 2018. Fundstelle: PDF 1–3. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2018/02257-18_kundeninfo_en.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2018/02257-18_kundeninfo_en.pdf?__blob=publicationFile).

### Quelle fcorail17
DePuy Sicherheitsinformation PIE-863755 / BfArM 07375-17. Stand: Juli 2017. Fundstelle: PDF 1–3. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07375-17_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07375-17_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle ftrial
DePuy Sicherheitsinformation PIE-1125109 / BfArM 06669-18. Stand: Mai 2018. Fundstelle: PDF 1–2. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/06/2018/06669-18_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/06/2018/06669-18_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle fpinnacle
DePuy aktualisierte Sicherheitsinformation PINNACLE, Ref. 1896433 / BfArM 22108-20. Stand: 18.02.2021. Fundstelle: PDF 1–4. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2021/22108-20_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2021/22108-20_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle favenir
Zimmer Biomet ZFA2018-00572, FA2018-06 / BfArM 13742-18. Stand: 31.10.2018. Fundstelle: PDF 1. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/13742-18_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/13742-18_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle fmetal
Zimmer Biomet FA 2016-10, ZFA 2016-150 / BfArM 01461-17. Stand: 13.02.2017. Fundstelle: PDF 1–2. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/01461-17_Kundeninfo_de.pdf?__blob=publicationFile&v=1](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/01461-17_Kundeninfo_de.pdf?__blob=publicationFile&v=1).

### Quelle fcpt
Zimmer Biomet ZFA2024-00121 / BfArM 21393-24, CPT. Stand: 01.07.2024. Fundstelle: PDF 1–2. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/21393-24_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2024/21393-24_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle fallofit
Zimmer Biomet ZFA2019-00187 / BfArM 10144-19, Allofit-S Alloclassic. Stand: 30.07.2019. Fundstelle: PDF 1, Produkttabelle. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2019/10144-19_kundeninfo_en.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2019/10144-19_kundeninfo_en.pdf?__blob=publicationFile).

### Quelle foptimys
Mathys FSCA 17/02 / BfArM 07038-17, optimys. Stand: 18.07.2017 (Schreiben; Portal 20.07.2017). Fundstelle: PDF 1. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07038-17_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07038-17_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle fr2020
Smith+Nephew Physician Communication, R-2020-04 / BfArM 05608-20. Stand: 2020; undatiertes Update im geöffneten PDF. Fundstelle: PDF 1, Affected Product/Background/Actions. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2020/05608-20_kundeninfo_en.pdf?__blob=publicationFile&v=1](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2020/05608-20_kundeninfo_en.pdf?__blob=publicationFile&v=1).

### Quelle fr2023
Smith+Nephew Dringender Sicherheitshinweis, R-2023-13 / BfArM 35762-23. Stand: 20.11.2023. Fundstelle: PDF 1–2. URL: [https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile).

### Quelle slmia
SL-PLUS MIA Surgical Technique, 31156-en V2. Stand: 11/2024. Fundstelle: S. 17–18/PDF 20–21; Warnungen S. 2/PDF 5. URL: [https://smith-nephew.stylelabs.cloud/api/public/content/c38ee11595e14dfdbdd7ade71a170ac9?v=3e0dbffa&download=true](https://smith-nephew.stylelabs.cloud/api/public/content/c38ee11595e14dfdbdd7ade71a170ac9?v=3e0dbffa&download=true).

### Quelle optimys
Enovis optimys – Produktseite. Stand: undatiert, Abruf 07.10.2026. Fundstelle: Product details/Bone Preservation. URL: [https://enovis-surgical.com/en/products/325/optimys.html](https://enovis-surgical.com/en/products/325/optimys.html).

### Quelle rm
RM Pressfit vitamys Product Information, 336.010.121 03-0123-01. Stand: 2023-01. Fundstelle: PDF 2–5, Monoblockkonzept. URL: [https://enovis-surgical.com/repo/storage/4724/file/produktinformation_rm-pressfit_en_v3.0.pdf](https://enovis-surgical.com/repo/storage/4724/file/produktinformation_rm-pressfit_en_v3.0.pdf).

### Quelle heads
Mathys Ceramic Product Information, 336.010.127 03-0319-01. Stand: 2019-03. Fundstelle: PDF 2–3, ceramys/symarec und Gleitpaarung. URL: [https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf](https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf).

### Quelle tga
TGA: SeleXys TH+ and TPS acetabular shells used in hip replacements. Stand: 16.09.2015; historisch, Australien. Fundstelle: Hazard alert; Lieferende/ARTG und Abgrenzung PC. URL: [https://www.tga.gov.au/safety/recalls-and-other-market-actions/market-actions/selexys-th-and-tps-acetabular-shells-used-hip-replacements](https://www.tga.gov.au/safety/recalls-and-other-market-actions/market-actions/selexys-th-and-tps-acetabular-shells-used-hip-replacements).

