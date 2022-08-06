# create a class Name and declare the __init__() and a method for printing the name

class Name:
    def __init__(self, fname, lname):   
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# use the Name class to create an object, and execute the printname method:

a = Name("Jorge", "Dummy")
a.printname()