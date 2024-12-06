class User:
    
    # constructor with user_name, first_name, last_name, starting_weight
    @staticmethod
    def speak_here():
        print("The user is here")

    def __init__(self, user_name: str, first_name: str, last_name: str, starting_weight: int, user_weight: int):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.starting_weight = starting_weight
        self.user_weight = user_weight
        # Check that starting_weight is an integer
        if not isinstance(starting_weight, int):
            raise TypeError(f"Weight must be an integer, got {type(starting_weight).__name__}")
        if not isinstance(user_weight, int):
            raise TypeError(f"Weight must be an integer, got {type(user_weight).__name__}")
    
    # Method that updates the user_weight with the weight change percentage
    def update_weight(self):
        # wrap input in check to ensure input is an int
        while True:
            try:
                # ask user their weight
                input_weight = input("What is your new weight? ")
                weight = int(input_weight)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        # update the variable
        self.user_weight = weight
    
    # Display user information
    def print_user_info(self):
        print(f"User Name: {self.user_name} \nWeight: {self.user_weight} \nStarting Weight: {self.starting_weight}")