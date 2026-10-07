# Enovis (Mathys) – optimys + RM Pressfit vitamys

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine EU-IFU gelesen; keine klinische Freigabe._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `enovis.optimys.schaft` | schaft | optimys | fixation: zementfrei (Kurzschaft); varianten: Standard und Lateral, 12 Größen (Produktseite); werte: Größenbezeichnungen/REF offen | optimys | belegt |
| `enovis.rm_pressfit_vitamys` | pfanne | RM Pressfit vitamys | fixation: zementfrei; bauart: Monoblock – kein separates modulares Inlay; werte: Größen offen | rm | belegt |
| `enovis.kopf.ceramys` | kopf | ceramys | werte: offen; keine named-stem-Matrix in der Broschüre | heads | offen |
| `enovis.kopf.symarec` | kopf | symarec | werte: offen | heads | offen |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `enovis.optimys.schaft` | `enovis.kopf.ceramys` | **offen** | Kopf-Chart (aktuelle Enovis-Fassung) fehlt | heads | – |

## Regeln
- RM Pressfit vitamys ist Monoblock – kein Inlay anbieten. (rm)
- seleXys TH+/TPS nicht in die Auswahl (historische TGA-Warnung 2015, Australien; seleXys PC nicht betroffen). (TGA 16.09.2015)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|
| optimys lateral TAV Gr. 7 unzementiert (REF 52.34.0207, Lot 2240248) – Siegelnaht | BfArM | FSCA 17/02 (07038-17), 18.07.2017 | EU/DE | – | nur diese Charge | `enovis.optimys.schaft` | https://www.bfarm.de/SharedDocs/Kundeninfos/DE/11/2017/07038-17_kundeninfo_de.pdf?__blob=publicationFile |

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.

## Offen
- [ ] optimys-Größen/REF und Kopf-Freigaben (OP-Technik V04 2020 bzw. aktuelle Enovis-Fassung)
- [ ] RM Pressfit vitamys Größen
- [ ] aktuelles Enovis-Kopf-Chart
- [ ] Duokopf: twinSys zementiert + Mathys bipolar (siehe enovis-twinsys)

## Quellen
- **optimys** Enovis optimys – Produktseite · undatiert, Abruf 07.10.2026 · S. Product details · Markt: international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/en/products/325/optimys.html
- **rm** RM Pressfit vitamys – Product Information · 336.010.121 03-0123-01, 2023-01 · S. PDF 2–5 (Monoblock) · Markt: EN/international · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4724/file/produktinformation_rm-pressfit_en_v3.0.pdf
- **heads** Mathys Ceramic Product Information · 336.010.127 03-0319-01, 2019-03 · S. PDF 2–3 · Markt: international; keine Schaftmatrix · gelesen: Grok/Astra 07.10.2026 · https://enovis-surgical.com/repo/storage/4763/file/produktinformation_keramik_en_v3.0.pdf
- **optimys-ot** optimys Operationstechnik (DE) · Art. 316.010.109, 04-0920 (V04), 09/2020 · S. Implantate S. 18; Dimensionen S. 24 · Markt: EU/CH · gelesen: Perplexity-Fundstelle – alter Link leitet laut Astra um · https://www.mathysmedical.com/Storages/User/Dokumente/Operationstechnik/Huefte/OP-Technik_optimys_DE_V04.pdf

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.

Bilder: keine übernommen – Rechte beim Hersteller.
