class Student:
    def __init__(self, name, school_id, gpa):
        #self is like this. in Java
        #it referes to the Object being initialized
        # name will become an instance variable in our student object
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        #this is for returning a string representation of an object
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA: {self.gpa}'

# python classes you don't list you variables or fields like in other languages
# very rare to write get and set methods in Python

#example student
alex = Student('Alex', 'a1b2c4', 3.4)
print(alex.name)
print(alex.school_id)
print(alex) #Student name: Alex, ID: a1b2c4

sam = Student('Sam', 'd3e5f0', 3.7)
print(sam)