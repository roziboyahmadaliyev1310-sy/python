class Students:
    def __init(self, name, age, semester, student_ID):
        self.name=name
        self.age=age
        self.semester=semester
        self.student_ID=student_ID
        self.students=[]
    
    def add_students(self, name, age, semester, student_ID):
        self.students.append(self.students(name, age, semester, student_ID))


while True:
    name=input("Student Name: ")
    age=int(input("Student Age: "))
    semester=int(input("Student Semester: "))
    student_ID=input("Student ID: ")
    if not name or not age or not semester or not student_ID:
        print("Please fill in all the fields.")
    elif age<=0 or semester<=0:
        print("Age and semester must be positive numbers or above 0.")
    else:
        break
