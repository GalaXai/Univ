import csv
with open("MockTest2/people.csv") as file:
    csv_file = csv.reader(file, delimiter=',')
    for row in csv_file:
        if row[-1] == "Female" and int(row[-2]) >= 160 and int(row[-2]) <= 180:
            print (row)