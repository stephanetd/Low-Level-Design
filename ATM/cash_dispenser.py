import threading

class CashDispenser:
    def __init__(self, initial_cash_amount):
        self.cash_available = initial_cash_amount
        self.thread_lock = threading.Lock()

    def dispense_cash(self, amount):
        with self.thread_lock:
            if amount > self.cash_available:
                raise ValueError("Insufficient cash reserve in the ATM to process this transaction!")
            else:
                self.cash_available -= amount
                print(f"Cash dispensed: ${amount}.")
