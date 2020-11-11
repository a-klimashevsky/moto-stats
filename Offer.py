class Offer:
    def __init__(self, id, mark, model, price, year):
        self.id = id
        self.mark = mark
        self.model = model
        self.price = price
        self.year = year

    def __repr__(self):
        return "Offer(id: %s, mark:%s, model:%s, year:%s, price: %s)" % (
            self.id, self.mark, self.model, self.year, self.price)
