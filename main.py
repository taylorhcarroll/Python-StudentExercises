from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

nutshell = Exercise("nutshell", "Javascript")
reactnutshell = Exercise("reactnutshell", "react")
bangazon = Exercise("bangazon", "C#/.Net")
trestlebridge = Exercise("Trestlebridge Farms", "C#")

cohort35 = Cohort("Day Cohort 35")
cohort36 = Cohort("Day Cohort 36")
cohort37 = Cohort("Day Cohort 37")
cohort38 = Cohort("Day Cohort 38")

student1 = Student("Taylor", "Carroll", "taylorhc")
student2 = Student("Sage", "Klein", "sagey")
student3 = Student("Keith", "Potempa", "kpotempa")
student4 = Student("Nate", "Vogel", "nvogel")

mo = Instructor("mo", "mo", "itsmo", "Backend C#")
madi = Instructor("Madi", "Pepper", "peppers", "Beat Saber")
brenda = Instructor("Brenda", "Long", "blong", "UX/UI")

mo.assign_exercise(student1, nutshell)
mo.assign_exercise(student1, reactnutshell)
mo.assign_exercise(student2, bangazon)
mo.assign_exercise(student3, trestlebridge)
mo.assign_exercise(student4, trestlebridge)

students = []
students.append(student1)
students.append(student2)
students.append(student3)
students.append(student4)

exercises = []
exercises.append(nutshell)
exercises.append(reactnutshell)
exercises.append(bangazon)
exercises.append(trestlebridge)

for student in students:
    print(f'{student.first_name}, {student.last_name} is working on:')
    for exercise in student.exercises:
        print(f'{exercise.name}')
    print()
