person = {
    "name": "Stefan",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone": {"landline":"123444321","mobile":"111333555"}
}
print(person)
print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
person["married"] = False
person["sex"] = "Male"
person["hobby"].append("bicycle")
person["phone"].update({"work":'313131444'})
for key, value in person.items():
    print(key, "=",value)