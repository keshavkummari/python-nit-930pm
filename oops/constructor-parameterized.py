# Parameterized __init__ Constructor example

class SampleNumber:
    # Constructor - Parameterized
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname  = lastname

    def names(self):
        print("FirstName: ", self.firstname)
        print("LastName : ", self.lastname)

# Create an Object and Call Class Blueprint
student_info = SampleNumber("Keshav","Kummari")
student_info.names()
