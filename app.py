"""
Welcome to Bastard Training Workout App:

This is a coding project to produce a functioning app that will allow the user to plan future workouts, record past workouts, and analyze GAINZ.
This coding project has four phases:

Phase 1 (Initial Code): The object of phase one is to create a fully functioning console app that allows users to:
    - Create user profile
    - Create customized workout plan
    - Record workouts in real time
    - Pull history of workouts
    TODO: 
        Build at least 2 premade programs and store in database
        Build logic to save from CSV 
    TODO:
        Create a link between User and a specific program they have chosen 
    TODO:
        Build UserInterface class

Phase 2 (App Refinement): The object of phase two is to refine the initial app to allow the user the following:
    - Create premade workouts
    - Create Database functionality to track user progress and display progress to the user
    
Phase 3 (Limited Deployment): The object of phase three is to generate UI using Django. After this phase, the user will be able to:
    - Log into the online application
    - Set a profile picture
    - Interact with all functions created in the console app
    
Phase 4 (Phone Deployment): The final phase is to allow users to interact with the app on a smartphone
"""

from models.user_models.user_manager import UserManager  # Import UserManager
from models.program_models.exercise import Exercise  # Import Exercise
from models.database_management.exercise_database_manager import ExerciseDatabaseManager  # Import ExerciseDatabaseManager
from models.program_models.work_week import WorkWeek
from models.program_models.program import Program

# To enter app, call UserManager.welcome_user()

"""
# Create instance of Exercise and print
name = "PUSH-UP"
target_area_tags = ["Chest", "Triceps", "Core"]
is_anaerobic = True

pushup = Exercise(name, target_area_tags, is_anaerobic)
ExerciseDatabaseManager.save_exercise(pushup)
ExerciseDatabaseManager.print_table()
"""
# Test save method // Test good
# Load method // Test good
# Print method // Test good

"""exercise_dict = ExerciseDatabaseManager.load_user(['PUSH-UP']) 
loaded_exercise = Exercise(exercise_dict['exercise_name'], exercise_dict['target_area_tags'], exercise_dict['is_anaerobic'])
loaded_exercise.print_class()"""

# csv_file = r"C:\Users\Danie\source\PythonProjects\WorkoutApp\CompanionFiles\MassExerciseUpload.CSV"

# Mass save from CSV method

ExerciseDatabaseManager.print_table()

# Make workout_list for use in test
workout_week_dict = {
    "week_1": {"day_1": {"movement_1": ["push-ups", ["Chest", "Arms"], False]}},
    "week_2": {"day_2": {"movement_2": ["squats", ["Legs", "Core"], False]}},
    "week_3": {"day_3": {"movement_3": ["jog", ["Legs", "Soul"], True]}}
}

# Create class instance
test_workout = Program(workout_week_dict)

# Call make_workout method
test_workout.make_program()
print(test_workout.program_dict)