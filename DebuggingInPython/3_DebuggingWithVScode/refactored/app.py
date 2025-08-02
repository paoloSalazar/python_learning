from portfolio import Portfolio

PORTFOLIO_NAME = "Cryptosight"

if __name__ == "__main__":
    portfolio = Portfolio(PORTFOLIO_NAME)
    portfolio.add_investment("bitcoin", 1.3, add_sell=True)
    portfolio.add_investment("ethereum", 13.4, add_sell=True)
    portfolio.add_investment("solana", 134.3, add_sell=True)
    portfolio.add_investment("dogecoin", 100000, add_sell=False)
    portfolio.summarize()