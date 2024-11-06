


class User:
      
# constuctor with UserName, First Name, Last Name, Weight
    @staticmethod
    def speakHere():
       print("The user is here")
    def __init__(self, userName: str, fName: str, lName: str, startingWeight: int, userWeight: int):
      self.userName = userName
      self.fName = fName
      self.lName = lName
      self.startingWeight = startingWeight
      self.userWeight = userWeight
      # Check that startingweight is an intgit
      if not isinstance(startingWeight, int):
          raise TypeError(f"Weight must be an integer, got {type(startingWeight).__name__}")
      if not isinstance(userWeight, int):
         raise TypeError(f"Weight must be an integer, got {type(userWeight).__name__}")
 
    
    # Method that updates the userWeight the weight change percentage
    def updateWeight(self):
       # wrap input in check to ensure input is int
       while True:
          try:
             # ask user their weight
             inputWeight = input("What is your new weight? ")
             weight = int(inputWeight)
             break
          except ValueError:
             print("Invalid input! Please enter a valid integer.")
       #update the variable
       self.userWeight = weight
             
# Display User Information
    def printUserInfo(self):
      print(f"UserName: {self.userName} \nWeight: {self.userWeight} \nStarting Weight: {self.startingWeight}")  