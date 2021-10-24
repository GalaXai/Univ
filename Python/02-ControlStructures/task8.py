Paul = 21
Annie = 18
"""
if Paul >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")
"""
###
"""
if Annie >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")
"""


def age_check(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult yet")
    return 0


age_check(Paul)
age_check(Annie)
