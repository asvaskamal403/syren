class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount >0 :
            self.__balance = self.__balance + amount

    def withdraw(self ,amount):
        if amount > 0 and amount<=self.__balance:
            self.__balance = self.__balance - amount

# ceate the object 
account = BankAccount('12345',1000)

# access the method
print('Account number : ', account.get_account_number())
print('Balance ' , account.get_balance())

# deposit and withdraw opeartion

account.deposit(500)
account.withdraw(200)

#
print('Account number : ', account.get_account_number())
print('Balance ' , account.get_balance())