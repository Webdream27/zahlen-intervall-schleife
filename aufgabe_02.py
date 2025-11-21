""" ****************************************************
Aufgabe 2: Schleife zwischen zwei Zahlen mit Validierung
*****************************************************""" 

# Funktion liest zwei Zahlen ein und stellt sicher, dass sie unterschiedlich sind. Gibt die kleinere und die größere Ganzzahl zurück.
def get_valid_numbers():
    while True:
        try:
            # Eingabe der beiden Zahlen
            zahl1 = float(input("Geben Sie die erste Zahl ein: "))
            zahl2 = float(input("Geben Sie die zweite Zahl ein: "))

            # Pruefen, ob die Zahlen gleich sind.
            if zahl1 == zahl2:
                print("Die Zahlen muessen unterschiedlich sein. Bitte erneut eingeben.")
                continue  # Springt zurueck an den Anfang der while-Schleife

            # Die kleinere und die groeßere Zahl ermitteln
            # Konvertierung zu Integer.
            kleiner = int(min(zahl1, zahl2))
            groesser = int(max(zahl1, zahl2))

            # Rueckgabe der sortierten Ganzzahlen
            return kleiner, groesser

        except ValueError:
            # Fehlerbehandlung für nicht-numerische Eingaben
            print("Ungueltige Eingabe. Bitte geben Sie nur Zahlen ein.")

# Die Funktion aufrufen, um die validierten Zahlen zu erhalten
kleiner, groesser = get_valid_numbers()

print(f"\nStarte Schleife von {kleiner} bis {groesser} (inklusive).")

anzahl_durchlaeufe = 0

# Erstellen der Schleife
for i in range(kleiner, groesser + 1):
    # Bei jedem Durchlauf wird der Zaehler erhöht
    anzahl_durchlaeufe += 1
    
# Endgültige Ausgabe der Anzahl der Durchlaeufe
print(f"\nDie Schleife wurde {anzahl_durchlaeufe} Mal durchlaufen.")



