class BalanceError(Exception):
    pass

class Bank:
    def __init__(self, name,initial_amount=0):
        self.name = name
        self.balance = initial_amount
        print(f"Bank '{self.name}' created with initial amount: {self.balance}")

    def getBalance(self):
        print(f"Acountname '{self.name}' Current balance: '{self.balance}'")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited '{amount}' to '{self.name}'. New balance: '{self.balance}'")
        else:
            print("Deposit amount must be positive.")  

    def viabletansaction(self, amount):
        if amount > self.balance:
            raise BalanceError(f"Insufficient funds for '{self.name}'. Available balance: '{self.balance}', Requested: '{amount}'")
        else:
            self.balance -= amount
            print(f"Withdrew '{amount}' from '{self.name}'. New balance: '{self.balance}'")   

    def withdraw(self, amount):
        try:
            self.viabletansaction(amount)
        except BalanceError as e:
            print(e)


    def transfer(self,account, amount):
        try:
           self.viabletansaction(amount)
           account.deposit(amount)
           print(f"Transferred '{amount}' from '{self.name}' to '{account.name}'")   
           print(f"'{self.name}' New balance: '{self.balance}'")
        except BalanceError as e:
            print(e)     

class RewardBank(Bank):
    def deposit(self, amount):
        self.balance = self.balance + (amount *1.05)
        print(f"Deposited '{amount}' to '{self.name}' with 5% bonus. New balance: '{self.balance}'")