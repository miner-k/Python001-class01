




class Person(object):

    @classmethod
    def print(cls):
        print(cls)

class Student(Person):
    pass


Person.print()

Student.print()