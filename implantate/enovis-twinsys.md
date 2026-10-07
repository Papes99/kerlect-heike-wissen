# Enovis (Mathys) – twinSys – zementfrei, zementiert, Duokopf; RM Classic, seleXys PC, ccB

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate: Werte von Grok und Astra am Original gelesen (07.10.2026), Claude-Änderungsliste von Julian abgenommen. Keine EU-IFU gelesen; keine klinische Freigabe. Hausbestand jeder Klinik am Etikett prüfen._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `enovis.twinsys.zementfrei` | schaft | twinSys zementfrei | fixation: zementfrei; varianten: {"Standard": "7–18", "Lateral": "7–18", "XS": "7–12", "Long": "12–15"}; hinweis: nur aufgeführte Einzel-REF; XS/Long sind dokumentierte Varianten, kein Bestandsnachweis | twinsys | belegt |
| `enovis.twinsys.zementiert` | schaft | twinSys zementiert | fixation: zementiert; varianten: {"Standard": "9–16", "Lateral": "9–16"} | twinsys | belegt |
| `enovis.rm_classic` | pfanne | RM Classic | fixation: zementfrei; bauart: Monoblock – kein modulares Inlay | rm-classic | belegt |
| `enovis.selexys_pc` | pfanne | seleXys PC | fixation: zementfrei; inlay: seleXys PE Einsatz (standard/überhöht) oder vitamys-Einsatz (S. 18/19) | selexys | Fundstelle |
| `enovis.ccb` | pfanne | ccB-Pfanne | fixation: zementiert; profile: Low-profile und Full-profile (Auswahl Julian: beide); hinweis: für 60–64 keine CCE-Ringe verfügbar | ccb | belegt |
| `enovis.selexys_pe_einsatz` | inlay | seleXys PE Einsatz (standard) (PE-Inlay Standard) | material: PE; nur_fuer: seleXys PC; varianten: standard / überhöht; hinweis: entspricht vermutlich „PE-Inlay Standard“; RM Classic hat kein Inlay | selexys | Fundstelle |
| `enovis.kopf.ceramys` | kopf | ceramys | werte: offen; keine twinSys-Paarung aus Keramik-Flyer | ceramics | offen |
| `enovis.kopf.symarec` | kopf | symarec | werte: offen | ceramics | offen |
| `enovis.kopf.cocr` | kopf | CoCr | werte: offen | – | offen |
| `enovis.duokopf.bipolar` | duokopf | Mathys Bipolarkopf | verwendung: mit twinSys zementiert; freigabe: offen – Produktseite ohne Schaft-Paarung | enovis-bipolar | offen |

### Größen – twinSys zementfrei (Quelle twinsys)
| variante | groesse | ref |
|---|---|---|
| Standard | 7 | 52.34.1157 |
| Standard | 8 | 52.34.1158 |
| Standard | 9 | 56.11.1000 |
| Standard | 18 | 56.11.1009 |
| Lateral | 7 | 52.34.1159 |
| Lateral | 8 | 52.34.1160 |
| Lateral | 9 | 56.11.1010 |
| Lateral | 18 | 56.11.1019 |
| XS | 7 | 56.11.1068 |
| XS | 8 | 56.11.1069 |
| XS | 9 | 56.11.1070 |
| XS | 10 | 56.11.1071 |
| XS | 11 | 52.34.1161 |
| XS | 12 | 52.34.1162 |
| Long | 12 | 56.11.3003 |
| Long | 13 | 56.11.3004 |
| Long | 14 | 56.11.3005 |
| Long | 15 | 56.11.3006 |

### Größen – twinSys zementiert (Quelle twinsys)
| variante | groesse | ref |
|---|---|---|
| Standard | 9 | 56.11.2000NG |
| Standard | 16 | 56.11.2007NG |
| Lateral | 9 | 56.11.2010NG |
| Lateral | 16 | 56.11.2017NG |

### T19b_ccb – CCB Profil ↔ Kopf-Ø ↔ Außen-Ø (Quelle ccb, S. 21–22)
| profil | kopf_mm | aussen_mm | pflicht |
|---|---|---|---|
| Low-profile | 28 | 42–64 | 42 nur mit Pfannendachverstärkungsring |
| Low-profile | 32 | 42–64 | 42/44/46 nur mit Pfannendachverstärkungsring |
| Full-profile | 28 | 44–58 | – |
| Full-profile | 32 | 44–58 | 44/46 nur mit Pfannendachverstärkungsring |
_jeweils 2-mm-Schritte_

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `enovis.selexys_pc` | `enovis.selexys_pe_einsatz` | **bedingt** | Zuordnung laut seleXys-PC-OP-Technik S. 11–12/19 – noch nicht am Original gelesen | selexys | 11–12, 19 |

## Regeln
- Keine Kopf-/Schaft-/Pfannen-Paarung ohne lesbares Original; Flyer und Produktseiten nennen keine twinSys-Kopffreigabe. (Astra 07.10.2026)
- ccB: kleine Größen nur mit Pfannendachverstärkungsring laut Tabelle. (ccb S. 21–22)
- RM Classic ist Monoblock – kein zusätzliches Inlay anbieten. (rm-classic)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| RM Pressfit vitamys / seleXys vitamys-Inlay (nicht RM Classic) | BfArM | FSCA 12/04 (01107/12), 16.02.2012 | EU/DE | – | IFU-Ergänzung zum Öffnen der Verpackung; nur bei vitamys-Einsätzen relevant | – | https://www.bfarm.de/SharedDocs/Kundeninfos/EN/11/2012/01107-12_kundeninfo_en.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] seleXys PC Original (V04 2019-10) von Grok/Astra lesen; aktuelle Enovis-Fassung
- [ ] Kopf-Kompatibilität twinSys (aktuelles Enovis-Chart)
- [ ] Mathys Bipolarkopf + twinSys zementiert Freigabe
- [ ] twinSys: nicht aufgeführte Einzel-REF
- [ ] EU-IFUs
- [ ] GTIN

## Quellen
- **twinsys** twinSys – Product Information · Item 336.010.078 / 04-0224-01 / 2024-02 · S. PDF 7 Ordering information; Kennung PDF 8 · Markt: EN/international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4721/file/EN_TSS_ProdInfo_V04%20%281%29.pdf
- **ccb** CCB cup – CCE roof reinforcement ring, Surgical Technique/Product Information · Item 336.010.151 / 01-0220-01 / 2020-02 · S. gedr.=PDF 21–22; Kennung 32 · Markt: EN/international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4723/file/op-technik_produktinfo-ccb-cce_en_v1.0.pdf
- **ceramics** Mathys – Ceramic implants, Product Information · Item 336.010.127 / 03-0319-01 / 2019-03 · S. PDF 1–6; Kennung PDF 8 · Markt: EN/international; keine twinSys-Paarung daraus · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf
- **rm-classic** Enovis – RM Classic (Monoblock) · HTML, undatiert · S. Produktbeschreibung · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/en/products/321/rm-classic.html
- **selexys** seleXys PC – Modulares zementfreies Pressfit-Pfannensystem (OP-Technik) · Art. Nr. 316.010.123; 04-1019-01; V04, 2019-10 · S. S. 11–12 Zuordnung; S. 18 vitamys-Einsatz; S. 19 seleXys PE Einsatz standard/überhöht · Markt: DE · gelesen: Perplexity-Fundstelle 07.10.2026; Astra: Altlink leitet um – Original noch nicht von Grok/Astra gelesen · https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_seleXys_PC_DE_V04.pdf
- **enovis-bipolar** Enovis – Bipolar (Hip Heads) · HTML, undatiert · S. Produktbeschreibung · Markt: international; keine twinSys-Paarung · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/en/products/335/bipolar.html
- **hipheads-alt** Mathys – Compatibility chart hip heads (alt) · V01 laut Dateiname · S. – · Markt: Altlink leitet laut Astra um · gelesen: Fundstelle · https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/Kompatibilitaets-Chart/Kompatibilit%C3%A4ts-Chart_OPT_Hipheads_Mathys_EN_V01.pdf

## Änderungen
- **v1.0** (2026-10-07, 001): Erstanlage in Lauf 001 (Fundstellen, Werte offen)
- **v1.1** (2026-10-07, 001-implantate): Größen/REF/Kombinationstabellen aus Grok + Astra (Astra-Korrekturen), feste IDs, passt_zu mit Bedingungen, Rückrufe mit betrifft; Perplexity-Fundstellen (eingang/001-perplexity-2/-3) als Fundstellen.

Bilder: keine übernommen – Rechte beim Hersteller.
