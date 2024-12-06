# Utility class
class Util:
    
    # Clear screen class
    @staticmethod
    def clear_screen(wait_time):
        import os, time
        if os.name == "nt":
            time.sleep(wait_time)
            os.system("cls")
        else:
            time.sleep(wait_time)
            os.system("clear")
         
    @staticmethod
    def try_again(method_one, method_two):
        while True:
            print("Select 1 to try again")
            print("Select 2 to return to main menu")
            user_selection = input("Your selection: ")
            if user_selection == "1":
                method_one()
                return 
            if user_selection == "2":
                method_two()
                return
            else:
                print("Invalid selection. Please try again.")
