#!/usr/bin/env python3
"""Read pruefung/STATUS.json and print next pipeline actor (PIPELINE-NEU). No file writes to STATUS."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "pruefung" / "STATUS.json"

# Map current STATUS runde values + v2 values → next actor label
NEXT = {
    "perplexity": ("Perplexity", "Quellenangaben → pruefung/NNN-perplexity.md, dann runde=cloud"),
    "cloud": ("Cloud", "Prüfung starten → an Grokbot (runde=grok)"),
    "grok": ("Grokbot", "Erstprüfung ganze Paketversion → pruefung/NNN-grok.md"),
    "openai": ("OpenAI", "Nur Implantate → pruefung/NNN-openai.md, zurück an Cloud"),
    "cloud-final": ("Cloud", "Letzter Check → Liste an Julian (runde=julian)"),
    "julian": ("Julian", "Okay → Astra implementiert (runde=astra-bau)"),
    "astra": ("Astra", "Legacy-STATUS: Prüfung/Einbau klären — Zielkette: astra-bau = implementieren"),
    "astra-bau": ("Astra", "Implementieren → abgeschlossen, dann Grok/Astra Dateien löschen"),
    "abgeschlossen": (None, "Fertig — Grok/Astra löschen eigene Prüfdateien falls noch vorhanden"),
    "wartet": ("Nutzer/Cloud", "Paket eingeben / Start → runde=perplexity"),
}


def is_implant_paket(meta: dict) -> bool:
    typ = (meta.get("typ") or "").lower()
    name = (meta.get("name") or meta.get("datei") or "").lower()
    key_hint = name
    return typ == "implantate" or "implantat" in key_hint


def after_grok(meta: dict) -> tuple[str, str]:
    if is_implant_paket(meta):
        return ("OpenAI", "Nach Grok: Implantat-Lauf → OpenAI (nicht Instrumente), dann Cloud-Final")
    return ("Cloud", "Nach Grok: kein Implantat-Schritt → cloud-final (letzter Check)")


def main() -> int:
    if not STATUS_PATH.is_file():
        print(f"STATUS fehlt: {STATUS_PATH}", file=sys.stderr)
        return 1
    data = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    pakete = data.get("pakete") or {}
    offen = []
    for key, meta in pakete.items():
        runde = meta.get("runde") or ""
        if runde == "abgeschlossen":
            continue
        actor, hint = NEXT.get(runde, ("Unbekannt", f"Unbekannte runde={runde!r} — Schema v2 prüfen"))
        if runde == "grok":
            actor, hint = after_grok(meta)
            # Still Grok's turn until grok file exists; Action reports both current + next after
            current = ("Grokbot", "Aktuell runde=grok — Grokbot soll pruefung/NNN-grok.md schreiben")
            offen.append(
                {
                    "paket": key,
                    "name": meta.get("name"),
                    "runde": runde,
                    "aktuell": {"wer": current[0], "hinweis": current[1]},
                    "danach": {"wer": actor, "hinweis": hint},
                    "implantate": is_implant_paket(meta),
                }
            )
            continue
        offen.append(
            {
                "paket": key,
                "name": meta.get("name"),
                "runde": runde,
                "aktuell": {"wer": actor, "hinweis": hint} if actor else {"wer": "—", "hinweis": hint},
                "implantate": is_implant_paket(meta),
            }
        )

    out = {
        "pipeline": "PIPELINE-NEU",
        "offen_count": len(offen),
        "offen": offen,
        "hinweis": "Action stößt an via Issue/Summary/Webhook; STATUS schreibt weiterhin Cloud.",
    }
    text = json.dumps(out, ensure_ascii=False, indent=2)
    print(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("## Prüf-Pipeline NEU — nächste Instanz\n\n")
            if not offen:
                fh.write("Keine offenen Pakete (`runde != abgeschlossen`).\n")
            else:
                for row in offen:
                    fh.write(f"### `{row['paket']}` — {row.get('name')}\n")
                    fh.write(f"- **runde:** `{row['runde']}`\n")
                    fh.write(f"- **jetzt:** {row['aktuell']['wer']} — {row['aktuell']['hinweis']}\n")
                    if "danach" in row:
                        fh.write(f"- **danach:** {row['danach']['wer']} — {row['danach']['hinweis']}\n")
                    fh.write("\n")
    # machine-readable for later steps
    out_path = Path(os.environ.get("PRUEF_NEXT_OUT", "/tmp/pruef-next.json"))
    out_path.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
