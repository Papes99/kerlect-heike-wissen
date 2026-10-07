# Implantat-Daten (Kompatibilität, REF, Bilder)

Pro System eine Datei `implantate/<hersteller>-<system>.json` + `.md`. **Nur exakte Herstellerdaten** (Kompatibilitätstabelle, OP-Technik, IFU, Katalog) mit Dokument, Stand und Link. Nichts schätzen. Firma **und** System müssen passen.

## Systeme im Haus (Julian, 07.10.2026 – korrigiert)
**Systeme werden nicht gemischt** – je System nur Komponenten, die der Hersteller ausdrücklich dafür vorsieht. Der Duokopf wird mit dem zementierten Schaft desselben Systems verwendet.

| Hersteller | System | Im Haus |
|---|---|---|
| **Stryker** | Accolade (V40, vermutl. Accolade II) | nur zementfreies Hüftsystem (alle Komponenten) |
| **Aesculap (B. Braun)** | Excia | zementfrei + zementiert + Duokopf (mit zementiertem Schaft) |
| **Smith+Nephew** | R3-System: SL-PLUS MIA (zementfrei), SPECTRON EF (zementiert), Pfannen R3 + REFLECTION, Liner R3 XLPE, Köpfe OXINIUM / BIOLOX delta / CoCr | zementfrei + zementiert + Duokopf (mit zementiertem Schaft, Name offen) |
| **Enovis (Mathys)** | twinSys | zementfrei + zementiert + Duokopf (mit zementiertem Schaft) |

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
