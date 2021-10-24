cm = int(input("How tall are u in centimeters: "))
foot = cm / 30.48
foot_1 = int(foot)
foot_2 = (foot-foot_1)*10
print("I am {} cm tall, i.e. {} feet and {:.0f} inches.".format(cm, foot_1, foot_2))
