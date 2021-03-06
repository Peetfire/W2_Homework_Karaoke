class Guest:

    def __init__(self, name, cash, fave_song):
        self.name = name
        self.cash = cash
        self.fave_song = fave_song
        self.shout_out = "Ya, dancer!"

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

    def get_fave_song(self):
        return self.fave_song

    def get_shout_out(self):
       return self.shout_out

