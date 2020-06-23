from cohort import Cohort


class NSSPerson():
    def __init__(self, first, last, slack):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = Cohort
