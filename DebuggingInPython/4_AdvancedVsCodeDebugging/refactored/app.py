from portfolio import Portfolio

PORTFOLIO_NAME = "Cryptosight"

if __name__ == "__main__":
    cryptosight = Portfolio(PORTFOLIO_NAME)
    cryptosight.add("bitcoin", 1.3)
    cryptosight.add("ethereum", 13.4)
    cryptosight.add("solana", 134.3)
    cryptosight.add("dogecoin", 100000, add_sell=False)
    cryptosight.summarize()