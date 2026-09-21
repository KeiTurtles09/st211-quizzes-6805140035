from bank import BankAccount

def testDeposit():
    account = BankAccount(balance=100)
    newBalance = account.deposit(50)
    assert newBalance == 150

def testWithdraw():
    account = BankAccount(balance=100)
    newBalance = account.withdraw(50)
    assert newBalance == 50
