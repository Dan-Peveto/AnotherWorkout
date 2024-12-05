# Imports
from models.ProgramModels.workWeek import WorkWeek

class Program:
    # create program class
    def __init__(self, instructionDict): # instruction Dict will be {Week1: [list of list with instuctions for the workout week class]}
        if not isinstance(instructionDict, dict):
            raise TypeError("instructionDict must be a Dictionary")
        self.instructionDict = instructionDict
        self.programDict = {}

    # Take the instruction dict and iterate over it and return as many instances of workWeek as there are keys for dict

    def makeProgram(self):
        # make the dictionary names easier to read
        instructionDict = self.instructionDict
        programDict = self.programDict
        weekCount = 1
        # For each key in instructionDict
        for key in instructionDict:
            # Make instance of workweek for each key passing the values to the constructor
            workWeek = WorkWeek(instructionDict[key])
            #  call make workWeek
            workWeek.makeWorkWeek()
            # Add to dictionary
            programDict[weekCount] = workWeek
            # increment weekCount
            weekCount += 1
        
    


