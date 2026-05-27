def generate_portfolio(profile, amount):

    if profile == "Conservative":

        allocation = {
            "HDFCBANK": 40,
            "TCS": 30,
            "INFY": 20,
            "RELIANCE": 10
        }

        explanation = """
        This portfolio focuses more on relatively stable and established companies.
        It aims to reduce volatility while maintaining steady long-term exposure.
        """

    elif profile == "Moderate":

        allocation = {
            "RELIANCE": 30,
            "TCS": 25,
            "INFY": 25,
            "ICICIBANK": 20
        }

        explanation = """
        This portfolio balances growth potential with moderate market risk.
        Diversification across sectors may help reduce concentrated exposure.
        """

    else:

        allocation = {
            "RELIANCE": 35,
            "INFY": 30,
            "ICICIBANK": 20,
            "TCS": 15
        }

        explanation = """
        This portfolio prioritizes higher growth potential with increased market exposure.
        Aggressive portfolios may experience stronger volatility during uncertain conditions.
        """

    investment_split = {}

    for stock, percent in allocation.items():

        investment_split[stock] = round((percent / 100) * amount, 2)

    return allocation, investment_split, explanation