ÄNDERN
Astra – Lauf 2026-10-07T03:55Z

Prüfung ausschließlich des Extra-Laufs 001-implantate, Basis A–E (22 Punkte), mit zwei zusätzlichen Befunden innerhalb dieses Umfangs. Keine klinische Freigabe. Ergebnis: 24 Prüfpunkte, davon 8 „Grok bestätigt“ und 16 eigene/korrigierte Bewertungen. „ok“ bei offenen Punkten heißt: Offenlassen ist richtig, nicht: Produkt freigegeben.

Laufnachweis: Grok-Datei aus Commit ef570eb4a23aaf083cd822e5a4b8fb464d486703, Commitdatum 07.10.2026 04:19:40Z, Laufkennung 2026-10-07T03:55Z. Bei Prüfstart keine 001-implantate-astra.md und kein Datei-Commitverlauf vorhanden. 000/001 bereits abgeschlossen; deren Astra-Dateien bereits gelöscht (87359a8 / 9af2f87). Basis-JSON und separater Quellen-Auftrag sind für diesen Extra-Lauf nicht vorhanden; die vier Implantat-JSONs sowie die 22 Quellenaufträge in 001-implantate-basis.md bilden den Prüfumfang. Perplexity-2 wurde als Fundstellenliste, nicht als Beleg verwendet.

Quellenschlüssel in Tabelle/Chips verweisen auf das Quellenverzeichnis mit Titel, Stand, gedruckter und PDF-Seite sowie Markt. Alle Zahlen sind Dokumentwerte, keine operative Auswahlentscheidung oder heutige Bestands-/EU-Freigabe. Quelle:null kennzeichnet offene Produktnachweise. Chip-Mengen bleiben null, weil hier Stammdaten geprüft werden, keine Materialanforderung.

## Prüftabelle

Sicherheitskritische Korrekturen zuerst; Nummern 1–22 entsprechen Grok/Basis, 23–24 sind zusätzliche Astra-Punkte.

| Nr | Von (Grok bestätigt / Astra) | ok/Fehler | Problem | Endgültiger Text im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|---|
| 5 | Astra | Fehler | Grok nennt FDA-Status, lässt aber aktualisierten Produkt-/Chargenumfang und Länderhinweis weg. LFIT-Status gilt für den einzelnen FDA-Datensatz, nicht die gesamte EU-Maßnahme. | `{"abschnitt":"implantate","label":"Rückrufstatus getrennt führen","menge":null,"einheit":null,"spez":"T5 übernehmen: Z-2299-2018 beendet 08.05.2020; Z-0842-2022 Open, Classified, aktualisiert nur Charge 89648802 der REF 6570-0-032. EU-RA nicht automatisch gleichsetzen. EU-Abschluss offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["fda-lfit","fda-delta","stryker-accolade-ii-rec2","stryker-accolade-ii-rec3"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [fda-lfit: FDA Class 2 Device Recall LFIT Anatomic V40 Femoral Head; Z-2299-2018, Event 80059; HTML Product, Code Information, Recall Status; beendet 08.05.2020, Abruf 07.10.2026; US-Datensatz](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm?ID=164630); [fda-delta: FDA Class 2 Device Recall BIOLOX delta Ceramic V40 Femoral Head; Z-0842-2022, Event 89592, PFA 2902313; HTML Recall Status, Product, Code Information, Action/Distribution; Update 17.03.2022, Abruf 07.10.2026; US-Datensatz mit Länderhinweisen](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id=191999); [stryker-accolade-ii-rec2: Stryker — Dringende Sicherheitsinformation RA2018-1757583, LFIT CoCr V40; 12.06.2018; PDF 1–2; DE über BfArM, Kennung 06604/18](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/06604-18_kundeninfo_de.pdf?__blob=publicationFile); [stryker-accolade-ii-rec3: Stryker — Dringende Sicherheitsinformation RA2022-2911584, BIOLOX delta V40; 18.01.2022; PDF 1 Produkt-/Chargentabelle und Statushinweis; DE über BfArM, Kennung 01953/22](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2022/01953-22_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 7 | Astra | Fehler | Größen/REF richtig; CCD steht gedr. S. 11, nicht S. 10. Kopfzulassung nicht pauschal aus dem Konus ableiten. | `{"abschnitt":"implantate","label":"Excia T getrennte Varianten","menge":null,"einheit":null,"spez":"T7: zementfrei 8–20 in 1er-Schritten; zementiert 10/12/14/16/18/20. Standard 135°, TL 128° (+6 mm Offset), gedr. S. 11/PDF 6. BIOLOX-delta- und Metallköpfe nur konkrete Reihen gedr. S. 19/PDF 10.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["e1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [e1: Aesculap Excia T Hüftschaft; Nr. 4008516, 01/2026; gedr. 11/PDF 6, gedr. 18–19/PDF 10, Kennung PDF 13; DE](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf) | hoch |
| 8 | Astra | Fehler | Grok verkürzt Liner- und Kopfzuordnung: nicht jeder kleinere Kopf passt in jede größere Pfanne; ISODUR F 22,2 hat nur M/L. | `{"abschnitt":"implantate","label":"Plasmafit Varianten präzisieren","menge":null,"einheit":null,"spez":"T8 übernehmen. Poly ausschließlich PE; Plus Keramik oder PE. Hausvariante Plus/Plus 3/Plus 7 und Liner-Form getrennt bestimmen. Ø22,2-Metallkopf nicht allein über Plasmafit auf Excia T freigeben.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["e2","e1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [e2: Aesculap Plasmafit — Acetabular Cup System; O45502 0718/1/4, 07/2018; gedr.=PDF S. 5–7, 18–21, 24, Kennung 34; EN auf DE-Herstellerseite](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf); [e1: Aesculap Excia T Hüftschaft; Nr. 4008516, 01/2026; gedr. 11/PDF 6, gedr. 18–19/PDF 10, Kennung PDF 13; DE](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf) | hoch |
| 9 | Astra | Fehler | Excia 12/14 und Excia T sind getrennt. Groks Satz, Kopf-REF dürften für 12/14 genutzt werden, ist als allgemeine Konusfreigabe zu weit. | `{"abschnitt":"implantate","label":"Excia ist nicht Excia T","menge":null,"einheit":null,"spez":"O90301 nur zur Abgrenzung: Excia 12/14 zementiert Standard 9–18, lateral 10–18; nicht auf Excia T übertragen. Excia-T-Köpfe aus 4008516 S. 19 statt aus gemeinsamem Konus ableiten.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["excia-old","e1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [excia-old: Aesculap Excia 12/14; O90301 1119/PDF/5, 11/2019; gedr.=PDF S. 14, 16; DE, ausdrücklich andere Schaftlinie](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-1214.pdf); [e1: Aesculap Excia T Hüftschaft; Nr. 4008516, 01/2026; gedr. 11/PDF 6, gedr. 18–19/PDF 10, Kennung PDF 13; DE](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf) | hoch |
| 12 | Astra | Fehler | Ed. 05/26 V12 bestätigt. Groks Sammelfreigabe übergeht rote Zellen: BIOLOX OPTION 40 XL ist nicht freigegeben; 26 mm und +16 unterscheiden sich nach Schaft. | `{"abschnitt":"implantate","label":"S+N Kopf-Schaft-Matrix","menge":null,"einheit":null,"spez":"T12 einschließlich Nein-Zeilen übernehmen. SL-PLUS MIA Größe 01 ist SAP 75000172; hochgestellte 3 ist Fußnote, keine Größe 013. BIOLOX OPTION nicht als Haus-BIOLOX-delta umetikettieren.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["matrix"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [matrix: Smith+Nephew — Hip implant compatibility matrix; Lit. No. 04758, Ed. 05/26 V12; S. 2/7 und 6/7, Länder-/IFU-Vermerke auf den Matrixseiten; international mit lokalen Zulassungsvorbehalten](https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de) | hoch |
| 14 | Astra | Fehler | Größen, Längen, REF und 131° stimmen; Specs-Seite ist gedr. 1/PDF 4, nicht gedr. 3. Katalog gedr. 12/PDF 15. | `{"abschnitt":"implantate","label":"SPECTRON EF Größen","menge":null,"einheit":null,"spez":"T14 übernehmen; 1–5 Standard und 1H–5H High Offset getrennt. 12/14 S+N; konkrete Kopf-Paarung nach T12. Marktfreigabe der aktuellen lokalen IFU offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["s3"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [s3: SPECTRON EF — Surgical Technique; 21885 V3, 71380478 REVB 03/23, ©2023; gedr. 1/PDF 4, gedr. 12/PDF 15, gedr. 14/PDF 17, gedr. 16/PDF 19, Kennung PDF 20; EN, keine pauschale EU-Freigabe abgeleitet](https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true) | hoch |
| 15 | Astra | Fehler | R3-Grafik ist visuell lesbar; Groks Offenlassen wäre unnötig. Katalog ist kein vollständiges Kreuzprodukt aller Ø und Schalen. | `{"abschnitt":"implantate","label":"R3 XLPE Zuordnung","menge":null,"einheit":null,"spez":"T15 übernimmt die markierten Schale/Inlay-Zellen; Varianten 0°,20°,0°+4,20°+4 und REF getrennt. Aktuelle EU-IFU offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["s4"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [s4: R3 Acetabular System — Operationstechnik; 7138-1560-de REVB 06/12, ©2017; gedr.=PDF S. 13, 17–18, Kennung 32; DE](https://smith-nephew-delivery.stylelabs.cloud/api/public/content/1bd7a20b4fdf4a158b95aad5987f2686?v=e321be27&download=true) | hoch |
| 17 | Astra | Fehler | TANDEM/SPECTRON-EF-Paarung belegt, Gleichsetzung des unspezifischen Hausnamens Bi-Polar Head mit TANDEM unbewiesen. Fußnoten * und ** nicht verwechseln. | `{"abschnitt":"implantate","label":"TANDEM Hausidentität offen","menge":null,"einheit":null,"spez":"Herstellerkandidat TANDEM Bipolar getrennt vom ungeklärten Hausprodukt führen. PDF 17: SPECTRON EF mit TANDEM Bipolar und S+N OXINIUM/CoCr 12/14, Innenkopf 22/28 mm. Keine BIOLOX-delta-Freigabe daraus. Haus-REF und lokale Geltung prüfen.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["tandem","s3"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [tandem: TANDEM Bipolar and Unipolar Hip System — INTL Surgical Technique; 29073 V2, 71380925 REVA 02/23; unnummerierte PDF 17 Implant Compatibility, Kennung PDF 20; INTL mit expliziten EU-Fußnoten](https://smith-nephew.stylelabs.cloud/api/public/content/8af4fc46aafd4be4a8d289f62a72ee8e?download=true&v=bdf205cd); [s3: SPECTRON EF — Surgical Technique; 21885 V3, 71380478 REVB 03/23, ©2023; gedr. 1/PDF 4, gedr. 12/PDF 15, gedr. 14/PDF 17, gedr. 16/PDF 19, Kennung PDF 20; EN, keine pauschale EU-Freigabe abgeleitet](https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true) | hoch |
| 18 | Astra | Fehler | R-2020-04-Update enthält mehr als Groks Nicht-gefunden-Aussage: betroffene Geräte seien bereits abgewickelt/zurückgesandt. Das ist kein behördlicher Abschlussstatus. | `{"abschnitt":"implantate","label":"R3 Maßnahmenstatus ergänzen","menge":null,"einheit":null,"spez":"R-2023-13: REF 71331854, Charge 23HM03659, Brief 20.11.2023. R-2020-04: Hersteller-Rücknahmehinweis aus PDF 1 dokumentieren; heutiger regulatorischer Abschluss und Hausbestand weiterhin ungeklärt.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["smith-nephew-r3-rec1","smith-nephew-r3-rec2"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [smith-nephew-r3-rec1: Smith+Nephew — Physician Communication, R-2020-04, R3 Acetabular Liners; Brief ohne sichtbares Tagesdatum, BfArM-Ablage 2020/05608-20; PDF 1 Rücknahmehinweis, 2 Rückmeldeformular; EN über BfArM](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2020/05608-20_kundeninfo_en.pdf?__blob=publicationFile); [smith-nephew-r3-rec2: Smith+Nephew — Dringende Sicherheitsinformation R-2023-13, R3 XLPE 20 DEG ACET LNR; 20.11.2023; PDF 1–2; DE über BfArM, Kennung 35762-23](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile) | hoch |
| 19 | Astra | Fehler | Pauschal nur HCP-Gate ist widerlegt. twinSys- und CCB-PDFs öffentlich gelesen; konkrete Zugriffsergebnisse statt allgemeinem Login-Hindernis erfassen. | `{"abschnitt":"implantate","label":"Enovis Originale ergänzen","menge":null,"einheit":null,"spez":"T19: twinSys-Größen/REF aus Flyer 2024-02 PDF 7. T19b: CCB-Unterlage 2020-02 PDF 21–22 mit Profil-/Kopfzuordnung und Verstärkungsringpflicht. Keramik-Flyer 2019-03 lesbar; keine allgemeine twinSys-Kopffreigabe daraus.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["twinsys","ccb","ceramics"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [twinsys: twinSys — Product Information; Item 336.010.078 / 04-0224-01 / 2024-02; PDF 7 Ordering information (unnummeriert), Kennung PDF 8; EN/international](https://enovis-surgical.com/repo/storage/4721/file/EN_TSS_ProdInfo_V04%20%281%29.pdf); [ccb: CCB cup — CCE roof reinforcement ring, Surgical Technique/Product Information; Item 336.010.151 / 01-0220-01 / 2020-02; gedr.=PDF S. 21–22, Kennung 32; EN/international](https://enovis-surgical.com/repo/storage/4723/file/op-technik_produktinfo-ccb-cce_en_v1.0.pdf); [ceramics: Mathys — Ceramic implants, Product Information; Item 336.010.127 / 03-0319-01 / 2019-03; PDF 1–6, Kennung PDF 8; EN/international, keine konkrete twinSys-Paarung daraus übernommen](https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf) | hoch |
| 22 | Astra | Fehler | Groks allgemeine Paarungen verlieren Varianten, Kopfgrößen, Fußnoten und Marktgrenzen. Ein bloßes Komponenten-ID-Paar ist dafür zu grob. | `{"abschnitt":"implantate","label":"Paarungen mit Bedingungen","menge":null,"einheit":null,"spez":"Stabile IDs; haus nur dokumentierte Hausliste. passt_zu je Variante mit Kopf-Ø, Offset, Schaftgröße, Linerform, Alpha, erforderlicher Hülse, Markt, Quellenstand und Seite. Ungeprüft≠verboten≠freigegeben. Hausname≠Herstelleridentität. Rückrufe mit Komponenten-ID UND REF/Charge/Herstellzeitraum/Markt/Statusdatum. Keine transitiven Freigaben.","gilt_fuer":["001"],"optional":false,"sicherheit":"hausabhängig","hausabhaengig":true,"quelle":["q5","matrix","tandem"],"hinweis":"Datenmodellvorschlag Astra; konkrete Paarungen ausschließlich aus den belegten Tabellen."}` | [q5: Trident II Tritanium — Surgical protocol; TRITRI-SP-3_Rev-6_29553, ©2022; gedr.=PDF S. 2, 4, 20–21, Kennung 31; EU/Canada, Eccentric 0° ausdrücklich ausgenommen](https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf); [matrix: Smith+Nephew — Hip implant compatibility matrix; Lit. No. 04758, Ed. 05/26 V12; S. 2/7 und 6/7, Länder-/IFU-Vermerke auf den Matrixseiten; international mit lokalen Zulassungsvorbehalten](https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de); [tandem: TANDEM Bipolar and Unipolar Hip System — INTL Surgical Technique; 29073 V2, 71380925 REVA 02/23; unnummerierte PDF 17 Implant Compatibility, Kennung PDF 20; INTL mit expliziten EU-Fußnoten](https://smith-nephew.stylelabs.cloud/api/public/content/8af4fc46aafd4be4a8d289f62a72ee8e?download=true&v=bdf205cd) | hoch |
| 23 | Astra | Fehler | Eigener Befund: TRITRI Tabelle 1 lässt 26 mm aus, Katalog S. 21 listet X3 10° 26C–26J. Das darf nicht stillschweigend vereinheitlicht werden. | `{"abschnitt":"implantate","label":"X3 26 mm Quellenkonflikt","menge":null,"einheit":null,"spez":"26-mm-X3-Zuordnung gesondert als Quellenwiderspruch führen. REF 623-10-26C oder 723-10-26C ist katalogisiert; keine automatische EU-Paarungsfreigabe aus der unvollständigen Tabelle 1 ableiten. Hersteller/aktuelle IFU klären.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["q5"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [q5: Trident II Tritanium — Surgical protocol; TRITRI-SP-3_Rev-6_29553, ©2022; gedr.=PDF S. 2, 4, 20–21, Kennung 31; EU/Canada, Eccentric 0° ausdrücklich ausgenommen](https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf) | hoch |
| 24 | Astra | Fehler | Eigener Befund: SL-PLUS-MIA-Dokument enthält abweichende Längen: Größen 1/2/6 in Dimensions 137/141/159, im Implantatkatalog 136/140/158 mm. | `{"abschnitt":"implantate","label":"SL-PLUS MIA Längen offen","menge":null,"einheit":null,"spez":"Größen/SAP dürfen übernommen werden, strittige Längen bis Herstellerklärung null lassen. Nicht die gesamte Dimensions-Tabelle als Kompatibilitätsnachweis nutzen; aktuelle Matrix sperrt +16 bei Größe 01.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["s1","matrix"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [s1: SL-PLUS MIA — Surgical Technique; 00884-en (1524) V4, 01/15; gedr. 16–19/PDF 18–21, Kennung PDF 28; EN/international](https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true); [matrix: Smith+Nephew — Hip implant compatibility matrix; Lit. No. 04758, Ed. 05/26 V12; S. 2/7 und 6/7, Länder-/IFU-Vermerke auf den Matrixseiten; international mit lokalen Zulassungsvorbehalten](https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de) | hoch |
| 1 | Grok bestätigt | ok | Größen/CCD und Trennung Raspel-REF gegenüber Implantat-REF stimmen. | `{"abschnitt":"implantate","label":"Accolade II Größen","menge":null,"einheit":null,"spez":"0–11; Standard 132°, High Offset 127°. Halsproben: 0/1=27 mm gelb, 2/3=30 mm blau, 4/5/6=35 mm grün, 7/8/9=37 mm schwarz, 10/11=40 mm rot. 1020-5200 bis 1020-5211 sind Raspeln; Schaft-REF bleibt offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["q1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [q1: Accolade II Femoral Hip System — Surgical protocol; ACCII-SP-1_Rev-4_34423, ©2022; gedr.=PDF S. 3–5, 11–12, 22, 24, Kennung 25; global mit getrennten EU/EMEA-/Australien-Indikationen](https://cdn.stryker.com/SYKGCSDOC-2-45343) | mittel |
| 2 | Grok bestätigt | ok | LFIT- und BIOLOX-delta-V40-Tabelle auf S. 12 stimmt. | `{"abschnitt":"implantate","label":"V40 Kopfgrößen und Offsets","menge":null,"einheit":null,"spez":"Tabelle T2 übernehmen; LFIT 6260-9-XXX und BIOLOX delta V40 6570-0-XXX getrennt führen. Keine Einzel-REF aus XXX bilden.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["q1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [q1: Accolade II Femoral Hip System — Surgical protocol; ACCII-SP-1_Rev-4_34423, ©2022; gedr.=PDF S. 3–5, 11–12, 22, 24, Kennung 25; global mit getrennten EU/EMEA-/Australien-Indikationen](https://cdn.stryker.com/SYKGCSDOC-2-45343) | hoch |
| 3 | Grok bestätigt | ok | Tabelle für X3 0°/10° samt †-Fußnote stimmt; nur für diesen Tabellenausschnitt. Eigener Quellenkonflikt zu 26 mm: Nr. 23. | `{"abschnitt":"implantate","label":"Trident II und X3","menge":null,"einheit":null,"spez":"T3 übernehmen. Solidback/Clusterhole 42–66 mm, Multihole 42–72 mm, jeweils 2-mm-Schritte. X3 Eccentric 0° laut Dokument nicht CE-markiert/nicht EU-vermarktet.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["q5"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [q5: Trident II Tritanium — Surgical protocol; TRITRI-SP-3_Rev-6_29553, ©2022; gedr.=PDF S. 2, 4, 20–21, Kennung 31; EU/Canada, Eccentric 0° ausdrücklich ausgenommen](https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf) | hoch |
| 4 | Grok bestätigt | ok | EU-IFUs im öffentlichen Abruf nicht erhalten; BR-Fundstelle ersetzt sie nicht. | `{"abschnitt":"implantate","label":"Stryker EU-IFU offen","menge":null,"einheit":null,"spez":"Accolade II, V40 und Trident X3: produktspezifischer aktueller EU-IFU-Nachweis bleibt offen; QIN4351 nicht als EU-Freigabe behandeln.","gilt_fuer":["001"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"Abruf Stryker-Portal und BR-Link dokumentiert; kein Beweis, dass eine EU-IFU nicht existiert."}` | Kein belastbarer Produktnachweis; Suchbefund siehe Quellenverzeichnis. | hoch |
| 6 | Grok bestätigt | ok | Tray Layout gelesen; Metadaten stimmen. | `{"abschnitt":"implantate","label":"Accolade II Tray-Quelle","menge":null,"einheit":null,"spez":"q2: ACCII-TL-1_25643, ©2020, PDF 1–3, CE-/Markthinweis PDF 3; Basic tray PDF 1, Broach tray PDF 2. Kein Schaftimplantat-Katalog.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["q2"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [q2: Accolade II — Tray Layout; ACCII-TL-1_25643, ©2020; PDF 1–3, unnummeriert; CE-/Marktvorbehalt PDF 3](https://www.stryker.com/content/dam/stryker/joint-replacement/products/accoladeii/resources/Accolade%20II%20Tray%20Layout_ACCII-TL-1_25643.pdf) | mittel |
| 10 | Grok bestätigt | ok | Hersteller-Anwendungstext belegt Bipolarpfanne plus zementierten Excia-T-Gradschaft; keine konkrete REF-/Kopf-/Größen-Freigabetabelle gefunden. | `{"abschnitt":"implantate","label":"Bipolar Cup Freigabe offen","menge":null,"einheit":null,"spez":"Hausangabe beibehalten; Anwendungstext als Fundstelle verlinken. Freigabe der konkreten Bipolar-Cup/Kopf/Schaft-Kombination bleibt offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"hausabhängig","hausabhaengig":true,"quelle":["bb-web","e3"],"hinweis":"HTML-Anwendungsbeispiel und Katalogfamilie sind keine vollständige lokale IFU-/REF-Paarung."}` | [bb-web: B. Braun — Zementierte Hüftprothese; undatiertes HTML, Abruf 07.10.2026; Abschnitt Operationstechniken; DE](https://www.bbraun.de/de/produkte-und-loesungen/therapien/orthopaedischer-gelenkersatz-und-regenerative-therapien/hueftendoprothetik/zementierte-hueftprothese.html); [e3: Aesculap Bipolar Cup, PRID00004418; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; internationaler EN-Katalog](https://catalogs.bbraun.com/en-01/p/PRID00004418/bipolar-cup) | hoch |
| 11 | Grok bestätigt | ok | Cemented Polyethylene Cups ist Katalogfamilie, keine identifizierte Hausvariante. | `{"abschnitt":"implantate","label":"Aesculap PE-Pfanne bestimmen","menge":null,"einheit":null,"spez":"Katalog PRID00002464 als Fundstelle behalten; Produktname/Profil/REF der Hauspfanne und EU-IFU offen. Keine Einzelgrößen oder Freigaben aus der Familienbeschreibung erzeugen.","gilt_fuer":["001"],"optional":false,"sicherheit":"hausabhängig","hausabhaengig":true,"quelle":["e4"],"hinweis":"Hausprodukt anhand Etikett identifizieren; Familie nicht als Müller-Pfanne umbenennen."}` | [e4: Aesculap Cemented Polyethylene Cups, PRID00002464; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; internationaler EN-Katalog](https://catalogs.bbraun.com/en-01/p/PRID00002464/cemented-polyethylene-cups) | mittel |
| 13 | Grok bestätigt | ok | Größen/SAP-Reihen und CCD stimmen; Maßkonflikt bei Längen separat Nr. 24. | `{"abschnitt":"implantate","label":"SL-PLUS MIA Größen","menge":null,"einheit":null,"spez":"Standard: 01,0,1–12; lateral: 1–12. 11/12 optionale Sondergrößen. CCD 131°/123°. SAP Standard 75000172–75000185; lateral 75000186–75000197. T13 führt jede Größe einzeln.","gilt_fuer":["001"],"optional":false,"sicherheit":"belegt","hausabhaengig":false,"quelle":["s1"],"hinweis":"Dokumentstand und Markt beachten; aktuelle lokale IFU vor Anwendung prüfen."}` | [s1: SL-PLUS MIA — Surgical Technique; 00884-en (1524) V4, 01/15; gedr. 16–19/PDF 18–21, Kennung PDF 28; EN/international](https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true) | mittel |
| 16 | Astra | ok | Zusätzliche offizielle REFLECTION-OP-Technik gefunden; aktuelle EU-Geltung und Müller-Hauspfanne damit nicht geklärt. | `{"abschnitt":"implantate","label":"REFLECTION EU-Nachweis offen","menge":null,"einheit":null,"spez":"00811 V1 10/13, ©2013 als historische EN-Fundstelle ergänzen; keine aktuellen EU-Größen/Paarungen daraus freigeben. REFLECTION All-Poly und Müller-PE-Identifikation bleiben offen.","gilt_fuer":["001"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":["reflection"],"hinweis":"Fremdmarkt-/Altunterlage und JP-Dokument ersetzen keine aktuelle lokale EU-IFU."}` | [reflection: REFLECTION — Surgical Technique; 00811 V1, 10/13, ©2013; PDF Titelblatt und Dokumentende/Impressum; historische EN-Unterlage mit US-Angaben und EC-Vertreter, kein aktueller EU-Nachweis](https://smith-nephew.stylelabs.cloud/api/public/content/7cada363f2224bc3957ac5e0fde018ad?download=true&v=eca89761) | hoch |
| 20 | Astra | ok | seleXys-PC-Altlink leitet auf Enovis-Startseite um; Katalogtreffer ebenfalls kein abrufbares PDF. Das belegt kein generelles Login-Erfordernis. | `{"abschnitt":"implantate","label":"PE-Inlay Zuordnung offen","menge":null,"einheit":null,"spez":"seleXys PC und PE-Inlay Standard: genaue Linerbezeichnung/Pfannenzuordnung, Größen und REF bleiben offen. RM Classic nicht mit einem zusätzlichen modularen Inlay ausstatten; Hersteller führt Monoblockpfanne.","gilt_fuer":["001"],"optional":false,"sicherheit":"offen","hausabhaengig":false,"quelle":null,"hinweis":"RM-Classic-HTML und erfolglose seleXys/Katalog-Abrufe siehe Quellenverzeichnis; fehlender Nachweis ist keine Paarung."}` | Kein belastbarer Produktnachweis; Suchbefund siehe Quellenverzeichnis. | hoch |
| 21 | Astra | ok | Bipolar-Produktseite lesbar, enthält aber keine ausdrücklich geprüfte Bipolar/twinSys-zementiert-Freigabe. | `{"abschnitt":"implantate","label":"Mathys Bipolar Paarung offen","menge":null,"einheit":null,"spez":"Hausangabe unverändert als Hausangabe; konkrete Bipolar-Innenkopf-Schaft-Kombination und EU-IFU bleiben offen. Keine Freigabe aus 12/14 oder der gemeinsamen Marke ableiten.","gilt_fuer":["001"],"optional":false,"sicherheit":"hausabhängig","hausabhaengig":true,"quelle":["enovis-bipolar"],"hinweis":"Web-Familiengrößen nicht als produktspezifische PDF-Wertetabelle übernehmen."}` | [enovis-bipolar: Enovis — Bipolar; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; EN/international, keine explizite twinSys-Paarung](https://enovis-surgical.com/en/products/335/bipolar.html) | hoch |

## Geprüfte Wertetabellen

Die folgenden Tabellen sind Teil der endgültigen Änderungsvorschläge. Bereiche mit Schritt 2 enthalten nur die genannten geraden Größen, keine Zwischenwerte. Katalogwerte belegen weder Hausbestand noch aktuelle EU-Verfügbarkeit. Keine REF aus einem Muster ergänzen, das im Original nicht zeilenweise geprüft wurde.

### T2 – Stryker Kopf-Ø und Offset, mm

Quelle q1, ACCII-SP-1_Rev-4_34423 ©2022, gedruckt/PDF S. 12; globales Dokument mit separaten EU-Indikationen. Nur folgende Haus-Kopffamilien:

| Familie | Ø | Offsets |
|---|---|---|
| LFIT CoCr V40 | 22 | 0, +3, +8 |
| LFIT CoCr V40 | 26 | −3, 0, +4, +8, +12 |
| LFIT CoCr V40 | 28 | −4, 0, +4, +6, +8, +12 |
| LFIT CoCr V40 | 32 | −4, 0, +4, +8, +12 |
| LFIT CoCr V40 | 36 | −5, 0, +5, +10 |
| LFIT CoCr V40 | 40 | −4, 0, +4, +8, +12 |
| LFIT CoCr V40 | 44 | −4, 0, +4, +8, +12 |
| BIOLOX delta V40 | 28 | −4, −2,7, 0, +4 |
| BIOLOX delta V40 | 32 | −4, 0, +4 |
| BIOLOX delta V40 | 36 | −5, −2,5, 0, +2,5, +5, +7,5 |

Accolade II ist gemäß q1 S. 3 in EU/EMEA mit CE-Anforderung und Australien für TEP, nicht Hemi bestimmt. Die vorstehenden Kopfwerte ändern diese Grenze nicht. Probekopfwerte aus q2 nicht auf Implantatköpfe übertragen.

### T3 – Trident II, X3 0°/10°, mm

q5, TRITRI-SP-3_Rev-6_29553 ©2022, gedruckt/PDF S. 4, Abgleich S. 20–21; EU/Canada. † = nur 0°. Maximales Ø ist nur für diese X3-Spalte gültig.

| Alpha | Schale | Kopf-Ø X3 0°/10° | Max. Ø |
|---|---|---|---|
| A | 42 | 22, 28† | 28 |
| B | 44 | 22, 28†, 32† | 32 |
| C | 46 | 22, 28, 32† | 32 |
| D | 48, 50 | 22, 28, 32, 36† | 36 |
| E | 52, 54 | 22, 28, 32, 36, 40† | 40 |
| F | 56, 58 | 22, 28, 32, 36, 40†, 44† | 44 |
| G | 60, 62 | 22, 28, 32, 36, 40†, 44† | 44 |
| H | 64, 66 | 22, 28, 32, 36, 40†, 44† | 44 |
| I | 68, 70 | 22, 28, 32, 36, 40†, 44† | 44 |
| J | 72 | 22, 28, 32, 36, 40†, 44† | 44 |

I/J nur Multihole. Weitere Varianten getrennt: X3 Eccentric 10° C/D: Ø28; E–J: Ø28/32/36. X3 Elevated Rim C/D: Ø28; E–J: Ø28/32/36. Eccentric 0° ist die ausdrücklich nicht CE-markierte/nicht EU-vermarktete Variante. Hersteller-Abgleich für 26-mm-X3-10° wegen Tabellen-/Katalogabweichung offen (Nr. 23). Eine Kopf-Ø-Freigabe ist keine Freigabe jeder Kopffamilie dieses Durchmessers.

### T5 – Rückrufstatus und Reichweite

| Dokument | Geprüfter Umfang/Status | Einbauentscheidung |
|---|---|---|
| FDA Z-2299-2018, Event 80059, ID 164630 | REF 6260-9-236; aufgelistete Lose; beendet 08.05.2020 | Nur diesen FDA-Status übernehmen. Kein EU-Abschluss und kein Ende sämtlicher LFIT-Maßnahmen. |
| EU/DE RA2018-1757583, 12.06.2018, PDF 1–2 | Köpfe vor 04.03.2011; REF-Widerspruch im Brief: S. 1 nennt 6260-9-126, Tabelle S. 2 6260-9-136 | Bestehenden Klärhinweis behalten; keine automatisch bereinigte Vollständigkeitsliste erzeugen. EU-Abschluss nicht gefunden. |
| FDA Z-0842-2022, Event 89592, ID 191999 | Open, Classified; REF 6570-0-032, Ø32/−4. Update 17.03.2022 zum Brief 15.03.2022: Charge 89648802 verbleibt; 89648801/03/04/05 aus Umfang entfernt | Aktualisierten US-Datensatz separat speichern. FDA-Text nennt auch Mitteilung an Deutschland, dass dort keine nichtkonformen Produkte eingegangen seien. Keine automatische Übertragung auf die anders bezeichnete EU-RA. |
| EU/DE RA2022-2911584, 18.01.2022, PDF 1 | Ursprünglich REF 6570-0-032: 89648801–89648805; REF 6570-0-136: 89549404; REF 6570-0-232: 89546202 | Historischen Briefumfang samt Datum behalten; ausdrückliche RA↔PFA-Zuordnung und EU-Abschluss fehlen in den gelesenen Originalen. Kein heutiger pauschaler Systemstatus. |

### T7 – Excia T

e1, Nr. 4008516, 01/2026, DE; Schäfte gedr. S. 18/PDF 10, Köpfe gedr. S. 19/PDF 10; CCD gedr. S. 11/PDF 6.

| Größe | Zementfrei Standard T | Zementfrei TL |
|---|---|---|
| 8 | NU208T | NU228T |
| 9 | NU209T | NU229T |
| 10 | NU210T | NU230T |
| 11 | NU211T | NU231T |
| 12 | NU212T | NU232T |
| 13 | NU213T | NU233T |
| 14 | NU214T | NU234T |
| 15 | NU215T | NU235T |
| 16 | NU216T | NU236T |
| 17 | NU217T | NU237T |
| 18 | NU218T | NU238T |
| 19 | NU219T | NU239T |
| 20 | NU220T | NU240T |

| Größe | Zementiert Standard T | Zementiert TL |
|---|---|---|
| 10 | NU270K | NU290K |
| 12 | NU272K | NU292K |
| 14 | NU274K | NU294K |
| 16 | NU276K | NU296K |
| 18 | NU278K | NU298K |
| 20 | NU280K | NU300K |

Standard 135°, TL 128°/+6 mm Offset. Zementfrei Ti6Al4V mit PLASMAPORE, zementiert CoCr. Dies ist keine Gleichsetzung mit Excia 12/14 (O90301).

| Excia-T-Hauskopf | Ø mm | Größen laut e1 S. 19 |
|---|---|---|
| BIOLOX delta | 28 | S/M/L; NK460D/NK461D/NK462D |
| BIOLOX delta | 32 | S/M/L/XL; NK560D/NK561D/NK562D/NK563D |
| BIOLOX delta | 36 | S/M/L/XL; NK650D/NK651D/NK652D/NK653D |
| BIOLOX delta | 40 | S/M/L/XL; NK750D/NK751D/NK752D/NK753D |
| Metall | 28 | S/M/L/XL/XXL; NK429K/NK430K/NK431K/NK432K/NK433K |
| Metall | 32 | S/M/L/XL/XXL; NK529K/NK530K/NK531K/NK532K/NK533K |
| Metall | 36 | S/M/L/XL/XXL; NK669K/NK670K/NK671K/NK672K/NK673K |
| Metall | 40 | S/M/L/XL/XXL; NK769K/NK770K/NK771K/NK772K/NK773K |

Relative Halslängen: Ø28 S/M/L/XL/XXL = −3,5/0/+3,5/+7/+10,5 mm; Ø≥32 = −4/0/+4/+8/+12 mm. Nur tatsächlich vorhandene Größenzeilen anwenden (kein BIOLOX-delta-XXL). Metallmaterial in e1 CoCrMo/ISO 5832-12; identische Metall-REF stehen in e2 S. 24 unter ISODUR F. Ø22,2 aus e2 steht **nicht** in dieser Excia-T-Kopfübersicht.

### T8 – Plasmafit und ISODUR F

e2, O45502 0718/1/4, S. 5–7, 18–21, 24, jeweils gedruckt=PDF. EN auf DE-Herstellerseite; aktuelle EU-IFU gesondert offen.

| System | Schalengrößen mm | Liner-Code-Zuordnung |
|---|---|---|
| Poly | 40–62, Schritt 2 | 40=B,42=C,44=D,46=E,48=F,50=G,52=H,54=I,56=J,58=K,60=L,62=M |
| Plus / Plus 3 / Plus 7 | 40–70, Schritt 2 | 40=A,42=B,44=C,46=D,48=E,50=F,52=G,54=H,56=I,58/60/62=J,64/66/68/70=K |

Gleicher Buchstabe allein genügt nicht: Poly und Plus ordnen gleiche Schalen-Ø verschiedenen Codes zu. Plus 7 mit 40/42/44 hat laut S. 20 Fußnote nur fünf Schraubenlöcher. Plus/Plus 3/Plus 7 sind Varianten, kein automatisch bestätigter Hausbestand.

| Liner, jeweils symmetrisch | Ø mm | Passende Poly-Schale mm | Passende Plus-Schale mm |
|---|---|---|---|
| Vitelene | 22,2 | 40/42 | 40/42/44 |
| Vitelene | 28 | 42–54, Schritt 2 | 44–56, Schritt 2 |
| Vitelene | 32 | 46–62, Schritt 2 | 48–70, Schritt 2 |
| Vitelene | 36 | 50–62, Schritt 2 | 52–70, Schritt 2 |
| Vitelene | 40 | 54–62, Schritt 2 | 56–70, Schritt 2 |
| BIOLOX delta | 28 | nicht vorgesehen | 44–54, Schritt 2 |
| BIOLOX delta | 32 | nicht vorgesehen | 48–70, Schritt 2 |
| BIOLOX delta | 36 | nicht vorgesehen | 52–70, Schritt 2 |
| BIOLOX delta | 40 | nicht vorgesehen | 56–70, Schritt 2 |

Diese Zuordnung gilt ausschließlich für die bezeichneten **symmetrischen** Liner. Posterior-wall/asymmetrisch/UHMWPE-with-shoulder haben eigene Zeilen; nicht aus obiger Tabelle freigeben. Beispiel aus S. 20–21: BIOLOX-delta-Ø36 Plus 52=NV113D,54=NV114D,56=NV115D,58/60/62=NV116D,64/66/68/70=NV117D. Nicht für Poly.

ISODUR-F-Kopf Ø22,2: nur M=NK330K und L=NK331K. Ø28/32/36/40: S/M/L/XL/XXL wie T7. BIOLOX delta Ø28 S/M/L, Ø32/36/40 S/M/L/XL. Gleicher Material- oder Konusname ersetzt keine konkrete Schaft- und Gleitpaarungsfreigabe; insbesondere keinen Metallkopf mit Keramikinlay freigeben.

### T12 – S+N-Matrix, Hausköpfe

matrix, Lit. No. 04758 **Ed. 05/26 V12**, PDF/gedruckt 2/7 und 6/7, international. Ja/Nein sind Hersteller-Matrixstatus; lokale Zulassung bleibt zu prüfen. Zeilenzeichen im Textauszug „a“ ist visuell ein Häkchen; rote leere Zelle = nicht freigegeben.

| Kopf | Ø mm | Halslängen mm bzw. Größen | SL-PLUS MIA 01 | MIA übrige | SPECTRON alle |
|---|---|---|---|---|---|
| OXINIUM / CoCrMo | 22 | 0,+4,+8,+12 | Ja | Ja | Ja |
| OXINIUM / CoCrMo | 26 | 0,+4,+8,+12 | **Nein** | **Nein** | Ja |
| OXINIUM / CoCrMo | 28 | −3,0,+4,+8,+12 | Ja | Ja | Ja |
| OXINIUM / CoCrMo | 28 | +16 | **Nein** | Ja | Ja |
| OXINIUM / CoCrMo | 32 | −3,0,+4,+8,+12 | Ja | Ja | Ja |
| OXINIUM / CoCrMo | 32 | +16 | **Nein** | Ja | Ja |
| OXINIUM / CoCrMo | 36 | −3,0,+4,+8,+12 | Ja | Ja | Ja |
| OXINIUM / CoCrMo | 40/44 | −4,0,+4,+8; zugehörige Ti-Hülse zwingend | Ja | Ja | Ja |
| BIOLOX delta | 32 | 0,+4,+8; SAP 765391-60/61/62 | Ja | Ja | Ja |
| BIOLOX delta | 36 | 0,+4,+8,+12; SAP 765391-65/66/67/53 | Ja | Ja | Ja |
| BIOLOX delta | 40 | 0,+4,+8; SAP 713460-04/05/06 | Ja | Ja | Ja |
| BIOLOX delta | 28 | S/M/L; SAP 750074-51/52/53 | Ja | Ja | Ja |
| BIOLOX delta | 32 | S/M/L/XL; SAP 750074-60/61/62/63 | Ja | Ja | Ja |
| BIOLOX delta | 36 | S/M/L/XL; SAP 750074-48/49/50/47 | Ja | Ja | Ja |

Ø40/44: OXINIUM Köpfe SAP 71342340/71342344; CoCrMo 71342640/71342644. Zugehörige Ti-Hülsen für −4/0/+4/+8: 71344245/71344247/71344248/71344249. Kein Ärmel- oder Kopfwechsel zwischen fremden Systemen.

BIOLOX OPTION ist eine eigene Kopf-/Hülsenfamilie: Ø28/32/36 S/M/L/XL und Ø40 S/M/L sind auf beiden Seiten freigegeben; **Ø40 XL, Kopf 75103516 + Hülse 75103520, ist für alle hier geprüften Spalten rot/nicht freigegeben.** OPTION nicht automatisch in die Hausliste aufnehmen. Stainless Steel bleibt für MIA/SPECTRON nicht freigegeben und ist kein Hauskopf. Die Spalte SL-PLUS Japan ist keine MIA-Spalte. Fußnote 3 bei MIA 01 = SAP 75000172, nicht Größenbezeichnung 013.

### T13 – SL-PLUS MIA INTEGRATION-PLUS

s1, 00884-en (1524) V4 01/15, gedruckt S. 18–19/PDF 20–21. Größenbezeichnungen als Strings speichern, damit „01“ und „0“ verschieden bleiben. Implantat-SAP, keine Proben-SAP:

| Größe | Standard SAP | Lateral SAP |
|---|---|---|
| 01 | 75000172 | – |
| 0 | 75000173 | – |
| 1 | 75000174 | 75000186 |
| 2 | 75000175 | 75000187 |
| 3 | 75000176 | 75000188 |
| 4 | 75000177 | 75000189 |
| 5 | 75000178 | 75000190 |
| 6 | 75000179 | 75000191 |
| 7 | 75000180 | 75000192 |
| 8 | 75000181 | 75000193 |
| 9 | 75000182 | 75000194 |
| 10 | 75000183 | 75000195 |
| 11, optional | 75000184 | 75000196 |
| 12, optional | 75000185 | 75000197 |

CCD 131° Standard/123° lateral: gedr. S. 16/PDF 18. Die älteren Maßtabellen sind kein Ersatz für matrix 05/26. Längenkonflikte Nr. 24 nicht still bereinigen.

### T14 – SPECTRON EF Primary

s3, 21885 V3 / 71380478 REVB 03/23, ©2023. Specs gedruckt 1/PDF 4; Implantatkatalog gedruckt 12/PDF 15. 131° für alle folgenden Größen.

| Größe Standard / High Offset | Länge mm | Implantat-REF Standard / High Offset |
|---|---|---|
| 1 / 1H | 115 | 71312101 / 71312111 |
| 2 / 2H | 125 | 71312102 / 71312112 |
| 3 / 3H | 135 | 71312103 / 71312113 |
| 4 / 4H | 135 | 71312104 / 71312114 |
| 5 / 5H | 135 | 71312105 / 71312115 |

### T15 – R3 Schale/XLPE

s4, 7138-1560-de REVB 06/12, ©2017, DE; gedruckt=PDF S. 13 visuell mit S. 17–18 Katalog abgeglichen.

| Schalen-Ø mm | Zulässige XLPE-Innen-Ø mm laut Grafik |
|---|---|
| 40/42/44 | 22 |
| 46 | 28 |
| 48/50 | 28,32 |
| 52/54 | 28,32,36 |
| 56/58 | 28,32,36,40 |
| 60 | 28,32,36,40,44 |
| 62 | 32,36,40,44 |
| 64/66/68/70/72/74/76/78/80 | 36,40,44 |

Katalog führt getrennt 0°,20°,0°+4,20°+4. Beispiel Ø36/Schale52: 7133-2752 / 7133-5752 / 7133-6952 / 7133-8552 (in dieser Reihenfolge). Große Schalen werden bei einzelnen Liner-REF gruppiert, z. B. Ø36/66–70: 7133-0766 / 7133-1266 / 7133-1566 / 7133-2666. Keine REF durch Zahlenfortsetzung erzeugen. Alte Keramik-Spalten der Grafik nicht als Haus-XLPE verwenden. Keine aktuelle EU-IFU damit nachgewiesen.

### T17 – TANDEM-Grenzen

tandem, 29073 V2 / 71380925 REVA 02/23, PDF 17 (keine gedruckte Seitennummer), Kennung PDF 20. SPECTRON EF Primary/Revision steht ohne EU-Sperrstern in der Bipolar-Tabelle. Für den hier gemeinten SPECTRON EF 12/14 sind die dortigen 12/14-OXINIUM-/CoCr-Innenköpfe Ø22/28 relevant; keine freie Wahl jedes Hauskopfs.

Die Tabelle trennt TANDEM INTL Bipolar (UHMWPE) und TANDEM Bipolar (XLPE). * = Kombination in EU nicht genehmigt; ** = Größe 01 nicht mit +16 oder TANDEM INTL Bipolar; *** = 10/12 nicht in EU verkauft. Grok vermengt * und **. Dokumentierte Schaftkompatibilität ersetzt weder Hausprodukt-Identifikation noch aktuelle EU-Verfügbarkeit. Kein BIOLOX-delta-Bipolar-Nachweis auf dieser Seite. Vor Umbenennung des Hausprodukts Etikett/REF prüfen; derzeit kein automatischer Alias „Bi-Polar Head = TANDEM“.

### T19 – twinSys: öffentliches Original

twinsys, Product Information, Item 336.010.078 / 04-0224-01 / 2024-02, PDF 7 Ordering information (ohne sichtbare gedruckte Seitenzahl), Kennung PDF 8. EN/international, keine pauschale aktuelle EU-IFU-Freigabe.

| Variante | Größen | Belegbare Implantat-REF-Beispiele |
|---|---|---|
| Zementfrei Standard | 7–18, Schritt 1 | 7=52.34.1157; 8=52.34.1158; 9=56.11.1000; 18=56.11.1009 |
| Zementfrei Lateral | 7–18, Schritt 1 | 7=52.34.1159; 8=52.34.1160; 9=56.11.1010; 18=56.11.1019 |
| Zementfrei XS | 7–12, Schritt 1 | 7=56.11.1068; 8=56.11.1069; 9=56.11.1070; 10=56.11.1071; 11=52.34.1161; 12=52.34.1162 |
| Zementfrei Long | 12/13/14/15 | 56.11.3003 / 56.11.3004 / 56.11.3005 / 56.11.3006 |
| Zementiert Standard | 9–16, Schritt 1 | 9=56.11.2000NG; 16=56.11.2007NG |
| Zementiert Lateral | 9–16, Schritt 1 | 9=56.11.2010NG; 16=56.11.2017NG |

Nicht aufgeführte Einzel-REF hier nicht ergänzen. Keine Kopf-/Pfannen-Paarung aus dem Flyer ableiten. XS/Long sind dokumentierte Varianten, kein nachgewiesener Hausbestand.

### T19b – CCB: öffentliches Original

ccb, Item 336.010.151 / 01-0220-01 / 2020-02, gedruckt=PDF S. 21–22, Kennung PDF 32. EN/international; aktuelle EU-IFU offen.

| CCB-Profil | Kopf-Ø mm | Außen-Ø mm | Zwingende Einschränkung laut Tabelle |
|---|---|---|---|
| Low-profile | 28 | 42–64, Schritt 2 | 42 nur mit Pfannendachverstärkungsring |
| Low-profile | 32 | 42–64, Schritt 2 | 42/44/46 nur mit Pfannendachverstärkungsring |
| Full-profile | 28 | 44–58, Schritt 2 | Keine Sternmarkierung in dieser Tabelle |
| Full-profile | 32 | 44–58, Schritt 2 | 44/46 nur mit Pfannendachverstärkungsring |

Quelle erklärt die Ringpflicht mit geringer Wandstärke; für 60–64 keine CCE-Ringe verfügbar. Keine zusätzliche REF-/Schaftfreigabe daraus ableiten. „ccB-Pfanne“ allein bestimmt das Hausprofil noch nicht.

## Nicht übernommen von Grok

| Grok-Nr. | Nicht genau so übernommen / Grund |
|---|---|
| 5 | FDA-Status ohne aktualisierte REF-/Chargen-/Länderreichweite zu grob; EU-Zuordnung bleibt offen. |
| 7 | CCD-Fundstelle gedr. 11/PDF 6 statt S. 10; Kopf-Paarungen konkretisieren. |
| 8 | Ø22,2 nicht S–XXL; Linerzuordnung hat auch Obergrenzen, Codes und Varianten. |
| 9 | Gemeinsamer 12/14-Konus rechtfertigt keine allgemeine Kopfverwendung; Excia-T-Original maßgeblich. |
| 12 | OPTION 40 XL ausdrücklich rot; 26 mm unterscheidet MIA/SPECTRON; Größe 01 nicht 013; keine Analog-Freigabe. |
| 14 | Specs gedruckt 1/PDF 4; exakte Seiten statt „~4/~15“. Werte an sich bestätigt. |
| 15 | Grafik vollständig visuell auflösbar; genauer Tabelleninhalt statt Offenlassen. |
| 16 | Weitere offizielle historische REFLECTION-Fundstelle gefunden, EU-Geltung bleibt offen. |
| 17 | TANDEM als Herstellerkandidat belegbar, Hausidentität nicht; ** ist keine allgemeine EU-Sperre; konkrete Innenköpfe erforderlich. |
| 18 | R-2020-04 enthält ausdrücklichen Rücknahmehinweis; formaler aktueller Abschluss dennoch offen. |
| 19 | Produkttexte, twinSys-, CCB- und Keramik-PDF öffentlich lesbar; pauschale Gate-/Login-Aussage falsch. |
| 20 | Offenlassen richtig, aber Ursache dokumentierter Redirect/fehlende Identifikation; kein pauschal bewiesenes HCP-Hindernis. |
| 21 | Bipolarseite lesbar; dort fehlt konkrete Schaft-Paarung. Nicht das Gate begründet das Offenlassen. |
| 22 | Strukturansatz sinnvoll; pauschale Systemkanten müssen konkrete Bedingungen und unbelegte Hausidentitäten berücksichtigen. |

## Nicht gefunden / bewusst offen

- Aktuelle produktspezifische EU-IFUs für die genannten Stryker-Systeme, R3 und die ungeklärten Komponenten; Portalabruf ist keine Freigabe. BR/JP-Unterlagen ersetzen dies nicht.
- EU-Abschluss RA2018-1757583, ausdrücklicher Gleichsetzungsnachweis RA2022-2911584/PFA 2902313 sowie heutiger formaler EU-Abschluss der R3-Maßnahmen.
- Konkrete Bipolar-Cup/Kopf/Excia-T-zementiert-Freigabetabelle; Animationstext ist nur Anwendungsfundstelle.
- Einzelprodukt/Profil/REF der zementierten Aesculap-Hauspfanne; aktuelle EU-Dokumente für REFLECTION All-Poly und Müller-PE-Hauspfanne.
- Etikett/REF des S+N-Hausduokopfs; TANDEM als Kandidat ist nicht identisch mit einer bestätigten Hausauswahl.
- Lesbares aktuelles seleXys-PC-Dokument, Zuordnung „PE-Inlay Standard“, konkrete Mathys-Bipolar/Kopf/twinSys-zementiert-Paarung und aktuelle EU-IFUs. Neue Flyer lösen diese offenen Punkte nicht vollständig.
- Schaftimplantat-REF Accolade II; X3-26-mm-Quellenabweichung; widersprüchliche SL-PLUS-MIA-Längen.

Keine Beurteilung des unveränderten übrigen Inhalts von 000/001. Keine Haus- oder Patientendatenprüfung; keine klinische Freigabe. Offene Nachweise bleiben offen, auch wenn das Wissenspaket organisatorisch abgeschlossen wird.

## Selbst geöffnete Quellen

Prüfdatum und Abrufdatum sämtlicher unten genannter Quellen: **07.10.2026 (UTC)**. Gedruckte Seiten und PDF-Seiten sind ausdrücklich unterschieden; bei HTML ist der Abschnitt angegeben. Quellenstände werden nicht durch das Abrufdatum ersetzt. PDF-Seiten wurden für die übernommenen Werte im Original geprüft; grafische Matrix-/Tabellenzellen zusätzlich visuell. Nicht alle Dokumente sind aktuelle EU-IFUs.

- **q1** — [Accolade II Femoral Hip System — Surgical protocol; ACCII-SP-1_Rev-4_34423, ©2022; gedr.=PDF S. 3–5, 11–12, 22, 24, Kennung 25; global mit getrennten EU/EMEA-/Australien-Indikationen](https://cdn.stryker.com/SYKGCSDOC-2-45343).
- **q2** — [Accolade II — Tray Layout; ACCII-TL-1_25643, ©2020; PDF 1–3, unnummeriert; CE-/Marktvorbehalt PDF 3](https://www.stryker.com/content/dam/stryker/joint-replacement/products/accoladeii/resources/Accolade%20II%20Tray%20Layout_ACCII-TL-1_25643.pdf).
- **q5** — [Trident II Tritanium — Surgical protocol; TRITRI-SP-3_Rev-6_29553, ©2022; gedr.=PDF S. 2, 4, 20–21, Kennung 31; EU/Canada, Eccentric 0° ausdrücklich ausgenommen](https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf).
- **e1** — [Aesculap Excia T Hüftschaft; Nr. 4008516, 01/2026; gedr. 11/PDF 6, gedr. 18–19/PDF 10, Kennung PDF 13; DE](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf).
- **e2** — [Aesculap Plasmafit — Acetabular Cup System; O45502 0718/1/4, 07/2018; gedr.=PDF S. 5–7, 18–21, 24, Kennung 34; EN auf DE-Herstellerseite](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf).
- **excia-old** — [Aesculap Excia 12/14; O90301 1119/PDF/5, 11/2019; gedr.=PDF S. 14, 16; DE, ausdrücklich andere Schaftlinie](https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b306/aesculap-excia-1214.pdf).
- **bb-web** — [B. Braun — Zementierte Hüftprothese; undatiertes HTML, Abruf 07.10.2026; Abschnitt Operationstechniken; DE](https://www.bbraun.de/de/produkte-und-loesungen/therapien/orthopaedischer-gelenkersatz-und-regenerative-therapien/hueftendoprothetik/zementierte-hueftprothese.html).
- **e3** — [Aesculap Bipolar Cup, PRID00004418; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; internationaler EN-Katalog](https://catalogs.bbraun.com/en-01/p/PRID00004418/bipolar-cup).
- **e4** — [Aesculap Cemented Polyethylene Cups, PRID00002464; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; internationaler EN-Katalog](https://catalogs.bbraun.com/en-01/p/PRID00002464/cemented-polyethylene-cups).
- **matrix** — [Smith+Nephew — Hip implant compatibility matrix; Lit. No. 04758, Ed. 05/26 V12; S. 2/7 und 6/7, Länder-/IFU-Vermerke auf den Matrixseiten; international mit lokalen Zulassungsvorbehalten](https://smith-nephew.stylelabs.cloud/api/public/content/18df5a64ab234b02acb3e147b753f771?v=2833a5de).
- **s1** — [SL-PLUS MIA — Surgical Technique; 00884-en (1524) V4, 01/15; gedr. 16–19/PDF 18–21, Kennung PDF 28; EN/international](https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true).
- **s3** — [SPECTRON EF — Surgical Technique; 21885 V3, 71380478 REVB 03/23, ©2023; gedr. 1/PDF 4, gedr. 12/PDF 15, gedr. 14/PDF 17, gedr. 16/PDF 19, Kennung PDF 20; EN, keine pauschale EU-Freigabe abgeleitet](https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true).
- **s4** — [R3 Acetabular System — Operationstechnik; 7138-1560-de REVB 06/12, ©2017; gedr.=PDF S. 13, 17–18, Kennung 32; DE](https://smith-nephew-delivery.stylelabs.cloud/api/public/content/1bd7a20b4fdf4a158b95aad5987f2686?v=e321be27&download=true).
- **tandem** — [TANDEM Bipolar and Unipolar Hip System — INTL Surgical Technique; 29073 V2, 71380925 REVA 02/23; unnummerierte PDF 17 Implant Compatibility, Kennung PDF 20; INTL mit expliziten EU-Fußnoten](https://smith-nephew.stylelabs.cloud/api/public/content/8af4fc46aafd4be4a8d289f62a72ee8e?download=true&v=bdf205cd).
- **reflection** — [REFLECTION — Surgical Technique; 00811 V1, 10/13, ©2013; PDF Titelblatt und Dokumentende/Impressum; historische EN-Unterlage mit US-Angaben und EC-Vertreter, kein aktueller EU-Nachweis](https://smith-nephew.stylelabs.cloud/api/public/content/7cada363f2224bc3957ac5e0fde018ad?download=true&v=eca89761).
- **twinsys** — [twinSys — Product Information; Item 336.010.078 / 04-0224-01 / 2024-02; PDF 7 Ordering information (unnummeriert), Kennung PDF 8; EN/international](https://enovis-surgical.com/repo/storage/4721/file/EN_TSS_ProdInfo_V04%20%281%29.pdf).
- **ccb** — [CCB cup — CCE roof reinforcement ring, Surgical Technique/Product Information; Item 336.010.151 / 01-0220-01 / 2020-02; gedr.=PDF S. 21–22, Kennung 32; EN/international](https://enovis-surgical.com/repo/storage/4723/file/op-technik_produktinfo-ccb-cce_en_v1.0.pdf).
- **ceramics** — [Mathys — Ceramic implants, Product Information; Item 336.010.127 / 03-0319-01 / 2019-03; PDF 1–6, Kennung PDF 8; EN/international, keine konkrete twinSys-Paarung daraus übernommen](https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf).
- **fda-lfit** — [FDA Class 2 Device Recall LFIT Anatomic V40 Femoral Head; Z-2299-2018, Event 80059; HTML Product, Code Information, Recall Status; beendet 08.05.2020, Abruf 07.10.2026; US-Datensatz](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm?ID=164630).
- **fda-delta** — [FDA Class 2 Device Recall BIOLOX delta Ceramic V40 Femoral Head; Z-0842-2022, Event 89592, PFA 2902313; HTML Recall Status, Product, Code Information, Action/Distribution; Update 17.03.2022, Abruf 07.10.2026; US-Datensatz mit Länderhinweisen](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id=191999).
- **stryker-accolade-ii-rec2** — [Stryker — Dringende Sicherheitsinformation RA2018-1757583, LFIT CoCr V40; 12.06.2018; PDF 1–2; DE über BfArM, Kennung 06604/18](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2018/06604-18_kundeninfo_de.pdf?__blob=publicationFile).
- **stryker-accolade-ii-rec3** — [Stryker — Dringende Sicherheitsinformation RA2022-2911584, BIOLOX delta V40; 18.01.2022; PDF 1 Produkt-/Chargentabelle und Statushinweis; DE über BfArM, Kennung 01953/22](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2022/01953-22_kundeninfo_de.pdf?__blob=publicationFile).
- **smith-nephew-r3-rec1** — [Smith+Nephew — Physician Communication, R-2020-04, R3 Acetabular Liners; Brief ohne sichtbares Tagesdatum, BfArM-Ablage 2020/05608-20; PDF 1 Rücknahmehinweis, 2 Rückmeldeformular; EN über BfArM](https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2020/05608-20_kundeninfo_en.pdf?__blob=publicationFile).
- **smith-nephew-r3-rec2** — [Smith+Nephew — Dringende Sicherheitsinformation R-2023-13, R3 XLPE 20 DEG ACET LNR; 20.11.2023; PDF 1–2; DE über BfArM, Kennung 35762-23](https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2023/35762-23_kundeninfo_de.pdf?__blob=publicationFile).
- **enovis-bipolar** — [Enovis — Bipolar; undatiertes HTML, Abruf 07.10.2026; Produktbeschreibung; EN/international, keine explizite twinSys-Paarung](https://enovis-surgical.com/en/products/335/bipolar.html).

### Weitere selbst geöffnete Fundstellen und erfolglose Abrufe

Die folgenden Fundstellen belegen nur den beschriebenen Abrufbefund; daraus wurden keine nicht belegten Produktwerte übernommen.

- [Stryker eIFU-Portal; Weiterleitung zu labeling.stryker.com/hcp, im Abruf kein auswertbarer EU-IFU-Text](https://ifu.stryker.com/).
- [Smith+Nephew eIFU-Portal; Suche verlangt REF bzw. IFU-Nummer; keine konkrete aktuelle R3-EU-IFU geöffnet](https://ifu.smith-nephew.com/).
- [Mathys eIFU-Portal; kein auswertbarer IFU-Inhalt im Abruf](https://ifu.mathysmedical.com/).
- [Enovis Resources; Ressourcen-/Downloadfundstellen, ohne Datum, international](https://enovis-surgical.com/resources.html).
- [Enovis RM Classic; Abschnitt Produktbeschreibung, Monoblock-System, ohne Datum, international](https://enovis-surgical.com/en/products/321/rm-classic.html).
- [Enovis Ceramic; Produktbeschreibung/Downloads lesbar, ohne Datum, international](https://enovis-surgical.com/en/products/332/ceramic.html).
- [Enovis Metal, vorgegebener Pfad; HTTP 404 im Abruf](https://enovis-surgical.com/en/products/333/metal.html).
- [Mathys twinSys OP-Technik Altlink; Weiterleitung auf Enovis-Startseite, kein PDF-Inhalt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_twinSys_EN_V06.pdf).
- [Mathys RM Classic Altlink; Weiterleitung auf Enovis-Startseite, kein PDF-Inhalt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_RM_Classic_Pfanne_DE.pdf).
- [Mathys seleXys PC Altlink; Weiterleitung auf Enovis-Startseite, kein PDF-Inhalt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_seleXys_PC_DE_V04.pdf).
- [Mathys CCB/CCE Altlink; Weiterleitung auf Enovis-Startseite; neues EN-PDF separat als ccb belegt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_Produktinfo_CCB_CCE_DE_V01.pdf).
- [Mathys Hipheads-Kompatibilitätschart Altlink; Weiterleitung auf Enovis-Startseite, kein PDF-Inhalt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Kompatibilitaets-Chart/Kompatibilit%C3%A4ts-Chart_OPT_Hipheads_Mathys_EN_V01.pdf).
- [Mathys Bipolar-Hemikopf Altlink; Weiterleitung auf Enovis-Startseite, kein PDF-Inhalt](https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Bipolar-Hemi/OP-Technik-Produktinfo_Bipolar-Hemikopf_FR_V01.pdf).
- [Enovis twinSys uncemented](https://enovis-surgical.com/en/products/327/twinsys-uncemented.html) und [twinSys cemented](https://enovis-surgical.com/en/products/328/twinsys-cemented.html): Produktbeschreibung öffentlich lesbar, ohne Datum, EN/international. Werte ausschließlich aus twinsys-PDF übernommen.
- [Enovis CCE](https://enovis-surgical.com/en/products/324/cce.html?country_code=SI): Downloadfundstelle des unter ccb belegten englischen Originals; Länderparameter SI ist keine allgemeine EU-Freigabe.
- [Stryker BR QIN4351](https://ifu.stryker.com.br/documentos/download/44): Abruf wegen Downloadformat nicht auswertbar; **nicht gelesen, nicht als Beleg** verwendet; ohnehin kein EU-Ersatz.

Prüfabschluss: **07.10.2026**. Fachliche Perspektive: OP-Pflege/OTA, Endoprothetik; dokumentenbasierte Gegenprüfung, keine behauptete persönliche Berufsqualifikation und keine klinische Freigabe.
