import time
from ctypes import CDLL, c_float

# Decorator om de uitvoeringstijd van een functie te meten
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("{} execution time: {} seconds".format(func.__name__, execution_time))
        return result
    return wrapper

# Laad de gedeelde bibliotheek in
sensors_lib = CDLL('./sensors.so')

# Definieer de functies die we willen oproepen
read_temperature = sensors_lib.readMockedTemperature
read_temperature.restype = c_float  # Aangeven van het retourtype

read_light_intensity = sensors_lib.readMockedLightIntensity
read_light_intensity.restype = c_float  # Aangeven van het retourtype

# Simuleer het inladen van de C++-klassen, omdat we alleen een simulatie hebben
class BME280:
    def __init__(self):
        self.temperature = 0

    @measure_execution_time
    def read_temperature(self):
        self.temperature = read_temperature()
        print("Received temperature in Python:", self.temperature)
        return self.temperature

class OPT3002:
    def __init__(self):
        self.light_intensity = 0

    @measure_execution_time
    def read_light_intensity(self):
        self.light_intensity = read_light_intensity()
        print("Received light intensity in Python:", self.light_intensity)
        return self.light_intensity

class Servo:
    def __init__(self):
        self.ventilation_status = "closed"  # Toevoegen van ventilation_status attribuut

    def open_ventilation(self):
        print("Opening ventilation")
        self.ventilation_status = "open"  # Bij het openen van de ventilatie, de status bijwerken

    def close_ventilation(self):
        print("Closing ventilation")
        self.ventilation_status = "closed"  # Bij het sluiten van de ventilatie, de status bijwerken


class LED:
    def __init__(self):
        self.is_on = False

    @measure_execution_time
    def turn_on(self):
        self.is_on = True
        print("LED is ON")

    @measure_execution_time
    def turn_off(self):
        self.is_on = False
        print("LED is OFF")

goal_temperature = 20
goal_light_intensity = 750

sensors = {
    'bme280': BME280(),
    'opt3002': OPT3002(),
    'servo': Servo()
}

status_led = LED()

if __name__ == "__main__":
    while True:
        current_temperature = sensors['bme280'].read_temperature()
        current_light_intensity = sensors['opt3002'].read_light_intensity()

        if current_temperature > goal_temperature:
            sensors['servo'].open_ventilation()
        else:
            sensors['servo'].close_ventilation()

        if current_light_intensity < goal_light_intensity:
            status_led.turn_on()
        else:
            status_led.turn_off()

        print("Temp goal: ", goal_temperature, " Current: ", current_temperature)
        print("Light goal: ", goal_light_intensity, " Current: ", current_light_intensity)
        print("----------------------------------------------")

        time.sleep(1)
