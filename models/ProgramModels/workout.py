
class Workout:

    def __init__(self, exerciseList):
        if not isinstance(exerciseList, dict):
            raise TypeError("exerciseDict must be a dictionary") #{Day 1: [exerciseName, reps, sets] Day 2: ...}
        self.exerciseList = exerciseList
                