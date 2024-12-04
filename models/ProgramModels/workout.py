from models.ProgramModels.exercise import Exercise
from models.DataBaseManagement.exerciseDatabaseManager import ExerciseDatabaseManager

class Workout:

    def __init__(self, exerciseDict):
        if not isinstance(exerciseDict, dict):
            raise TypeError("exerciseDict must be a dictionary") #{Movement 1: [exerciseName, reps, sets] }
        self.exerciseDict = exerciseDict
        self.workoutDict = {}
        

    # make as many instances of exercise as size fo exercise MDict and return dict with each key containing an instance of exercise 
    def makeWorkout(self):
        # Create return dictionary
        exerciseDict = self.exerciseDict # the input dictionary with instructions to create an exercise
        workoutDict = self.workoutDict # The return dictionary with instructions to create a workout
        movementNumber = 1
        # for each key in exercise dictionary 
        for key in exerciseDict:
            # name the list for readeability
            movementList  = exerciseDict[key]
            # Load the exercise from the database using the first element as the key 
            loadedExerciseList = ExerciseDatabaseManager.loadExercise(movementList[0])
            # Create instance of exercise using the loadedExerciseList
            exercise = Exercise(loadedExerciseList[0], loadedExerciseList[1], loadedExerciseList[2])
            # Add to dictioniry movementNumber : Instance of Exercise, Reps, Sets
            workoutDict[movementNumber] = exercise, movementList[1], movementList[2]
            movementNumber += 1
        # Return workoutDict
        return workoutDict
    



        

                