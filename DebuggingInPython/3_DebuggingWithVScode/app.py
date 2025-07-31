import datetime
from faker import Faker

FAKER_PRICES = {"bitcoin": 10000, "ethereum": 1000, "solana": 100}

portfolio = []
fake = Faker()
fake.seed_instance(3824)

def get_current_price(coin):
    if coin in FAKER_PRICES:
        return FAKER_PRICES[coin]
    raise ValueError(f"{coin} is not valid")

def get_buy_sell_dates():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    one_week_ago = yesterday - datetime.timedelta(days=7)

    buy_date = fake.date_between(start_date=one_week_ago, end_date=yesterday)
    sell_date = buy_date + datetime.timedelta(days=1)
    
    return buy_date, sell_date

def add_investment(coin, quantity, buy=True, add_sell=False):
    buy_date, sell_date = get_buy_sell_dates()
    new_investment = {
        "coin": coin,
        "quantity": quantity,
        "buy": buy,
        "timestamp": buy_date,
    }
    portfolio.append(new_investment)

    if add_sell:
        portfolio.append({
            "coin": coin,
            "quantity": quantity*0.1,
            "buy": False,
            "timestamp": sell_date,
        })

def summarize(list_investments=False):
    if list_investments:
        print("\nInvestments:")
        print("-"*20)
        for investment in portfolio:
            formatted_timestamp = investment["timestamp"].strftime("%Y/%m/%d")
            buy_sell = "bought" if investment["buy"] else "sold"
            print(
                f"You {buy_sell} {investment['quantity']} {investment['coin']} on {formatted_timestamp}"
            )


if __name__ == "__main__":
    add_investment("bitcoin", 1.3, buy=True, add_sell=True)
    add_investment("ethereum", 13.4, buy=True, add_sell=True)
    add_investment("solana", 134.3, buy=True, add_sell=True)
    add_investment("dogecoin", 100000)
    summarize(list_investments=True)

    # Example of getting current price
    try:
        print(f"Current price of Bitcoin: {get_current_price('bitcoin')}")
    except ValueError as e:
        print(e)