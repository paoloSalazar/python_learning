def get_bitcoin_price():
    print("Checking the blockchain...")
    return 10000

def get_ethereum_price():
    print("Checking the blockchain...")
    return 1000

def get_solana_price():
    print("Checking the blockchain...")
    return 100

def get_current_price(coin):
    print(f"Getting current price for {coin}")
    if coin == "Bitcoin":
        price = get_bitcoin_price()
        return price
    if coin == "Ethereum":
        price = get_ethereum_price()
        return price
    if coin == "Solana":
        price = get_solana_price()
        return price
    raise ValueError(f"Unknown coin: {coin}")


def get_investment_info(i):
    name = i["name"]
    quantity = i["quantity"]
    import ipdb; ipdb.set_trace()
    # breakpoint()
    current_price = get_current_price(name)
    print(f"The current value of your {quantity} {name} is {current_price*quantity}")

if __name__ == "__main__":
    portfolio = [
        {"name": "Bitcoin", "quantity": 1.3, "buy": True},
        {"name": "Ethereum", "quantity": 13.4, "buy": True},
        {"name": "Solana", "quantity": 134.3, "buy": True}
    ]

    for investment in portfolio:
        get_investment_info(investment)
