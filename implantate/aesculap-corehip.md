# Aesculap (B. Braun) – CoreHip

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Neuanlage P1 aus CoreHip-Broschüre DE Nr. 4008487 (02/2024) und O61502. Plasmafit/All POLY nur Kontext (EPRD ≠ Freigabe)._

## Komponenten (Auswahl)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.corehip.primary.zementfrei` | schaft | CoreHip Primary zf | Konus 12/14; Linien VLG 142° / STD 132° / VAR 122° / DYS 142°; REF NK10xxT… | ch-de | belegt |
| `aesculap.corehip.primary.zementiert` | schaft | CoreHip Primary zem / AS | Größen 1/3/5/7/9; Centralizer NK128x; AS = Z-REF | ch-de | belegt |
| `aesculap.corehip.extended.zementfrei` | schaft | CoreHip Extended zf | längere Schäfte; REF NK11xxT… | ch-de | belegt |
| `aesculap.plasmafit.plus.corehip_kontext` | pfanne | Plasmafit Plus (Kontext) | EPRD; Freigabe offen; Details `aesculap-excia` | es | offen |
| `aesculap.all_poly.corehip_kontext` | pfanne | All POLY (Kontext) | EPRD; Freigabe offen | es | offen |
| `aesculap.kopf.biolox_delta.corehip` | kopf | BIOLOX delta 12/14 | REF in Broschüre | ch-de | belegt |
| `aesculap.kopf.isodur.corehip` | kopf | Isodur F 12/14 | REF in Broschüre | ch-de | belegt |

### Offset / CCD (Primary)
| Linie | CCD | Offset (mm) |
|---|---|---|
| Valgus (VLG) | 142° | 30,5–38,0 |
| Standard (STD) | 132° | 38,0–45,5 |
| Varus (VAR) | 122° | 45,5–53,0 |
| Dysplasie (DYS) | 142° | 30,5–38,0 (−10 mm Beinlänge vs. VLG; ASIA-Raspel) |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle |
|---|---|---|---|---|
| CoreHip Primary | BIOLOX / Isodur 12/14 | ja | Konus 12/14 | ch-de |
| CoreHip | Plasmafit | offen | EPRD ≠ Freigabe | es |
| CoreHip zem | All POLY | offen | EPRD ≠ Freigabe | es |

## Regeln
- Schaftlinie = Probehalsadapter + Raspelposition.
- Dysplasie nur mit ASIA-Raspel NT1154.
- Größe 0 (alle Linien) und Dysplasie Größe 1: Gewicht max. 60 kg laut Broschüre.

## Offen
- [ ] Explizite Freigabe CoreHip ↔ Plasmafit / All POLY
- [ ] Isocer-Köpfe vollständig (nur PE/XLPE)
- [ ] BfArM CoreHip

## Quellen
- **ch-de** https://www.bbraun.de/content/dam/catalog/bbraun/bbraunProductCatalog/S/AEM2015/de-de/b307/corehip-broschuere.pdf (Nr. 4008487, 02/2024)
- **ch-en** O61502 0321 (EN)
- **pf** Plasmafit O45502
- **es** EPRD 2025 / auswahl-dach

## Änderungen
- **v1.0** (2026-10-07, p1-fehlende-systeme): Neuanlage.

Bilder: keine übernommen – Rechte beim Hersteller.
