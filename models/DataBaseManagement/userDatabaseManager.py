import sqlite3
from models.util import Util
# To write and read from database

# Class with static methods for saving and loading users
class user_database_manager:
    
    # method to save
    @staticmethod
    def save_user(user_class):
        
        # establish connection
        connection = sqlite3.connect('another_workout_database.db')
        # Try
        try:
            # create cursor variable to allow database interaction
            cursor = connection.cursor()
            # Create user table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_name TEXT PRIMARY KEY, -- Primary key (unique)
                f_name TEXT NOT NULL,
                l_name TEXT NOT NULL,
                starting_weight INTEGER NOT NULL,
                user_weight INTEGER NOT NULL
                )
            """)
        
            cursor.execute(""" 
                INSERT OR REPLACE INTO users (user_name, f_name, l_name, starting_weight, user_weight)
                VALUES (?, ?, ?, ?, ?)
                """, (user_class.user_name, user_class.f_name, user_class.l_name, user_class.starting_weight, user_class.user_weight))
        
            # Commit the transaction and close the connection
            connection.commit()

        except sqlite3.Error as e:
            print(f"Database error occurred: {e}")
        # Error handling for non-database error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            connection.close()
        
        
    # Method to load
    @staticmethod    
    def load_user(user_name):
        # establish connection
        connection = sqlite3.connect('another_workout_database.db')
        # create cursor variable to allow database interaction
        cursor = connection.cursor()
        
        # query to select user by user_name
        cursor.execute("""
            SELECT user_name, f_name, l_name, starting_weight, user_weight
            FROM users 
            WHERE user_name = ?
        """, (user_name,))
        
        # Fetch one record
        row = cursor.fetchone()
        
        # close the connection
        connection.close()
        
        # check if the user was found
        if row:
            # unpack the row data in variables and return the user data
            user_name, f_name, l_name, starting_weight, user_weight = row
            return {
                'user_name': user_name,
                'f_name': f_name,
                'l_name': l_name, 
                'starting_weight': starting_weight,
                'user_weight': user_weight
            }
        else:
            # return None if the user is not found
            return None


    # Method checks database for user_name and returns true if found
    @staticmethod
    def check_user_name(user_name_input):
        user_name = user_name_input.upper()
        # establish connection
        connection = sqlite3.connect("another_workout_database.db")
        # Create cursor variable to allow database interaction
        cursor = connection.cursor()
        # query to check if the user_name exists
        cursor.execute("""
            SELECT user_name FROM users WHERE user_name = ?
        """, (user_name,))
        # Fetch one record
        result = cursor.fetchone()
        # close connection
        connection.close()
        # return true if a user with that user_name exists, otherwise False
        return result is not None
        
    # Method to clear database used for testing purposes
    def clear_database():
        print("Preparing to clear the database.")
        print("Please press 1 to continue with deletion or press any other key to exit")
        user_selection = input("User Selection: ")
        if user_selection == "1":
            Util.clear_screen(1)
            print("You have chosen to delete the entire database...no going back now")
            # establish connection
            connection = sqlite3.connect("another_workout_database.db")
            cursor = connection.cursor()
            # Execute the DELETE statement to clear the table
            cursor.execute("DELETE FROM users")
            # Commit and Close
            connection.commit()
            connection.close()
            print("Database cleared successfully.")
        else:
            pass