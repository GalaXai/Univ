class TV:
    def __init__(self):
        self.is_on = "off"
        self.channel_num = 1

    def turn_on(self):
        self.is_on = "on"

    def turn_off(self):
        self.is_on = "off"

    def show_status(self):
        if self.is_on == "on":
            print("TV is {}, channel {}".format(
                self.is_on,self.channel_num))
        else:
            print("TV is {}".format(self.is_on))
    
    def set_channel(self,number):
        self.channel_num = number


if __name__ == '__main__':
    p0 = TV()
    p0.show_status()
    p0.turn_on()
    p0.show_status()
    p0.set_channel(5)
    p0.show_status()
    p0.turn_off()
    p0.show_status()