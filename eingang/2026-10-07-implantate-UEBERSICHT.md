# Implantat-Extrakt Hüft-TEP – Übersicht (07.10.2026)

**Status: BLOCKIERT – keine Herstellerdaten extrahiert.**

## Was passiert ist
Die Extraktions-Sitzung sollte Herstellerdokumente (OP-Techniken, Kompatibilitäts-Charts, Kataloge) von drei Herstellern laden. Der ausgehende Netzwerk-Proxy der Sitzung hat **alle drei Hersteller-Hosts mit HTTP 403 (Egress-Policy)** abgelehnt:

| Host | Ergebnis |
|---|---|
| www.mathysmedical.com (twinSys OP-Technik V05, Kompatibilitäts-Chart Hipheads V01) | 403 – blockiert |
| www.stryker.com | 403 – blockiert |
| www.smith-nephew.com | 403 – blockiert |

Gegenprobe: pypi.org war erreichbar (200) – der Proxy funktioniert, nur die Hersteller-Domains sind nicht freigeschaltet.

## Gelesene Dokumente
Keine. Es wurden daher **keine** Extrakt-Dateien (`…-extrakt.json/.md`) angelegt – nichts geschätzt, nichts aus Erinnerung ergänzt.

## Offen
- Netzwerkfreigabe für `www.mathysmedical.com`, `www.stryker.com`, `www.smith-nephew.com` in der Umgebung prüfen (Umgebungs-Einstellungen → Netzwerkzugriff) und Extraktion in einer neuen Sitzung wiederholen.
- Alternativ: Julian legt die PDFs selbst ab (nicht ins Repo – Urheberrecht), dann nur die Daten extrahieren.

## Von Julian zu bestätigen (unverändert aus implantate/LIESMICH.md)
- Stryker: Accolade II oder Accolade TMZF? Name der zementfreien Pfanne (Trident / Trident II?) und des Duokopfs?
- Mathys: Namen der Pfannen (zementfrei/zementiert) und des Duokopfs.
- Smith & Nephew: Systemnamen von Schaft (zementfrei/zementiert), Pfannen und Duokopf.
