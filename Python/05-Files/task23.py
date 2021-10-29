import csv
with open('Python/05-Files/students.txt.') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_file:
        if line_count ==0:
            print("Column names are {}.".format(", ".join(row)))
            line_count+=1
        else:
            print("\t Name: {}, Surname: {}, Email= {}.".format(row[0],row[1],row[4]))
            line_count += 1
        print("Processed {} lines.".format(line_count))