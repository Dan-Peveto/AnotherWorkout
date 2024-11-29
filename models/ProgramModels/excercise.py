# Class for excercise
class Excercise:
    # initialize class
    def __init__(self, name, targetAreaTag, isAnaerobic: bool):
        self.name = name; # String for name 
        if not isinstance(targetAreaTag, list):
            raise ValueError("targetAreaTag must be a list")
        self.targetAreaTag = targetAreaTag; # String for 
        if not isinstance(isAnaerobic, bool):
            raise ValueError("isAnaerobic must be a boolean value")
        self.isAnaerobic = isAnaerobic;

    # Print to console
    def printClass(self):
        print(f"{self.name}:")
        for tag in self.targetAreaTag:
            print(tag)
        if (self.isAnaerobic):
            print("Strength")
        else:
            print("Conditioning")