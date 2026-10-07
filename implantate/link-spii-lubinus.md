# Waldemar Link – SP II Modell Lubinus

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Neuanlage P1 aus Link SP-II-OP-Technik (US 2020-05) und Produktseiten. Lubinus Cup Hersteller-Paarung; IP/CombiCup offen. Keine klinische Freigabe._

## Komponenten (Auswahl)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `link.spii.standard` | schaft | SP II Standard | nur zementiert; CoCrMo; Konus 12/14; CCD 117/126/135°; Längen 130/150/170 mm; R/L | sp1 | belegt |
| `link.spii.xl` | schaft | SP II XL | Hals +10,5 mm; CCD 117/126° | sp1 | belegt |
| `link.pfanne.lubinus` | pfanne | Lubinus Cup | zementiert UHMWPE/X-Linked; **explizit mit SPII** laut Produktseite | cup-web | belegt |
| `link.pfanne.ip` | pfanne | IP Cup | zementiert; EPRD SPII+IP; Freigabeformel schwächer → offen | cup-web | offen |
| `link.pfanne.combicup` | pfanne | CombiCup | zementfrei eigenes System; EPRD Hybrid; Freigabe offen | combi | offen |
| `link.kopf.modular_1214` | kopf | Modular 12/14 | max. +4 mm Halszusatz laut sp1; Material-REF offen | sp1 | hausabhängig |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle |
|---|---|---|---|---|
| SP II | Kopf 12/14 | bedingt | Halszusatz ≤ +4 mm | sp1 |
| SP II | Lubinus Cup | ja | Hersteller-Produktseite | cup-web |
| SP II | IP Cup | offen | EPRD / keine gleich starke Freigabeformel | cup-web; es |
| SP II | CombiCup | offen | eigenes zf-System | combi; es |

## Regeln
- SP II nur zementiert (sp1).
- Keine Fremdhersteller-Kombination (sp1); EPRD SPII+Allofit ⚠ keine Freigabe.
- Schaft eine Größe kleiner als letzte Raspel für ~2–3 mm Zementmantel (sp1).

## Offen
- [ ] EU/DE-OP-Technik (EN 2026-04) abgleichen
- [ ] Vollständige REF-Matrix in App-Tabelle
- [ ] Kopf-REF Katalog
- [ ] IP/FAL/FC Größen & Freigabe
- [ ] CombiCup: bewusst getrennt oder Freigabe nachziehen

## Quellen
- **sp1** https://www.link-ortho.com/fileadmin/user_upload/Fuer_den_Arzt/Produkte/Downloads/US/6431_SP_II_OP-Impl-Instr_us_2020-05_001_MAR-01247_1.0_final.pdf
- **sp-web** https://www.link-ortho.com/products/hip/link-spii
- **cup-web** https://www.link-ortho.com/products/hip/cemented-acetabular-cup-system
- **combi** CombiCup R OP 2020-09 (Link)
- **es** EPRD 2025 / auswahl-dach

## Änderungen
- **v1.0** (2026-10-07, p1-fehlende-systeme): Neuanlage.

Bilder: keine übernommen – Rechte beim Hersteller.
