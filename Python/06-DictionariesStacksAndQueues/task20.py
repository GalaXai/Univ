import json

with open("06-DictionariesStacksAndQueues/students.json" ,"r") as file:
    with open("06-DictionariesStacksAndQueues/limited.json" ,"w") as f:
        data = json.load(file)
    #name surname and id
        output = {}
        ans=[]
        for i in range(len(data)):
            output = {}
            output["name "] =data[i]["name "]
            output["surname"] =data[i]["surname"]
            output["student id"] =data[i]["student id"]
            ans.append(output)
        json.dump(ans, f,indent=True)
        f.write('\n')