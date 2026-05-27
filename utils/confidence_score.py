def calculate_confidence(volatility):

    if volatility < 0.20:

        confidence = "High Confidence"

        explanation = """
        Historical price movement has been relatively stable
        making short-term forecasting slightly more reliable.
        """

        color = "green"

    elif volatility < 0.35:

        confidence = "Moderate Confidence"

        explanation = """
        Moderate market fluctuations may affect prediction reliability.
        Forecasts should be interpreted carefully.
        """

        color = "orange"

    else:

        confidence = "Low Confidence"

        explanation = """
        Strong market volatility reduces forecasting reliability.
        Predictions should not be treated as guaranteed outcomes.
        """

        color = "red"

    return confidence, explanation, color