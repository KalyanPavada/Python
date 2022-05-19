class Marks:         ## parent class / base class
    def __init__(self,english,math,phys,chem):   # constructor
        self.english = english
        self.math = math
        self.phys = phys
        self.chem = chem

    def find_sum(self):
        self.s = (self.english,self.math,self.phys,self.chem)
        print("sum of marks :",sum(self.s))

class Length_marks(Marks):   ## derived / child class
    def __init__(self,english,math,phys,chem,history):
        self.history = history
        Marks.__init__(self,english,math,phys,chem)
    def find_leng(self):
        self.l = (self.english,self.math,self.phys,self.chem,self.history)
        print("the length of marks ",len(self.l))
    def find_avg(self):
        self.avg = sum(self.s)/ len(self.l)
        print("the avg of marks : ",self.avg)

english = int(input("enter the marks eng : "))
math = int(input("enter the marks math : "))
phys = int(input("enter the marks phys : "))
chem = int(input("enter the marks chem : "))
history = int(input("enter the marks hist : "))

avg = Length_marks(english,math,phys,chem,history)
avg.find_sum()
avg.find_leng()
avg.find_avg()




