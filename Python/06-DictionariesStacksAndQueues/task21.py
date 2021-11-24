import json
with open("06-DictionariesStacksAndQueues/api.nbp.pl.json" ,"r",encoding="UTF-8") as file:
    with open("06-DictionariesStacksAndQueues/cenausd.json","w") as f:
            #json.dump("Date            Buying Rate     Selling Rate",f)
            #f.write('\n')
            #json.dump("============================================",f)
            #f.write('\n')
            f.write('[')
            data = json.load(file)
            #print(type(data))
            i=0
            for x in data["rates"]:
                #x =  dict
                #date = x.get("effectiveDate")
                #buy = x.get("bid")
                #sell = x.get("ask")
                #json.dump(f'{date}      {buy}          {sell}',f)
                output = {
                    "date" : x.get("effectiveDate"),
                    "buy" : x.get("bid"),
                    "sell" : x.get("ask"),
                }
                if i==0:
                    i+=1
                else:
                    f.write(',\n')
                json.dump(output,f)
                #json.dump(  x.get("effectiveDate"),f,indent=3)
                #json.dump(  x.get("bid"),f,indent=3)
                #json.dump(  x.get("ask"),f,indent=3)
            f.write(']')