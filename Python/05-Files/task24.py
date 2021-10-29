import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C,Friday: 30C"
temperatures = re.findall("\d{2}",message)
avg_temp = 0
for temp in temperatures:
    avg_temp +=int(temp)
print("Average temperature = {}".format(avg_temp/len(temperatures)))