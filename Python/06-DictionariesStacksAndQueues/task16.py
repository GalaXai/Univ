NATO_phonetic_alphabet = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Echo",
    "e": "Foxtrot",
    "f": "Golf",
    "g": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu"
 }
word = input("Enter text: ")
print("Spelled text: ",end=" ")
for letter in word:
    print(NATO_phonetic_alphabet.get(letter.lower()),end=" ")
