# Class for exercise
class Exercise:
    # Initialize class
    def __init__(self, exercise_name, target_area_tags, is_anaerobic):
        self.exercise_name = exercise_name  # String for name 
        if not isinstance(target_area_tags, list):
            raise ValueError("target_area_tags must be a list")
        self.target_area_tags = target_area_tags  
        if not isinstance(is_anaerobic, bool):
            raise ValueError("is_anaerobic must be a boolean value")
        self.is_anaerobic = is_anaerobic

    # Method to add a single tag
    def add_single_tag(self, tag):
        # Ensure type
        if not isinstance(tag, str):
            raise ValueError("tag must be a string")
        self.target_area_tags.append(tag)
    
    # Method to add a list of tags
    def add_tag_list(self, tag_list):
        # Ensure that we have the right type passed
        if not isinstance(tag_list, list):
            raise ValueError("tag_list must be a list")
        self.target_area_tags.extend(tag_list)

    # Print to console
    def print_exercise(self):
        print(f"{self.exercise_name}:")
        print(self.target_area_tags)
        if self.is_anaerobic:
            print("Strength")
        else:
            print("Conditioning")