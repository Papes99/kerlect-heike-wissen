# Implantat-Daten (Kompatibilität, REF, Bilder)

Pro System eine Datei `implantate/<hersteller>-<system>.json` + `.md`. **Nur exakte Herstellerdaten** (Kompatibilitätstabelle, OP-Technik, IFU, Katalog) mit Dokument, Stand und Link. Nichts schätzen. Firma **und** System müssen passen.

## Systeme im Haus (Julian, Auswahlliste 07.10.2026)
**Systeme werden nicht gemischt** – je System nur Komponenten, die der Hersteller ausdrücklich dafür vorsieht. Duokopf mit dem zementierten Schaft desselben Systems.

| Hersteller · System | Schaft zementfrei | Schaft zementiert | Pfanne zementfrei | Pfanne zementiert | Inlay | Kopf | Duokopf (mit zementiertem Schaft) |
|---|---|---|---|---|---|---|---|
| **Stryker** · Accolade – nur zementfrei | Accolade II | – | Trident II Tritanium | – | X3 Polyethylen | V40 BIOLOX delta, V40 CoCr (LFIT) | – |
| **Aesculap (B. Braun)** · Excia | Excia T | Excia zementiert | Plasmafit Plus, Plasmafit Poly | Aesculap PE-Pfanne zementiert (Name offen) | BIOLOX delta Inlay | BIOLOX delta, Isodur CoCr | Aesculap Bipolarkopf / Duokopf (Name offen) |
| **Smith+Nephew** · R3 | SL-PLUS MIA | SPECTRON EF | R3, REFLECTION (zementfrei) | REFLECTION All-Poly (zementiert), Müller-PE-Pfanne (S+N) | R3 XLPE | OXINIUM, BIOLOX delta, CoCr | Bi-Polar Head (S+N) |
| **Enovis (Mathys)** · twinSys | twinSys zementfrei | twinSys zementiert | RM Classic, seleXys PC | ccB-Pfanne | PE-Inlay Standard | ceramys, symarec, CoCr | Mathys Bipolarkopf |

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

## Bilder
Produktfotos der Hersteller sind urheberrechtlich geschützt und dürfen nicht einfach übernommen werden. Erlaubt: eigene Fotos (Verpackung/Etikett, ohne Patientendaten), Bilder mit schriftlicher Freigabe des Herstellers, eigene Zeichnungen. Feld `bild.rechte` immer ausfüllen.

## REF / UDI
REF exakt laut Herstellerkatalog. Wenn öffentlich verfügbar zusätzlich GTIN (UDI-DI), damit die App später den Barcode auf der Verpackung scannen und mit der Planung abgleichen kann.
