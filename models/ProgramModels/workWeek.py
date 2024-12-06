from models.program_models.workout import Workout

class WorkWeek:
    # Init method will take in a dictionary of seven dictionaries list as such: { week 1 : { movement 1 : [exercise_name, reps, sets]}} Off days will be signified as empty lists
    def __init__(self, program_dict):
        if not isinstance(program_dict, dict):
            raise TypeError("program_dict must be a dictionary")
        self.program_dict = program_dict
        self.work_week_dict = {}

    def make_work_week(self):
        # Take in a dictionary with seven keys (one for each day) and the value is a list to create a workout instance
        work_week_dict = self.work_week_dict
        day_count = 1  # Key to keep track of the week
        # For each key make a workout instance
        for key in self.program_dict:
            # Create an instance of workout for each movement stored at each week
            workout = Workout(self.program_dict[key])
            workout.make_workout()  # Call make_workout
            # Push new instances onto the return dictionary with each day as a key
            work_week_dict[day_count] = workout
            day_count += 1
        

    
    
    
    