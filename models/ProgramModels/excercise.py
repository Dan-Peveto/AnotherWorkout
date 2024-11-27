# Class for excercise
class Excercise:
    def __init__(self, name, targetArea, isAnaerobic: bool):
        self.name = name; # String for name 
        self.targetArea = targetArea; # String for 
        if not isinstance(isAnaerobic, bool):
            raise ValueError("isAnaerobic must be a boolean value")
        self.isAnaerobic = isAnaerobic;