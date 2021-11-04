import json
def studentData():
    student={
        "Name": "",
        "Surname": "",
        "Age": None,
        "Parents Name": [],
        "Status": False,
    }
    for key in student:
        output = input("Students {}:".format(key))
        student.update({key: output})
    return student
with open("Python/06-DictionariesStacksAndQueues/student.json" ,"w", encoding="utf-8") as file:
    json.dump(studentData(),file,ensure_ascii=False)