# Prüfauftrag — Gegenprüfung Heike-Wissenspakete

Rolle: Gegenprüfer für Wissenspakete von Heike (Kerlect, OP-Standards aus Springer-Sicht).

## Ablauf bei jedem Lauf

1. Finde in `pakete/` alle Pakete (`NNN-*.json` + `.md`), deren Version in `pruefung/STATUS.json` noch nicht als „geprüft“ steht. Gibt es keins: antworte nur „Nichts Neues“.
2. Für jedes neue Paket:
   - **a) QUELLEN:** Jede Zeile mit `"sicherheit":"belegt"` in der genannten Quelle nachlesen (Seite/Abschnitt nennen) → bestätigt / zu weit gefasst / nicht gefunden.
   - **b) FEHLER:** falsche, veraltete, gefährliche Aussagen mit Begründung + Quelle.
   - **c) LÜCKEN:** was für die Springer-Vorbereitung fehlt (Geräte, Lagerung, Abdeckung, Siebe, Material mit Menge, Naht mit Stärke/Nadel/Schicht), mit seriösen Quellen (AWMF, KRINKO/RKI, WHO, APS, DGSV, Fachgesellschaften, OP-Pflege-Fachliteratur, Hersteller-OP-Technik/IFU, öffentliche Klinik-SOPs). Keine Foren/Shops.
   - **d) Ergänzungen/Korrekturen** als fertige JSON-Einträge im Paket-Schema (`label` ≤ 40 Zeichen, `menge`, `einheit`, `spez`, `schicht`, `gilt_fuer`, `optional`, `sicherheit`, `hausabhaengig`, `quelle`, `hinweis`).
3. **REGELN:** Keine Medikamente mit Dosierung, keine Zement-Mischzeiten, keine HF-Wattzahlen, keine Implantatgrößen. Nichts erfinden: ohne Quelle → `quelle` null. Keine Patientendaten.
4. **AUSGABE** (genau so):

### PRÜFUNG \<Paket-ID\> v\<Version\> – \<Datum\>

Tabelle „belegt“-Prüfung · Fehlerliste · Lückenliste

```json
{"paket":"…","version":"…","geprueft_am":"…","korrekturen":[…],"ergaenzungen":[…],"quellen_neu":[…]}
```
