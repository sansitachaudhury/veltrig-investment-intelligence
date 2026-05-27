def generate_ai_insight(stock, risk_level, confidence, price_change):

    stock_name = stock.replace(".NS", "")

    market_observation = ""
    beginner_reminder = ""
    investment_perspective = ""

    # Market Observation

    if price_change > 20:

        market_observation = f"""
        {stock_name} has shown strong upward momentum during the selected period
        indicating positive market sentiment and growth activity.
        """

    elif price_change > 0:

        market_observation = f"""
        {stock_name} has shown relatively stable positive movement with moderate growth behavior.
        """

    else:

        market_observation = f"""
        {stock_name} has experienced downward movement
        which may indicate short-term uncertainty or sector-related weakness.
        """

    # Beginner Reminder

    if risk_level == "High Risk":

        beginner_reminder = """
        High-volatility stocks can experience rapid price swings.
        Beginner investors should avoid emotional short-term decisions.
        """

    elif risk_level == "Moderate Risk":

        beginner_reminder = """
        Moderate-risk investments may balance growth and stability
        but diversification remains important.
        """

    else:

        beginner_reminder = """
        Lower-risk stocks may provide steadier long-term exposure
        although no investment is completely risk-free.
        """

    # Investment Perspective

    if confidence == "High Confidence":

        investment_perspective = """
        Historical stability makes trend forecasting relatively more reliable for this stock.
        """

    elif confidence == "Moderate Confidence":

        investment_perspective = """
        Forecast reliability may fluctuate due to changing market conditions and moderate volatility.
        """

    else:

        investment_perspective = """
        Forecast uncertainty is currently high due to strong market fluctuations.
        Predictions should be interpreted carefully.
        """

    final_text = f"""
    ### Market Observation
    {market_observation}

    ### Beginner Reminder
    {beginner_reminder}

    ### Investment Perspective
    {investment_perspective}
    """

    return final_text