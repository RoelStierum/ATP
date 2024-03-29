class LED:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("LED is ON")

    def turn_off(self):
        self.is_on = False
        print("LED is OFF")
