# ''' oops concepts :
# -- class
# --object
# --inheritance
# --polymorphism
# --encapsulation
# '''
#
# # inheritance

import math

class triangle:       # parent class / base class
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


class find_area(triangle):    # derived class / child class

    def __init__(self,a,b,c):



        triangle.__init__(self,a,b,c)
    def find(self):
        self.s = (self.a + self.b + self.c) / 2
        print('semi perimeter:', self.s)
        print('area of traingle: ',(self.s*((self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5))


a = int(input('enter side1: '))
b = int(input('enter side2: '))
c = int(input('enter side3: '))


area = find_area(a,b,c)


area.find()


