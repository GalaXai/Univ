import json

with open("06-DictionariesStacksAndQueues/imported.json" ,"r", encoding="utf-8") as file:
    data = json.load(file)
    for key,value in data.items():
        print(key,":",value)