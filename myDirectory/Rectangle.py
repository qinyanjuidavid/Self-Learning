#The main2.py File will handle everything
from myDirectory.ModulesWithClass import Polygon #Polygon is the class
class Rectangle(Polygon):
    def Area(self):
        return self.getHeight()*self.getWidth()
