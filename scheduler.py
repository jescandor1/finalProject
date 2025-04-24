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
    def visualize_schedule(cls, classes: list):
        """
        Function: the function returns a visual representation of the schedule.

        Parameters:
            classes (list): the schedule of the entered classes.

        Returns:
            schedule (list): the visual representation of the schedule.
        """

        time_slot = []
        # from json file, ex is ["7:25 - 8:15"]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

        schedule_grid = {(day, time): "" for day in days for time in time_slot}

        for course in classes:
            for time in course.get_times():
                try:
                    day, hour = time.split()
                    if (day, hour) in schedule_grid:
                        # that row column pairing gets the course name inputted there
                        schedule_grid[(day, hour)] = course.get_name()
                except ValueError:
                    print(f"Invalid time stated")

        # truncate course names that are too long
        # display by returning the grid

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
        for time in self.get_times(): #for every time of the course
            for course in courses: #for every course already in schedule
                if time in course.get_times(): #if the time of the course is ine the times of the already scheduled course
                    ret = True #ret becomes True, meaning there is overlap
        return ret


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