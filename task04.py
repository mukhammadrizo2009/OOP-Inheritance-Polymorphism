### 4. 📐 **Shapes**

import math

class Shape:
    def area(self):
        raise NotImplementedError ("This method has not been written yet!")

# Circle's function !       
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
        
    def area(self):
        print("Circle's Function: math.pi * self.radius ** 2")
        return math.pi * self.radius ** 2
    
    
# Restangle's function !

class Restangle(Shape):
    def __init__(self , height: int , width: int):
        """_summary_

        Args:
            a (int): _description_
            b (int): _description_
        """
        self.width  = width
        self.height = height
        
    def area(self):
        print("Restangle's Function: self.width * self.height ")
        return self.width * self.height
    
    
# Triangle's function !

class Triangle(Shape):
    def __init__(self , base: int , height: int ):
        """_summary_

        Args:
            base (int): _description_
            height (int): _description_
        """
        
        self.base   = base
        self.height = height
        
    def area(self):
        print("Triangle's Function: 0.5 * self.base * self.height")
        return 0.5 * self.base * self.height
        
# Results
  
circle = Circle(5)
print("Circle's Result: ",circle.area())

restangle = Restangle(5 , 5)
print("Restangle's Result: ",restangle.area())

triangle = Triangle(3 , 5)
print("Triangle's Result: ",triangle.area())