class Course:
    def __init__(self, name, id, days, periods, credits):
        self.name = name
        self.id = id
        self.days = days
        self.periods = periods
        self.credits = credits

    #getters and setters
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_days(self):
        return self.days

    def get_periods(self):
        return self.periods

    def get_credits(self):
        return self.credits

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_days(self):
        return self.days

    def set_periods(self, periods):
        self.periods = periods

    def set_credits(self, credits):
        self.credits = credits

    def __str__(self):
        return f"Course Name: {self.name}, Class ID: {self.id}, Credits: {self.credits}, Days: {self.days}, Periods: {self.periods}"

    @classmethod
    def visualize_schedule(cls, classes: list):
        """
        Function: the function returns a visual representation of the schedule.

        Parameters:
            classes (list): the schedule of the entered classes.

        Returns:
            schedule (list): the visual representation of the schedule.
        """
        schedule = ""
        for course in classes:
            days, periods = course.get_times()
            periods_str = ", ".join(map(str, periods))
            schedule += f"{course.get_name()} meets on {days} during periods: {periods_str}\n"
        return schedule

    def check_overlap(self, courses: list):
        """
            Function: checks for overlap between classes chosen

            Parameters:
                other class that's being compared

            Returns:
                boolean of whether there is overlap or not
        """
        # if overlap returns true, otherwise returns false
        ret = False
        while ret == False:
            for period in self.get_periods(): #for every time of the course
                for course in courses: #for every course already in schedule
                    if period in course.get_periods(): #if the time of the course is ine the times of the already scheduled course
                        ret = True #ret becomes True, meaning there is overlap
        return ret

    #def alternative(self):
    #possibly generate alternative schedule

    @classmethod
    def get_total_credits(cls, schedule: list):
        """
        Function: the function returns the total credits of your schedule.
        Parameter: schedule(list)
        Return: int
        """
        credits = 0
        for course in schedule:
            credits += course.get_credits()
        return credits

    @classmethod
    def get_schedule(cls, courses: list):
        """
        Function: the function returns a schedule of the entered classes, prioritizing classes listed first and keeping in mind the preferences of early/ midday/ or late classes.

        Parameters:
            courses (list): the list of classes to schedule.

        Returns:
            schedule (list): the schedule of the entered classes.
        """

        schedule = []

        for course in courses:
                if cls.get_total_credits(schedule) < 18 and course.check_overlap(schedule) == False:
                    schedule.append(course)
        return schedule