import unittest
from main import BME280, Servo, LED

class TestBME280(unittest.TestCase):
    def test_read_temperature(self):
        bme = BME280()
        temperature = bme.read_temperature()
        self.assertIsInstance(temperature, float)

class TestServo(unittest.TestCase):
    def test_open_ventilation(self):
        servo = Servo()
        self.assertIsNone(servo.open_ventilation())

    def test_close_ventilation(self):
        servo = Servo()
        self.assertIsNone(servo.close_ventilation())

class TestLED(unittest.TestCase):
    def test_turn_on(self):
        led = LED()
        self.assertIsNone(led.turn_on())

    def test_turn_off(self):
        led = LED()
        self.assertIsNone(led.turn_off())

if __name__ == '__main__':
    # Voer de unittests uit
    unittest.main()
