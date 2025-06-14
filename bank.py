from abc import ABC, abstractmethod

# Base abstract class
class Account(ABC):
    def __init__(self, acc_holder, acc_number, balance=0):
        self._acc_holder = acc_holder
        self._acc_number = acc_number
        self.__balance = balance  # private

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"Account Holder: {self._acc_holder}")
        print(f"Account Number: {self._acc_number}")
        print(f"Balance: ₹{self.__balance}")

    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance


# Savings Account
class SavingsAccount(Account):
    def __init__(self, acc_holder, acc_number, balance=0):
        super().__init__(acc_holder, acc_number, balance)

    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self._get_balance() + amount)
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")


# Current Account 
class CurrentAccount(Account):
    def __init__(self, acc_holder, acc_number, balance=0):
        super().__init__(acc_holder, acc_number, balance)

    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self._get_balance() + amount)
            print("Deposit added.")
        else:
            print("Amount not valid.")

    def withdraw(self, amount):
        if 0 < amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")


# Sample account testing
savings = SavingsAccount("tejas", "4598", 5000)
current = CurrentAccount("prasad", "5674", 2000)

print("\n--- Savings Account ---")
savings.deposit(1000)
savings.withdraw(2000)
savings.show_balance()

print("\n--- Current Account ---")
current.deposit(500)
current.withdraw(2800)  
current.show_balance()
