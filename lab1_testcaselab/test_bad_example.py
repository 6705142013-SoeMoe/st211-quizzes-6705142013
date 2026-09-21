from bank import BankAccount

def test_everything():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.deposit(10)

    assert account.balance == 130