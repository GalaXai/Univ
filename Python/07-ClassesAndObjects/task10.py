class TV:
    def __init__(self):
        self.is_on = "off"

    def turn_on(self):
        self.is_on = "on"

    def turn_off(self):
        self.is_on = "off"

    def show_status(self):
        print("TV is {}".format(self.is_on))
if __name__ == '__main__':
    p0=TV()
    p0.show_status()
    p0.turn_on()
    p0.show_status()
    p0.turn_off()
    p0.show_status()
