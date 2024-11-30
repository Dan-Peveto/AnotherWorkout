
class Program:
    # Init Method will take in a list of seven list as such [[exerciseName, sets, reps] ... ] index 1 = day 1...Off days will be signified as empty lists
    def __init__(self, programList):
        if not isinstance(programList, list):
           raise TypeError("inputList must be a list")
        self.programList = programList