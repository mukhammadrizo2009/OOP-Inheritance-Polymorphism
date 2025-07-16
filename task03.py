### 3. 👤 **User Roles**

class User:
    def __init__(self , name: str , job: str):
        """_summary_

        Args:
            name (str): _description_
            job (str): _description_
        """
        self.name = name
        self.job  = job
        
        
class Admin(User):
    def access_level(self):
        """_summary_
        
        """
        print(f"{self.name} | {self.job}: Login with (his/her) Name and Surname or with (his/her) password")
    

class Guest(User):
    def access_level(self):
        """_summary_
        
        """
        print(f"{self.name} | {self.job}: Login with (his/her) ID Code and Phone number(SMS Code)")
    
    
guest = Guest("Abubakr" , "Guests")
admin = Admin("Shohjahon" , "Admin")

guest.access_level()
admin.access_level()