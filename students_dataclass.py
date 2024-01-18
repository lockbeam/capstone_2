from dataclasses import dataclass

@dataclass
#decorator
class Student:
    # new for python defining and setting variable type
    name: str
    college_id: int
    gpa: float

    #optional if you want to modify output to override print format
    #otherwise printing would look like
    #Student(name='Alice, college_id=123987, gpa=3.11)
    def __str__(self):
        return f'Name {self.name}, GPA: {self.gpa}'

def main():

    alice = Student('Alice', 123987, 3.11)
    bobbet = Student('Bobbet', 654258, 2.08)

    print(alice)
    print(alice.college_id)
    print(bobbet)
    print(bobbet.name)

main()