class Instructor:
    def __init__(self, first_name, last_name, slack, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack
        self.exercise = []
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
