
class WorkWeek:
    # Init Method will take in a list of seven list as such [[exerciseName, sets, reps] ... ] index 1 = day 1...Off days will be signified as empty lists
    def __init__(self, programList):
        if not isinstance(programList, list):
           raise TypeError("List must be a list")
        self.programList = programList
        # Build 7 variables that are dictionaries for each workout if the workout is a skip create dictionary that is {skip: Random Quote}...Connect to random quote genorator API
        day1 = programList[0]
        day2 = programList[1]
        day3 = programList[2]
        day4 = programList[3]
        day5 = programList[4]
        day6 = programList[5]
        day7 = programList[6]

        

    
    
    
    