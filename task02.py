### 2. 🚗 **Transport Info**


class Transport:
    def __init__(self , kind: int):
        """_summary_

        Args:
            kind (int): _description_
        """
        self.kind = kind
        
    def drive(self):
        """_summary_
        """
        pass
    
class Car(Transport):
    def show_info(self):
        print(f"{self.kind}: Fast and comfortable!")
        print(f"{self.kind}: Expensive!")
        print(f"{self.kind}: You can drive!")
        
class Bike(Transport):
    def show_info(self):
        print(f"{self.kind}: Physical activity!")
        print(f"{self.kind}: Cheap and good for health!")
        print(f"{self.kind}: You can cycle!")
        
bike = Bike("Sport bike")
car  = Car("Malibu")

car.show_info()
bike.show_info()