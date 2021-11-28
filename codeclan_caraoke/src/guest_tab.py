class Guest_tab:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_tab_value(self):
        return sum([item.price * item.quantity for item in self.items])