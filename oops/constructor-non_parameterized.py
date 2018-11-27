# NON-Parameterized __init__ Constructor example

class SampleNumber:

    def __init__(self):
        print("This is a NON-PARAMETERIZED Constructor")

    def show(self,firstname,lastname):
        print("FirstName: ", firstname)
        print("LastName : ", lastname)


# Creating an Object:

a1 = SampleNumber()
a1.show("Keshav","Kummari")

