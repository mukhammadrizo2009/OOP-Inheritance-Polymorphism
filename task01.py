### 1. 🐶 **Animal Sounds**


class Animal:
    def __init__(self , name: str , age: int):
        """_summary_

        Args:
            name (str): _description_
            age (int): _description_
        """
        self.name = name
        self.age  = age
        
    def eat(self):
        """_summary_
        """
        print(f"{self.name} berganizni evuradi!")
        
    def sleep(self):
        """_summary_
        """
        print(f"{self.name} ishi buning uhlash!")
        
class Dog(Animal):
    def speak(self):
        """_summary_
        """
        print(f"{self.name}: Vov - Wow - Vov - Wow")
        
class Cat(Animal):
    def speak(self):
        """_summary_
        """
        print(f"{self.name}: Miyov - Miyov - Miyov")
        
        
cat = Cat("Jerry" , 4)
dog = Dog("Balto" , 5)

cat.speak()
dog.speak()