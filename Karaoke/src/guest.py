class Guest:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def get_cash(self):
        return self.cash

    def reduce_cash(self, amount):
        self.cash -= amount

    def pay_entry_fee(self, amount):
        if self.cash >= amount:
            self.reduce_cash(amount)
            return True
        else:
            return False