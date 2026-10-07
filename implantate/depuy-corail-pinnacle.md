# DePuy Synthes (Johnson & Johnson MedTech) – CORAIL (zementfrei/zementiert) + PINNACLE

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine EU-IFU gelesen; keine klinische Freigabe._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `depuy.corail.zementfrei` | schaft | CORAIL zementfrei (HA) | fixation: zementfrei; konus: 12/14 ARTICUL/EZE Mini Taper (AMT); varianten: {"STD 135° ohne/mit Kragen": "8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20", "HO 135° ohne/mit Kragen": "9, 10, 11, 12, 13, 14, 15, 16, 18, 20", "KLA 125° mit Kragen": "9, 10, 11, 12, 13, 14, 15, 16, 18, 20", "Dysplasie": "6A/6S (eigene Regeln)"}; hinweis: STD125/SN135 nicht aus anderen Familien ableiten | corail | belegt |
| `depuy.corail.zementiert` | schaft | CORAIL zementiert | fixation: zementiert; konus: 12/14 AMT; varianten: {"STD": "8–16, 18, 20", "HO": "9–16, 18, 20"}; hinweis: HA-beschichtete Schäfte dürfen nicht zementiert werden | corail | belegt |
| `depuy.pinnacle.schale` | pfanne | PINNACLE Press Fit | fixation: zementfrei; werte: aktuelle EMEA-Matrix Schale × Liner × max. Kopf-Ø offen | pinnacle | offen |
| `depuy.pinnacle.liner` | inlay | PINNACLE Liner | konfigurationen: Neutral, +4 Neutral, +4 10° Face-Changing, Lipped (pinnacle S. 8–10); material: AltrX/Marathon PE, Keramik – je Schale/Kopf offen; hinweis: Probeliner 28–44 mm sind keine Implantatfreigabe | pinnacle | belegt |
| `depuy.triloc2.zementiert` | pfanne | TRILOC II-PE (zementiert) | fixation: zementiert; werte: offen – nur Registerbeleg (EPRD zementiert #5) | – | offen |
| `depuy.kopf.biolox_delta` | kopf | ARTICUL/EZE BIOLOX delta | konus: 12/14; werte: Ø/Offsets offen | corail | offen |
| `depuy.kopf.cocr` | kopf | ARTICUL/EZE CoCr | konus: 12/14; werte: Ø/Offsets offen | corail | offen |
| `depuy.duokopf.self_centering` | duokopf | SELF-CENTERING Bipolar | verwendung: mit CORAIL zementiert (zu prüfen); freigabe: offen – nur US-Technik; in CH häufig: CORAIL zementiert + Cathcart (unipolar) | scb | offen |
| `depuy.duokopf.cathcart` | duokopf | Modular Cathcart Unipolar | art: unipolar (Endokopf), kein bipolarer Duokopf; registerbeleg: SIRIS Tab. 4.34: CORAIL zementiert / J&J Cathcart 2024 n=300 | scb | offen |

### Größen – CORAIL zementfrei (HA) (Quelle corail)
| groesse | STD_135 | HO_135 | KLA_125 |
|---|---|---|---|
| 8 | ja | – | – |
| 9 | ja | ja | ja |
| 10 | ja | ja | ja |
| 11 | ja | ja | ja |
| 12 | ja | ja | ja |
| 13 | ja | ja | ja |
| 14 | ja | ja | ja |
| 15 | ja | ja | ja |
| 16 | ja | ja | ja |
| 18 | ja | ja | ja |
| 20 | ja | ja | ja |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `depuy.corail.zementfrei` | `depuy.kopf.biolox_delta` | **bedingt** | DePuy-12/14-Kopf laut konkreter Produktfreigabe; vollständige Ø/Offset-Matrix offen | corail | 13 |
| `depuy.corail.zementfrei` | `depuy.kopf.cocr` | **bedingt** | wie oben | corail | 13 |
| `depuy.pinnacle.schale` | `depuy.pinnacle.liner` | **offen** | Liner-Konfiguration belegt, Schale × Liner × Kopf offen | pinnacle | 8–10 |
| `depuy.corail.zementiert` | `depuy.duokopf.self_centering` | **offen** | EU-Freigabe fehlt | scb | – |

## Regeln
- Kopf-Offset max. 13 mm gilt nur für den Dysplasie-Schaft Größe 6; dort keine Hemiarthroplastik und kein Patientengewicht > 60 kg. Keine allgemeine CORAIL-Grenze. (corail S. 13)
- HA-beschichtete CORAIL-Schäfte nie zementieren. (corail)
- Nur DePuy-Synthes-12/14-Köpfe laut Produktfreigabe; keine markenübergreifende Freigabe aus 12/14. (corail)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| CORAIL zementfrei HA 12/14 AMT 135° STD ohne Kragen Gr. 12 (REF 3L92512, Lot 5300693; enthält Gr. 11) | BfArM | PIE-1104627 (02257-18), 02/2018 | EU/DE | – | nur diese Charge | `depuy.corail.zementfrei` | https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2018/02257-18_kundeninfo_en.pdf?__blob=publicationFile |
| CORAIL KLA mit Kragen Gr. 9 (REF 3L93709, Lot 5291990) / HO ohne Kragen Gr. 14 (REF L20314, Lot 5292130) vertauscht | BfArM | PIE-863755 (07375-17), 07/2017 | EU/DE | – | nur diese Chargen | `depuy.corail.zementfrei` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07375-17_kundeninfo_de.pdf?__blob=publicationFile |
| CORAIL AMT Probehälse L94003–L94007 (Instrumente, alle Chargen) | BfArM | PIE-1125109 (06669-18), 05/2018 | EU/DE | – | Instrumentenkorrektur (Dichtungsringpartikel), kein Schaft-Rückruf | – | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/06/2018/06669-18_kundeninfo_de.pdf?__blob=publicationFile |
| PINNACLE Pfannen bestimmter Chargen (Gewinde Apex-Loch) | BfArM | Ref. 1896433 (22108-20), aktualisiert 18.02.2021 | EU/DE | kein Abschluss belegt | betrifft alle gelisteten Pfannen unabhängig von Apex-Schraube; Lot-Liste im Anhang | `depuy.pinnacle.schale` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2021/22108-20_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] PINNACLE EMEA: Schale × Liner (AltrX/Marathon/Keramik) × max. Kopf-Ø
- [ ] ARTICUL/EZE-Köpfe Ø/Offsets je Material
- [ ] SELF-CENTERING Bipolar EU-IFU + Freigabe mit CORAIL zementiert
- [ ] TRILOC II-PE Dokument
- [ ] Implantat-REF
- [ ] ACTIS EU-Dokument (nur Ranking: EPRD n=3.993, SIRIS 2024 n=606)

## Quellen
- **corail** CORAIL Total Hip System Surgical Technique · 198918-211214 UK, ©2022 · S. S. 11, 13, 15, 20–26 / PDF 12, 14, 16, 21–27 · Markt: EMEA (UK-Ausgabe) · gelesen: Grok/Astra 07.10.2026 · https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/198918-170655.pdf
- **pinnacle** PINNACLE Hip Solutions Surgical Technique · 142532-220805 EMEA, ©2022 · S. S. 8–10 / PDF 10–12; S. 16 / PDF 18 · Markt: EMEA · gelesen: Grok/Astra 07.10.2026 · https://p1.aprimocdn.net/jjamp/en/depuy-synthes/ous-only-%E2%80%93-surgical-technique-guide-(stg)/142532-149038.pdf
- **actis** ACTIS Total Hip System Surgical Technique (nur Ranking-Bezug) · 190156-210922 NZ / AU 2020 · S. Warnung S. 8 / PDF 10; Technical Specifications S. 12 / PDF 14 · Markt: AU/NZ – kein EU-Ersatz · gelesen: Grok/Astra 07.10.2026 · https://www.jnjmedtech.com/system/files/pdf/190156.210922%20NZ_134763.200315AU%20ACTIS%20Surgical%20Technique%20FINAL.pdf
- **scb** SELF-CENTERING Bipolar and Modular Cathcart Unipolar Endo Heads – Surgical Technique · DSUS/JRC/0317/2044 Rev. B, ©2017/2022 · S. – · Markt: US – kein EU-Ersatz · gelesen: Perplexity-Fundstelle · http://synthes.vo.llnwd.net/o16/LLNWMB8/US%20Mobile/Synthes%20North%20America/Product%20Support%20Materials/Technique%20Guides/

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.

Bilder: keine übernommen – Rechte beim Hersteller.
