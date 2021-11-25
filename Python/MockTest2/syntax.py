"Syntax that u need to remember for the test"
"Files:"
#with open()asfile: #encoding = "UTF-8"
#file.read()
#file.write("\n") brakes line
#json.dump("") will dump string or dictr #indent=True
#json.loads() #loads data as dictr or list
"Dictionaries:"
#dict.get(value) => key
#dict.items => key,value
#dict.keys => key
#dict.vales => values
#dict.update 
#dict.pop
"Regex :"
"""
a.	All words ‘Poland’
r"Poland"g

b.	Country names (Poland, Germany and France)
r"France|Germany|Poland

c.	Punctuation marks (dots and commas)
r" [\W]\s"g

d.	Numbers representing a year (four-digit numbers)
r" \d{4}"g

e.	Capital letters
r" [A-Z]"g

f.	Vowels
r" a|e|i|o|u|y"g

g.	Words with at least five letters.
r" \w{5,0}"g

h.	Words starting with capital letters
r"[A-Z]\w+
"""