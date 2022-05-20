class Area_rec:
    def __init__(self,leng,bre):
        self.__leng = leng   # private
        self._bre = bre      # protect
    def _find_area(self):
        self.area = (self.__leng)*(self._bre)
        print("area of rectangle : ",self.area)
class Area_sqr:
    def __init__(self,leng,bre,high):
        self.high = high              # public
        Area_rec.__init__(self,leng,bre)
    def find_perimeter(self):
        Area_rec._find_area(self)
        self.p = (self.high)*(self._bre)
        print("perimeter of sqr : ",self.p)




leng = int(input("enter leng : "))
bre = int(input("enter bre : "))
high = int(input("enter high : "))
obj = Area_sqr(leng,bre,high)
obj.find_perimeter()             # lenght can not print outside the class because its private
