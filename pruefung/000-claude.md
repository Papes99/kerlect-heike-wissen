# 000 – Claude

_Arbeitsdatei Runde 000 (000-grundwissen). Wird bei jeder Runde **überschrieben**. Nach Astras Urteil baut Claude ein und **löscht 000-claude, 000-grok und 000-astra** – übrig bleibt nur das Paket._

## Ablauf dieser Runde
1. **Grok** prüft diese Datei → schreibt `pruefung/000-grok.md`.
2. **Astra** prüft diese Datei **und** `pruefung/000-grok.md` (Grok-Datei unverändert lassen) → schreibt `pruefung/000-astra.md`. Erste Zeile `FREIGEGEBEN` oder `ÄNDERN`. Bei `ÄNDERN`: Tabelle | Nr | Quelle des Punkts (Claude/Grok/Astra) | Entscheidung | Endgültiger Text im Paket-Schema | Quelle (Titel, Stand, Seite, URL) |. Astra entscheidet abschließend, auch zwischen Claude und Grok.
3. **Claude** baut Astras Entscheidung 1:1 ein, schickt Julian die Auflistung und löscht die drei Arbeitsdateien.

## Was Claude geändert hat (noch nicht abschließend geprüft)
Die Änderungen stehen schon im Paket (`pakete/`). Geprüft wird nur, was hier steht. Alles andere ist unverändert.

### 000-grundwissen (v1.1 → v1.3)
Grundlage: Grok-Prüfung 2026-10-07-000-grundwissen-v1.1-grok.md (im Repo unter eingang/) (Grok Nr. 1–7, 11; Nr. 8–10 bleiben offen) = v1.2; KRINKO-Seitenklärung aus 2026-10-07-001-hueft-tep-v1.1-grok.md (im Repo unter eingang/) (sterile Tische S. 462) = v1.3. Abdeckung/Antiseptikum nach deiner 001-Prüfung (S. 461, Abschnitt 4.1). Erstmals bei Astra – nur diese Änderungen prüfen.

| Nr | Art | Abschnitt · Eintrag | ALT (nur geänderte Felder) | NEU | Quelle |
|---|---|---|---|---|---|
| 1 | geändert | facts · **Patientenidentität geprüft** | spez: Armband + Rückfrage; hinweis: None | spez: Patient bestätigt Identität (WHO); Armband + aktive Rückfrage zusätzlich (KVWL/APS); hinweis: Armband steht nicht in der WHO-Checkliste; Armband + Rückfrage laut q_kvwl. | q_who – Implementation Manual WHO Surgical Safety Checklist 2009 |
| 2 | geändert | draping · **Sterile Tische erst kurz vor Beginn** | hinweis: None | hinweis: KRINKO gedruckte S. 462 (PDF-S. 15) Kat. II; Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 3 | geändert | draping · **Abdeckung flüssigkeitsdicht** | spez: passend zum Eingriff; sicherheit: hausabhängig; hausabhaengig: True; quelle: None; hinweis: None | spez: Flüssigkeitsundurchlässig, sobald Durchfeuchten nicht auszuschließen ist (KRINKO Kat. IB).; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Konkretes Abdeckprodukt nach Hausstandard; die Schutzanforderung bleibt bestehen. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 4 | geändert | draping · **Keine nicht imprägnierte Inzisionsfolie** | spez: None | spez: nicht antiseptisch imprägnierte Folien nicht verwenden (Kat. IB) | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 5 | geändert | count · **Nadeln, Klingen, Clips, Drahtteile** | spez: None | spez: Nadeln, Clips, Drahtteile; Instrumente/Klingen laut Haus-Zählplan | q_aps – Flyer „Jeder Tupfer zählt! Zählkontrolle ist Teamarbeit“ |
| 6 | geändert | implants · **Anästhesie vor Zement informieren** | spez: None; hinweis: None | spez: Anästhesie über jeden Schritt des Zementiervorgangs informieren; hinweis: AMBOSS: vor Einbringen; q_bcis: jeden Zementierschritt. | q_amboss – Endoprothetik des Hüftgelenks (Zementhinweis) |
| 7 | neu | pitfalls · **Keine Antiseptikum-Pfützen** | – | spez: Patient darf nicht in angesammeltem Hautantiseptikum liegen.; gilt_fuer: ['alle']; optional: False; sicherheit: belegt; hausabhaengig: False; quelle: q_krinko; hinweis: Einwirkzeit/Abtrocknen laut Antiseptikum-IFU; besonders vor monopolarer HF. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 8 | geändert | heike_hinweise | Zement geplant? Sag der Anästhesie vor dem Einbringen Bescheid. | Zement geplant? Anästhesie über jeden Zementierschritt informieren. | keine (hausabhängig) |
| 9 | geändert | quellen · **q_krinko** | – | Gedruckte S. 461 (PDF-S. 14), Abschnitt 4.1: Antiseptikum-Ansammlung Kat. II, flüssigkeitsundurchlässige Abdeckung bei nicht ausschließbarem Durchfeuchten Kat. IB; S. 460: nicht imprägnierte Inzisionsfolie Kat. IB, Türen/Fluktuation Kat. II; S. 462 (PDF-S. 15): sterile Tische bis OP-Beginn abdecken Kat. II; Erläuterung S. 454. | q_krinko – Prävention postoperativer Wundinfektionen, Bundesgesundheitsbl 2018;61:448–473 |
| 10 | neu | quellen · **q_bcis** | – | Factsheet Implantationssyndrom / BCIS – PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1: Anästhesie über jeden Schritt des Zementiervorgangs informieren. | q_bcis – Factsheet Implantationssyndrom / BCIS |
