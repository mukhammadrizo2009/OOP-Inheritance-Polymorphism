### 6. 👨‍💻 **Employee Types**


class Employee:
    def __init__(self , name: str , job: str):
        """_summary_

        Args:
            name (str): _description_
            job (str): _description_
        """
        self.name    = name
        self.job     = job
    
class Developer(Employee):
    def calculate_bonus(self , monthly):
        """_summary_

        Args:
            monthly (_type_): _description_
        """
        result01 = monthly * 0.5
        result = monthly + result01
        print(f"{self.name} | {self.job}'s | Salary: {result}")
    
class Manager(Employee):
    def calculate_bonus(self , monthly):
        """_summary_

        Args:
            monthly (_type_): _description_
        """
        result01 = monthly * 0.6
        result = monthly + result01
        print(f"{self.name} | {self.job}'s | Salary: {result}")
        
developer = Developer("Jamshid" , "Developer")
manager = Manager("Sodiq" , "Manager")

developer.calculate_bonus(10_000_000)
manager.calculate_bonus(9_000_000)