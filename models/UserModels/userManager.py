# TODO: add clear screen methods across Class for screen readability

# Class allows user to manage actions ie create user, update user, etc.
class UserManager:
    
    def with_user_manager():
        print("Hello I am the user manager")
    
    @staticmethod
    # TODO: Place in Util.try_again
    def welcome_user():
        # Welcome Screen = 1. Make User 2. Load User   
        while True:   
  
            # Print Welcome Statement
            print("Welcome to Just Another Workout App")
            print("1. Create New User")
            print("2. Load Existing user")
            # user selection
            user_selection = int(input("Your Selection: "))
            # If not a 1 or a 2
            if user_selection != 1 and user_selection != 2: 
                Util.clear_screen(1)
                print("**Incorrect input**")
            else:
                # If one create new user 
                if user_selection == 1:
                    new_user = UserManager.create_user()
                    print(f"You have created {new_user.first_name} {new_user.last_name}")
                    # Launch user portal
                # otherwise load user
                else:
                    user = UserManager.load_user()
                    # print user for testing purposes
                    user.print_user_info()
                    
    def create_user():
        # Gather Info for New User
        
        while True:
            user_name = input("User Name: ")
            Util.clear_screen(1)
            duplicate_name = UserDatabaseManager.check_user_name(user_name)
            if duplicate_name:
                print(f"{user_name} is already taken.")
                print("Please try input a different username")
            else:
                break
        # TODO: Ensure that user_name is not a duplicate
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        while True:
            starting_weight = input("Starting Weight: ")
            try:
                starting_weight_number = int(starting_weight)
                break
            except ValueError:
                print("Invalid input! Please enter an integer for your starting weight")
        
        # create and save user
        user_weight = starting_weight_number        
        user = User(user_name, first_name, last_name, starting_weight_number, user_weight)
        # TODO Save User
        UserDatabaseManager.save(user)
        return user
        
    # load user
    def load_user():
        # Ask for user name 
        while True:
            user_name_input = input("Please enter your userName: ")
            user_name = user_name_input.upper()
            # Check that user_name exists 
            correct_name = UserDatabaseManager.check_user_name(user_name)
            # If yes Great!
            if correct_name: 
                user_data = UserDatabaseManager.load(user_name)
                if user_data:
                    user = User(
                        user_name=user_data['user_name'],
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name'],
                        starting_weight=user_data['starting_weight'],
                        user_weight=user_data['user_weight']
                    )   
                    return user
            # If user_name does not exist ask again or let user escape back to main menu
            else:
                method_one = UserManager.load_user
                method_two = UserManager.welcome_user
                Util.try_again(method_one, method_two)
        
    @staticmethod
    def user_portal(user_name):
        pass
        # load user
        # Give user options
                    
            

    
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

