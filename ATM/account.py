
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

    def get_account_number(self) -> int:
        return self.account_number

    def get_balance(self) -> int:
        return self.balance
