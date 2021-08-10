"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account, Transaction


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank: Bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank: Bank):
    accounts = bank.accounts
    accounts.append(Account('New Account'))

    assert len(bank.accounts) == 0


# TODO: Add unit tests for bank.add_funds()
def test_add_funds(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')
    bank.add_funds('Test', 25)
    transactions = bank.transactions

    assert transactions[0].account == account
    assert transactions[0].amount == 25
    assert len(transactions) == 1

def test_add_negative_funds(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')
    with pytest.raises(Exception):
        bank.add_funds('Test', -30)

def test_add_float_funds(bank: Bank):
    bank.create_account('Test')
    bank.add_funds('Test', 15.85)
    transaction = bank.transactions

    assert bank.transactions[0].amount == 15.85