class Card:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def get_card_number(self):
        return self.card_number

    def get_pin_number(self):
        return self.pin_number
