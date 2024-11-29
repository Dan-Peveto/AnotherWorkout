# Imports
import sqlite3
import csv
from models.util import Util

# Class contains logic for saving exercises 
class ExerciseDatabaseManager:

    # Method to save 
    @staticmethod
    def saveExercise(exerciseClass):
        # Establish Connection 
        conn = sqlite3.connect('AnotherWorkoutDatabase.db')
        try: 
            # Create cursor 
            cur = conn.cursor()
            # Create Exercise Table
            cur.execute(""" 
            CREATE TABLE IF NOT EXISTS exercises (
                exerciseName TEXT PRIMARY KEY, -- Primary Key (unique)
                targetAreaTags TEXT NOT NULL, 
                isAnaerobic INTEGER NOT NULL -- Store booleans as integers
                )
            """)
            # stringify list prior to saving
            targetAreaTagsStr = ','.join(exerciseClass.targetAreaTags)
            # Create execute demand for incoming data 
            cur.execute(""" 
                INSERT OR REPLACE INTO exercises (exerciseName, targetAreaTags, isAnaerobic)
                VALUES (?, ?, ?)
                """, (exerciseClass.exerciseName, targetAreaTagsStr, int(exerciseClass.isAnaerobic)))
            
            # Commit
            conn.commit()
        # Error handling for database error
        except sqlite3.Error as e:
            print(f"Database error occurred {e}")
        # Error handling for nonDatabase error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            #close the dB
            conn.close()


    # Method to load
    @staticmethod
    def loadUser(exerciseName):
        #Establish Connectino 
        conn = sqlite3.connect('AnotherWorkoutDatabase.db')
        # Create cursor
        cur = conn.cursor()

        # query to select exercise by exercise name
        cur.execute(""" 
            SELECT exerciseName, targetAreaTags, isAnaerobic
            FROM exercises
            WHERE exerciseName = ?           
            """, (exerciseName))
        
        # Fetch one record
        row = cur.fetchone()

        # Close the connection 
        conn.close()
        # If row found an exercise
        if (row):
            # Unpack and return a dictionary 
            exerciseName, targetAreaTags, isAnaerobic = row
            # Convert back to list
            targetAreaTagsList = targetAreaTags.split(",")
            return {
                'exerciseName': exerciseName,
                'targetAreaTags': targetAreaTagsList,
                'isAnaerobic': bool(isAnaerobic)
            }

    def massLoadFromCSV(CSVFilePath):
        # Create Connection 
        conn = sqlite3.connect("AnotherWorkoutDatabase.db")
        # Try connection
        try:
            cur = conn.cursor()
            cur.execute(""" 
            CREATE TABLE IF NOT EXISTS exercises(
                exerciseName TEXT PRIMARY KEY, -- Primary Key (unique)
                targetAreaTags TEXT NOT NULL,
                isAnaerobic INTEGER NOT NULL -- Store booleans as integers
            )
            """)
            # Open the CSV File 
            with open(CSVFilePath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    exerciseName = row['exerciseName']
                    # convert the comma-sepearted string to a list and then back to a comma seperated string
                    targetAreaTags = row['targetAreaTags']
                    # convert CSV string to int 
                    isAnaerobic = int(row[isAnaerobic])
                    # Add it to the database
                    cur.execute(""" 
                        INSERT OR REPLACE INTO exercises (exerciseNae, targetAreaTags, isAnaerobic)
                        VALUES (?, ?, ?)
                    """, (exerciseName, targetAreaTags, isAnaerobic))
            # Committ and Let me know
            conn.commit()
            print(f"Successfully imported exercises from {CSVFilePath}")
        # Error handeling for fiel not found
        except FileNotFoundError:
            print(f"File {CSVFilePath} not found. Please verify the filepath is correct")
        # Error handeling for database
        except sqlite3.Error as e:
            print(f"Database error occurredL {e}")
        # Error handling for nonDatabase error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            #close the dB
            conn.close()

    def printTable():
        # establish connection
        conn = sqlite3.connect("AnotherWorkoutDatabase.db")
        # make cursor
        cur = conn.cursor()
        # iterate over each row 
        cur.execute("SELECT * FROM exercises")
        rows = cur.fetchall()
        for index, row in enumerate(rows, start=1):
            print(f"Exercise {index}: {row[0]}")
        # Print "Number of rows: {count}"
        print(f"Total Exercises Saved: {len(rows)}")