class Course:
    def __init__(self,title):
        self.course_title = title
        self.stundets_list = []

    def add_student(self,student):
        if len(self.students) < 10:
            self.students.append(student)
            print(f"{student} has been enrolled in the course.")
        else:
            print("The course is already full. Enrollment is closed.")
