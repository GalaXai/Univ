import re
vowels = ['a','e','i','o','u','y']
text="To be, or not to be, that is the question"
AmmountOfVowels = re.findall("[vowels]",text)
print(AmmountOfVowels)
print("Number of vowels = {}".format(len(AmmountOfVowels)))