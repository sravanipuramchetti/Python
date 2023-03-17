from OOPS import SampleClass
from excerise import example


class Childclass(SampleClass, example):
    num2 = 10  # class variable

    def __init__(self):
        SampleClass.__init__(self, 2, 3)

    def getcompletedata(self):
        return self.num2 + self.a + self.Summation()
    obj = example()
    value = obj.testcase1()
    
# Object creation for the child class
obj = Childclass()
print(obj.getcompletedata())
