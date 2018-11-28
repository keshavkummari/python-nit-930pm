
# Private Methods

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving....")

    def __updateSoftware(self):
        print("Updating Software...")

audi = Car()

audi.drive()

audi._Car__updateSoftware()
