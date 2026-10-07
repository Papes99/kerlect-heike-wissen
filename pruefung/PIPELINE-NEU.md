# Prüf-Pipeline NEU (Julian, 07.10.2026)

Ereignisgesteuert über Push (GitHub Action). Kein Sekundentakt-Polling.
Vorherige `automation/`-Ideen gelten **nicht**.

README.md und PRUEFAUFTRAG.md bleiben unverändert, bis Julian sie explizit freigibt.

## Kette

1. **Nutzer** gibt Paket ein (Beispiel: `003`).
2. **Perplexity** macht die Quellenangaben **als Erstes** (Recherche, belegt mit Titel/Stand/Seite/URL) → `pruefung/NNN-perplexity.md`.
3. **Cloud** startet die Prüfung.
4. **Cloud → Grokbot**: gründliche Erstprüfung der **ganzen** Paketversion → `pruefung/NNN-grok.md`.
5. **Nur bei Implantaten:** Cloud → **OpenAI** (NUR Implantate: Herstellerangaben, Kompatibilitätstabellen, Indikationsgrenzen — **nicht** Instrumente) → `pruefung/NNN-openai.md`.
6. OpenAI schickt es zurück an Cloud.
7. **Cloud** macht den letzten Check.
8. **Julian** gibt das okay.
9. **Astra implementiert.**
10. Danach: **Grok** und **Astra** löschen jeweils **nur** ihre eigenen Prüfdateien.

## `runde` (v2)

Siehe `runde-schema-v2.json`:

`wartet` → `perplexity` → `cloud` → `grok` → (`openai` nur Implantate) → `cloud-final` → `julian` → `astra-bau` → `abgeschlossen`

## Automatisierung

- Workflow-Vorlage im Repo: `pruefung/github-action-pruef-pipeline.yml`  
  → einmalig nach `.github/workflows/pruef-pipeline.yml` kopieren (GitHub braucht dafür Token-Scope `workflow`; der Push der Action-Datei selbst kann hier nicht per OAuth App erfolgen).
- Bei Push auf `main` (u. a. `pruefung/`, `pakete/`, `implantate/`, `eingang/`): Action liest `pruefung/STATUS.json`, schreibt Job-Summary und aktualisiert Issue **„Prüf-Pipeline: nächste Instanz“**.
- Optionale Secrets zum echten Anstoßen: `PIPELINE_WEBHOOK_PERPLEXITY`, `PIPELINE_WEBHOOK_GROK`, `PIPELINE_WEBHOOK_OPENAI`, `PIPELINE_WEBHOOK_CLOUD`, `PIPELINE_WEBHOOK_ASTRA`.
- Die Action **ändert keine** bestehenden Paket-/Prüfdateien und **schreibt STATUS.json nicht**.

## Rollenhinweis Cloud vs. Claude

In der bisherigen README heißt die Orchestrierungsrolle **Claude**. In dieser Pipeline heißt sie **Cloud**. Bis README/STATUS migriert sind, gilt: **Cloud = bisherige Claude-Rolle** (Basis, STATUS, letzter Check) — Vereinheitlichung der Doku erst nach Julians Go.
