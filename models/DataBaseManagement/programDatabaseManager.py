# Imports
import json

'''
    program_database_manager will use a nested dictionary of dictionaries with the program name key used as the key to return all the specific program:
    ie
    { 
        air_force : {week_1 : {day_1: { movement_1: 
                                         movement_2: 
                                         }
                            day_2: 
                                    } 
                      week_2 : 
                    }
        marines : {}
    }
'''

# Class to save a program 
class ProgramDatabaseManager:
    
    # Save the input dict
    @staticmethod
    def save_program_instructions(program_instructions_dict):
        # Save to JSON using with open 
        with open("program_database.json", "w") as f:
            json.dump(program_instructions_dict, f)

    # Load the dictionary and return the key 
    @staticmethod
    def load_program_instructions(program_name):
        # Load JSON 
        with open("program_database.json", "r") as f:
            loaded_dict = json.load(f)
        # iterate through the loaded dictionary
        for key in loaded_dict:
            # if key matches 
            if key == program_name:
                # return the dictionaries at that key    
                return loaded_dict[key]