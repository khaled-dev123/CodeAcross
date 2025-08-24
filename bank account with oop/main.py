from bank_account import *

account1 = Bank("Ahmed", 1000)
account2 = Bank("Ali", 500)


account1.getBalance()
#account2.getBalance()

account1.deposit(200)
#account1.getBalance()

account2.deposit(300)
#account2.getBalance()

try:
    account1.viabletansaction(500)
except BalanceError as e:
    print(e)

try:
    account1.withdraw(500)
except BalanceError as e:
    print(e)

try:
    account1.transfer(account2, 100)
except BalanceError as e:
    print(e)

Jim= RewardBank("Jim", 1000)
Jim.deposit(200)
Jim.getBalance()


Jim.transfer(account1, 500)
  