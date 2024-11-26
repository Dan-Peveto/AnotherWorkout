
from collections import UserString
import sqlite3
from models.util import Util
# To write and read from database

class UserDatabaseManager:
         
    # method to save
    @staticmethod
    def save(userInput):
        user = userInput.upper()
        print("Saving User")
        #establish connection 
        connection = sqlite3.connect('users.db')
        # create cursor variable to allow database interaction
        cursor = connection.cursor()
        # Create user table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS  users (
            userName TEXT PRIMARY KEY, -- Primary key (unique)
            fName TEXT NOT NULL,
            lName TEXT NOT NULL,
            startingWeight INTEGER NOT NULL,
            userWeight INTEGER NOT NULL
        )
   """, )
        
        cursor.execute(""" 
            INSERT OR REPLACE INTO users (userName, fName, lName, startingWeight, userWeight)
            VALUES (?, ?, ?, ?, ?)
        """, (user.userName, user.fName, user.lName, user.startingWeight, user.userWeight))
        
        # Commit the transaction and close the connection 
        connection.commit()
        connection.close()
        Util.clearScreen(3)
        
        
        
    # Method to load
    @staticmethod    
    def load(userNameInput):
        userName = userNameInput.upper()
        # establish connection 
        connection = sqlite3.connect('users.db')
        # create cursor variable to allow database interaciton 
        cursor = connection.cursor()
        
        # query to select user by userName
        cursor.execute("""
            SELECT userName, fName, lName, startingWeight, userWeight
            FROM Users 
            WHERE userName = ?
        """, (userName,))
        
        # Fetch one record
        row = cursor.fetchone()
        
        # close the connection 
        connection.close()
        
        #check if the user was found
        
        if row:
            # unpack the row data in variables and return the user data
            userName, fName, lName, startingWeight, userWeight = row
            return {
                'userName': userName,
                'fName': fName,
                'lName': lName, 
                'startingWeight': startingWeight,
                'userWeight': userWeight
            }
        else:
            # return None if the user is not found
            return None


    # Method checks database for userName and returns true if found
    @staticmethod
    def checkUserName(userNameInput):
        userName = userNameInput.upper()
        #establish connection 
        connection = sqlite3.connect("users.db")
        # Create cursor variable to allow database interaction
        cursor = connection.cursor()
        #query to check if the userName exists
        cursor.execute("""
            SELECT userName FROM users WHERE userName = ?
        """, (userName,))
        # Fetch one record
        result = cursor.fetchone()
        #close connection 
        connection.close()
        # return true if a user with that userName exist, otherwise False
        return result is not None
        
    #Method to clear database Used for testing purposes
    def clearDatabase():
        print("Preparing to clear the Database.")
        print("Please press 1 to continue with deletion or press any other key to exit")
        userSelection = input("User Selection: ")
        if userSelection == "1":
            Util.clearScreen(1)
            print("You have chosen to delete the entire database...no going back now")
            #establish connection 
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            # Execute the DELETE statement to clear the table
            cursor.execute("DLETE FROM users")
            # Commit and Close
            connection.commit()
            connection.close()
            print("Database cleared successfully.")
        else:
            pass

    








# TODO: Add check of database so that no two username's are created  