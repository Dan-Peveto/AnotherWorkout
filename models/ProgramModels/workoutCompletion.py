# Class for individual workouts
class WorkoutCompletion:
    def __init__(self, name, cal_out, time):
        self.name = name
        self.cal_out = cal_out
        self.time = time
        self.total = 0  # Initialize total calories burned

    def cal_burned(self):
        self.total = self.cal_out * self.time