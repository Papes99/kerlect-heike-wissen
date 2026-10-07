# Implantat-Daten (Kompatibilität, REF, Bilder)

Pro System eine Datei `implantate/<hersteller>-<system>.json` + `.md`. **Nur exakte Herstellerdaten** (Kompatibilitätstabelle, OP-Technik, IFU, Katalog) mit Dokument, Stand und Link. Nichts schätzen. Firma **und** System müssen passen.

## Ausgewählte Systeme (häufig in DACH; Julian 07.10.2026)
Auswahl nach Häufigkeit in DACH (EPRD, SIRIS, Österreich) – Erweiterung um DePuy Synthes, Zimmer Biomet, weitere Mathys-Systeme im Lauf `001-implantate-dach`. Jede Klinik prüft ihren Bestand am Etikett.

**Systeme werden nicht gemischt** – je System nur Komponenten, die der Hersteller ausdrücklich dafür vorsieht. Duokopf mit dem zementierten Schaft desselben Systems.

| Hersteller · System | Schaft zementfrei | Schaft zementiert | Pfanne zementfrei | Pfanne zementiert | Inlay | Kopf | Duokopf (mit zementiertem Schaft) |
|---|---|---|---|---|---|---|---|
| **Stryker** · Accolade – nur zementfrei | Accolade II | – | Trident II Tritanium | – | X3 Polyethylen | V40 BIOLOX delta, V40 CoCr (LFIT) | – |
| **Aesculap (B. Braun)** · Excia | Excia T | Excia T zementiert | Plasmafit Plus, Plasmafit Poly | Aesculap PE-Pfanne zementiert (Name offen) | BIOLOX delta Inlay (nur Plus), PE-Inlay Standard (UHMWPE) | BIOLOX delta, Isodur CoCr | Bipolar Cup |
| **Smith+Nephew** · R3 | SL-PLUS MIA, POLARSTEM | SPECTRON EF, POLARSTEM zementiert | R3, REFLECTION (zementfrei) | REFLECTION All-Poly (zementiert), Müller-PE-Pfanne (S+N) | R3 XLPE | OXINIUM, BIOLOX delta, CoCr | TANDEM Bipolar |
| **Enovis (Mathys)** · twinSys | twinSys zementfrei | twinSys zementiert | RM Classic, seleXys PC | ccB-Pfanne (Low- und Full-profile) | seleXys PE Einsatz standard (nur seleXys PC; RM Classic = Monoblock) | ceramys, symarec, CoCr | Mathys Bipolarkopf |
| **DePuy Synthes** · CORAIL/PINNACLE | CORAIL (STD/HO/KLA) | CORAIL zementiert | PINNACLE Press Fit | TRILOC II-PE | PINNACLE Liner | ARTICUL/EZE BIOLOX delta, CoCr | SELF-CENTERING Bipolar (offen) |
| **Zimmer Biomet** | Avenir, Fitmore, CLS Spotorno, Alloclassic | M.E.M., MS-30, Avenir zementiert | Allofit/Allofit-S, G7 | Flachprofil | G7-Liner | BIOLOX delta, CoCr 12/14 | ZB Bipolarkopf |
| **Enovis (Mathys)** · optimys | optimys | – | RM Pressfit vitamys (Monoblock) | – | – | ceramys, symarec | (twinSys-Datei) |
| **Medacta** | Quadra-H, Quadra-P, Amistem-P | Quadra-C, Amistem-C | Versafitcup CC Trio | – | offen | offen | Medacta bipolar |

**Dateien:** `stryker-accolade-ii`, `aesculap-excia`, `aesculap-bicontact`, `aesculap-corehip`, `smith-nephew-r3`, `enovis-twinsys`, `enovis-optimys`, `depuy-corail-pinnacle`, `zimmer-biomet`, `medacta-quadra-amistem`, `link-spii-lubinus` (je .json + .md). Ranking: `auswahl-dach.md`. Bicontact, CoreHip und SP II Lubinus von Julian angelegt (07.10.2026).

## Schema je Datei
```json
{
 "hersteller": "Stryker", "system": "Accolade II", "region": "hüfte", "verified": false,
 "quellen": [{"id":"q1","dokument":"…Kompatibilitätstabelle/OP-Technik/Katalog…","stand":"…","url":"…","seiten":"…"}],
 "komponenten": [
  {"typ":"schaft|kopf|duokopf|pfanne|inlay|schraube|…","bezeichnung":"…","groesse":"…",
   "ref":"Artikelnummer (REF) exakt laut Katalog","gtin":"GTIN/UDI-DI falls öffentlich",
   "attribute":{"konus":"…","durchmesser_mm":…,"halslaenge":"…","offset":"…","material":"…","innen_d_mm":…,"max_kopf_mm":…,"fixation":"zementfrei|zementiert"},
   "bild":{"typ":"eigenes_foto|lizenziert|zeichnung|keins","datei":null,"rechte":"…"},
   "quelle":"q1"}
 ],
 "regeln": [
  {"wenn":"kopf","pruefe":"kopf.konus == schaft.konus","text":"Konus muss gleich sein","quelle":"q1"},
  {"wenn":"inlay","pruefe":"inlay.innen_d_mm == kopf.durchmesser_mm","text":"…","quelle":"q1"}
 ],
 "hinweise": ["Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument maßgeblich."],
 "offen": ["…"]
}
```

## Erweiterung ab v1.1 (Lauf 001-implantate)
- `version`, `aenderungsprotokoll` je Datei.
- Komponente: `id` (fest, z. B. `stryker.trident2.schale`), `auswahl_dach`, `sicherheit` (belegt / hausabhängig / Fundstelle / offen), `aliase`, `groessen` (Liste mit Größe/REF/Varianten genau laut Original).
- `tabellen`: benannte Original-Tabellen (z. B. `T3_trident_x3`) mit `quelle`, `seite`, `zeilen`, `legende`.
- `passt_zu`: `{von, zu, status: ja|bedingt|nein|offen, bedingung, quelle, seite, tabelle}` – nur was das Original ausdrücklich sagt; ungeprüft ≠ verboten ≠ freigegeben; keine transitiven Freigaben.
- `rueckrufe[].betrifft`: Komponenten-IDs; `markt`, `status`.

## Bilder
Produktfotos der Hersteller sind urheberrechtlich geschützt und dürfen nicht einfach übernommen werden. Erlaubt: eigene Fotos (Verpackung/Etikett, ohne Patientendaten), Bilder mit schriftlicher Freigabe des Herstellers, eigene Zeichnungen. Feld `bild.rechte` immer ausfüllen.

## REF / UDI
REF exakt laut Herstellerkatalog. Wenn öffentlich verfügbar zusätzlich GTIN (UDI-DI), damit die App später den Barcode auf der Verpackung scannen und mit der Planung abgleichen kann.
