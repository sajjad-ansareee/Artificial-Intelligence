# learning the basics of classes in python


#Banking System
class Bank:
  def __init__(self, amount=1000):
    self.amount=amount
  def display_amount(self):
    print(f"The amount in your bank account is ${self.amount}.")
  def deposit(self, amount):
    print(f"Deposited ${amount}")
    self.amount+=amount
  def withdraw(self, amount):
    if self.amount>=amount:
      print(f"Withdrawn ${amount}")
      self.amount-=amount
    else:
      print(f"Withdrawn all money in your account which was only ${self.amount}.")
      self.amount=0
# Create an object
customer=Bank(900)
# So we can instantiate class data members outside of the class aswell
customer.money=100
print(customer.money)
customer.display_amount()
customer.withdraw(100)
customer.deposit(500)
customer.display_amount()
