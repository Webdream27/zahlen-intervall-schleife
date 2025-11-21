# Zahlen-Intervall-Schleife

Eine Python-Anwendung zur logischen Verarbeitung von Zahlenbereichen. Das Programm demonstriert den Umgang mit Benutzereingaben, Typkonvertierung und Schleifensteuerung.

## Aufgabenstellung
1.  Einlesen von zwei beliebigen Zahlen.
2.  Validierung: Sicherstellen, dass die Zahlen unterschiedlich sind (Wiederholung der Eingabe bei Gleichheit).
3.  Logik: Automatische Erkennung, welcher Wert die Unter- und welcher die Obergrenze ist (beliebige Eingabereihenfolge).
4.  Verarbeitung: Durchlaufen einer Schleife vom Start- bis zum Endwert.
5.  Ausgabe: Anzeige der Anzahl der durchgeführten Schleifendurchläufe.

## Technische Umsetzung
Der Code zeichnet sich durch folgende Merkmale aus:
*   **Input-Validierung:** Nutzung einer `while True`-Schleife in Kombination mit `try-except`, um Fehleingaben (z.B. Buchstaben) abzufangen.
*   **Dynamische Sortierung:** Verwendung von `min()` und `max()`, um unabhängig von der Eingabereihenfolge den korrekten Start- und Endwert zu ermitteln.
*   **Typ-Sicherheit:** Konvertierung von `float` Eingaben zu `int`, da die `range()`-Funktion in Python Ganzzahlen benötigt.

## Nutzung
Führen Sie das Skript in der Konsole aus:

```bash
python main.py
