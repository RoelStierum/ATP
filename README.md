# ATP


# Regelsysteem voor Temperatuur- en Lichtcontrole

Dit project bevat een regelsysteem geschreven in Python, waarbij ook C++ wordt gebruikt voor bepaalde functionaliteiten. Het systeem controleert de temperatuur en lichtintensiteit in een ruimte en past de ventilatie en verlichting dienovereenkomstig aan.

### Vereisten

- Python 3.6.9
- C++ compiler (bijv. g++)
- unittest module (standaard in Python)

### Installatie en Uitvoering

1. Compileer de C++-bestanden:
   ```bash
   g++ -shared -o sensors.so -fPIC sensors.cpp
   ```

2. Voer de Python-bestanden uit:
   ```bash
   python3 main.py
   ```

3. Voer de unittests uit:
   ```bash
   python3 -m unittest test_main.py
   ```

   ```bash
   python3 -m unittest test_integration.py
   ```

   ```bash
   python3 -m unittest test_system.py
   ```

