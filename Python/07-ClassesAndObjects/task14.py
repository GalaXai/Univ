class TV:
    def __init__(self):
        self.is_on = "off"
        self.channel_num = 0
        self.channel_list = []

    def turn_on(self):
        self.is_on = "on"

    def turn_off(self):
        self.is_on = "off"

    def show_status(self):
        if self.is_on == "on":
            print("TV is {}, channel {} ({})".format(
                self.is_on,self.channel_num,self.display_channel()))
        else:
            print("TV is {}".format(self.is_on))
    
    def display_channel(self):
        try:
            return self.channel_list[self.channel_num]
        except:
            return "no avaiable channels"
    
    def set_channel(self,number):
        self.channel_num = number

    def show_channels(self):
        if self.channel_list == []:
            print("TV not programmed, no available channel")
        else:
            print(self.channel_list)

    def set_channels(self,*argv):
        for arg in argv:
            self.channel_list.append(arg)
if __name__ == '__main__':
    p0 = TV()
    p0.show_status()
    p0.turn_on()
    p0.show_status()
    p0.show_channels()
    p0.set_channels("TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery")
    p0.show_channels()
    p0.set_channel(7)
    p0.show_status()
    p0.turn_off()