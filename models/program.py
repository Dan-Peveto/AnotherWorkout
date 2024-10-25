class User:
    def __init__(self, programName):
        self.programName = programName

class Workout:
    def __init__(self, name, cal_out, time):
        self.name = name
        self.cal_out = cal_out
        self.time = time
        self.total = 0  # Initialize total calories burned

    def cal_burned(self):
        self.total = self.cal_out * self.time

    @classmethod
    def userinput(cls):
        name = input("Enter exercise name: ")
        duration = int(input("Enter duration in minutes: "))
        intensity = input("Enter intensity (low, medium, high): ")
        cal_out = {'low': 5, 'medium': 8, 'high': 12}[intensity.lower()]
        return cls(name, cal_out, duration)

    def display_workout(self):
        print(f"Exercise name: {self.name}")
        print(f"Duration: {self.time} minutes")
        print(f"Calories burned: {self.total}\n")

if __name__ == '__main__':
    list_exercises = []
    while True:
        workout = Workout.userinput()
        workout.cal_burned()  # Calculate calories burned
        list_exercises.append(workout)
        more = input("Would you like to add another exercise? (y/n): ")
        if more.lower() != 'y':
            break


    for ex in list_exercises:
        ex.display_workout()