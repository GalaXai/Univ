class Course:
    def __init__(self):
        self.stundets_list = []

    def add_student(self,student):
        if len(self.stundets_list) < 10:
            self.stundets_list.append(student)
            print(f"{student} has been enrolled in the course.")
        else:
            print("The course is already full. Enrollment is closed.")
