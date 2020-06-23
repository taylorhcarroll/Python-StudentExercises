from NSSPerson import NSSPerson


class Instructor(NSSPerson):
    def __init__(self, first, last, slack, specialty):
        self.specialty = specialty
        super(Instructor, self).__init__(first, last, slack)

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
