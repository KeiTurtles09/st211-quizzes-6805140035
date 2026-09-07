class BankAccount:
    def __init__(self, balance = 0):
        self.actBalance = balance

    def deposit(self, depositAmount):
        if depositAmount <= 0:
            raise ValueError("Deposit must be positive")
        self.actBalance += depositAmount
        return self.actBalance

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.actBalance:
            raise ValueError("Insufficient funds")
        self.actBalance -= withdrawAmount
        return self.actBalance
    