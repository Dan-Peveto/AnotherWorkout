import sqlite3
# To write and read from database

class UserDatabaseManager:
    # method to save
    @staticmethod
    def save(user):
        #establish connection 
        connection = sqlite3.connect('users.db')\
        # create cursor variable to allow database interaction
        cursor = connection.cursor()
        # Create user table
        cursor.execute("""
        CREATE TALE IF NOT EXISTS  users (
            userName """, )