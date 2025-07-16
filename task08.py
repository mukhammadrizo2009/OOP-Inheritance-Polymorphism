### 8. 🏦 **Bank Accounts**


class BankAccount:
    def __init__(self , user: int):
        """_summary_

        Args:
            user (int): _description_
        """
        self.user = user
    
class SavingsAccount(BankAccount):
    def withdraw(self):
        """_summary_
        """
        print(f"{self.user} hisobidan pul yechildi!")
        
    def get_interest(self):
        pass
class CheckingAccount(BankAccount):
    def withdraw(self):
        pass
    
    
    