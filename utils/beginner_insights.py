def generate_beginner_insight(stock, risk_level, price_change):

    stock_name = stock.replace(".NS", "")

    if risk_level == "Low Risk":

        insight = f"""
        {stock_name} has shown relatively stable movement over the selected period.
        This may suit beginner investors looking for lower volatility and steadier growth.
        However lower risk does not guarantee profits.
        """

    elif risk_level == "Moderate Risk":

        insight = f"""
        {stock_name} shows moderate price fluctuations and balanced growth potential.
        It may suit investors comfortable with medium market risk and gradual long-term investing.
        """

    else:

        insight = f"""
        {stock_name} has experienced strong price swings during the selected period.
        Beginner investors should approach carefully and avoid investing based only on short-term momentum.
        """

    if price_change > 25:

        insight += """
        
        The stock has recently shown strong upward movement.
        Rapid growth periods can sometimes increase volatility and emotional trading decisions.
        """

    elif price_change < 0:

        insight += """
        
        Recent downward movement suggests market uncertainty or sector weakness.
        Investors should evaluate long-term fundamentals instead of reacting emotionally to short-term declines.
        """

    return insight