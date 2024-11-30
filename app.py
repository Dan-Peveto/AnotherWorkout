"""
Well come to Bastard Training Workout App:

This is a coding project to produce a functioning app that will allow the user to plan future workouts, record past workouts, and analyze GAINZ
This coding project has four phases

Phase 1 (Initial Code): The object of phase one is to create a fully functioning console app that allows users to:
    - Create user profile
    - Create customized workout plan
    - Record workouts in real time
    - Pull history of workouts
    TODO: 
        Build at least 2 premade programs and store in database
        Build logic to save from CSV 
    TODO:
        Create a link between User and a Specific Program they have chosen 
    TODO:
        Build UserInterface class


        
Phase 2 (App Refinement): The object of phase two is to refine the initial app to allow user the following:
    - Create premade workouts
    - Create Database functionality to track user progress and display progress to the user
    
Phase 3 (Limited Deployement): The object of phase three is to generate UI using Django. After this phase the user will be able to:
    - Log into the online application
    - Set a profile picture
    - Interact with all functions created in the console App
    
Phase 4 (Phone Deployement): The final phase is to allow users to interact with the app on a smartphone
 """

from models.UserModels.userManager import UserManager # Import UserManager
from models.ProgramModels.exercise import Exercise # Import Exercise
from models.DataBaseManagement.exerciseDatabaseManager import ExerciseDatabaseManager # Import ExerciseDatabaseManager



# To Enter App UserManager.welcomeUser()
"""
# Create Instance of Exercise and print
name =  "PUSH-UP"
targetAreaTags = ["Chest", "Triceps", "Core"]
isAnaerobic = True

pushup = Exercise(name, targetAreaTags, isAnaerobic)
ExerciseDatabaseManager.saveExercise(pushup)
ExerciseDatabaseManager.printTable()
"""
# Test Save Method // Test Good
#Load Method // Test Good
#Print Method // Test Good

"""exerciseDict = ExerciseDatabaseManager.loadUser(['PUSH-UP']) 
loadedExercise = Exercise(exerciseDict['exerciseName'], exerciseDict['targetAreaTags'], exerciseDict['isAnaerobic'])
loadedExercise.printClass()"""

csvFile = r"C:\Users\Danie\source\PythonProjects\WorkoutApp\CompanionFiles\MassExerciseUpload.CSV"

#Mass save from CSV Method

ExerciseDatabaseManager.printTable();
