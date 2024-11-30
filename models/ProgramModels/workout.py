
class Workout:

    def __init__(self, exerciseDict ):
        if not isinstance(exerciseDict, dict):
            raise TypeError("exerciseDict must be a dictionary") #{Day 1: [exerciseName, reps, sets] Day 2: ...}
        self.exerciseDict = exerciseDict 
                