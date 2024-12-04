# Class for excercise
class Exercise:
    # initialize class
    def __init__(self, exerciseName, targetAreaTags, isAnaerobic):
        
        self.exerciseName = exerciseName; # String for name 
        if not isinstance(targetAreaTags, list):
            raise ValueError("targetAreaTag must be a list")
        self.targetAreaTags = targetAreaTags; 
        if not isinstance(isAnaerobic, bool):
            raise ValueError("isAnaerobic must be a boolean value")
        self.isAnaerobic = isAnaerobic

    # Method to add tag 
    def addSingleTag(self, tag):
        # Ensure type
        if not isinstance(tag, str):
            raise ValueError("tag must be a string")
        self.targetAreaTags.append(tag);
    
    # Method to add a list of tags
    def addTagList(self, tagList):
        # Ensure that we have the right type passed
        if not isinstance(tagList, list):
            raise ValueError("tagList must be a list")
        self.targetAreaTags.extend(tagList)


    # Print to console
    def printExercise(self):
        print(f"{self.exerciseName}:")
        print(self.targetAreaTags)
        if (self.isAnaerobic):
            print("Strength")
        else:
            print("Conditioning")

            # name, targetAreaTags, isAnaerobic: bool