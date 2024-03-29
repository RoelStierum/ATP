import unittest
from main import BME280, Servo, LED, OPT3002

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.bme = BME280()
        self.opt = OPT3002()
        self.servo = Servo()
        self.led = LED()

    def test_system_response(self):
        goal_temperature = 20
        goal_light_intensity = 750

        current_temperature = self.bme.read_temperature()
        current_light_intensity = self.opt.read_light_intensity()

        if current_temperature > goal_temperature:
            self.servo.open_ventilation()
            self.assertEqual(self.servo.ventilation_status, "open")
        else:
            self.servo.close_ventilation()
            self.assertEqual(self.servo.ventilation_status, "closed")

        if current_light_intensity < goal_light_intensity:
            self.led.turn_on()
            self.assertTrue(self.led.is_on)
        else:
            self.led.turn_off()
            self.assertFalse(self.led.is_on)

if __name__ == '__main__':
    unittest.main()
