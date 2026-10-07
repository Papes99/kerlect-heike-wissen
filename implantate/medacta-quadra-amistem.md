# Medacta – Quadra (H/C/P), AMIStem (P/C) + Versafitcup CC Trio

_Version 1.1 · Stand 2026-10-07 · **verified: false** – Lauf 001-implantate-dach: Werte von Grok und Astra am Original gelesen (07.10.2026), Änderungsliste von Julian abgenommen. Aufnahme wegen Häufigkeit in DACH (EPRD/SIRIS) – Häufigkeit ist keine Kompatibilitätsfreigabe. Keine klinische Freigabe. Lauf 001-implantate-luecken: Größen/REF aus Medacta-OP-Techniken, 99.99.COM rev. 12 und IFU 75.09.017 rev. 26 vom Claude-Helfer am Original gelesen, mit OpenAI-Korrekturen (Familien getrennt, kleine Schäfte, CC-Trio-Bohrungen, P-Schäfte nicht in COM)._

## Komponenten (Auswahl häufiger DACH-Systeme)
| ID | Typ | Bezeichnung | Angaben | Quelle | Sicherheit |
|---|---|---|---|---|---|
| `medacta.quadra_h` | schaft | QUADRA-H | registerbeleg: EPRD zf-Schaft #13 (n=15.013); Kombi mit Versafitcup CC Trio #10; fixation: zementfrei; material: Titan-Niob-Legierung mit Hydroxyapatit-(HA)-Beschichtung (q_quadra_de S. 2; EN S. 2); konus: 12/14 (nur laut 99.99.COM rev. 12 S. 1; in der OP-Technik nicht genannt); ccd_offset_laengen: nicht genannt; hinweis: Lateralisiert nur 1SN–3SN und 1–7; 00SN und 10 auf Anfrage. Kurzhals-Schäfte (0SN–3SN): Probehälse blau (S. 7). Dokument ist Systembroschüre Quadra-S/-H/-C (Quadra-S nicht übernommen). EN 99.14HSC.12 S. 10 identisch. | q_quadra_de | belegt (Original, 2 Prüfer) |
| `medacta.quadra_c` | schaft | QUADRA-C | registerbeleg: EPRD zementiert #9 (n=3.400); Hybrid mit Versafitcup #7; fixation: zementiert; material: nichtrostender Stahl mit hoher Stickstoffanreicherung (q_quadra_de S. 2; EN: „high nitrogen stainless steel“); konus: 12/14 (nur laut 99.99.COM rev. 12 S. 1); hinweis: Nur Standard 0–7, keine lateralisierte Ausführung, kein Short Neck. Keine Schäfte 9/10 (S. 9). Nicht verwechseln mit QUADRA-P Cemented (eigener Schaft). | q_quadra_de | belegt (Original, 2 Prüfer) |
| `medacta.quadra_p` | schaft | QUADRA-P | registerbeleg: SIRIS 2024 #4 mit Versafitcup (n=1.179); fixation: zementfrei; material: Titan-Niobium-Legierung, proximal Titan-Plasma-Beschichtung (MectaGrip), Hydroxylapatit über gesamte Schaftlänge (q_quadra_p S. 4); konus: None; konus_hinweis: nicht belegt – OP-Technik nennt nur „Konus“; Quadra-P nicht in 99.99.COM rev. 12; hinweis: Reguläre Halslänge und Short Neck, je STD und LAT (S. 4, S. 13). Eigene Familie – nicht mit Quadra-H gleichsetzen. | q_quadra_p | belegt (Original, 2 Prüfer) |
| `medacta.quadra_p_collared` | schaft | QUADRA-P Collared | fixation: zementfrei; material: Titan-Niobium-Legierung, proximal Titan-Plasma-Beschichtung (MectaGrip), Hydroxylapatit über gesamte Schaftlänge; mit Kragen (q_quadra_p S. 4); konus: None; konus_hinweis: nicht belegt (nicht in 99.99.COM rev. 12); hinweis: Nur reguläre Halslänge. „Abstand von 1 mm zwischen dem Kragen und dem medialen Kalkar“ (S. 10). | q_quadra_p | belegt (Original, 2 Prüfer) |
| `medacta.quadra_p_cemented` | schaft | QUADRA-P Cemented | fixation: zementiert; material: hochglanzpolierter Edelstahl (q_quadra_p S. 4); konus: None; konus_hinweis: nicht belegt (nicht in 99.99.COM rev. 12); hinweis: Eigener Schaft – NICHT Quadra-C. Größen 0–8 STD/LAT, kein 00, kein 9 (S. 11, S. 13). | q_quadra_p | belegt (Original, 2 Prüfer) |
| `medacta.amistem_p` | schaft | AMIStem-P | registerbeleg: SIRIS 2024 #6 mit Versafitcup (n=1.032); fixation: zementfrei; material: Niob-Titan-Legierung, proximal TPS-Beschichtung (Titan-Plasma-Spray), HA-Beschichtung auf dem Schaft (q_amistem_p S. 4); konus: None; konus_hinweis: nicht belegt – AMIStem-P nicht in 99.99.COM rev. 12 (dort nur AMIStem H / H Collared / H Proximal Coating / C); hinweis: Regular Neck STD 00–9, LAT 0–8; Short Neck STD 00SN–9SN, LAT 0SN–8SN (S. 15). Nicht mit AMIStem-H (EN 2014) gleichsetzen. | q_amistem_p | belegt (Original, 2 Prüfer) |
| `medacta.amistem_p_collared` | schaft | AMIStem-P Collared | fixation: zementfrei; material: Niob-Titan-Legierung mit Kragen, proximal TPS-Beschichtung, HA-Beschichtung auf dem Schaft (q_amistem_p S. 4); konus: None; konus_hinweis: nicht belegt (nicht in 99.99.COM rev. 12); hinweis: Nur Regular Neck: STD 00–9, LAT 0–8 (S. 15). | q_amistem_p | belegt (Original, 2 Prüfer) |
| `medacta.amistem_c` | schaft | AMIStem-C | registerbeleg: SIRIS Hybrid 183; Hemi mit Medacta bipolar (221) / endohead (345); fixation: zementiert; material: rostfreier Stahl mit hohem Stickstoffgehalt (q_amistem_p S. 4; EN 2014 S. 2: „high nitrogen stainless steel“); konus: 12/14 (nur laut 99.99.COM rev. 12 S. 1 „AMIStem C (12/14)“); hinweis: Maßgeblich DE 99.14ASTEMPS.42 (07/2022) S. 16: Regular Neck STD 00–8, LAT 0–8; Short Neck STD 00SN–8SN, LAT 0SN–8SN. Abweichung zur älteren EN 99.14ASTEM.12 (07/2014) S. 12: dort ohne Größe 00 und ohne Short Neck; Raspel-/Schafttabelle ebenfalls abweichend (siehe Tabellen). Nicht aufgelöst – Lieferbarkeit 00 und SN bei Medacta bestätigen. Größe 9 nicht erhältlich (S. 13). | q_amistem_p | belegt (Original, 2 Prüfer) |
| `medacta.kopf.edelstahl` | kopf | Femurkopf Edelstahl (nichtrostender Stahl) | material: nichtrostender Stahl / Edelstahl (Bezeichnung laut Kopftabelle); konus: None; konus_hinweis: COM rev. 12 führt Edelstahl- und CoCr-Köpfe in 10/12 (nur Native) und 12/14; welche REF welchem Konus entspricht, ist in den OP-Techniken nicht angegeben – Konus am Etikett prüfen (IFU DE S. 26).; durchmesser_mm: ["22", "28", "32"]; hinweis: XL (Ø 28/32) und XXL (Ø 28/32) mit Kragen – kann Bewegungsumfang verringern (q_quadra_de S. 8–9; q_quadra_p S. 9). Ø 22 S kann ROM mit nativer Hüftpfanne verringern (q_quadra_p S. 9). Halslängen in mm: nicht genannt.; fundstellen: q_quadra_de S. 11; q_quadra_en S. 11; q_quadra_p S. 12; q_amistem_p S. 14; q_amistem_en S. 13 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.kopf.cocr` | kopf | Femurkopf CoCr | material: CoCr; konus: None; konus_hinweis: COM rev. 12 führt Edelstahl- und CoCr-Köpfe in 10/12 (nur Native) und 12/14; welche REF welchem Konus entspricht, ist in den OP-Techniken nicht angegeben – Konus am Etikett prüfen (IFU DE S. 26).; durchmesser_mm: ["22", "28", "32", "36"]; hinweis: XL (Ø 28/32) und XXL (Ø 28/32/36) mit Kragen – kann Bewegungsumfang verringern. Halslängen in mm: nicht genannt.; fundstellen: q_quadra_de S. 11; q_quadra_en S. 11; q_quadra_p S. 12; q_amistem_p S. 14; q_amistem_en S. 13 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.kopf.ceramtec_biolox_delta` | kopf | CeramTec BIOLOX delta | material: Keramik BIOLOX delta (CeramTec); konus: 12/14 (COM rev. 12: „Ceramtec BIOLOX delta (12/14 taper)“); durchmesser_mm: ["28", "32", "36", "40"]; hinweis: Kein XL bei Ø 28; kein XXL. Halslängen in mm: nicht genannt.; fundstellen: q_quadra_de S. 11; q_quadra_en S. 11; q_quadra_p S. 12; q_amistem_p S. 14; q_amistem_en S. 13 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.kopf.ceramtec_biolox_option` | kopf | CeramTec BIOLOX Option | material: Keramik BIOLOX Option (CeramTec), mit Metallhülse; konus: 12/14 (COM rev. 12: „Ceramtec BIOLOX OPTION (12/14 taper)“); durchmesser_mm: ["28", "32", "36", "40"]; indikation: Spezifisch für Revisionsfälle („Specific for revision cases“ / „for ceramic head revision“); hinweis: Reihenfolge der Endziffern wörtlich: S .81, M .82, L .85, XL .84. Halslängen in mm: nicht genannt.; fundstellen: q_quadra_de S. 11; q_quadra_en S. 11; q_quadra_p S. 12; q_amistem_p S. 14; q_amistem_en S. 13 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.kopf.mectacer_biolox_delta` | kopf | Mectacer BIOLOX delta | material: Keramik BIOLOX delta (Medacta „Mectacer“); konus: 12/14 (COM rev. 12: „Mectacer BIOLOX delta (12/14 taper)“); durchmesser_mm: ["28", "32", "36", "40"]; hinweis: Nur in q_quadra_p S. 12 und q_amistem_p S. 14 gelistet (nicht in den Quadra-/AMIStem-Fassungen 2012–2016). Ø 40 ohne Anfrage-Marker.; fundstellen: q_quadra_p S. 12; q_amistem_p S. 14 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.kopf.mectacer_biolox_option` | kopf | Mectacer BIOLOX Option System (Kopf + Hülse) | material: Keramikkopf BIOLOX Option + Hülse; konus: 12/14 (COM rev. 12: „ball head + sleeve 12/14 taper“); indikation: „Speziell für Revisions-Eingriffe“ (q_quadra_p S. 12); hinweis: Kopf und passende Hülse (S/M/L/XL) getrennt wählen. Nur in q_quadra_p S. 12 / q_amistem_p S. 14.; fundstellen: q_quadra_p S. 12; q_amistem_p S. 14 | q_quadra_p | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio` | pfanne | Versafitcup CC Trio (mit seitlichen Schraubenlöchern) | registerbeleg: EPRD zf-Pfanne #6 (n=20.423); fixation: zementfrei; form: elliptisch, Aufweitung am Äquator; kranialer Rand 5° (S. 4, S. 6); material: None; material_hinweis: Schalenmaterial/Beschichtung im Dokument nicht genannt; pruefstand: Zuordnung Schale→Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio_nohole` | pfanne | Versafitcup CC Trio No-Hole | fixation: zementfrei; form: elliptisch, ohne seitliche Löcher (S. 4); material: None; material_hinweis: nicht genannt; pruefstand: Zuordnung Schale→Inlaygröße 2 Prüfer; Einzel-REF nur Claude-Helfer | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | inlay | Versafitcup CC Trio UHMWPE-Flach-Inlay | material: UHMWPE (Standard); form: flach; kopf_mm_je_groesse: {"AZ": ["22"], "B": ["28"], "C": ["28"], "E": ["28", "32"], "F": ["28", "32"], "G": ["28", "32"]}; com_spalte: Versafitcup CC Flat and Hooded UHMWPE; pruefstand: Kopf-Ø je Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer (OpenAI-Stichproben stimmen) | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | inlay | Versafitcup CC Trio Überhöhtes Inlay aus UHMWPE | material: UHMWPE (Standard); form: überhöht; kopf_mm_je_groesse: {"AZ": ["22"], "B": ["28"], "C": ["28"], "E": ["28", "32"], "F": ["28", "32"], "G": ["28", "32"]}; com_spalte: Versafitcup CC Flat and Hooded UHMWPE; pruefstand: Kopf-Ø je Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer (OpenAI-Stichproben stimmen) | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.inlay_hc_flach` | inlay | Versafitcup CC Trio Highcross UHMWPE-Flach-Inlay | material: Highcross UHMWPE; form: flach; kopf_mm_je_groesse: {"AZ": ["22"], "B": ["28"], "C": ["28", "32"], "E": ["28", "32", "36"], "F": ["28", "32", "36"], "G": ["28", "32", "36"]}; com_spalte: Versafitcup CC Flat and Hooded HC UHMWPE; pruefstand: Kopf-Ø je Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer (OpenAI-Stichproben stimmen) | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | inlay | Versafitcup CC Trio Highcross überhöhtes Inlay aus UHMWPE | material: Highcross UHMWPE; form: überhöht; kopf_mm_je_groesse: {"AZ": ["22"], "B": ["28"], "C": ["28"], "E": ["28", "32"], "F": ["28", "32"], "G": ["28", "32"]}; hinweis: Kein 36 mm in überhöhter Form – nicht aus der flachen Variante ableiten (OpenAI 4.2; S. 9).; com_spalte: Versafitcup CC Flat and Hooded HC UHMWPE; pruefstand: Kopf-Ø je Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer (OpenAI-Stichproben stimmen) | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.inlay_keramik` | inlay | Versafitcup CC Trio Keramik-Inlay | material: Keramik (Hersteller/Typ im Dokument nicht genannt); kopf_mm_je_groesse: {"B": ["28"], "C": ["28", "32"], "E": ["28", "32", "36"], "F": ["28", "32", "36", "40"], "G": ["28", "32", "36", "40"]}; com_spalte: Mectacer BIOLOX delta bzw. Ceramtec BIOLOX delta (Zuordnung der REF 01.29.4xx nicht angegeben); hinweis: Kein Keramik-Inlay der Größe AZ. Keramik-Inlay nur mit Keramikkopf (IFU DE S. 27). Abgeraten bei Inklination > 45° (S. 11).; pruefstand: Kopf-Ø je Inlaygröße von Claude-Helfer und OpenAI gelesen (2 Prüfer); Einzel-REF nur Claude-Helfer (OpenAI-Stichproben stimmen) | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.verschluss` | verschluss | Hüftpfanne zentraler Verschluss | hinweis: Lochverschlussschraube ist in der Pfannenverpackung enthalten (S. 8). | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.schraube_flachkopf` | schraube | Spongiosaschraube (Flachkopf) Ø 6,5 mm | durchmesser_mm: 6,5; hinweis: „Verwenden Sie immer Flachkopfschrauben (aufgeführt auf Seite 12)“ (S. 8). | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.versafitcup_cc_trio.schraube_spongiosa` | schraube | Spongiosaschraube Ø 6,5 mm (01.43.xxxx) | durchmesser_mm: 6,5; instrument: spezielle Bohrerführung 01.10.10.372 erforderlich (S. 8); hinweis: Dokument sagt auf S. 8 zugleich „Verwenden Sie immer Flachkopfschrauben (aufgeführt auf Seite 12)“ – Verhältnis zu diesen Schrauben nicht erläutert; nicht aufgelöst. | q_cctrio | belegt (Original, 1 Prüfer) |
| `medacta.duokopf.bipolar` | duokopf | Medacta Bipolar Kopf (Duokopf) (Duokopf, Bipolar Head) | registerbeleg: SIRIS 2024: Amistem-C + Medacta bipolar n=221; material: äußere Schale Edelstahl, hochglanzpoliert; innen UHMWPE-Lagerschale; interner elastischer Rückhaltering (q_bipolar S. 4); innen_mm: ["22", "28"]; femurkopf: Metall oder Keramik (S. 4); Kopfgruppen laut COM S. 2; freigabe: Schäfte im Bipolar-Dokument nicht genannt; COM rev. 12 nur Kopf × Bipolar; hinweis: „Nicht alle in den Größenangaben angegebenen Größen sind für die beiden Medacta Bipolar Head Größen Ø 22 mm und Ø 28 mm vorhanden.“ (S. 5). Konflikt: OpenAI fand auf S. 5–6 keine Außen-Ø/REF-Tabelle; Tabelle steht laut Claude-Helfer auf S. 7 (von OpenAI nicht genannt) – 2. Prüfung S. 7 offen. | q_bipolar | belegt (Original, 1 Prüfer) |
| `medacta.endokopf` | endokopf | Medacta Endo Head (unipolar) (Endokopf, Hemikopf unipolar) | material: High Nitrogen stainless steel ISO 5832-9 (PDF 2); konus: 12/14 (PDF 2; COM S. 1); aufbau: unipolar, Monobloc-Kopf, artikuliert direkt mit dem Acetabulum (PDF 2); freigabe: „designed to be assembled with all the Medacta® stems with 12/14 taper“ (PDF 2) – Herstelleraussage, keine freie Konusregel; hinweis: Implantate 40–56 mm in 2-mm-Schritten, Sizer 39–56 mm in 1-mm-Schritten (WARNING, PDF 2). Halslängen S/M/L in mm nicht genannt. Kein Innenkopf.; pruefstand: Größen 40–56 × S/M/L 2 Prüfer; Einzel-REF 42–54 nur Claude-Helfer (OpenAI: Beispiele 40 und 56) | q_endo | belegt (Original, 2 Prüfer) |

### Größen – QUADRA-H (Quelle q_quadra_de)
| groesse | ausfuehrung | ref | seite | fussnote | hals |
|---|---|---|---|---|---|
| 00SN | Standard | 01.12.98SN | 10 | II Auf Anfrage | Short Neck |
| 0SN | Standard | 01.12.20SN | 10 | – | Short Neck |
| 1SN | Standard | 01.12.21SN | 10 | – | Short Neck |
| 1SN | Lateralisiert | 01.12.31SN | 10 | – | Short Neck |
| 2SN | Standard | 01.12.22SN | 10 | – | Short Neck |
| 2SN | Lateralisiert | 01.12.32SN | 10 | – | Short Neck |
| 3SN | Standard | 01.12.23SN | 10 | – | Short Neck |
| 3SN | Lateralisiert | 01.12.33SN | 10 | – | Short Neck |
| 0 | Standard | 01.12.020 | 10 | – | regulär |
| 1 | Standard | 01.12.021 | 10 | – | regulär |
| 1 | Lateralisiert | 01.12.031 | 10 | – | regulär |
| 2 | Standard | 01.12.022 | 10 | – | regulär |
| 2 | Lateralisiert | 01.12.032 | 10 | – | regulär |
| 3 | Standard | 01.12.023 | 10 | – | regulär |
| 3 | Lateralisiert | 01.12.033 | 10 | – | regulär |
| 4 | Standard | 01.12.024 | 10 | – | regulär |
| 4 | Lateralisiert | 01.12.034 | 10 | – | regulär |
| 5 | Standard | 01.12.025 | 10 | – | regulär |
| 5 | Lateralisiert | 01.12.035 | 10 | – | regulär |
| 6 | Standard | 01.12.026 | 10 | – | regulär |
| 6 | Lateralisiert | 01.12.036 | 10 | – | regulär |
| 7 | Standard | 01.12.027 | 10 | – | regulär |
| 7 | Lateralisiert | 01.12.037 | 10 | – | regulär |
| 8 | Standard | 01.12.028 | 10 | – | regulär |
| 9 | Standard | 01.12.029 | 10 | – | regulär |
| 10 | Standard | 01.12.030 | 10 | II Auf Anfrage | regulär |

### Größen – QUADRA-C (Quelle q_quadra_de)
| groesse | ausfuehrung | ref | seite | fussnote |
|---|---|---|---|---|
| 0 | Standard | 01.12.040 | 10 | I Begrenzte Verwendung – EN: „Limited use body mass not exceeding 65 kg“ (DE: „Body-Mass-Index nicht über 65 kg“) |
| 1 | Standard | 01.12.041 | 10 | – |
| 2 | Standard | 01.12.042 | 10 | – |
| 3 | Standard | 01.12.043 | 10 | – |
| 4 | Standard | 01.12.044 | 10 | – |
| 5 | Standard | 01.12.045 | 10 | – |
| 6 | Standard | 01.12.046 | 10 | – |
| 7 | Standard | 01.12.047 | 10 | – |

### Größen – QUADRA-P (Quelle q_quadra_p)
| groesse | ausfuehrung | ref | seite | fussnote | hals |
|---|---|---|---|---|---|
| 00 | Standard | 01.12.119 | 13 | II Auf Anfrage | regulär |
| 0 | Standard | 01.12.120 | 13 | – | regulär |
| 0 | Lateralisiert | 01.12.140 | 13 | – | regulär |
| 1 | Standard | 01.12.121 | 13 | – | regulär |
| 1 | Lateralisiert | 01.12.141 | 13 | – | regulär |
| 2 | Standard | 01.12.122 | 13 | – | regulär |
| 2 | Lateralisiert | 01.12.142 | 13 | – | regulär |
| 3 | Standard | 01.12.123 | 13 | – | regulär |
| 3 | Lateralisiert | 01.12.143 | 13 | – | regulär |
| 4 | Standard | 01.12.124 | 13 | – | regulär |
| 4 | Lateralisiert | 01.12.144 | 13 | – | regulär |
| 5 | Standard | 01.12.125 | 13 | – | regulär |
| 5 | Lateralisiert | 01.12.145 | 13 | – | regulär |
| 6 | Standard | 01.12.126 | 13 | – | regulär |
| 6 | Lateralisiert | 01.12.146 | 13 | – | regulär |
| 7 | Standard | 01.12.127 | 13 | – | regulär |
| 7 | Lateralisiert | 01.12.147 | 13 | – | regulär |
| 8 | Standard | 01.12.128 | 13 | – | regulär |
| 8 | Lateralisiert | 01.12.148 | 13 | – | regulär |
| 9 | Standard | 01.12.129 | 13 | – | regulär |
| 9 | Lateralisiert | 01.12.149 | 13 | – | regulär |
| 10 | Standard | 01.12.130 | 13 | – | regulär |
| 10 | Lateralisiert | 01.12.150 | 13 | – | regulär |
| 00SN | Standard | 01.12.249 | 13 | II Auf Anfrage | Short Neck |
| 0SN | Standard | 01.12.250 | 13 | – | Short Neck |
| 0SN | Lateralisiert | 01.12.270 | 13 | – | Short Neck |
| 1SN | Standard | 01.12.251 | 13 | – | Short Neck |
| 1SN | Lateralisiert | 01.12.271 | 13 | – | Short Neck |
| 2SN | Standard | 01.12.252 | 13 | – | Short Neck |
| 2SN | Lateralisiert | 01.12.272 | 13 | – | Short Neck |
| 3SN | Standard | 01.12.253 | 13 | – | Short Neck |
| 3SN | Lateralisiert | 01.12.273 | 13 | – | Short Neck |
| 4SN | Standard | 01.12.254 | 13 | – | Short Neck |
| 4SN | Lateralisiert | 01.12.274 | 13 | – | Short Neck |
| 5SN | Standard | 01.12.255 | 13 | – | Short Neck |
| 5SN | Lateralisiert | 01.12.275 | 13 | – | Short Neck |
| 6SN | Standard | 01.12.256 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 6SN | Lateralisiert | 01.12.276 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 7SN | Standard | 01.12.257 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 7SN | Lateralisiert | 01.12.277 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 8SN | Standard | 01.12.258 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 8SN | Lateralisiert | 01.12.278 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 9SN | Standard | 01.12.259 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 9SN | Lateralisiert | 01.12.279 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 10SN | Standard | 01.12.260 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |
| 10SN | Lateralisiert | 01.12.280 | 13 | I (Fußnote bezieht sich wörtlich auf den Lieferumfang der Instrumente) | Short Neck |

### Größen – QUADRA-P Collared (Quelle q_quadra_p)
| groesse | ausfuehrung | ref | seite | fussnote |
|---|---|---|---|---|
| 00 | Standard | 01.12.159 | 13 | II Auf Anfrage |
| 0 | Standard | 01.12.160 | 13 | – |
| 0 | Lateralisiert | 01.12.180 | 13 | – |
| 1 | Standard | 01.12.161 | 13 | – |
| 1 | Lateralisiert | 01.12.181 | 13 | – |
| 2 | Standard | 01.12.162 | 13 | – |
| 2 | Lateralisiert | 01.12.182 | 13 | – |
| 3 | Standard | 01.12.163 | 13 | – |
| 3 | Lateralisiert | 01.12.183 | 13 | – |
| 4 | Standard | 01.12.164 | 13 | – |
| 4 | Lateralisiert | 01.12.184 | 13 | – |
| 5 | Standard | 01.12.165 | 13 | – |
| 5 | Lateralisiert | 01.12.185 | 13 | – |
| 6 | Standard | 01.12.166 | 13 | – |
| 6 | Lateralisiert | 01.12.186 | 13 | – |
| 7 | Standard | 01.12.167 | 13 | – |
| 7 | Lateralisiert | 01.12.187 | 13 | – |
| 8 | Standard | 01.12.168 | 13 | – |
| 8 | Lateralisiert | 01.12.188 | 13 | – |
| 9 | Standard | 01.12.169 | 13 | – |
| 9 | Lateralisiert | 01.12.189 | 13 | – |
| 10 | Standard | 01.12.170 | 13 | – |
| 10 | Lateralisiert | 01.12.190 | 13 | – |

### Größen – QUADRA-P Cemented (Quelle q_quadra_p)
| groesse | ausfuehrung | ref | seite |
|---|---|---|---|
| 0 | Standard | 01.12.210 | 13 |
| 0 | Lateralisiert | 01.12.230 | 13 |
| 1 | Standard | 01.12.211 | 13 |
| 1 | Lateralisiert | 01.12.231 | 13 |
| 2 | Standard | 01.12.212 | 13 |
| 2 | Lateralisiert | 01.12.232 | 13 |
| 3 | Standard | 01.12.213 | 13 |
| 3 | Lateralisiert | 01.12.233 | 13 |
| 4 | Standard | 01.12.214 | 13 |
| 4 | Lateralisiert | 01.12.234 | 13 |
| 5 | Standard | 01.12.215 | 13 |
| 5 | Lateralisiert | 01.12.235 | 13 |
| 6 | Standard | 01.12.216 | 13 |
| 6 | Lateralisiert | 01.12.236 | 13 |
| 7 | Standard | 01.12.217 | 13 |
| 7 | Lateralisiert | 01.12.237 | 13 |
| 8 | Standard | 01.12.218 | 13 |
| 8 | Lateralisiert | 01.12.238 | 13 |

### Größen – AMIStem-P (Quelle q_amistem_p)
| groesse | ausfuehrung | ref | seite | fussnote | hals |
|---|---|---|---|---|---|
| 00 | Standard | 01.18.399 | 15 | I Auf Anfrage | Regular Neck |
| 0 | Standard | 01.18.400 | 15 | – | Regular Neck |
| 0 | Lateralisiert | 01.18.410 | 15 | – | Regular Neck |
| 1 | Standard | 01.18.401 | 15 | – | Regular Neck |
| 1 | Lateralisiert | 01.18.411 | 15 | – | Regular Neck |
| 2 | Standard | 01.18.402 | 15 | – | Regular Neck |
| 2 | Lateralisiert | 01.18.412 | 15 | – | Regular Neck |
| 3 | Standard | 01.18.403 | 15 | – | Regular Neck |
| 3 | Lateralisiert | 01.18.413 | 15 | – | Regular Neck |
| 4 | Standard | 01.18.404 | 15 | – | Regular Neck |
| 4 | Lateralisiert | 01.18.414 | 15 | – | Regular Neck |
| 5 | Standard | 01.18.405 | 15 | – | Regular Neck |
| 5 | Lateralisiert | 01.18.415 | 15 | – | Regular Neck |
| 6 | Standard | 01.18.406 | 15 | – | Regular Neck |
| 6 | Lateralisiert | 01.18.416 | 15 | – | Regular Neck |
| 7 | Standard | 01.18.407 | 15 | – | Regular Neck |
| 7 | Lateralisiert | 01.18.417 | 15 | – | Regular Neck |
| 8 | Standard | 01.18.408 | 15 | – | Regular Neck |
| 8 | Lateralisiert | 01.18.418 | 15 | – | Regular Neck |
| 9 | Standard | 01.18.409 | 15 | – | Regular Neck |
| 00SN | Standard | 01.18.459 | 15 | II Kombinierbar ausschließlich mit den Köpfen der Größen S, M und L. | Short Neck |
| 0SN | Standard | 01.18.460 | 15 | – | Short Neck |
| 0SN | Lateralisiert | 01.18.470 | 15 | – | Short Neck |
| 1SN | Standard | 01.18.461 | 15 | – | Short Neck |
| 1SN | Lateralisiert | 01.18.471 | 15 | – | Short Neck |
| 2SN | Standard | 01.18.462 | 15 | – | Short Neck |
| 2SN | Lateralisiert | 01.18.472 | 15 | – | Short Neck |
| 3SN | Standard | 01.18.463 | 15 | – | Short Neck |
| 3SN | Lateralisiert | 01.18.473 | 15 | – | Short Neck |
| 4SN | Standard | 01.18.464 | 15 | – | Short Neck |
| 4SN | Lateralisiert | 01.18.474 | 15 | – | Short Neck |
| 5SN | Standard | 01.18.465 | 15 | – | Short Neck |
| 5SN | Lateralisiert | 01.18.475 | 15 | – | Short Neck |
| 6SN | Standard | 01.18.466 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 6SN | Lateralisiert | 01.18.476 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 7SN | Standard | 01.18.467 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 7SN | Lateralisiert | 01.18.477 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 8SN | Standard | 01.18.468 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 8SN | Lateralisiert | 01.18.478 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |
| 9SN | Standard | 01.18.469 | 15 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck |

### Größen – AMIStem-P Collared (Quelle q_amistem_p)
| groesse | ausfuehrung | ref | seite | fussnote |
|---|---|---|---|---|
| 00 | Standard | 01.18.429 | 15 | I Auf Anfrage |
| 0 | Standard | 01.18.430 | 15 | – |
| 0 | Lateralisiert | 01.18.440 | 15 | – |
| 1 | Standard | 01.18.431 | 15 | – |
| 1 | Lateralisiert | 01.18.441 | 15 | – |
| 2 | Standard | 01.18.432 | 15 | – |
| 2 | Lateralisiert | 01.18.442 | 15 | – |
| 3 | Standard | 01.18.433 | 15 | – |
| 3 | Lateralisiert | 01.18.443 | 15 | – |
| 4 | Standard | 01.18.434 | 15 | – |
| 4 | Lateralisiert | 01.18.444 | 15 | – |
| 5 | Standard | 01.18.435 | 15 | – |
| 5 | Lateralisiert | 01.18.445 | 15 | – |
| 6 | Standard | 01.18.436 | 15 | – |
| 6 | Lateralisiert | 01.18.446 | 15 | – |
| 7 | Standard | 01.18.437 | 15 | – |
| 7 | Lateralisiert | 01.18.447 | 15 | – |
| 8 | Standard | 01.18.438 | 15 | – |
| 8 | Lateralisiert | 01.18.448 | 15 | – |
| 9 | Standard | 01.18.439 | 15 | – |

### Größen – AMIStem-C (Quelle q_amistem_p)
| groesse | ausfuehrung | ref | seite | fussnote | hals | en_2014 | hinweis |
|---|---|---|---|---|---|---|---|
| 00 | Standard | 01.18.149 | 16 | II Kombinierbar ausschließlich mit den Köpfen der Größen S, M und L. | Regular Neck | nicht gelistet (Zeile „-“) | – |
| 0 | Standard | 01.18.150 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 0 | Lateralisiert | 01.18.100 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 1 | Standard | 01.18.151 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 1 | Lateralisiert | 01.18.101 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 2 | Standard | 01.18.152 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 2 | Lateralisiert | 01.18.102 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 3 | Standard | 01.18.153 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 3 | Lateralisiert | 01.18.103 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 4 | Standard | 01.18.154 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 4 | Lateralisiert | 01.18.104 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 5 | Standard | 01.18.155 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 5 | Lateralisiert | 01.18.105 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 6 | Standard | 01.18.156 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 6 | Lateralisiert | 01.18.106 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 7 | Standard | 01.18.157 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 7 | Lateralisiert | 01.18.107 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 8 | Standard | 01.18.158 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 8 | Lateralisiert | 01.18.108 | 16 | – | Regular Neck | gelistet (S. 12) | – |
| 00SN | Standard | 01.18.699 | 16 | II Kombinierbar ausschließlich mit den Köpfen der Größen S, M und L. | Short Neck | keine Short-Neck-Variante | – |
| 0SN | Standard | 01.18.700 | 16 | II Kombinierbar ausschließlich mit den Köpfen der Größen S, M und L. | Short Neck | keine Short-Neck-Variante | – |
| 0SN | Lateralisiert | 01.18.710 | 16 | – | Short Neck | keine Short-Neck-Variante | Marker II steht in der Größenspalte der Zeile 0SN; OpenAI ordnet die S/M/L-Grenze nur STD 0SN zu. Ob sie auch für LAT 0SN (01.18.710) gilt: offen – vorsorglich nur S/M/L, Medacta fragen. |
| 1SN | Standard | 01.18.701 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 1SN | Lateralisiert | 01.18.711 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 2SN | Standard | 01.18.702 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 2SN | Lateralisiert | 01.18.712 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 3SN | Standard | 01.18.703 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 3SN | Lateralisiert | 01.18.713 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 4SN | Standard | 01.18.704 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 4SN | Lateralisiert | 01.18.714 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 5SN | Standard | 01.18.705 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 5SN | Lateralisiert | 01.18.715 | 16 | – | Short Neck | keine Short-Neck-Variante | – |
| 6SN | Standard | 01.18.706 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |
| 6SN | Lateralisiert | 01.18.716 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |
| 7SN | Standard | 01.18.707 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |
| 7SN | Lateralisiert | 01.18.717 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |
| 8SN | Standard | 01.18.708 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |
| 8SN | Lateralisiert | 01.18.718 | 16 | III Erhältlich nur auf besondere Nachfrage mit Bestätigung. | Short Neck | keine Short-Neck-Variante | – |

### Größen – Femurkopf Edelstahl (nichtrostender Stahl) (Quelle q_quadra_p)
| durchmesser_mm | groesse | ref | fussnote |
|---|---|---|---|
| 22 | S | 01.25.130 | Auf Anfrage (alle Kopftabellen) |
| 22 | M | 25055.2203 | Auf Anfrage (alle Kopftabellen) |
| 28 | S | 25055.2801 | – |
| 28 | M | 25055.2803 | – |
| 28 | L | 25055.2805 | – |
| 28 | XL | 25055.2807 | – |
| 28 | XXL | 25055.2810 | Auf Anfrage (alle Kopftabellen) |
| 32 | S | 25055.3201 | – |
| 32 | M | 25055.3203 | – |
| 32 | L | 25055.3205 | – |
| 32 | XL | 25055.3207 | – |
| 32 | XXL | 25055.3210 | Auf Anfrage (alle Kopftabellen) |

### Größen – Femurkopf CoCr (Quelle q_quadra_p)
| durchmesser_mm | groesse | ref | fussnote |
|---|---|---|---|
| 22 | S | 01.25.124 | Auf Anfrage (alle Kopftabellen) |
| 22 | M | 01.25.123 | Auf Anfrage (alle Kopftabellen) |
| 28 | S | 01.25.011 | – |
| 28 | M | 01.25.012 | – |
| 28 | L | 01.25.013 | – |
| 28 | XL | 01.25.014 | – |
| 28 | XXL | 01.25.015 | Auf Anfrage (alle Kopftabellen) |
| 32 | S | 01.25.021 | – |
| 32 | M | 01.25.022 | – |
| 32 | L | 01.25.023 | – |
| 32 | XL | 01.25.024 | – |
| 32 | XXL | 01.25.025 | Auf Anfrage (alle Kopftabellen) |
| 36 | S | 01.25.030 | – |
| 36 | M | 01.25.031 | – |
| 36 | L | 01.25.032 | – |
| 36 | XL | 01.25.033 | – |
| 36 | XXL | 01.25.034 | Auf Anfrage (alle Kopftabellen) |

### Größen – CeramTec BIOLOX delta (Quelle q_quadra_p)
| durchmesser_mm | groesse | ref | fussnote |
|---|---|---|---|
| 28 | S | 38.49.7175.445.00 | – |
| 28 | M | 38.49.7175.455.00 | – |
| 28 | L | 38.49.7175.465.00 | – |
| 32 | S | 38.49.7175.665.00 | – |
| 32 | M | 38.49.7175.675.00 | – |
| 32 | L | 38.49.7175.685.00 | – |
| 32 | XL | 38.49.7181.345.00 | – |
| 36 | S | 38.49.7179.275.00 | – |
| 36 | M | 38.49.7179.285.00 | – |
| 36 | L | 38.49.7179.295.00 | – |
| 36 | XL | 38.49.7175.925.00 | – |
| 40 | S | 38.49.7179.885.00 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | M | 38.49.7179.895.00 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | L | 38.49.7179.905.00 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | XL | 38.49.7179.915.00 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |

### Größen – CeramTec BIOLOX Option (Quelle q_quadra_p)
| durchmesser_mm | groesse | ref | fussnote |
|---|---|---|---|
| 28 | S | 38.49.7176.935.81 | – |
| 28 | M | 38.49.7176.935.82 | – |
| 28 | L | 38.49.7176.935.85 | – |
| 28 | XL | 38.49.7176.935.84 | – |
| 32 | S | 38.49.7176.945.81 | – |
| 32 | M | 38.49.7176.945.82 | – |
| 32 | L | 38.49.7176.945.85 | – |
| 32 | XL | 38.49.7176.945.84 | – |
| 36 | S | 38.49.7176.965.81 | – |
| 36 | M | 38.49.7176.965.82 | – |
| 36 | L | 38.49.7176.965.85 | – |
| 36 | XL | 38.49.7176.965.84 | – |
| 40 | S | 38.49.7179.815.81 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | M | 38.49.7179.815.82 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | L | 38.49.7179.815.85 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |
| 40 | XL | 38.49.7179.815.84 | Auf Anfrage nur in q_quadra_p S. 12 / q_amistem_p S. 14 (2021/2022); in q_quadra_de 2016 und q_amistem_en 2014 ohne Marker |

### Größen – Mectacer BIOLOX delta (Quelle q_quadra_p)
| durchmesser_mm | groesse | ref |
|---|---|---|
| 28 | S | 01.29.201 |
| 28 | M | 01.29.202 |
| 28 | L | 01.29.203 |
| 32 | S | 01.29.204 |
| 32 | M | 01.29.205 |
| 32 | L | 01.29.206 |
| 32 | XL | 01.29.207 |
| 36 | S | 01.29.208 |
| 36 | M | 01.29.209 |
| 36 | L | 01.29.210 |
| 36 | XL | 01.29.211 |
| 40 | S | 01.29.212 |
| 40 | M | 01.29.213 |
| 40 | L | 01.29.214 |
| 40 | XL | 01.29.215 |

### Größen – Mectacer BIOLOX Option System (Kopf + Hülse) (Quelle q_quadra_p)
| teil | durchmesser_mm | ref | groesse |
|---|---|---|---|
| Kopf | 28 | 01.29.230H | – |
| Kopf | 32 | 01.29.231H | – |
| Kopf | 36 | 01.29.232H | – |
| Kopf | 40 | 01.29.233H | – |
| Hülse (Manschette) | – | 01.29.240A | S |
| Hülse (Manschette) | – | 01.29.241A | M |
| Hülse (Manschette) | – | 01.29.242A | L |
| Hülse (Manschette) | – | 01.29.243A | XL |

### Größen – Versafitcup CC Trio (mit seitlichen Schraubenlöchern) (Quelle q_cctrio)
| durchmesser_mm | ref | inlay_groesse | seite | fussnote |
|---|---|---|---|---|
| 40 | 01.26.45.0040 | AZ | 12 | Auf Anfrage |
| 42 | 01.26.45.0042 | AZ | 12 | Auf Anfrage |
| 44 | 01.26.45.0044 | B | 12 | Auf Anfrage |
| 46 | 01.26.45.0046 | C | 12 | – |
| 48 | 01.26.45.0048 | C | 12 | – |
| 50 | 01.26.45.0050 | E | 12 | – |
| 52 | 01.26.45.0052 | E | 12 | – |
| 54 | 01.26.45.0054 | E | 12 | – |
| 56 | 01.26.45.0056 | F | 12 | – |
| 58 | 01.26.45.0058 | F | 12 | – |
| 60 | 01.26.45.0060 | F | 12 | – |
| 62 | 01.26.45.0062 | G | 12 | – |
| 64 | 01.26.45.0064 | G | 12 | – |

### Größen – Versafitcup CC Trio No-Hole (Quelle q_cctrio)
| durchmesser_mm | ref | inlay_groesse | seite | fussnote |
|---|---|---|---|---|
| 44 | 01.26.45.1144 | B | 12 | Auf Anfrage |
| 46 | 01.26.45.1146 | C | 12 | – |
| 48 | 01.26.45.1148 | C | 12 | – |
| 50 | 01.26.45.1150 | E | 12 | – |
| 52 | 01.26.45.1152 | E | 12 | – |
| 54 | 01.26.45.1154 | E | 12 | – |
| 56 | 01.26.45.1156 | F | 12 | – |
| 58 | 01.26.45.1158 | F | 12 | – |
| 60 | 01.26.45.1160 | F | 12 | – |
| 62 | 01.26.45.1162 | G | 12 | – |
| 64 | 01.26.45.1164 | G | 12 | – |

### Größen – Versafitcup CC Trio UHMWPE-Flach-Inlay (Quelle q_cctrio)
| inlay_groesse | kopf_mm | ref | seite | fussnote |
|---|---|---|---|---|
| AZ | 22 | 01.26.2233STT | 13 | Auf Anfrage |
| B | 28 | 01.26.2837STT | 13 | Auf Anfrage |
| C | 28 | 01.26.2839STT | 13 | – |
| E | 28 | 01.26.2844STT | 13 | – |
| E | 32 | 01.26.3244STT | 13 | – |
| F | 28 | 01.26.2848STT | 13 | – |
| F | 32 | 01.26.3248STT | 13 | – |
| G | 28 | 01.26.2852STT | 13 | – |
| G | 32 | 01.26.3252STT | 13 | – |

### Größen – Versafitcup CC Trio Überhöhtes Inlay aus UHMWPE (Quelle q_cctrio)
| inlay_groesse | kopf_mm | ref | seite | fussnote |
|---|---|---|---|---|
| AZ | 22 | 01.26.2233AT | 13 | Auf Anfrage |
| B | 28 | 01.26.2837AT | 13 | Auf Anfrage |
| C | 28 | 01.26.2839AT | 13 | – |
| E | 28 | 01.26.2844AT | 13 | – |
| E | 32 | 01.26.3244AT | 13 | – |
| F | 28 | 01.26.2848AT | 13 | – |
| F | 32 | 01.26.3248AT | 13 | – |
| G | 28 | 01.26.2852AT | 13 | – |
| G | 32 | 01.26.3252AT | 13 | – |

### Größen – Versafitcup CC Trio Highcross UHMWPE-Flach-Inlay (Quelle q_cctrio)
| inlay_groesse | kopf_mm | ref | seite | fussnote |
|---|---|---|---|---|
| AZ | 22 | 01.26.2233HCT | 13 | Auf Anfrage |
| B | 28 | 01.26.2837HCT | 13 | Auf Anfrage |
| C | 28 | 01.26.2839HCT | 13 | – |
| C | 32 | 01.26.3239HCT | 13 | – |
| E | 28 | 01.26.2844HCT | 13 | – |
| E | 32 | 01.26.3244HCT | 13 | – |
| E | 36 | 01.26.3644HCT | 13 | – |
| F | 28 | 01.26.2848HCT | 13 | – |
| F | 32 | 01.26.3248HCT | 13 | – |
| F | 36 | 01.26.3648HCT | 13 | – |
| G | 28 | 01.26.2852HCT | 13 | – |
| G | 32 | 01.26.3252HCT | 13 | – |
| G | 36 | 01.26.3652HCT | 13 | – |

### Größen – Versafitcup CC Trio Highcross überhöhtes Inlay aus UHMWPE (Quelle q_cctrio)
| inlay_groesse | kopf_mm | ref | seite | fussnote |
|---|---|---|---|---|
| AZ | 22 | 01.26.2233HCAT | 13 | Auf Anfrage |
| B | 28 | 01.26.2837HCAT | 13 | Auf Anfrage |
| C | 28 | 01.26.2839HCAT | 13 | – |
| E | 28 | 01.26.2844HCAT | 13 | – |
| E | 32 | 01.26.3244HCAT | 13 | – |
| F | 28 | 01.26.2848HCAT | 13 | – |
| F | 32 | 01.26.3248HCAT | 13 | – |
| G | 28 | 01.26.2852HCAT | 13 | – |
| G | 32 | 01.26.3252HCAT | 13 | – |

### Größen – Versafitcup CC Trio Keramik-Inlay (Quelle q_cctrio)
| inlay_groesse | kopf_mm | ref | seite | fussnote |
|---|---|---|---|---|
| B | 28 | 01.29.402 | 13 | Auf Anfrage |
| C | 28 | 01.29.403 | 13 | – |
| C | 32 | 01.29.408 | 13 | – |
| E | 28 | 01.29.405 | 13 | – |
| E | 32 | 01.29.410 | 13 | – |
| E | 36 | 01.29.413 | 13 | – |
| F | 28 | 01.29.406 | 13 | – |
| F | 32 | 01.29.411 | 13 | – |
| F | 36 | 01.29.414 | 13 | – |
| F | 40 | 01.29.416 | 13 | – |
| G | 28 | 01.29.407 | 13 | – |
| G | 32 | 01.29.412 | 13 | – |
| G | 36 | 01.29.415 | 13 | – |
| G | 40 | 01.29.417 | 13 | – |

### Größen – Hüftpfanne zentraler Verschluss (Quelle q_cctrio)
| ref | seite |
|---|---|
| 01.26.45.0070 | 12 |

### Größen – Spongiosaschraube (Flachkopf) Ø 6,5 mm (Quelle q_cctrio)
| laenge_mm | ref | seite |
|---|---|---|
| 20 | 01.26.65.20 | 12 |
| 25 | 01.26.65.25 | 12 |
| 30 | 01.26.65.30 | 12 |
| 35 | 01.26.65.35 | 12 |
| 40 | 01.26.65.40 | 12 |
| 45 | 01.26.65.45 | 12 |

### Größen – Spongiosaschraube Ø 6,5 mm (01.43.xxxx) (Quelle q_cctrio)
| laenge_mm | ref | seite | fussnote |
|---|---|---|---|
| 15 | 01.43.0015 | 12 | – |
| 20 | 01.43.0020 | 12 | – |
| 25 | 01.43.0025 | 12 | – |
| 30 | 01.43.0030 | 12 | – |
| 35 | 01.43.0035 | 12 | – |
| 40 | 01.43.0040 | 12 | – |
| 45 | 01.43.0045 | 12 | – |
| 50 | 01.43.0050 | 12 | Verfügbarkeit nur auf genehmigte Sonderanfrage |
| 55 | 01.43.0055 | 12 | Verfügbarkeit nur auf genehmigte Sonderanfrage |
| 60 | 01.43.0060 | 12 | Verfügbarkeit nur auf genehmigte Sonderanfrage |
| 65 | 01.43.0065 | 12 | Verfügbarkeit nur auf genehmigte Sonderanfrage |
| 70 | 01.43.0070 | 12 | Verfügbarkeit nur auf genehmigte Sonderanfrage |

### Größen – Medacta Bipolar Kopf (Duokopf) (Quelle q_bipolar)
| innen_mm | aussen_mm | ref | seite | fussnote |
|---|---|---|---|---|
| 28 | 42 | 25060.2842 | 7 | – |
| 28 | 43 | 25060.2843 | 7 | – |
| 28 | 44 | 25060.2844 | 7 | – |
| 28 | 45 | 25060.2845 | 7 | – |
| 28 | 46 | 25060.2846 | 7 | – |
| 28 | 47 | 25060.2847 | 7 | – |
| 28 | 48 | 25060.2848 | 7 | – |
| 28 | 49 | 25060.2849 | 7 | – |
| 28 | 50 | 25060.2850 | 7 | – |
| 28 | 51 | 25060.2851 | 7 | – |
| 28 | 52 | 25060.2852 | 7 | – |
| 28 | 53 | 25060.2853 | 7 | – |
| 28 | 54 | 25060.2854 | 7 | – |
| 28 | 55 | 25060.2855 | 7 | – |
| 28 | 56 | 25060.2856 | 7 | – |
| 28 | 57 | 25060.2857 | 7 | – |
| 28 | 58 | 25060.2858 | 7 | – |
| 28 | 59 | 25060.2859 | 7 | – |
| 28 | 60 | 25060.2860 | 7 | – |
| 22 | 39 | 25060.2239 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 40 | 25060.2240 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 41 | 25060.2241 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 42 | 25060.2242 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 43 | 25060.2243 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 44 | 25060.2244 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 45 | 25060.2245 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 46 | 25060.2246 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 47 | 25060.2247 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 48 | 25060.2248 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 49 | 25060.2249 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 50 | 25060.2250 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 51 | 25060.2251 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |
| 22 | 52 | 25060.2252 | 7 | III Bipolare Köpfe für Femurköpfe Ø 22 mm sind auf spezifische Anfrage hin verfügbar. |

### Größen – Medacta Endo Head (unipolar) (Quelle q_endo)
| aussen_mm | groesse | ref | seite |
|---|---|---|---|
| 40 | S | 01.25.140S | PDF 1 |
| 40 | M | 01.25.140M | PDF 1 |
| 40 | L | 01.25.140L | PDF 1 |
| 42 | S | 01.25.142S | PDF 1 |
| 42 | M | 01.25.142M | PDF 1 |
| 42 | L | 01.25.142L | PDF 1 |
| 44 | S | 01.25.144S | PDF 1 |
| 44 | M | 01.25.144M | PDF 1 |
| 44 | L | 01.25.144L | PDF 1 |
| 46 | S | 01.25.146S | PDF 1 |
| 46 | M | 01.25.146M | PDF 1 |
| 46 | L | 01.25.146L | PDF 1 |
| 48 | S | 01.25.148S | PDF 1 |
| 48 | M | 01.25.148M | PDF 1 |
| 48 | L | 01.25.148L | PDF 1 |
| 50 | S | 01.25.150S | PDF 1 |
| 50 | M | 01.25.150M | PDF 1 |
| 50 | L | 01.25.150L | PDF 1 |
| 52 | S | 01.25.152S | PDF 1 |
| 52 | M | 01.25.152M | PDF 1 |
| 52 | L | 01.25.152L | PDF 1 |
| 54 | S | 01.25.154S | PDF 1 |
| 54 | M | 01.25.154M | PDF 1 |
| 54 | L | 01.25.154L | PDF 1 |
| 56 | S | 01.25.156S | PDF 1 |
| 56 | M | 01.25.156M | PDF 1 |
| 56 | L | 01.25.156L | PDF 1 |

### T1_com_kopf_schaft – 99.99.COM rev. 12 – Heads × Stems (Quelle q_com, S. 1)
| Kopf | AMIS-K | AMIStem C | AMIStem H | AMIStem H Collared | AMIStem H Proximal Coating | MasterLoc | MiniMAX | M-Vizion Femoral Revision System | Native (10/12) | Quadra-C | Quadra-H | Quadra-S | Quadra-R | X-Acta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stainless Steel (10/12 taper) | nein | nein | nein | nein | nein | nein | nein | nein | ja | nein | nein | nein | nein | nein |
| Stainless Steel (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| CoCr (10/12 taper) | nein | nein | nein | nein | nein | nein | nein | nein | ja | nein | nein | nein | nein | nein |
| CoCr (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| Mectacer BIOLOX delta (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| Mectacer BIOLOX OPTION (ball head + sleeve 12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| Ceramtec BIOLOX delta (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| Ceramtec BIOLOX OPTION (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
| Endo Head (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | ja | ja | ja | ja |
_ja = ✓ (Textschicht „P“) „Combination approved by Medacta International“; nein = × (Textschicht „O“) „Combination NOT approved by Medacta International“. Funktionale Kompatibilität, nicht automatisch Zulassungsstatus. Quadra-P, Quadra-P Collared/Cemented, AMIStem-P, AMIStem-P Collared sind in rev. 12 NICHT aufgeführt → offen._

### T2_com_kopf_liner – 99.99.COM rev. 12 – Heads × Liners / UHMWPE Cups / Bipolar / Converter (Quelle q_com, S. 2)
| Kopf | (1) DM UHMWPE | (2) DM HC UHMWPE | (3) CC Flat/Hooded UHMWPE | (4) CC Flat/Hooded HC UHMWPE | (5) Mectacer BIOLOX delta Liner | (6) Ceramtec BIOLOX delta Liner | (7) Mpact Flat/Hooded HC UHMWPE | (8) Apricot Cemented HC flat cup | (9) Native Cemented HC Cup | (10) Medacta Bipolar Head | (11) DM Converter Liner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Stainless Steel (10/12 taper) | ja | ja | ja | ja | nein | nein | ja | ja | ja | ja | nein |
| Stainless Steel (12/14 taper) | ja | ja | ja | ja | nein | nein | ja | ja | ja | ja | nein |
| CoCr (10/12 taper) | ja | ja | ja | ja | nein | nein | ja | ja | ja | ja | nein |
| CoCr (12/14 taper) | ja | ja | ja | ja | nein | nein | ja | ja | ja | ja | nein |
| Mectacer BIOLOX delta (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | nein |
| Mectacer BIOLOX OPTION (ball head + sleeve 12/14 taper) | ja (iii) | ja (iii) | ja | ja | ja | ja | ja | ja | nein | ja | nein |
| Ceramtec BIOLOX delta (12/14 taper) | ja | ja | ja | ja | ja | ja | ja | ja | nein | ja | nein |
| Ceramtec BIOLOX OPTION (12/14 taper) | ja (iii) | ja (iii) | ja | ja | ja | ja | ja | ja | nein | ja | nein |
| Endo Head (12/14 taper) | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein |
_ja = ✓ (Textschicht „P“) „Combination approved by Medacta International“; nein = × (Textschicht „O“) „Combination NOT approved by Medacta International“. Funktionale Kompatibilität, nicht automatisch Zulassungsstatus. Quadra-P, Quadra-P Collared/Cemented, AMIStem-P, AMIStem-P Collared sind in rev. 12 NICHT aufgeführt → offen. iii: „The internal sleeve of BIOLOX OPTION of ø28 mm, size XL, and sometimes size L, do not completely cover the femoral stem threaded taper. This may cause a premature wear of the double mobility liner. We recommend to follow the combinations indicated in the table below ‚Double Mobility Liners - BIOLOX OPTION Combinations‘.“_

### T3_com_dm_option – 99.99.COM rev. 12 – Double Mobility Liners – BIOLOX OPTION Combinations (Schäfte 12/14) (Quelle q_com, S. 2)
| Kopf | AMIS-K | AMIStem C | AMIStem H | AMIStem H Collared | AMIStem H PC | MasterLoc | MiniMAX | M-Vizion | Quadra-C | Quadra-H | Quadra-S | Quadra-R | X-Acta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ceramtec BIOLOX OPTION S Ø 28 mm | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja |
| Ceramtec BIOLOX OPTION M Ø 28 mm | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja |
| Ceramtec BIOLOX OPTION L Ø 28 mm | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | nein |
| Ceramtec BIOLOX OPTION XL Ø 28 mm | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein |
| Mectacer BIOLOX OPTION Ø 28 + sleeve S | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja |
| Mectacer BIOLOX OPTION Ø 28 + sleeve M | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja |
| Mectacer BIOLOX OPTION Ø 28 + sleeve L | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | ja | nein |
| Mectacer BIOLOX OPTION Ø 28 + sleeve XL | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein | nein |
_ja = ✓ (Textschicht „P“) „Combination approved by Medacta International“; nein = × (Textschicht „O“) „Combination NOT approved by Medacta International“. Funktionale Kompatibilität, nicht automatisch Zulassungsstatus. Quadra-P, Quadra-P Collared/Cemented, AMIStem-P, AMIStem-P Collared sind in rev. 12 NICHT aufgeführt → offen. Gilt nur für Double-Mobility-Liner (nicht Teil dieser Datei)._

### T4_com_schale_liner – 99.99.COM rev. 12 – Acetabular Shells × Liners (Quelle q_com, S. 3)
| Schale | (1) DM UHMWPE | (2) DM HC UHMWPE | (3) CC Flat/Hooded UHMWPE | (4) CC Flat/Hooded HC UHMWPE | (5) Mectacer BIOLOX delta Liner | (6) Ceramtec BIOLOX delta Liner | (7) Mpact Flat/Hooded HC UHMWPE | (8) DM Converter Liner |
|---|---|---|---|---|---|---|---|---|
| Mpact No-hole | nein | nein | nein | nein | ja | ja | ja | ja |
| Mpact Two-hole | nein | nein | nein | nein | ja | ja | ja | ja |
| Mpact DM | ja | ja | nein | nein | nein | nein | nein | nein |
| Mpact Multi-hole | nein | nein | nein | nein | nein | nein | ja | ja |
| Mpact Rim-hole | nein | nein | nein | nein | ja (iiii) | ja | ja | ja |
| Versacem | ja | ja | nein | nein | nein | nein | nein | nein |
| Versafitcup CC Trio | nein | nein | ja | ja | ja | ja | nein | nein |
| Versafitcup CC Trio No-Hole | nein | nein | ja | ja | ja | ja | nein | nein |
| Versafitcup DM | ja | ja | nein | nein | nein | nein | nein | nein |
_ja = ✓ (Textschicht „P“) „Combination approved by Medacta International“; nein = × (Textschicht „O“) „Combination NOT approved by Medacta International“. Funktionale Kompatibilität, nicht automatisch Zulassungsstatus. Quadra-P, Quadra-P Collared/Cemented, AMIStem-P, AMIStem-P Collared sind in rev. 12 NICHT aufgeführt → offen. iiii: „only for Mpact Rim-hole acetabular shell from Ø56 to Ø70mm“. Seite 3 ist Liner × Schale, keine Schaft-Matrix._

### T5_cctrio_schale_inlay – Versafitcup CC Trio / No-Hole – Schale → Größe des Inlays (Quelle q_cctrio, S. 12)
| inlay_groesse | schale_mm_cc_trio | schale_mm_nohole |
|---|---|---|
| AZ | 40, 42 | - |
| B | 44 | 44 |
| C | 46, 48 | 46, 48 |
| E | 50, 52, 54 | 50, 52, 54 |
| F | 56, 58, 60 | 56, 58, 60 |
| G | 62, 64 | 62, 64 |
_40, 42, 44 (CC Trio) und 44 (No-Hole) auf Anfrage. Kein Code D. No-Hole beginnt bei 44/B._

### T6_cctrio_inlay_kopf – Versafitcup CC Trio – Kopf-Ø je Inlaygröße und Inlaytyp (Quelle q_cctrio, S. 13)
| inlay_groesse | UHMWPE flach | UHMWPE überhöht | Highcross flach | Highcross überhöht | Keramik |
|---|---|---|---|---|---|
| AZ | 22 | 22 | 22 | 22 | - |
| B | 28 | 28 | 28 | 28 | 28 |
| C | 28 | 28 | 28, 32 | 28 | 28, 32 |
| E | 28, 32 | 28, 32 | 28, 32, 36 | 28, 32 | 28, 32, 36 |
| F | 28, 32 | 28, 32 | 28, 32, 36 | 28, 32 | 28, 32, 36, 40 |
| G | 28, 32 | 28, 32 | 28, 32, 36 | 28, 32 | 28, 32, 36, 40 |
_Konkrete Kopfbohrungen in mm, kein Bereich – keine Regel „kopf ≤ max“. Leer = kein Artikel („-“). 36 mm nur Keramik und Highcross flach (S. 9). Gleicher Code UND passende Bohrung UND freigegebene Materialpaarung erforderlich (OpenAI 4.2)._

### T7_raspel_quadra_c – Quadra-C – Raspel → Schaft zementiert (Quelle q_quadra_de, S. 9)
| raspel | technik_1 | technik_2 |
|---|---|---|
| 0 | - | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 5 | 4 | 5 |
| 6 | 5 | 6 |
| 7 | 6 | 7 |
| 8 | 7 | - |
_Technik 1: femorale Öffnung 1.4 mm größer als Prothese; Technik 2: line-to-line (S. 8). „Verwenden Sie nicht die Größen 9 und 10; es sind keine Schäfte der entsprechenden Größen lieferbar.“_

### T8_raspel_quadra_p_cemented – QUADRA-P Cemented – Raspel → Schaft zementiert (Quelle q_quadra_p, S. 11)
| raspel | technik_1 | technik_2 |
|---|---|---|
| 00 | - | - |
| 0 | - | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 5 | 4 | 5 |
| 6 | 5 | 6 |
| 7 | 6 | 7 |
| 8 | 7 | 8 |
| 9 | 8 | - |
_Schaft 9 erforderlich → Technik 1, Schaft 8. Femur auf 0 finalisiert → nur Technik 2 (kein zementierter 00) (S. 11)._

### T9_raspel_amistem_c_2022 – AMIStem-C – Raspel → Schaft zementiert (DE 2022) (Quelle q_amistem_p, S. 12)
| raspel | technik_1 | technik_2 |
|---|---|---|
| 00 | - | 00 |
| 0 | 00 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 5 | 4 | 5 |
| 6 | 5 | 6 |
| 7 | 6 | 7 |
| 8 | 7 | 8 |
| 9 | 8 | - |
_S. 13: „Die Größe 9 ist nicht erhältlich, daher ist nach Tech. 1 vorzugehen, wenn eine Raspel der Größe verwendet wurde.“ (Zahl fehlt im Original)._

### T10_raspel_amistem_c_2014 – AMIStem-C – Broach → Stem cemented (EN 2014, ältere Fassung) (Quelle q_amistem_en, S. 11)
| raspel | technik_1 | technik_2 |
|---|---|---|
| 0 | - | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 4 |
| 5 | 4 | 5 |
| 6 | 5 | 6 |
| 7 | 6 | 7 |
| 8 | 7 | 8 |
| 9 | 8 | - |
_Abweichung zu T9 (2022): keine Raspel/Schaft 00; Raspel 0 → Tech 1 „-“. Nicht aufgelöst._

## Kombinationen (passt_zu)
| Von | Zu | Status | Bedingung | Quelle | Seite |
|---|---|---|---|---|---|
| `medacta.quadra_h` | `medacta.kopf.edelstahl` | **bedingt** | Nur Ausführung „Stainless Steel (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. | q_com | 1 |
| `medacta.quadra_h` | `medacta.kopf.cocr` | **bedingt** | Nur Ausführung „CoCr (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. | q_com | 1 |
| `medacta.quadra_h` | `medacta.kopf.ceramtec_biolox_delta` | **ja** | COM-Zelle ✓ für Quadra-H (12/14). | q_com | 1 |
| `medacta.quadra_h` | `medacta.kopf.ceramtec_biolox_option` | **ja** | COM-Zelle ✓ für Quadra-H (12/14). OPTION: Revision. | q_com | 1 |
| `medacta.quadra_h` | `medacta.kopf.mectacer_biolox_delta` | **ja** | COM-Zelle ✓ für Quadra-H (12/14). | q_com | 1 |
| `medacta.quadra_h` | `medacta.kopf.mectacer_biolox_option` | **ja** | COM-Zelle ✓ für Quadra-H (12/14). OPTION: Revision. | q_com | 1 |
| `medacta.quadra_h` | `medacta.endokopf` | **ja** | COM „Endo Head (12/14 taper)“ ✓; Endo-Faltblatt: alle Medacta-Schäfte mit 12/14-Konus. | q_com; q_endo | 1; PDF 2 |
| `medacta.quadra_c` | `medacta.kopf.edelstahl` | **bedingt** | Nur Ausführung „Stainless Steel (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. Größe 0: Körpergewicht ≤ 65 kg. | q_com | 1 |
| `medacta.quadra_c` | `medacta.kopf.cocr` | **bedingt** | Nur Ausführung „CoCr (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. Größe 0: Körpergewicht ≤ 65 kg. | q_com | 1 |
| `medacta.quadra_c` | `medacta.kopf.ceramtec_biolox_delta` | **ja** | COM-Zelle ✓ für Quadra-C (12/14). Größe 0: Körpergewicht ≤ 65 kg. | q_com | 1 |
| `medacta.quadra_c` | `medacta.kopf.ceramtec_biolox_option` | **ja** | COM-Zelle ✓ für Quadra-C (12/14). Größe 0: Körpergewicht ≤ 65 kg. OPTION: Revision. | q_com | 1 |
| `medacta.quadra_c` | `medacta.kopf.mectacer_biolox_delta` | **ja** | COM-Zelle ✓ für Quadra-C (12/14). Größe 0: Körpergewicht ≤ 65 kg. | q_com | 1 |
| `medacta.quadra_c` | `medacta.kopf.mectacer_biolox_option` | **ja** | COM-Zelle ✓ für Quadra-C (12/14). Größe 0: Körpergewicht ≤ 65 kg. OPTION: Revision. | q_com | 1 |
| `medacta.quadra_c` | `medacta.endokopf` | **ja** | COM „Endo Head (12/14 taper)“ ✓; Endo-Faltblatt: alle Medacta-Schäfte mit 12/14-Konus. Größe 0: Körpergewicht ≤ 65 kg. | q_com; q_endo | 1; PDF 2 |
| `medacta.amistem_c` | `medacta.kopf.edelstahl` | **bedingt** | Nur Ausführung „Stainless Steel (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. | q_com | 1 |
| `medacta.amistem_c` | `medacta.kopf.cocr` | **bedingt** | Nur Ausführung „CoCr (12/14 taper)“ = ja; 10/12 = nein. Konus am Etikett prüfen. AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. | q_com | 1 |
| `medacta.amistem_c` | `medacta.kopf.ceramtec_biolox_delta` | **ja** | COM-Zelle ✓ für AMIStem C (12/14). AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. | q_com | 1 |
| `medacta.amistem_c` | `medacta.kopf.ceramtec_biolox_option` | **ja** | COM-Zelle ✓ für AMIStem C (12/14). AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. OPTION: Revision. | q_com | 1 |
| `medacta.amistem_c` | `medacta.kopf.mectacer_biolox_delta` | **ja** | COM-Zelle ✓ für AMIStem C (12/14). AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. | q_com | 1 |
| `medacta.amistem_c` | `medacta.kopf.mectacer_biolox_option` | **ja** | COM-Zelle ✓ für AMIStem C (12/14). AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. OPTION: Revision. | q_com | 1 |
| `medacta.amistem_c` | `medacta.endokopf` | **ja** | COM „Endo Head (12/14 taper)“ ✓; Endo-Faltblatt: alle Medacta-Schäfte mit 12/14-Konus. AMIStem-C 00, 00SN, STD 0SN: nur Köpfe S/M/L (q_amistem_p S. 16); COM 2016 unterscheidet keine Größen/Short-Neck-Varianten. | q_com; q_endo | 1; PDF 2 |
| `medacta.quadra_p` | `medacta.kopf.edelstahl` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.kopf.cocr` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.kopf.ceramtec_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.kopf.ceramtec_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.kopf.mectacer_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.kopf.mectacer_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p` | `medacta.endokopf` | **offen** | Nicht in 99.99.COM rev. 12; Konus des Schafts nicht belegt – Endo-Aussage „12/14“ daher nicht anwendbar. | q_com; q_endo | 1; PDF 2 |
| `medacta.quadra_p_collared` | `medacta.kopf.edelstahl` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.kopf.cocr` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.kopf.ceramtec_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.kopf.ceramtec_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.kopf.mectacer_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.kopf.mectacer_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_collared` | `medacta.endokopf` | **offen** | Nicht in 99.99.COM rev. 12; Konus des Schafts nicht belegt – Endo-Aussage „12/14“ daher nicht anwendbar. | q_com; q_endo | 1; PDF 2 |
| `medacta.quadra_p_cemented` | `medacta.kopf.edelstahl` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.kopf.cocr` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.kopf.ceramtec_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.kopf.ceramtec_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.kopf.mectacer_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.kopf.mectacer_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 12), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_quadra_p; q_com | 12; 1 |
| `medacta.quadra_p_cemented` | `medacta.endokopf` | **offen** | Nicht in 99.99.COM rev. 12; Konus des Schafts nicht belegt – Endo-Aussage „12/14“ daher nicht anwendbar. | q_com; q_endo | 1; PDF 2 |
| `medacta.amistem_p` | `medacta.kopf.edelstahl` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.kopf.cocr` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.kopf.ceramtec_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.kopf.ceramtec_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.kopf.mectacer_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.kopf.mectacer_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p` | `medacta.endokopf` | **offen** | Nicht in 99.99.COM rev. 12; Konus des Schafts nicht belegt – Endo-Aussage „12/14“ daher nicht anwendbar. AMIStem-P 00SN: nur Köpfe S/M/L (S. 15). | q_com; q_endo | 1; PDF 2 |
| `medacta.amistem_p_collared` | `medacta.kopf.edelstahl` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.kopf.cocr` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.kopf.ceramtec_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.kopf.ceramtec_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.kopf.mectacer_biolox_delta` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.kopf.mectacer_biolox_option` | **offen** | Nicht in 99.99.COM rev. 12. OP-Technik listet Femurköpfe im Implantatverzeichnis (S. 14), ohne Kombinationstabelle/Konusangabe – aktuelle COM bzw. Medacta fragen. | q_amistem_p; q_com | 14; 1 |
| `medacta.amistem_p_collared` | `medacta.endokopf` | **offen** | Nicht in 99.99.COM rev. 12; Konus des Schafts nicht belegt – Endo-Aussage „12/14“ daher nicht anwendbar. | q_com; q_endo | 1; PDF 2 |
| `medacta.quadra_c` | `medacta.duokopf.bipolar` | **offen** | Bipolar-Dokument nennt keine Schäfte; COM rev. 12 nur Kopf × Bipolar. Registerdaten (SIRIS) sind keine Freigabe. | q_bipolar; q_com | 7; 2 |
| `medacta.amistem_c` | `medacta.duokopf.bipolar` | **offen** | Bipolar-Dokument nennt keine Schäfte; COM rev. 12 nur Kopf × Bipolar. Registerdaten (SIRIS) sind keine Freigabe. | q_bipolar; q_com | 7; 2 |
| `medacta.quadra_p_cemented` | `medacta.duokopf.bipolar` | **offen** | Bipolar-Dokument nennt keine Schäfte; COM rev. 12 nur Kopf × Bipolar. Registerdaten (SIRIS) sind keine Freigabe. | q_bipolar; q_com | 7; 2 |
| `medacta.kopf.edelstahl` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.kopf.cocr` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.duokopf.bipolar` | **ja** | COM Spalte „Medacta Bipolar Head“ ✓. Kopf-Ø = Innen-Ø des Bipolarkopfs (22 bzw. 28); Bipolar 22 nur auf spezifische Anfrage. | q_com; q_bipolar | 2; 7 |
| `medacta.endokopf` | `medacta.duokopf.bipolar` | **nein** | COM: Endo Head × Medacta Bipolar Head = ×. | q_com | 2 |
| `medacta.kopf.edelstahl` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.edelstahl` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.edelstahl` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.edelstahl` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.edelstahl` | `medacta.versafitcup_cc_trio.inlay_keramik` | **nein** | COM: Metallkopf × Mectacer/Ceramtec BIOLOX delta Liner = ×; IFU: Keramik-Inlays stets mit Keramikkopf. | q_com; q_ifu | 2; DE 27 |
| `medacta.kopf.cocr` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.cocr` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.cocr` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.cocr` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓ (beide Konusgruppen). Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.cocr` | `medacta.versafitcup_cc_trio.inlay_keramik` | **nein** | COM: Metallkopf × Mectacer/Ceramtec BIOLOX delta Liner = ×; IFU: Keramik-Inlays stets mit Keramikkopf. | q_com; q_ifu | 2; DE 27 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. Keramik-Inlay-REF 01.29.4xx: Mectacer/CeramTec-Zuordnung nicht angegeben – beide COM-Spalten ✓. Abgeraten bei Inklination > 45°. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.ceramtec_biolox_option` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. Keramik-Inlay-REF 01.29.4xx: Mectacer/CeramTec-Zuordnung nicht angegeben – beide COM-Spalten ✓. Abgeraten bei Inklination > 45°. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_delta` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. Keramik-Inlay-REF 01.29.4xx: Mectacer/CeramTec-Zuordnung nicht angegeben – beide COM-Spalten ✓. Abgeraten bei Inklination > 45°. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. | q_com; q_cctrio | 2; 13 |
| `medacta.kopf.mectacer_biolox_option` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Kopf-Ø muss als Bohrung des Inlaytyps in T6 vorkommen. Keramik-Inlay-REF 01.29.4xx: Mectacer/CeramTec-Zuordnung nicht angegeben – beide COM-Spalten ✓. Abgeraten bei Inklination > 45°. | q_com; q_cctrio | 2; 13 |
| `medacta.endokopf` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **nein** | COM: Endo Head × alle Liner = ×. | q_com | 2 |
| `medacta.endokopf` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **nein** | COM: Endo Head × alle Liner = ×. | q_com | 2 |
| `medacta.endokopf` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **nein** | COM: Endo Head × alle Liner = ×. | q_com | 2 |
| `medacta.endokopf` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **nein** | COM: Endo Head × alle Liner = ×. | q_com | 2 |
| `medacta.endokopf` | `medacta.versafitcup_cc_trio.inlay_keramik` | **nein** | COM: Endo Head × alle Liner = ×. | q_com | 2 |
| `medacta.versafitcup_cc_trio` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio_nohole` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_flach` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio_nohole` | `medacta.versafitcup_cc_trio.inlay_uhmwpe_ueberhoeht` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio_nohole` | `medacta.versafitcup_cc_trio.inlay_hc_flach` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio_nohole` | `medacta.versafitcup_cc_trio.inlay_hc_ueberhoeht` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |
| `medacta.versafitcup_cc_trio_nohole` | `medacta.versafitcup_cc_trio.inlay_keramik` | **ja** | COM ✓. Gleiche Inlaygröße (Buchstabencode) laut T5; Kopf-Ø laut T6. | q_com; q_cctrio | 3; 12–13 |

## Regeln
- Quadra-H, Quadra-C, Quadra-P (inkl. Collared/Cemented), AMIStem-P (inkl. Collared) und AMIStem-C nicht zusammenlegen; QUADRA-P Cemented ist nicht Quadra-C. (q_quadra_p S. 4, 13; OpenAI 4.1)
- Quadra-C Größe 0: begrenzte Verwendung, Körpergewicht höchstens 65 kg (EN „body mass not exceeding 65 kg“; DE-Fassung „Body-Mass-Index“ ist missverständlich). (q_quadra_en S. 10; q_quadra_de S. 10)
- AMIStem-P 00SN (01.18.459) sowie AMIStem-C 00 (01.18.149), 00SN (01.18.699) und STD 0SN (01.18.700): „Kombinierbar ausschließlich mit den Köpfen der Größen S, M und L“ – gilt auch für Endo-/Bipolar-Aufbauten; nicht auf andere Größe-0-Varianten ausweiten. LAT 0SN (01.18.710): offen, vorsorglich S/M/L. (q_amistem_p S. 15–16; OpenAI 4.1/4.3)
- AMIStem-P/-C Short Neck 6SN–9SN bzw. 6SN–8SN: „Erhältlich nur auf besondere Nachfrage mit Bestätigung.“ (q_amistem_p S. 15–16)
- Quadra-C: keine Schäfte 9/10. QUADRA-P Cemented: kein 9 (Technik 1 → Schaft 8), kein 00 (bei Raspel 0 nur Technik 2). AMIStem-C: kein 9 (Technik 1 → Schaft 8). (q_quadra_de S. 9; q_quadra_p S. 11; q_amistem_p S. 12–13)
- Metallköpfe XL (Ø 28/32) und XXL (Ø 28/32/36) haben einen Kragen – Bewegungsumfang kann reduziert sein. Ø 22 S kann ROM mit nativer Hüftpfanne verringern. (q_quadra_de S. 8–9; q_quadra_p S. 9; q_amistem_p S. 11)
- Edelstahl-/CoCr-Köpfe: nur 12/14-Ausführung auf Quadra-H/-C, AMIStem-C (COM S. 1: 10/12 = nein). Etikett kann Konusgröße/Einschränkungen angeben – Schaft-Kopf-Passung vor Montage prüfen. (q_com S. 1; q_ifu DE S. 26 / EN S. 5)
- BIOLOX Option (CeramTec) und Mectacer BIOLOX Option (Kopf + passende Hülse) sind für Revisionsfälle bestimmt. (q_quadra_p S. 12; q_amistem_p S. 14)
- CC Trio: Inlay nach Buchstabencode der Schale wählen; Innendurchmesser = Kopf-Ø; Kopf-Ø ist je Typ eine Liste konkreter Bohrungen (kein Maximalwert). 36 mm nur Keramik und Highcross flach; kein 36 überhöht. (q_cctrio S. 9, 12–13; OpenAI 4.2)
- Keramik-Inlays stets mit Keramikkopf; bei Keramik-auf-Keramik zwingend kompatible Keramikköpfe und -Inlays. (q_ifu DE S. 27 / EN S. 6; q_quadra_de S. 10)
- Keramik-Inlay nicht empfohlen, wenn die Pfanne zu senkrecht steht (Inklination > 45°). (q_cctrio S. 11)
- CC Trio / No-Hole nicht mit Double-Mobility-, Mpact- oder Converter-Linern (COM S. 3 = ×). (q_com S. 3)
- Nur die spezifische Schraube im vorgesehenen Schraubenloch. Spongiosaschraube 01.43.xxxx nur mit Bohrerführung 01.10.10.372; 01.43.0050–0070 nur auf genehmigte Sonderanfrage. (q_ifu DE S. 28; q_cctrio S. 8, 12)
- Mit HA beschichtete Implantate (Quadra-H, Quadra-P, AMIStem-P inkl. Collared) dürfen nicht mit Zement implantiert werden. (q_ifu DE S. 27 / EN S. 5)
- Keine Kombination mit Komponenten anderer Hersteller (außer ausdrücklich in der OP-Technik angegeben). Zulässige Kombinationen stehen in der Operationstechnik. (q_ifu DE S. 27 / EN S. 5)
- Kopfwechsel auf verbleibendem Schaft: je nach Inlay-Material Metallkopf oder BIOLOX Option-Kopf; nach Bruch einer Keramikkomponente sind Metallköpfe kontraindiziert. Bei Versagen eines Keramikkopfes UHMWPE-Pfanne/-Inlay mit austauschen. (q_ifu DE S. 27, 30 / EN S. 6, 8)
- Komponenten nie reimplantieren; wiederholte Montage/Demontage modularer Teile vermeiden; Probereposition nur mit (unveränderten) Probeprothesen. (q_ifu DE S. 27 / EN S. 5–6)
- Raspeln mit „Erhöhung“/„Anstieg“ nicht mit QUADRA-P- bzw. AMIStem-P-Probehals koppeln. (q_quadra_p S. 8; q_amistem_p S. 10)
- Bipolar: Innen-Ø 28 (außen 42–60) oder 22 (außen 39–52, nur auf spezifische Anfrage); nicht jede Größe für beide Innen-Ø. Schaftfreigabe nicht dokumentiert. (q_bipolar S. 5, 7)
- Endo Head (unipolar) nur auf Medacta-Schäften mit 12/14-Konus; kein Liner, kein Bipolar. Außen-Ø 40–56 in 2-mm-Schritten (Sizer 39–56 in 1-mm-Schritten). (q_endo PDF 2; q_com S. 1–2)
- Sicherheit im MR-Umfeld unbekannt (Symbol „MR Unsafe“). (q_ifu DE S. 26, S. 1)
- 99.99.COM zeigt funktionale Kompatibilität, nicht den Zulassungsstatus; Quadra-P/AMIStem-P sind in rev. 12 nicht enthalten → offen. (q_com S. 1)

## Rückrufe / Sicherheitsmeldungen (chargenspezifisch – Bestand mit MPB prüfen)
| Produkt | Behörde | Kennung | Markt | Status | Hinweis | Betrifft | Link |
|---|---|---|---|---|---|---|---|

## Hinweise
- Vor dem Öffnen Komponente, Seite und Größe laut ansagen; Herstellerdokument und aktuelle EU-IFU maßgeblich.
- Systeme nicht mischen: nur Komponenten, die der Hersteller ausdrücklich für dieses System vorsieht. Gleicher Konus oder gleiche Keramikmarke ist kein Kombinationsnachweis.
- Werte nur aus dem genannten Original mit Seite; nicht dokumentierte Kombinationen bleiben „offen – Operateur fragen“ (ungeprüft ≠ verboten ≠ freigegeben).
- Rückrufe sind chargenspezifisch: Betroffenheit nur über REF/Charge im Original und mit der/dem Medizinprodukte-Beauftragten klären – keine pauschale Sperre oder Freigabe.
- Medacta-PDFs tragen den Portal-Stempel „Valid on 07 Oct 2026“ – das ist kein Dokumentstand; Stand = „Letztes Update“ im Impressum.
- Registerhäufigkeit (EPRD/SIRIS) ist keine Kombinationsfreigabe; Freigaben nur aus 99.99.COM und OP-Technik.
- AMIStem-C: aktuelle DE-Fassung 99.14ASTEMPS.42 (07/2022) und ältere EN 99.14ASTEM.12 (07/2014) weichen ab (Größe 00, Short Neck, Raspeltabelle) – nicht aufgelöst.

## Offen
- [ ] Aktuelle 99.99.COM (nach rev. 12/Okt. 2016) mit Quadra-P, Quadra-P Collared/Cemented, AMIStem-P, AMIStem-P Collared – bis dahin Kopf-/Endo-/Bipolar-Kombinationen für P-Schäfte offen
- [ ] Konus Quadra-P/AMIStem-P (in OP-Techniken nicht genannt)
- [ ] Edelstahl-/CoCr-Kopf-REF ↔ Konus 10/12 oder 12/14: Zuordnung nicht im Dokument (Etikett)
- [ ] AMIStem-C: DE 2022 (00, Short Neck) vs. EN 2014 (ohne 00/SN, andere Raspeltabelle) – Lieferbarkeit bei Medacta bestätigen
- [ ] AMIStem-C LAT 0SN (01.18.710): gilt S/M/L-Kopfgrenze? (Marker in Größenspalte; OpenAI nur STD)
- [ ] Quadra-P 6SN–10SN Fußnote I verweist auf Instrumente – Bedeutung für Implantatverfügbarkeit
- [ ] Bipolar: Nomenklatur S. 7 nur von einem Prüfer gelesen (OpenAI prüfte S. 4–6, 8); freigegebene Schäfte nicht dokumentiert
- [ ] Keramik-Inlay 01.29.4xx: Hersteller/Material (Mectacer vs. CeramTec BIOLOX delta) nicht angegeben
- [ ] Versafitcup CC Trio Schalenmaterial/Beschichtung nicht genannt
- [ ] CCD-Winkel, Offset, Schaftlängen, Kopf-Halslängen in mm: in keinem gelesenen Dokument
- [ ] Endo Head 99.18.12 rev.03: kein Ausgabedatum
- [ ] Etikett-/Packungsbilder, UDI/GTIN: nicht in Dokumenten; Medacta-Webseite nicht geprüft
- [ ] BfArM-Meldungen Medacta (10 Jahre)

## Quellen
- **siris** SIRIS Report Hip & Knee 2025 · Dezember 2025 · S. Tab. 4.16 S. 95; 4.19 S. 103; 4.34 S. 129 · Markt: CH (nur Ranking) · gelesen: Grok/Astra 07.10.2026 · https://www.siris-implant.ch/images/content/download/20251204_SIRISReportHipandKnee2025_Final.pdf
- **es** EPRD Implantatergebnisse Hüftschäfte/-pfannen/-versorgungen · Jahresbericht 2025 · S. Excel-Tabellen · Markt: DE (nur Ranking) · gelesen: Grok/Astra 07.10.2026 · https://www.eprd.de/de/downloads/tabellen/jahresbericht2025

## Änderungen
- **v1.0** (2026-10-07, 001-implantate-dach): Neuanlage nach DACH-Ranking (EPRD 2025, SIRIS 2025); Werte nur soweit von Astra am Original bestätigt, Rest offen.
- **v1.1** (2026-10-07, 001-implantate-luecken): Schäfte Quadra-H/-C, Quadra-P/-P Collared/-P Cemented, AMIStem-P/-P Collared/-C mit allen Größen/REF; Köpfe (Edelstahl, CoCr, CeramTec delta/Option, Mectacer delta/Option); Versafitcup CC Trio + No-Hole, 5 Inlaytypen, Verschluss, Schrauben; Bipolar 28/22; Endo Head; COM rev. 12 als Tabellen T1–T4 + passt_zu (P-Schäfte offen); CC-Trio- und Raspeltabellen; IFU-Warnungen als Regeln; Etikett-Schema-Hinweise.

Bilder: keine übernommen – Rechte beim Hersteller.
