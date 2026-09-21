import pytest
from bank import BankAccount

def test_initial_balance():
    account = BankAccount()
    assert account.balance == 0
def test_deposit():
    account = BankAccount()
    result = account.deposit(100)

    assert result == 100
    assert account.balance == 100
def test_deposit_zero():
    account = BankAccount()

    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw():
    account = BankAccount(100)

    result = account.withdraw(40)

    assert result == 60
    assert account.balance == 60

def test_withdraw_insufficient_funds():
    account = BankAccount(100)

    with pytest.raises(ValueError):
        account.withdraw(150)

def test_withdraw_zero():
    account = BankAccount(100)

    with pytest.raises(ValueError):
        account.withdraw(0)