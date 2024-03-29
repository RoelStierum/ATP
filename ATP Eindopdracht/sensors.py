import ctypes
import time

# Laad de gedeelde bibliotheek in
sensors_lib = ctypes.CDLL("./sensors.so")

# Specificeer het retourtype voor de C-functies
sensors_lib.readMockedTemperature.restype = ctypes.c_float
sensors_lib.readMockedLightIntensity.restype = ctypes.c_float

class BME280:
    def __init__(self):
        pass

    def read_temperature(self):
        return sensors_lib.readMockedTemperature()

class OPT3002:
    def __init__(self):
        pass

    def read_light_intensity(self):
        return sensors_lib.readMockedLightIntensity()

class Servo:
    def __init__(self):
        pass

    def open_ventilation(self):
        print("Opening ventilation")

    def close_ventilation(self):
        print("Closing ventilation")
