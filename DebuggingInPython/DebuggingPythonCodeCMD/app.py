def get_current_price(coin):
    print(f"Getting current price for {coin}")
    if coin == "Bitcoin":
        return 10000
    elif coin == "Ethereum":
        return 1000
    elif coin == "solana":
        return 100
    else:
        return -1

def get_investment_info(investment):
    name = investment["name"]
    quantity = investment["quantity"]
    import pdb; pdb.set_trace()
    # breakpoint()
    current_price = get_current_price(name)
    print(f"The current value of your {quantity} {name} is {current_price*quantity}")

if __name__ == "__main__":
    portfolio = [
        {"name": "Bitcoin", "quantity": 0.5, "buy": True},
        {"name": "Ethereum", "quantity": 2, "buy": True},
        {"name": "solana", "quantity": 10, "buy": True}
    ]

    for investment in portfolio:
        get_investment_info(investment)