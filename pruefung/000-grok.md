# Prüfung 000-grundwissen v1.3 – Grok – 07.10.2026

Scope: nur Delta v1.1→v1.3 („Zur Prüfung in dieser Runde“, Nr 1–10). Quellen selbst geöffnet (pdftotext). Nichts erfunden. Kein Eingriffsspezifisches.

| Nr | ok/Fehler | Problem | Vorschlag im Paket-Schema | Quelle (Titel, Stand, Seite, URL) | Priorität |
|---|---|---|---|---|---|
| 1 | ok | umgesetzt wie beschrieben (WHO = Patientenbestätigung; Armband + aktive Rückfrage in `hinweis` über q_kvwl) | – | WHO Implementation Manual Surgical Safety Checklist 2009, Sign-in „Has the patient confirmed his/her identity…“ · https://www.who.int/docs/default-source/patient-safety/9789241598590-eng.pdf · KVWL Handlungsempfehlung Vermeidung einer Eingriffsverwechslung, 2. Aufl. 2024, Kap. Sichere Patientenidentifikation / 1.2 Armband · https://www.kvwl.de/fileadmin/user_upload/pdf/Mitglieder/Qualitaetssicherung/Patientensicherheit/Vermeidung_einer_Eingriffsverwechslung.pdf | – |
| 2 | ok | umgesetzt wie beschrieben (Fundstelle S. 462 Kat. II; Erläuterung S. 454) | – | KRINKO Prävention postop. WI, Bundesgesundheitsbl 2018;61:448–473, gedr. S. 462 (PDF-S. 15): bis OP-Beginn mit sterilen Tüchern abdecken Kat. II; S. 454: Instrumentarium erst unmittelbar vor Schnitt aufdecken · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 3 | ok | umgesetzt wie beschrieben (nicht auszuschließen / Kat. IB; `hausabhaengig: false`) | – | KRINKO 2018, gedr. S. 461 (PDF-S. 14), Abschn. 4.1: flüssigkeitsundurchlässige Abdeckung, sobald Durchfeuchten nicht auszuschließen, Kat. IB · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 4 | ok | umgesetzt wie beschrieben (Kat. IB; Spez klar) | – | KRINKO 2018, gedr. S. **461** (PDF-S. 14), Abschn. 4.1: Verwendung nicht antiseptisch imprägnierter Inzisionsfolien wird nicht empfohlen, Kat. IB · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 5 | ok | umgesetzt wie beschrieben (Klingen/Instrumente über Haus-Zählplan) | – | APS Flyer „Jeder Tupfer zählt!“, zu zählen u. a. Nadeln, Clips, Drahtteile; Instrumentensiebe/Zusatzinstrumente; Umfang laut Hausfestlegung · https://www.aps-ev.de/wp-content/uploads/2024/06/flyer-JTZ.pdf | – |
| 6 | Fehler | `spez` fordert „jeden Schritt des Zementiervorgangs“ (= BCIS), `quelle` ist aber `q_amboss` (AMBOSS nur „vor Einbringen“). Beleg und Primärquelle passen nicht. | `quelle`: `q_bcis` (ggf. `hinweis` belassen: „AMBOSS: vor Einbringen; BCIS: jeden Zementierschritt.“). Alternativ beide IDs, wenn Schema mehrere erlaubt. | Heraeus/PALACADEMY Factsheet Implantationssyndrom/BCIS, PDF S. 1, Vorsichtsmaßnahmen Chirurgie Nr. 1 · https://www.heraeus-medical.com/dam/jcr:b107fb34-cb46-452f-b5e0-076c7946ee4c/palacademy-factsheet-implantationssyndrom.pdf | mittel |
| 7 | ok | umgesetzt wie beschrieben (`gilt_fuer: alle`, Kat. II) | – | KRINKO 2018, gedr. S. 461 (PDF-S. 14), Abschn. 4.1: Patient nicht in Flüssigkeitsansammlung des Hautantiseptikums, Kat. II · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | – |
| 8 | Fehler | Heike-Satz „jeden Zementierschritt“ korrekt, aber `quelle: q_amboss` – Wortlaut/Beleg ist BCIS (in 001 bereits `Q_BCIS`). | `quelle`: `q_bcis` | BCIS Factsheet, PDF S. 1, Chirurgie Nr. 1 (s. Nr 6) | mittel |
| 9 | Fehler | Fundstelle `q_krinko` ordnet Inzisionsfolie und Türen/Fluktuation fälschlich **S. 460** zu. Beide stehen auf **S. 461** (PDF-S. 14) in Abschn. 4.1. S. 460: Beginn Abschn. 4.1 (Überschrift + erste Empfehlungen). Sterile Tische S. 462 und Erläuterung S. 454 stimmen. | `fundstelle` korrigieren: gedr. S. **461** (PDF-S. 14), Abschn. 4.1: Antiseptikum-Ansammlung Kat. II; flüssigkeitsundurchlässige Abdeckung Kat. IB; nicht imprägnierte Inzisionsfolie Kat. IB; Fluktuation/Türen Kat. II. S. **462** (PDF-S. 15): sterile Tische bis OP-Beginn abdecken Kat. II. Erläuterung S. 454. | KRINKO Empf_postopWI.pdf selbst geprüft 07.10.2026 (pdftotext PDF-S. 13–15 = gedr. 460–462) · https://edoc.rki.de/bitstream/handle/176904/6416/Empf_postopWI.pdf | hoch |
| 10 | ok | umgesetzt wie beschrieben (q_bcis neu, Fundstelle Chirurgie Nr. 1) | – | BCIS Factsheet Implantationssyndrom, PDF S. 1 · URL s. Nr 6 | – |

**Sum:** 7× ok · 3× Fehler (1× hoch, 2× mittel)

## Zusatz (Praxis)
- PDF-Zuordnung Empf_postopWI.pdf: PDF-S. 13 = gedr. 460 · 14 = 461 · 15 = 462.
- Inhalt Nr 4 (Inzisionsfolie) ist fachlich richtig; nur die Seitenzahl in `quellen.q_krinko` (Nr 9) ist falsch – nicht doppelt strafen.
- 001 setzt denselben Zement-Satz bereits auf `Q_BCIS`; 000 sollte angleichen (Nr 6/8), sonst Quellen-Widerspruch 000↔001.
