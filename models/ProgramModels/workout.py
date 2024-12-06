from models.ProgramModels.exercise import Exercise
from models.DataBaseManagement.exercise_database_manager import ExerciseDatabaseManager

class Workout:

    def __init__(self, exercise_dict):
        if not isinstance(exercise_dict, dict):
            raise TypeError("exercise_dict must be a dictionary")  # {movement_1: [exercise_name, reps, sets] }
        self.exercise_dict = exercise_dict
        self.workout_dict = {}

    # Make as many instances of exercise as size of exercise_dict and return dict with each key containing an instance of exercise
    def make_workout(self):
        # Create return dictionary
        exercise_dict = self.exercise_dict  # The input dictionary with instructions to create an exercise
        workout_dict = self.workout_dict  # The return dictionary with instructions to create a workout
        movement_number = 1
        # For each key in exercise_dict
        for key in exercise_dict:
            # Name the list for readability
            movement_list = exercise_dict[key]
            # Load the exercise from the database using the first element as the key
            loaded_exercise_list = ExerciseDatabaseManager.load_exercise(movement_list[0])
            # Create instance of exercise using the loaded_exercise_list
            exercise = Exercise(loaded_exercise_list[0], loaded_exercise_list[1], loaded_exercise_list[2])
            # Add to dictionary movement_number: Instance of Exercise, Reps, Sets
            workout_dict[movement_number] = exercise, movement_list[1], movement_list[2]
            movement_number += 1

        
    



        

                