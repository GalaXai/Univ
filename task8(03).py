Paul = 21
Annie = 18
ageOfMajority = 21

if Paul >=ageOfMajority and Annie >=ageOfMajority:
    print("They are both adults")
else:
    print("Both of them aren't adults")

def age_check(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult yet")
    return 0


age_check(Paul)
age_check(Annie)
