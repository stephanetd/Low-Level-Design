from abc import ABC, abstractmethod
from account import Account

class Transaction(ABC):
    def __init__(self, transaction_id: str, account: Account, amount: int):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass