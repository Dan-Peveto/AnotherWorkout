
# utilitiy class
class Util:
    
    # clear screen class
    @staticmethod
    def clearScreen(waitTime):
        import os, time
        if os.name == "nt":
            time.sleep(waitTime)
            os.system("cls")
        else:
            time.sleep(waitTime)
            os.system("clear")
         
    @staticmethod
    def tryAgain(methodOne, methodTwo):
        while True:
            print("Select 1 to try again")
            print("Select 2 to return to main menu")
            userSelection = input("Your selection: ")
            if userSelection == "1":
                methodOne()
                return 
            if userSelection == "2":
                methodTwo()
                return
            else:
                print("Invalid selection Please Try Again")