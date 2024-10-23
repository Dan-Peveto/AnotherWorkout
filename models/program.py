class User:
     def __init__(self, programName):
         self.programName = programName
        
class Workout:
    list_exercises = []
    def __init__(self, exercise, cal_out, time):
         self.exercise = exercise
         self.cal_out = cal_out
         self.time = time

    def cal_burned(self, total):
        self.total = self.cal_out * total
        print(self.total)
        
sprint = Workout(exercise="sprint",cal_out=100,time=1)
walk = Workout(exercise="walk",cal_out=50,time=2)

def additional_exercise(): 
    while True:
        choice = input("please input workout activity:")
        Workout.list_exercises.append(choice.strip())
        for item in Workout.list_exercises:
            print(item,end=" ")        
        break

if __name__ == '__main__':
    print(f'your exercise is {walk.exercise} and you will burn {walk.cal_out} calories')