import datetime

class Investment:
    def __init__(self, coin, quantity, buy=True, timestamp=datetime.datetime.now()):
        self.coin = coin
        self.quantity = quantity
        self.buy = buy
        self.timestamp = timestamp

    def __repr__(self):
        buy_sell = "bought" if self.buy else "sold"
        formatted_timestamp = self.timestamp.strftime("%Y/%m/%d")
        return f"Investment {buy_sell} {self.quantity} {self.coin} on {formatted_timestamp}"
