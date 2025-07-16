### 5. 📺 **Appliance States**


class Appliance:
    def __init__(self):
        pass
    
class TV(Appliance):
    def turn_on(self):
        print("ZO'R TV-kanali ko'rsatilyabdi!")
        
    def turn_off(self):
        print("Svet o'chdi!")
        
class Fridge(Appliance):
    def turn_on(self):
        print("Muzlatgich ishlayabdi!")
        
    def turn_off(self):
        print("Muzlatgich o'chdi!")
        
        
devices = [TV() , Fridge()]

for device in devices:
    device.turn_on()
    device.turn_off()