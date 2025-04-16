class Course:
    def __init__(self, name, id, times, credits):
        self.name = name
        self.id = id
        self.times = times
        self.credits = credits

    #getters and setters
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_times(self):
        return self.times

    def get_credits(self):
        return self.credits

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_times(self, times):
        self.times = times

    def set_credits(self, credits):
        self.credits = credits

    def __str__(self):
        return f"Course Name: {self.name}, Class ID: {self.id}, Credits: {self.credits}, Times: {self.times}"

    @classmethod
    def get_schedule(cls, classes: list, preference: str):
        """
        Function: the function returns a schedule of the entered classes, prioritizing classes listed first and keeping in mind the preferences of early/ midday/ or late classes.

        Parameters:
            classes (list): the list of classes to schedule.
            preference (str): the preference of early / midday or late classes.

        Returns:
            schedule (list): the schedule of the entered classes.
        """
        schedule = []
        return schedule

    @classmethod
    def visualize_schedule(cls, classes: list):
        """
        Function: the function returns a visual representation of the schedule.

        Parameters:
            classes (list): the schedule of the entered classes.

        Returns:
            schedule (list): the visual representation of the schedule.
        """

        schedule = []
        return schedule

    def check_overlap(self, other):
        """
            Function: checks for overlap between classes chosen

            Parameters:
                other class that's being compared

            Returns:
                boolean of whether there is overlap or not
        """
        # if overlap returns true, otherwise returns false

    #def alternative(self):
    #possibly generate alternative schedule

