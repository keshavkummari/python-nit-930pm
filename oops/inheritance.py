print("###################")
print("# Inheritance")
print("###################")

# Inheritance is a way to form new classes using classes that have already
# been defined. The newly formed classes are called derived classes, the classes
# that we derive from are called base classes. Important benefits of inheritance
# are code reuse and reduction of complexity of a program. The derived classes
# (descendants) override or extend the functionality of base classes (ancestors).
#
# Lets see an example by incorporating our previous work on the Dog class:

class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()

d.whoAmI()

d.eat()

d.bark()


# In this example, we have two classes: Animal and Dog. The Animal is the base
# class, the Dog is the derived class.
#
# The derived class inherits the functionality of the base class.
#
# * It is shown by the eat() method.
#
# The derived class modifies existing behavior of the base class.
#
# * shown by the whoAmI() method.
#
# Finally, the derived class extends the functionality of the base class,
# by defining a new bark() method.

