import datetime

from faker import Faker

MIN_DATE = datetime.date(2024, 1, 1)
MAX_DATE = datetime.date(2024, 1, 30)

FAKER_PRICES = {"bitcoin": 10000, "ethereum": 1000, "solana": 100}

fake = Faker()
fake.seed_instance(3824)

def get_buy_sell_dates():
    """Generate random buy and sell dates within a specified range."""
    buy_date = fake.date_between(start_date=MIN_DATE, end_date=MAX_DATE)
    sell_date = buy_date + datetime.timedelta(days=1)
    return buy_date, sell_date

def get_current_price(coin):
    """Return the current price of a given coin."""
    if coin in FAKER_PRICES:
        return FAKER_PRICES[coin]
    raise ValueError(f"{coin} is not valid")

