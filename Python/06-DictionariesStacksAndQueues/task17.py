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
with open("Python/06-DictionariesStacksAndQueues/ICAO.txt", "w") as file:
    for key,value in NATO_phonetic_alphabet.items():
        file.write(key.upper()+" "+value+"\n")