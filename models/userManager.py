
from models import userDatabaseManager
from models.user import User
from models.util import Util
from models.userDatabaseManager import UserDatabaseManager

#TODO: add clear screen methods across Class for screen readability

# Clas allows user to manage actions ie create user update user etc.
class UserManager:
    
    def withUserManager():
        print("Hello I am the userManager")
    
    @staticmethod
    #TODO Place in Util.tryAgain
    def welcomeUser():
        # Welcom Screen = 1. Make User 2. Load User   
        while True:    
            # Print Welcome Statement
            print("Welcome to Just Another Workout App")
            print("1. Create New User")
            print("2. Load Existing user")
            #user selection
            userSelection = int(input("Your Selection: "))
            # If not a 1 or a 2
            if userSelection != 1 and userSelection != 2: 
                Util.clearScreen(1)
                print("**Incorrect input**")
            else:
                # If one create new user 
                if userSelection == 1:
                    newUser = UserManager.createUser()
                    print(f"You have created {newUser.fName} {newUser.lName}")
                    # Launch userPortal
                # otherwise load user
                else:
                    
                    user = UserManager.loadUser()
                    # print user for testing purpose
                    user.printUserInfo()
                    
                    
            

    
    def createUser():
        # Gather Info for New User
        
        while True:
            userName = input("User Name: ")
            Util.clearScreen(1)
            duplicateName = UserDatabaseManager.checkUserName(userName)
            if duplicateName:
                print(f"{userName} is already taken.")
                print("Please try input a different username")
            else:
                break
        # TODO: Ensure that userName is not a duplicate
        fName = input("First Name: ")
        lName = input("Last Name: ")
        while True:
            startingWeight = input("Starting Weight: ")
            try:
                startingWeightNumber = int(startingWeight)
                break
            except ValueError:
                print("Invalid input! Please enter an integer for your starting weight")
        
        # create and save user
        userWeight = startingWeightNumber        
        user = User(userName, fName, lName, startingWeightNumber, userWeight)
        #TODO Save User
        UserDatabaseManager.save(user)
        return user
        
        
        # load user
    def loadUser():
        # Ask for user name 
        while True:
            userNameInput = input("Please enter your userName: ")
            userName = userNameInput.upper()
            # Check that userName exist 
            correctName = UserDatabaseManager.checkUserName(userName)
            # If yes Great!
            if correctName: 
                userData = UserDatabaseManager.load(userName)
                if userData:
                    user = User(
                    userName = userData['userName'],
                    fName = userData['fName'],
                    lName = userData['lName'],
                    startingWeight = userData['startingWeight'],
                    userWeight = userData['userWeight']
                )   
                return user
                    
            # If userName does not exist ask again or let user escape back to main menue
            else:
                methodOne = UserManager.loadUser
                methodTwo = UserManager.welcomeUser
                Util.tryAgain(methodOne, methodTwo)
        
            
        
    

    @staticmethod
    def userPortal(userName):
        pass
        # load user
        # Give user options

