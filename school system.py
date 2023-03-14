students = []

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def add_student():
    print("Enter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = int(input("Grade: "))
    student = Student(name, age, grade)
    students.append(student)
    print(f"{name} has been added to the school system.")

def view_students():
    print("Student List:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student.name} ({student.age} years old, grade {student.grade})")

while True:
    print("\nSchool System Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Quit")
    choice = int(input("Enter choice (1-3): "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
