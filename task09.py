### 9. ✉️ **Notifications**


class Notification:
    def __init__(self , email: str , phone_number: int):
        """_summary_

        Args:
            email (str): _description_
            phone_number (int): _description_
        """
        self.email = email
        self.phone_number = phone_number
        
class EmailNotification(Notification):
    """_summary_

    Args:
        Notification (_type_): _description_
    """
    def send(self):
        """_summary_
        """
        print(f"{self.email} to send SMS...!")
        
class SMSNotification(Notification):
    """_summary_

    Args:
        Notification (_type_): _description_
    """
    def send(self):
        """_summary_
        """
        print(f"{self.phone_number} to send SMS...!")
        
p_number = SMSNotification("muhammadrizomirzaev671@gmail.com" , 992_97_652_2727)
email    = EmailNotification("muhammadrizomirzaev671@gmail.com" , 992_97_652_2727)

p_number.send()
email.send()