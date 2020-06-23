#from cohort import Cohort
from NSSPerson import NSSPerson


class Student(NSSPerson):
    def __init__(self, first, last, slack):
        super(Student, self).__init__(first, last, slack)

        self.exercises = list()
