# Prüfauftrag für Gegenprüfer

Für jedes Paket in `pakete/`, dessen Version in `pruefung/STATUS.json` nicht „geprüft“ ist:

1. **Quellen:** Jede Zeile mit `"sicherheit":"belegt"` in der angegebenen Quelle nachlesen (Seite/Abschnitt). Ergebnis: bestätigt / zu weit gefasst / nicht gefunden.
2. **Fehler:** falsche, veraltete oder gefährliche Aussagen mit Begründung und Quelle.
3. **Lücken:** was für die Springer-Vorbereitung fehlt (Geräte, Lagerung, Abdeckung, Siebe, Material mit Menge, Naht mit Stärke/Nadel/Schicht).
4. **Einträge** für Korrekturen/Ergänzungen im Paket-Schema: `label` (≤ 40 Zeichen), `menge`, `einheit`, `spez`, `schicht`, `gilt_fuer`, `optional`, `sicherheit` (belegt/üblich/hausabhängig), `hausabhaengig`, `quelle`, `hinweis`.

**Quellen nur seriös:** AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-OP-Techniken/IFU, öffentliche Klinik-SOPs, AMBOSS. Keine Foren, keine Shops.

**Verboten:** Medikamente mit Dosierung, Zement-Mischzeiten, HF-Wattzahlen, Implantatgrößen, Patientendaten. Nichts erfinden – ohne Quelle `quelle: null`.

**Ausgabeformat:**
```
### PRÜFUNG <paket> v<version> – <Datum>
Tabelle „belegt“-Prüfung · Fehlerliste · Lückenliste
```json
{"paket":"…","version":"…","geprueft_am":"…","korrekturen":[…],"ergaenzungen":[…],"quellen_neu":[…]}
```
```
