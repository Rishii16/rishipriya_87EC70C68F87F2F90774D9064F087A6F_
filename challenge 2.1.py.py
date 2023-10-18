class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited {amount}. Current balance: {self.__account_balance}")
      else:
          print("Invalid amount for deposit.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrew {amount}. Current balance: {self.__account_balance}")
      else:
          print("Insufficient balance or invalid amount for withdrawal.")

  def display_balance(self):
      print(f"Account balance: {self.__account_balance}")

# Example usage
if __name__ == '__main__':
  account = BankAccount("123456789", "boomika", 1000)
  account.display_balance()  # Account balance: 1000
  account.deposit(500)  # Deposited 500. Current balance: 1500
  account.withdraw(200)  # Withdrew 200. Current balance: 1300
  account.display_balance()  # Account balance: 1300
