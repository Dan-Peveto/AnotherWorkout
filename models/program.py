class User:
     def __init__(self, programName):
         self.programName = programName
#define workout exercies, how many calories burned and for what duration using a class, storing it in list_exercises
class Workout:
    def __init__(self, name, cal_out, time):
         self.name = name
         self.cal_out = cal_out
         self.time = time

    #finding total calories burned per minute
    def cal_burned(self):
        self.total = self.cal_out * self.time
        print(self.total)

    #assign userinput to belong to class
    @classmethod
    def userinput(cls):
        name = input("Enter exercise name: ")
        duration = int(input("Enter duration in minutes: "))
        intensity = input("Enter intensity (low, medium, high): ")

    def display_workout(self):
        print(f"Exercise name: {self.name}")
        print(f"Duration: {self.time} minutes")
        print(f"calories burned {self.total}")



if __name__ == '__main__':
    list_exercises = []
    while True:
        name = Workout.userinput()
        list_exercises.append(name)

        more = input("Would you like to add another exercise? (y/n): ")
        if more.lower != 'y':
            break


    for ex in list_exercises:
        ex.display_workout()