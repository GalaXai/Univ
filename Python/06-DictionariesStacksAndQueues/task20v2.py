import json

with open("06-DictionariesStacksAndQueues/students.json" ,"r") as file:
    with open("06-DictionariesStacksAndQueues/limitedv2.json" ,"w") as f:
        data = json.load(file)
        output = []
        for i in range(len(data)):
            temp = data[i]
            dict(temp)
    #name surname and id
            ans = {
                "name": temp.get("name "),
                "surname": temp.get("surname"),
                "student id": temp.get("student id"),
            }
            output.append(ans)
        json.dump(output, f,indent=True)
            #f.write('\n')