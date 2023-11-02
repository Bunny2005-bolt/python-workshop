class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number #protected number
        self.__balance=balance  #private number
    
    def get_balance(self): #accessing a protected number
        return self.__balance #accessing a private number
    
account1=BankAccount("1234",1000)
print(account1._account_number)
print(account1.get_balance())