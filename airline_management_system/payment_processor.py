from threading import Lock
from payment import Payment

class PaymentProcessor:
    _lock = Lock()
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def process_payment(self, payment):
        # Process payment using the selected payment method
        payment.process_payment()