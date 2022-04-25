
        class Person:
    def __init__(self,name,age):
        self.name = name          # public use  with in or outside of class
        self.__age = age            # private use only with in class
    def details(self):
        print('my name is : {} \nmy age is : {}'.format(self.name,self.__age))
class Employee(Person):
    def __init__(self,name,age,salary):
        self.salary = salary
        Person.__init__(self,name,age)
    def emp_details(self):
       #Person.details(self)          #  function to functin call
        print("my emp details is  : ",self.salary,self.name)



data =Employee('kalyan',25,10100)
data.emp_details()

