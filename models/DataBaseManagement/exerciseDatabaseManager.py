# Imports
import sqlite3
import csv
# TODO: Create error handling if key is not correct

# Class contains logic for saving exercises
class ExerciseDatabaseManager:

    # Method to save 
    @staticmethod
    def save_exercise(exercise_class):
        # Establish Connection 
        conn = sqlite3.connect('another_workout_database.db')
        try: 
            # Create cursor 
            cur = conn.cursor()
            # Create Exercise Table
            cur.execute(""" 
            CREATE TABLE IF NOT EXISTS exercises (
                exercise_name TEXT PRIMARY KEY, -- Primary Key (unique)
                target_area_tags TEXT NOT NULL, 
                is_anaerobic INTEGER NOT NULL -- Store booleans as integers
                )
            """)
            # stringify list prior to saving
            target_area_tags_str = ','.join(exercise_class.target_area_tags)
            # Create execute demand for incoming data 
            cur.execute(""" 
                INSERT OR REPLACE INTO exercises (exercise_name, target_area_tags, is_anaerobic)
                VALUES (?, ?, ?)
                """, (exercise_class.exercise_name, target_area_tags_str, int(exercise_class.is_anaerobic)))
            
            # Commit
            conn.commit()
        # Error handling for database error
        except sqlite3.Error as e:
            print(f"Database error occurred {e}")
        # Error handling for non-database error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Close the DB
            conn.close()


    # Method to load
    @staticmethod
    def load_exercise(exercise_name):
        # Establish Connection 
        conn = sqlite3.connect('another_workout_database.db')
        # Create cursor
        cur = conn.cursor()

        # Query to select exercise by exercise name
        cur.execute(""" 
            SELECT exercise_name, target_area_tags, is_anaerobic
            FROM exercises
            WHERE exercise_name = ?           
            """, (exercise_name,))
        
        # Fetch one record
        row = cur.fetchone()

        # Close the connection 
        conn.close()
        # If row found an exercise
        if row:
            # Unpack and return a dictionary 
            exercise_name, target_area_tags, is_anaerobic = row
            # Convert back to list
            target_area_tags_list = target_area_tags.split(",")
            return [exercise_name, target_area_tags_list, bool(is_anaerobic)]

    @staticmethod
    def mass_load_from_csv(csv_file_path):
        # Create Connection 
        conn = sqlite3.connect("another_workout_database.db")
        # Try connection
        try:
            cur = conn.cursor()
            cur.execute(""" 
            CREATE TABLE IF NOT EXISTS exercises(
                exercise_name TEXT PRIMARY KEY, -- Primary Key (unique)
                target_area_tags TEXT NOT NULL,
                is_anaerobic INTEGER NOT NULL -- Store booleans as integers
            )
            """)
            # Open the CSV File 
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    exercise_name = row['exerciseName']
                    # Convert the comma-separated string to a list and then back to a comma-separated string
                    target_area_tags = row['targetAreaTags']
                    # Convert CSV string to int 
                    is_anaerobic = int(row['isAnaerobic'])
                    # Add it to the database
                    cur.execute(""" 
                        INSERT OR REPLACE INTO exercises (exercise_name, target_area_tags, is_anaerobic)
                        VALUES (?, ?, ?)
                    """, (exercise_name, target_area_tags, is_anaerobic))
            # Commit and let me know
            conn.commit()
            print(f"Successfully imported exercises from {csv_file_path}")
        # Error handling for file not found
        except FileNotFoundError:
            print(f"File {csv_file_path} not found. Please verify the filepath is correct")
        # Error handling for database
        except sqlite3.Error as e:
            print(f"Database error occurred: {e}")
        # Error handling for non-database error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Close the DB
            conn.close()

    @staticmethod
    def print_table():
        # Establish connection
        conn = sqlite3.connect("another_workout_database.db")
        # Create cursor
        cur = conn.cursor()
        # Iterate over each row 
        cur.execute("SELECT * FROM exercises")
        rows = cur.fetchall()
        for index, row in enumerate(rows, start=1):
            print(f"Exercise {index}: {row[0]}")
        # Print "Number of rows: {count}"
        print(f"Total exercises saved: {len(rows)}")