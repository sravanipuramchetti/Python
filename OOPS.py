class SampleClass:
    a = 100
    b = 200

    # default constructor in the class
    def __init__(self, c, d):
        self.firstnumber = c
        self.secondnumber = d
        print("I am the constructor called default")

    def getData(self):
        print("This method is executed from the class")

    def Summation(self):
        return self.firstnumber + self.secondnumber


# Creating an object to the class to utilize the method defined with in it
obj = SampleClass(2, 3)
obj.getData()
print(obj.Summation())

# Creating another object for the same class

obj1 = SampleClass(4, 5)
obj1.getData()
print(obj1.Summation())
print("***********END of Class Concept******************88")

# Inheritance in python
# Inheritance means accruing the properties of parent class to child class
