# Imports
from models.ProgramModels.work_week import WorkWeek

class Program:
    # Create program class
    def __init__(self, instruction_dict):  # instruction_dict will be {week_1: [list of list with instructions for the workout week class]}
        if not isinstance(instruction_dict, dict):
            raise TypeError("instruction_dict must be a dictionary")
        self.instruction_dict = instruction_dict
        self.program_dict = {}

    # Take the instruction dict and iterate over it and return as many instances of work_week as there are keys for dict
    def make_program(self):
        # Make the dictionary names easier to read
        instruction_dict = self.instruction_dict
        program_dict = self.program_dict
        week_count = 1
        # For each key in instruction_dict
        for key in instruction_dict:
            # Make instance of work_week for each key passing the values to the constructor
            work_week = WorkWeek(instruction_dict[key])
            # Call make work_week
            work_week.make_work_week()
            # Add to dictionary
            program_dict[week_count] = work_week
            # Increment week_count
            week_count += 1