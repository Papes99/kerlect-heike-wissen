# 002 Knie-TEP – Implementierungsauftrag (Entwurf, nicht klinisch freigegeben)

## Ziel
Kerlect Consumer-App ID 6aa3f64b0b23cc244ce7686d; Knie-Implantat-Tablett analog Hüfte: physikalisches Drag-and-drop, Magnet-Snap, federndes Einrasten, Fehlkombination prallt zurück, unterbrechbar, reduced-motion, Profilsteuerung für Ton/Haptik. Keine Änderungen an Kerlect Kliniken.

## Auswahl
Nach tatsächlicher Häufigkeit in DACH, belegt mit EPRD 2025, SIRIS 2025 und österreichischen Registerdaten. **Keine Rangliste aus Bekanntheit ableiten.** Primäre Knie-TEP und unikondyläre Systeme getrennt; Revision separat.

## Daten je System und Komponente
Hersteller, System, Implantattyp (Femur/Tibia/Insert/Patella), Seite, Größe, Variante (CR/PS/UC etc.), Fixation, Material, echte REF, GTIN/UDI-DI soweit verfügbar, Quelle mit Dokumentrevision/Seite/URL, Marktregion und Evidenzstatus. Kompatibilitätsrelationen nur bei ausdrücklicher Herstellerfreigabe. Keine stillschweigenden Paarungen.

## Produktbilder und Packungen
1. Verifiziertes echtes Produktfoto mit Hersteller-URL und Bildnachweis; andernfalls neutrales schematisches Produktbild.
2. Packung als **klar markiertes Mock-up**, sofern kein authentisches Verpackungsfoto mit belastbarem Nachweis vorliegt.
3. Auf Mock-up Hersteller, System, REF, Größe, Seite, Material, LOT/UDI ausschließlich als ausdrücklich gekennzeichnete Beispieldaten bzw. nur verifizierte Produktdaten; niemals erfundene echte LOT/UDI oder scheinbar scanbare Codes.
4. In der App keine Behauptung von Sterilität, Lieferbarkeit oder Freigabe allein aus einem Bild ableiten.

## Interaktion
Filter Hersteller/System/CR-PS/Größe/Seite/Fixation; schwungvolles Größenrad mit Ticks; Femur- und Tibia-Komponente setzen, Insert einrasten, optionale Patella; bei Fehlpaarung Gummi-Abprall plus konkrete Erklärung; Verpackungsdetail per Tap; Abschlussrotation. 1,1 Sekunden Halten für „Steril anreichen“ als Simulation. Performance und Bedienbarkeit vor Animation.

## Qualitäts-Gates
- Registerbeleg für Häufigkeit vorhanden?
- Jede REF und Größe direkt am Original verifiziert?
- Jede Kombination explizit in Herstellerdokumenten zugelassen?
- Fotos lizenziert/verlinkbar, Herkunft dokumentiert?
- Keine ungeprüfte klinische Freigabe; lokaler Klinikbestand und Etikett maßgeblich.

## Ausgangsquellen
- https://www.eprd.de/de/downloads/tabellen/jahresbericht2025
- https://www.anq.ch/de/fachbereiche/akutsomatik/messinformation-akutsomatik/implantatregister-siris-huefte-knie-schulter/

**Status:** Spezifikation erstellt; Herstellerliste, echte REF/Größen und Fotos müssen noch systemweise verifiziert werden. Keine App-Implementierung behauptet.
