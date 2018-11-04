class Student: 

    def __init__(self, name, major, gpa, is_on_probation): # student's data type. 'self' - it's referring to an actual object
        self.name = name  # the name of the student object is going to be = the name we passed in 
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
