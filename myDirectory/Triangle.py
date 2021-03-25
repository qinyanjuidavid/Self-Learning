#The Main2.py will handle everything
from myDirectory.ModulesWithClass import Polygon
class Triangle(Polygon):
    def Area(self):
        return (self.getHeight()*self.getWidth())/2
