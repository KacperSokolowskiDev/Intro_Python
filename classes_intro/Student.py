class Student:  # defines what a student is, a template

    # Initialized function
    # storing info about the student
    # exemple : self.name = name => the name of the student object is gonna be equal to the name value
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
