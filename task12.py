### 12. 🎓 **Online Learning Users**


class User:
    """_summary_
    """
    def __init__(self , name: str , level: str):
        """_summary_

        Args:
            name (str): _description_
            level (str): _description_
        """
        self.name  = name
        self.level = level 
class Student(User):
    """_summary_

    Args:
        User (_type_): _description_
    """
    def get_dashboard(self):
        """_summary_
        """
        print(f"{self.name} | {self.level}")
        print("Class: From 15:30 to 16:50")
        
class Instructor(User):
    """_summary_

    Args:
        User (_type_): _description_
    """
    def get_dashboard(self):
        """_summary_
        """
        print(f"{self.name} | {self.level}")
        print("Class: From 09:00 to 10:20")
        
student = Student("Shodibek" , "Elementary")
instructor = Instructor("Nilufar" , "Biggenner")

student.get_dashboard()
instructor.get_dashboard()