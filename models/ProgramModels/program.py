
class Program:
    # create program class
    def __init__(self, instanceName, instructionDict): # instruction Dict will be {Week1: [list of list with instuctions for the workout week class]}
        self.instanceName = instanceName
        if not isinstance(instructionDict, dict):
            raise TypeError("instructionDict must be a Dictionary")
        self.programList = []
        # use diction to create the list
        for key in instructionDict:
            self.programList.append(key, instructionDict[key])
    
    # Methods
    def lengthOfProgram(self):
        # use the length of the program list to determine how long the program is
        print("lengthOfProgram")
    


