### 13. 🚚 **Delivery Agents**


class Courier:
    """_summary_
    """
    def __init__(self , name: str , transport: str):
        """_summary_

        Args:
            name (str): _description_
            transport (str): _description_
        """
        self.name = name
        self.transport = transport
        
class BikeCourier(Courier):
    """_summary_

    Args:
        Courier (_type_): _description_
    """
    def delivery_range(self):
        """_summary_
        """
        print(f"{self.name} deliveried with {self.transport}")
        
class CarCourier(Courier):
    """_summary_

    Args:
        Courier (_type_): _description_
    """
    def delivery_range(self):
        """_summary_
        """
        print(f"{self.name} deliveried with {self.transport}")
        
class DroneCourier(Courier):
    """_summary_

    Args:
        Courier (_type_): _description_
    """
    def delivery_range(self):
        """_summary_
        """
        print(f"{self.name} deliveried with {self.transport}")
        
bike = BikeCourier("Ali" , "Bike")
car  = CarCourier("Vali" , "Car")
drone = DroneCourier("Bob" , "Motorcycle")

car.delivery_range()
bike.delivery_range()
drone.delivery_range()