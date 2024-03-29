import unittest
from main import BME280, Servo, LED, OPT3002

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.bme = BME280()
        self.opt = OPT3002()
        self.servo = Servo()
        self.led = LED()

    def test_temperature_and_servo(self):
        temperature = self.bme.read_temperature()
        if temperature > 20:
            self.servo.open_ventilation()
            self.assertEqual(self.servo.ventilation_status, "open")
        else:
            self.servo.close_ventilation()
            self.assertEqual(self.servo.ventilation_status, "closed")

    def test_light_and_led(self):
        light_intensity = self.opt.read_light_intensity()
        if light_intensity < 750:
            self.led.turn_on()
            self.assertTrue(self.led.is_on)
        else:
            self.led.turn_off()
            self.assertFalse(self.led.is_on)

if __name__ == '__main__':
    unittest.main()
