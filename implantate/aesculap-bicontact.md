# Aesculap (B. Braun) – Bicontact (S/H/SD/N)

_Version 1.0 · Stand 2026-10-07 · **verified: false** – Neuanlage P1 aus O10702 0113/1/1 und B.Braun-Produktseite. Plasmafit/All POLY nur Kontext (EPRD ≠ Freigabe). Keine klinische Freigabe._

## Komponenten (Auswahl)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `aesculap.bicontact.s.zementfrei` | schaft | Bicontact S zementfrei | Konus 12/14; CCD 135°; ISOTAN F + PLASMAPORE; REF NK510T–NK521T | bc1 | belegt |
| `aesculap.bicontact.h.zementfrei` | schaft | Bicontact H zementfrei | Konus 12/14; CCD 128°; +6 mm Offset; REF NK110T–NK121T | bc1 | belegt |
| `aesculap.bicontact.s.zementiert` | schaft | Bicontact S zementiert | Konus 12/14; CoCr; REF NK610K–NK618K | bc1 | belegt |
| `aesculap.bicontact.h.zementiert` | schaft | Bicontact H zementiert | Konus 12/14; REF NK312K–NK318K | bc1 | belegt |
| `aesculap.bicontact.sd.zementfrei` | schaft | Bicontact SD zementfrei | Konus 12/14; enge/dysplastische Markräume; REF NK709T–NK716T | bc1 | belegt |
| `aesculap.bicontact.n` | schaft | Bicontact N | **Konus 8/10** | bc1 | belegt |
| `aesculap.bicontact.revision` | schaft | Bicontact Revision | Konus 12/14; Details offen | bc1 | offen |
| `aesculap.plasmafit.plus.bicontact_kontext` | pfanne | Plasmafit Plus (Kontext) | EPRD-Kombi; Freigabe offen; Details in `aesculap-excia` | es | offen |
| `aesculap.plasmafit.poly.bicontact_kontext` | pfanne | Plasmafit Poly (Kontext) | nur PE laut Plasmafit-Dok; Freigabe mit Bicontact offen | pf | offen |
| `aesculap.all_poly.bicontact_kontext` | pfanne | All POLY zementiert (Kontext) | EPRD; Freigabe offen | es | offen |
| `aesculap.kopf.biolox_delta.bicontact_1214` | kopf | BIOLOX delta 12/14 | REF laut O10702 | bc1 | belegt |
| `aesculap.kopf.isodur.bicontact_1214` | kopf | Isodur F CoCr 12/14 | REF laut O10702 | bc1 | belegt |

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle |
|---|---|---|---|---|
| Bicontact S/H/SD zf | BIOLOX / Isodur 12/14 | ja | Konus 12/14 | bc1 |
| Bicontact N | Köpfe 12/14 | nein | N = 8/10 | bc1 |
| Bicontact | Plasmafit | offen | EPRD ≠ Freigabe | es |
| Bicontact zem | All POLY | offen | EPRD ≠ Freigabe | es |

## Regeln
- Bicontact N (8/10) nicht mit Köpfen 12/14 kombinieren.
- Excia T und Bicontact sind getrennte Schaftlinien.
- Registerpaarungen (Plasmafit/All POLY) sind keine Herstellerfreigabe.

## Offen
- [ ] Aktuelle EU-IFU (neuer als O10702 0113)
- [ ] Explizite Freigabetabelle Bicontact ↔ Plasmafit / All POLY
- [ ] Revision: vollständige REF/Längen
- [ ] BfArM Bicontact

## Quellen
- **bc1** O10702 0113/1/1 · https://knoglemekanik.dk/Vejledninger/O10702%20Bicontact%202013.pdf — korrigiert: siehe JSON-URL
- **bc-web** https://www.bbraun.de/de/products/b/bicontact-hueftendoprothesensystem.html
- **pf** O45502 Plasmafit · bbraun.de
- **es** EPRD 2025 / auswahl-dach

## Änderungen
- **v1.0** (2026-10-07, p1-fehlende-systeme): Neuanlage.

Bilder: keine übernommen – Rechte beim Hersteller.
