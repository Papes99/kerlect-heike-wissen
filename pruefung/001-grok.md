Grok – Lauf 2026-10-07T02:10Z

OP-Gegenprüfung Kerlect Heike-Wissen, Paket 001 v1.2. Originalquellen geöffnet: KRINKO Empf. postop. WI (edoc.rki.de), HEBU GAHF113V004, Stryker ACCII-SP-1 Rev-4, Heraeus BCIS-Factsheet, Stryker Trident II Tritanium TRITRI-SP-3 Rev-6 (EU/Canada), Accolade II Design Rationale, Aesculap Excia T-Broschüre, Plasmafit EN, S+N SL-PLUS MIA / SPECTRON EF / R3-Broschüre / Compatibility Matrix 04758, POLARSTEM US-IFU 81098832 Rev.2. Mathys/Enovis-PDFs: Abruf 415 bzw. HCP-Gate – Inhalte nicht am Original geprüft.

### Zur Prüfung – Teil A

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| 1 | ok | – | – | KRINKO Prävention postoperativer Wundinfektionen, 2018, Bgbl. 61:448–473, gedr. S. 461 (PDF-S. 14), Abschn. 4.1: „Bei Operationen, bei denen ein Durchfeuchten nicht auszuschließen ist, flüssigkeitsundurchlässige Abdeckungen zu verwenden (Kat. IB).“ https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 2 | ok | – | – | keine (hausabhängig/Praxis); BCIS fordert Kommunikation der Zementschritte, nicht die konkrete Rückbestätigungs-SOP. Heraeus Palacademy Factsheet Implantationssyndrom, PDF S. 1. | – |
| 3 | ok | – | – | keine (hausabhängig/Praxis); Markraumstopper vs. Mess-/Einführhilfe trennen ist Zähl-/IFU-Logik, kein KRINKO-/BCIS-Wortlaut. | – |
| 4 | ok | – | – | KRINKO Abschn. 4.1, gedr. S. 461 (PDF-S. 14): Patient darf nicht in Flüssigkeitsansammlung des Hautantiseptikums liegen (Kat. II). gilt_fuer hf_mono konsistent mit 000-Eintrag „Keine Antiseptikum-Pfützen“ (gilt_fuer alle). Brandrisiko ergänzend HEBU Abschn. 6 Gefahrenhinweise (exogene Verbrennungen / entzündete Desinfektionsmittel). | – |
| 5 | ok | – | – | HEBU Einmal-Neutralelektroden GAHF113V004, 20.02.2026: Abschn. 5.2 „darf nicht mit Flüssigkeiten in Berührung kommen“; Abschn. 8 „Eindringen von Flüssigkeiten … vermeiden“. https://www.hebumedical.de/ga/GAHF113.pdf | – |
| 6 | ok | – | – | Accolade II Femoral Hip System Surgical protocol ACCII-SP-1_Rev-4_34423, © 2022, S. 3 (EU/EMEA/Australia: nur THA, kein Hemi) und S. 12 Fußnote Figure 10. https://cdn.stryker.com/SYKGCSDOC-2-45343 | – |
| 7 | ok | – | – | Streichung der alten, kombinationsnahen Accolade-Duokopf-Formulierung korrekt. | – |
| 8 | ok | – | – | Neutrale Duokopf-Rückfrage + Accolade-II-Hemi-Grenze korrekt umgesetzt (ACCII-SP-1 S. 3/12). Hausfolge (kein Stryker-Duokopf): siehe Teil D. | – |
| 9 | ok | – | – | Alte kombinationsnahe Rückfrage gestrichen. | – |
| 10 | ok | – | – | KRINKO 2018, gedr. S. 461 = PDF-S. 14, Abschn. 4.1: Antiseptikum-Ansammlung Kat. II; flüssigkeitsundurchlässige Abdeckung Kat. IB. Fundstelle in Q_KRINKO korrekt. | – |
| 11 | ok | – | – | ACCII-SP-1_Rev-4_34423, © 2022; S. 3 EU-Indikationen; S. 12 Hemi-Ausschluss EU; Dokumentcode S. 25. URL wie Nr 6. | – |

### Zur Prüfung – Teil A2

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| 1 | ok | – | – | verified=false + Teilprüfungshinweis in beiden Implantat-JSONs umgesetzt. | – |
| 2 | ok | – | – | ACCII-SP-1: S. 3/12 EU-Grenze, S. 5 CCD 132°/127°, S. 12 Kopfwerte, S. 15/17 Hülsen. | – |
| 3 | ok | – | – | UHR nur Japan-Katalog HE01-160 Rev1; Hemi-Sperre über q1. Umsetzung Astra-K5 korrekt. Hausfolge: UHR streichen → Teil D. | – |
| 4 | Fehler | Attribut „keine bestellfähige REF“ zur Familie 6519-T-XX ist ungenau: ACCII-SP-1 listet konkrete Sleeve-REFs. | `komponenten[Universal Taper].attribute.konus`: Familie 6519-T-XX; bestellfähige REFs laut IFU: 6519-T-025 (−2,5), 6519-T-100 (0), 6519-T-204 (+4); Hülse nach Offset/aktueller IFU wählen. | ACCII-SP-1 Rev-4, S. 15 und Katalog S. 17. | mittel |
| 5 | ok | – | – | ACCII-SP-1 S. 15 Final reduction Notes: Sleeve zuerst auf Schaftkonus, nicht im Keramikkopf vormontieren. | – |
| 6 | ok | – | – | POLARSTEM IFU 81098832 Rev. 2, 06/2021, S. 1: „US only“. | – |
| 7 | ok | – | – | US-IFU S. 4: Standard 135°, lateral 126°, valgus 145°; Standard/lateral auch mit Kragen; EU-Varianten offen. | – |
| 8 | ok | – | – | US-IFU S. 5: Cemented stem only with OXINIUM or BIOLOX delta; keine pauschale EU-Regel. | – |
| 9 | ok | – | – | US-IFU S. 2/5 Combination restrictions; gleicher Konus/Marke ≠ Freigabe. | – |
| 10 | ok | – | – | offen „Aktuelle EU-IFU POLARSTEM nachfordern“ korrekt; zusätzlich Haus: POLARSTEM nicht im Haus → Teil D streichen. | – |

### Zur Prüfung – Teil B1

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| B1-1 | ok | – | Nach 000 `pitfalls`, `gilt_fuer: ['hf_mono']`, `quelle: q_hebu` (neu). HEBU nur Produktbeispiel. | HEBU GAHF113V004, Abschn. 5.2 / 8. | – |
| B1-2 | Fehler | 001-Hinweis enthält „Beinbeweglichkeit“ → Hüft-Bezug; für 000 ungeeignet. | `spez/hinweis` ohne Bein/Hüfte: „Sterilfeld, Bewegungsraum und ggf. Bildgebung freihalten; keine Zugbelastung.“ `gilt_fuer: ['alle']`, `sicherheit: hausabhängig`. | keine (Praxis) | mittel |
| B1-3 | ok | – | – | keine (Praxis) | – |
| B1-4 | ok | – | – | APS-Zählprinzipien allgemein; keine Hüft-Spezifik. | – |
| B1-5 | ok | – | `gilt_fuer: ['implantat']` in 000 (nicht „alle“). | keine (Praxis) | – |
| B1-6 | ok | – | `gilt_fuer: ['implantat']`. | keine (Praxis) | – |
| B1-7 | ok | – | `gilt_fuer: ['zement']` (000-Situation); Abschnitt `implants` oder `workflow`. | Praxis; BCIS nur für Informieren der Anästhesie, nicht für Rückbestätigungs-SOP. | – |
| B1-8 | ok | – | `gilt_fuer: ['zement']`; keine Mischzeit. | keine (IFU des Hausprodukts) | – |
| B1-9 | ok | – | `gilt_fuer: ['zement']`. | keine (Praxis) | – |
| B1-10 | ok | – | `gilt_fuer: ['alle']`; Mengen hausabhängig. KRINKO erwähnt Doppelhandschuhe nur situationsbezogen (Kat. II) – hier bewusst hausabhängig belassen. | KRINKO Abschn. 4.1 (Kontext), keine pauschale Pflicht für alle Eingriffe. | – |
| B1-11 | ok | – | – | keine (Praxis) | – |
| B1-12 | ok | – | `optional: true`, `gilt_fuer: ['alle']` nur wenn Antriebe geplant; Hinweis ohne hüftspezifische Gerätepflicht. | keine (IFU) | – |
| B1-13 | ok | – | `optional: true`; keine Medikamentenempfehlung. | keine (Praxis) | – |
| B1-14 | ok | – | – | keine (Praxis) | – |

### Zur Prüfung – Teil B2

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| B2-1 | Fehler | 000 deckt Ort/Anlage ab, nicht explizit „nach Umlagerung erneut kontrollieren“ (HEBU). Inhalt ist allgemein, nicht hüftspezifisch. | Kern in 001 streichen; Umlagerungskontrolle nach 000 `position`/`Neutralelektrode-Ort` ergänzen (`quelle: q_hebu`). | HEBU GAHF113V004 Abschn. 5.2 (Kontrolle nach Lageänderung). | mittel |
| B2-2 | ok | – | In 001 streichen; 000 `Abdeckung flüssigkeitsdicht` ist inhaltsgleich. | KRINKO S. 461 / 000 q_krinko. | – |
| B2-3 | ok | – | KRINKO-Kern in 001 streichen (000 `Keine Antiseptikum-Pfützen`). HEBU-Brandrisiko-Querverweis ggf. in 000-hinweis oder bei B1-1 belassen, nicht doppelt in 001. | KRINKO S. 461; HEBU Abschn. 6. | – |
| B2-4 | ok | – | In 001 streichen; 000 hat `Druckstellen gepolstert` + `Arme gesichert`. | – | – |
| B2-5 | ok | – | In 001 streichen; 000 `Anästhesie vor Zement informieren` (q_bcis) deckt ab. | BCIS Factsheet S. 1. | – |
| B2-6 | ok | – | In 001 streichen. | – | – |
| B2-7 | ok | – | In 001 streichen. | – | – |
| B2-8 | Fehler | 001 enthält Hüft-/Eingriffsspezifisches (Zugang, Fixation, Bewegungsvorgaben), das 000 so nicht abdeckt. | Allgemeinen Kern streichen; in 001 belassen: `hinweis` „Zugang, Fixation, angeordnete Bewegungsvorgaben, Zählstatus“ (hüft-/eingriffsspezifisch). | – | mittel |
| B2-9 | ok | – | In 001 streichen. | – | – |
| B2-10 | ok | – | In 001 streichen. | – | – |
| B2-11 | ok | – | In 001 streichen; 000 `OP-Licht ausgerichtet + Lichtgriffe` deckt ab. | – | – |
| B2-12 | ok | – | In 001 streichen; Schärfung „Jod zu unspezifisch“ / Implantatmaterial ggf. in 000 `Allergien/…` übernehmen. | – | niedrig |
| B2-13 | Fehler | Nicht deckungsgleich: 000 = „nicht-imprägnierte Folie nicht verwenden“ (KRINKO Kat. IB); 001 = „nur nach Hausplan / keine allgemeine Pflicht zur Folie“. | 000-Eintrag behalten. 001 nicht ersatzlos streichen: `optional: true`, `hinweis`: antiseptisch imprägniert nur falls Hausplan; keine allgemeine Folienpflicht. Oder diesen Satz nach 000 ergänzen. | KRINKO S. 461 (nicht antiseptisch imprägnierte Inzisionsfolien nicht empfohlen, Kat. IB). | hoch |
| B2-14 | ok | – | In 001 streichen. | – | – |
| B2-15 | ok | – | In 001 streichen. | – | – |
| B2-16 | ok | – | In 001 streichen (000 `Hautdesinfektion laut Haus`). | – | – |
| B2-17 | Fehler | 000 = Funktions-/Leistungsprüfung; 001 = Betriebsart mono/bi klären – nicht identisch. | Betriebsart-Klärung nach 000 `HF-Gerät funktionsgeprüft` ergänzen oder in 001 als HF-allgemein belassen (kein Hüft-Bezug). Nicht als reine Doppelung streichen. | – | mittel |
| B2-18 | ok | – | In 001 streichen. | – | – |
| B2-19 | ok | – | In 001 streichen. | – | – |
| B2-20 | Fehler | 001-Hinweis „Pfannen-/Schaftphase … Probekomponenten“ ist hüftspezifisch; 000 deckt nur allgemeinen Ansage-Kern. | Allgemeinen Kern streichen; in 001 behalten: Pfannen-/Schaftphase, Probekomponenten, sterile Übergabe. | – | hoch |
| B2-21 | ok | – | In 001 streichen; optionale Schärfung „Durchgängigkeit/Auffangsystem IFU“ ggf. nach 000. | – | niedrig |
| B2-22 | ok | – | In 001 streichen. | – | – |

### Zur Prüfung – Teil D (Haussysteme / Implantatdateien)

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| D-1 | Fehler | `stryker-accolade-ii.json` enthält weiter UHR/Duokopf (Komponente, q3 Japan, Regel duokopf+schaft, offen zu Duokopf). Haus: Stryker **kein** Duokopf. | UHR-Komponente, q3, Regel `duokopf+schaft`, offen-Punkte zu Duokopf/UHR streichen; `system` ohne „+ UHR“. Accolade-II-Hemi-EU-Sperre als Schaft-Attribut/`regeln` belassen (keine Indikation, kein Haus-Duokopf). | STATUS.json haus_systeme; ACCII-SP-1 S. 3/12. | hoch |
| D-2 | Fehler | `julian_pruefen` in 001 fragt weiter nach Duokopf/Schaft inkl. Accolade II/TMZF/Exeter – widerspricht Haus (kein Stryker-Duokopf; Exeter nicht Haussystem). | Duokopf-Rückfrage auf Haus-Systeme mit Duokopf begrenzen: Aesculap Bipolar Cup + Excia zementiert; S+N Bi-Polar Head + SPECTRON EF; Mathys Bipolarkopf + twinSys zementiert. Accolade II nur als „nicht für Hemi/EU“ erwähnen, nicht als Duokopf-Träger. | STATUS.json haus_systeme; ACCII-SP-1. | hoch |
| D-3 | Fehler | `smith-nephew-polarstem.json` ist Haus-fremd (Haus-Schaft zf: SL-PLUS MIA; z: SPECTRON EF). | Datei `implantate/smith-nephew-polarstem.json` (+ .md) streichen bzw. archivieren; gehoert_dazu in STATUS anpassen. | STATUS.json; Julian 07.10.2026. | hoch |
| D-4 | Fehler | Neue Haus-Dateien fehlen: Aesculap Excia, S+N R3, Enovis twinSys. | Neue JSON nur mit am Original bestätigten Feldern anlegen (keine abgeleiteten Kombinationen). Wo nur Broschüre/IT/US: `verified: false`, Markt kennzeichnen, Größen/REF offen. | siehe Abschnitt Quellen | hoch |
| D-5 | ok | – | Systeme nicht mischen: bestätigt. Accolade II EU nicht für Hemi; kein Stryker-Duokopf ableiten. | ACCII-SP-1; STATUS. | – |

### Quellen

| Hersteller | System | Komponente | Dokumenttyp | Titel | Nr./Revision | Stand | Markt | PDF-Link | Seite |
|---|---|---|---|---|---|---|---|---|---|
| Stryker | Accolade | Accolade II zementfrei | OP-Technik | Accolade II Femoral Hip System Surgical protocol | ACCII-SP-1_Rev-4_34423 | © 2022 | EU-Abschnitte vorhanden (S. 3 EU/EMEA/Australia); globale Ausgabe mit EU-Indikationen | https://cdn.stryker.com/SYKGCSDOC-2-45343 | S. 3 Indikationen EU; S. 5 CCD; S. 12 Köpfe/Hemi-Fußnote; S. 15/17 Hülsen; S. 25 Dokumentcode |
| Stryker | Accolade | Accolade II | Design Rationale | Accolade II Femoral Hip Stem Design Rationale | ACCII-PG-3_Rev-1 (Dateiname) | nicht gefunden (kein Datum im geprüftem Kopf) | EU/US/JP nicht eindeutig | https://www.stryker.com/content/dam/stryker/joint-replacement/products/accoladeii/resources/Accolade%20II%20Design%20Rationale%20ACCII-PG-3_Rev-1_22894.pdf | Seitenprüfung offen – keine Größenwerte übernommen |
| Stryker | Accolade | Trident II Tritanium | OP-Technik | Trident II Tritanium Acetabular System Surgical protocol | TRITRI-SP-3_Rev-6_29553 | © 2022 | **EU und Canada** (explizit) | https://az621074-1-cugdarb7eqgsg5g5.a01.azurefd.net/syk-mobile-content-cdn/global-content-system/SYKGCSDOC-2-46747/U2Nvsp-rN0chhVDJe1FHVBhcwuKCRw/TRITRI_SP_3.pdf | S. 1 Distribution EU/Canada; S. 3–4 Indikationen; S. 4 Table 1 X3/Shell/Kopf; Catalog ab S. 20 |
| Stryker | Accolade | Trident II Tritanium | OP-Technik (IT) | Trident II Tritanium sistema acetabolare – Protocollo chirurgico | nicht gefunden | CreationDate 2018-10-01 | IT-Sprachfassung; EU-Gültigkeit der konkreten Ausgabe nicht bestätigt | https://www.stryker.com/content/dam/stryker/joint-replacement/products/trident-ii/resources/Trident%20II%20Tritanium%20Surgical%20Protocol%20-%20IT.pdf | Seitenprüfung offen; für Werte EU-Protokoll TRITRI-SP-3 bevorzugen |
| Stryker | Accolade | X3 Polyethylen-Inlay | in Trident-II-OP-Technik | Trident II Tritanium Surgical protocol (X3 Inserts) | TRITRI-SP-3_Rev-6_29553 | © 2022 | EU/Canada | wie Trident EU oben | Table 1 S. 4; IFU-Hinweis Trident X3 QIN 4351 (ifu.stryker.com) – QIN-PDF selbst nicht gefunden |
| Stryker | Accolade | V40 BIOLOX delta Kopf | OP-Technik (Kopfwerte im Schaft-Protokoll) | ACCII-SP-1 | ACCII-SP-1_Rev-4_34423 | © 2022 | EU-Abschnitte im Dokument | https://cdn.stryker.com/SYKGCSDOC-2-45343 | S. 12 Ø/Offsets; eigenständige EU-IFU V40 BIOLOX: nicht gefunden |
| Stryker | Accolade | V40 CoCr LFIT Kopf | OP-Technik / Rückrufe | ACCII-SP-1 (LFIT CoCr V40 Tabelle); BfArM-Kundeninfos | ACCII-SP-1 Rev-4; BfArM u. a. 06414/15, 08312/16, 06604/18 | 2022 / 2015–2018 | EU-Abschnitte ACCII; BfArM DE–EU | ACCII URL; https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2015/06414-15_kundeninfo_de.html | ACCII S. 12; chargenspezifische Rückrufe – keine pauschale Übertragung |
| Stryker | Accolade | Duokopf | – | – | – | – | – | nicht gefunden (Haus: kein Stryker-Duokopf) | – |
| Aesculap | Excia | Excia T zementfrei | OP-/Produktbroschüre | AESCULAP Excia T – Hüftendoprothesensystem | nicht gefunden (Broschüre DE) | PDF CreationDate 2026-01-09 | DE-Sprachfassung; CE-Markt nicht separat bestätigt | https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/broschuere-exciathueftschaft.pdf | OP-Technik ab S. 12; Implantatübersicht ab S. 18 (BIOLOX delta / Isocer 12/14 genannt) |
| Aesculap | Excia | Excia zementiert | Broschüre (im Excia-T-Dokument als „Excia T zementiert“) | AESCULAP Excia T | nicht gefunden | 2026-01-09 | DE; Zuordnung „Excia ohne T“ vs. „Excia T zementiert“ offen | wie Excia T oben | Konzept zementiert in Broschüre; eigene EU-IFU: nicht gefunden |
| Aesculap | Excia | Plasmafit Plus / Poly | OP-/Produktbroschüre | AESCULAP Plasmafit – Cementless Acetabular Cup System | O45502 0718-1-4 (pdfinfo Title) | Kennung 0718; aktuellste Rev. nicht bestätigt | EN auf DE-Domain; EU nicht separat bestätigt | https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/aesculap-plasmafit.pdf | Plus/Poly im Text; exakte Katalog-/Kompatibilitätsseite für Größen: Seitenprüfung offen |
| Aesculap | Excia | PE-Pfanne zementiert | Produktkatalog HTML | Cemented Polyethylene Cups | nicht gefunden | nicht gefunden | Katalog EU-Auftritt; konkrete Produktbezeichnung/REF offen | https://catalogs.bbraun.com/en-01/p/PRID00002464/cemented-polyethylene-cups | kein PDF; Name offen |
| Aesculap | Excia | BIOLOX delta Inlay / Kopf | Broschüren-Fundstelle | Excia T / Plasmafit | nicht gefunden | nicht gefunden | DE/EN Broschüre | Excia-T-/Plasmafit-URLs | keine eigenständige EU-IFU gefunden |
| Aesculap | Excia | Isodur CoCr Kopf | EU-IFU / Katalog | – | – | – | – | nicht gefunden | – |
| Aesculap | Excia | Duokopf | Produktkatalog HTML | Bipolar Cup | nicht gefunden | nicht gefunden | Katalog; Excia-zementiert–Kompatibilitätstabelle nicht gefunden | https://catalogs.bbraun.com/en-01/p/PRID00004418/bipolar-cup | HTML; Herstellername „Bipolar Cup“; PDF-IFU nicht gefunden |
| Smith+Nephew | R3 | SL-PLUS MIA | OP-Technik | SL-PLUS MIA Surgical Technique | nicht gefunden | CreationDate 2015-05-01 | EN international; EU nicht eindeutig bestätigt | https://smith-nephew.stylelabs.cloud/api/public/content/6eef714e29534cdab814571b84d5d554?v=d8cda33b&download=true | Seitenprüfung offen – keine Größenwerte übernommen |
| Smith+Nephew | R3 | Kopf–Schaft Matrix (SL-PLUS MIA) | Compatibility Matrix | Stem and Femoral Ball Head Combinations SL-PLUS / MIA / SLR-PLUS | Lit. No. 04758 Ed. 05/23 V11 | 05/2023 | Marktfreigaben länderspezifisch (Disclaimer) | https://smith-nephew.stylelabs.cloud/api/public/content/109d0b33697846fc8e9694f4e70ac4ff?v=0758f390 | 1 Seite; konkrete Paarungen nur nach lokaler Freigabe – keine Werte übernommen |
| Smith+Nephew | R3 | SPECTRON EF | OP-Technik | SPECTRON EF Surgical Technique | nicht gefunden | CreationDate 2023-06-19 | EU/US/JP nicht eindeutig | https://smith-nephew.stylelabs.cloud/api/public/content/bc33e9a6123b4239b48d4df8c9d84aa9?v=1c492828&download=true | Seitenprüfung offen |
| Smith+Nephew | R3 | R3 Pfanne / R3 XLPE | Systembroschüre DE | R3 Acetabulum-System / JN245-17 | JN245-17 | CreationDate 2017-04-27 | DE; aktuelle EU-IFU nicht bestätigt | https://smith-nephew-delivery.stylelabs.cloud/api/public/content/1bd7a20b4fdf4a158b95aad5987f2686?v=e321be27&download=true | Seitenprüfung offen |
| Smith+Nephew | R3 | REFLECTION zementfrei | EU-OP-Technik / IFU | – | – | – | – | nicht gefunden | – |
| Smith+Nephew | R3 | REFLECTION All-Poly zementiert | EU-OP-Technik / IFU | – | – | – | – | nicht gefunden | – |
| Smith+Nephew | R3 | Müller-PE-Pfanne | EU-OP-Technik / IFU | – | – | – | – | nicht gefunden | – |
| Smith+Nephew | R3 | OXINIUM / BIOLOX delta / CoCr Köpfe | eigenständige EU-IFU | – | – | – | – | nicht gefunden (nur übergeordnete Matrix 04758) | – |
| Smith+Nephew | R3 | Bi-Polar Head | EU-OP-Technik / IFU | – | – | – | – | nicht gefunden | – |
| Smith+Nephew | (nicht Haus) | POLARSTEM | IFU | POLARSTEM Non-Cemented and Cemented Stem System IFU | 81098832 Rev. 2 | 06/2021 | **USA only** (S. 1) | https://smith-nephew.stylelabs.cloud/api/public/content/dda3044cb508477195f9fb946f902eef?download=true&v=277c7283 | S. 1 US only; S. 4 Device Description; S. 5 Cemented+OXINIUM/BIOLOX – nicht für Hausdatei verwenden |
| Enovis/Mathys | twinSys | twinSys zf/z | OP-Technik | twinSys Surgical technique V06 (Perplexity-Link) | V06 laut Dateiname | nicht gefunden | Abruf 415 / HCP-Gate – Original nicht geprüft | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_twinSys_EN_V06.pdf | nicht gefunden |
| Enovis/Mathys | twinSys | RM Classic | OP-Technik | RM Classic Pfanne Operationstechnik | nicht gefunden | nicht gefunden | Abruf nicht möglich | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_RM_Classic_Pfanne_DE.pdf | nicht gefunden |
| Enovis/Mathys | twinSys | seleXys PC | OP-Technik | seleXys PC V04 | V04 laut Dateiname | nicht gefunden | Abruf nicht möglich | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_seleXys_PC_DE_V04.pdf | nicht gefunden |
| Enovis/Mathys | twinSys | ccB-Pfanne | OP-Technik/Produktinfo | CCB/CCE V01 | V01 laut Dateiname | nicht gefunden | Abruf nicht möglich | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_Produktinfo_CCB_CCE_DE_V01.pdf | nicht gefunden |
| Enovis/Mathys | twinSys | PE-Inlay Standard | EU-IFU | – | – | – | – | nicht gefunden | – |
| Enovis/Mathys | twinSys | ceramys / symarec | Produktinfo | Prospekt Keramik / symarec | V03 / V01 laut Dateiname | nicht gefunden | Abruf nicht möglich | mathysmedical.com Produktinfo-URLs laut eingang/001-perplexity.md | nicht gefunden |
| Enovis/Mathys | twinSys | CoCr Kopf | EU-IFU | – | – | – | – | nicht gefunden | – |
| Enovis/Mathys | twinSys | Bipolarkopf | OP-Technik FR | Têtes bipolaires … V01 | V01 laut Dateiname | nicht gefunden | Abruf nicht möglich | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Bipolar-Hemi/OP-Technik-Produktinfo_Bipolar-Hemikopf_FR_V01.pdf | nicht gefunden |
| Enovis/Mathys | twinSys | Kompatibilitätsübersicht | Compatibility chart | OPT Hipheads Mathys EN V01 | V01 laut Dateiname | nicht gefunden | Abruf nicht möglich | https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Kompatibilitaets-Chart/Kompatibilit%C3%A4ts-Chart_OPT_Hipheads_Mathys_EN_V01.pdf | nicht gefunden |

### Zusatz (Praxis)

- Zementansage rückbestätigen und Stopper/Messhilfe unterscheiden: klinisch sinnvoll, haus-SOP; kein Leitlinien-Wortlaut als Beleg.
- Mathys-Downloadcenter verlangt Nutzungsbedingungen/HCP – ohne akzeptierten Abruf keine Werte.
- Trident II EU-Protokoll (TRITRI-SP-3) ist die belastbare Grundlage für Haus-Pfanne/X3; IT-Protokoll nur Hilfsfundstelle.
- Excia-Broschüre spricht von „Excia T zementiert“; Julian-Auftrag „Excia zementiert“ (ohne T) – Namensabgleich am Etikett nötig (Teil E/Julian).

