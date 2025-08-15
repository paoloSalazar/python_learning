from typing import List

import utilities
from investment import Investment

class Portfolio:
    def __init__(self, name):
        self.name = name
        self.investments: List[Investment] = []

    # def add_investment(self, coin: str, quantity: float, add_sell: bool = False):
    #     buy_date, sell_date = utilities.get_buy_sell_dates()
    #     self.investments.append(
    #         Investment(coin, quantity, True, buy_date)
    #     )

    #     if add_sell:
    #         self.investments.append(
    #             Investment(coin, quantity * 0.2, False, sell_date)
    #         )

    def add(self, coin, quantity, add_sell=True):
        buy_date, sell_date = utilities.get_buy_sell_dates()
        self.investments.append(
            Investment(coin, quantity, True, buy_date)
        )

        if add_sell:
            self.investments.append(
                Investment(coin, quantity * 0.2, False, sell_date)
            )

    def summarize(self, list_investments: bool = True):
        totals = {}
        for investment in self.investments:
            if investment.coin not in totals:
                totals[investment.coin] = 0
            if investment.buy:
                totals[investment.coin] += investment.quantity
            else:
                totals[investment.coin] -= investment.quantity
        
        for coin, total in totals.items():
            try:
                current_price = utilities.get_current_price(coin)
                print(f"you own {total} {coin} worth {current_price*total}")
            except ValueError as e:
                print(e)
        if list_investments:
            print("\nInvestments:")
            for investment in self.investments:
                print(investment)