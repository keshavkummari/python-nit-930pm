#!/usr/bin/python
class Human:

    def __init__(self, n, o): # Constructors 
        self.name = n         # Properties of Human Class
        self.occupation = o   # Properties of Human Class

    def do_work(self):     # Method of class
        if self.occupation == "singer":
            print(self.name,"Sings songs")
        elif self.occupation == "actor":
            print(self.name,"Acts in Films")
        else:
            print(self.name,"It's not in our list")

    def speaks(self):      # Method of class
        print(self.name,"Says how are you?")

# Creating an Object
abiel = Human("vin diesel","actor")
# Executing or Calling Class Methods
abiel.do_work()
abiel.speaks()

# Creating an Object
enrique = Human("Enrique Abiel","DevOps")
# Executing or Calling Class Methods
enrique.do_work()
enrique.speaks()

