
from  models.ProgramModels.workout import Workout

class WorkWeek:
    # Init Method will take in a dictionary of seven dictionaries list as such: { week 1 : { movement 1 : [exericeName, Reps, Sets]}} Off days will be signified as empty lists
    def __init__(self, programDict):
        if not isinstance(programDict, dict):
           raise TypeError("List must be a list")
        self.programDict = programDict
        self.workWeekDict = {}

    def makeWorkWeek(self):
        # Take in a dictionary with seven keys (one for each day) and the value is a list of to create a workout instance
        workWeekDict = self.workWeekDict
        weekCount = 1 # Key to keep track of week
        # For each key make a workout instance
        for key in self.programDict:
            # Create an instance of workout for each movement stored at each week
            workout = Workout(self.programDict[key])
            workout.makeWorkout
            # Push new instances onto return dictionary with each day a key
            workWeekDict[weekCount] = workout
            weekCount += 1
        # return dictionary
        return self.workWeekDict
        

    
    
    
    