#!/usr/bin/env python3

class Bank:

    def __init__(self):
        self._accounts = dict()

    def deposit_money(self, account: int, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than 0!")

        try:
            self._accounts[account] += amount
        except KeyError as e:
            raise ValueError("Account does not exist!")

    def get_balance(self, account) -> float:
        try:
            return self._accounts[account]
        except KeyError as e:
            raise ValueError("Account does not exist!")

