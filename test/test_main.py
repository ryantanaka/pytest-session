#!/usr/bin/env python3
import pytest

from main import Bank

@pytest.fixture(scope="function")
def test_bank_instance():
    bank = Bank()
    bank._accounts[1] = 100
    bank._accounts[2] = 200

    return bank

class TestBank:
    def test_Bank(self):
        assert Bank()

    def test_deposit_money_1(self, test_bank_instance):
        test_bank_instance.deposit_money(1, 100)
        assert test_bank_instance._accounts == {1:200, 2:200}

    def test_deposit_money_2(self, test_bank_instance):
        test_bank_instance.deposit_money(2, 200)
        assert test_bank_instance._accounts == {1:100, 2:400}

    @pytest.mark.parametrize(
            "account,amount,expected_balances",
            [
                (1, 100, {1:200, 2:200}),
                (2, 200, {1:100, 2:400}),
            ]
    )
    def test_deposit_money_parametrized(self, test_bank_instance, account, amount, expected_balances):
        test_bank_instance.deposit_money(account, amount)
        assert test_bank_instance._accounts == expected_balances

    def test_deposit_money_into_invalid_account(self, test_bank_instance):
        with pytest.raises(ValueError) as e:
            test_bank_instance.deposit_money(account="bad_account", amount=1)

        assert "Account does not exist" in str(e)

    def test_deposit_negative_amount(self, test_bank_instance):
        with pytest.raises(ValueError) as e:
            test_bank_instance.deposit_money(account=1, amount=0)

        assert "Deposit amount should be greater than 0!" in str(e)

    def test_get_balance(self, test_bank_instance):
        assert test_bank_instance.get_balance(account=1) == 100

    '''
    def test_get_balance_invalid_account(self, test_bank_instance):
        with pytest.raises(ValueError) as e:
            test_bank_instance.get_balance(account="bad_account")

        assert "Account does not exist" in str(e)
    '''


#https://www.ibm.com/topics/software-testing
