### 11. 🛒 **Ecommerce Products**


class Product:
    """_summary_
    """
    def __init__(self , name_product: str):
        """_summary_

        Args:
            name_product (str): _description_
        """
        self.name_product = name_product
        
class PhysicalProduct(Product):
    """_summary_

    Args:
        Product (_type_): _description_
    """
    def get_delivery_method(self):
        """_summary_
        """
        print(f"{self.name_product} is physical product...!")
        
class DigitalProduct(Product):
    """_summary_

    Args:
        Product (_type_): _description_
    """
    def get_delivery_method(self):
        """_summary_
        """
        print(f"{self.name_product} is digital product...!")
        
physical = PhysicalProduct("Lactel")
digital  = DigitalProduct("Iphone")

digital.get_delivery_method()
physical.get_delivery_method()