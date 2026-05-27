def get_investor_guidance(profile, risk_level):

    if profile == "Conservative":

        if risk_level == "High Risk":

            return """
            This stock may not align well with conservative investing goals due to its strong volatility.
            Consider balancing with more stable assets or diversified investments.
            """

        return """
        This stock may suit conservative investors looking for relatively stable long-term exposure.
        Diversification is still important even for lower-risk investments.
        """

    elif profile == "Moderate":

        return """
        This stock may suit investors comfortable with moderate market fluctuations and balanced growth strategies.
        Long-term consistency is often more important than short-term momentum.
        """

    else:

        return """
        Aggressive investors may tolerate higher volatility in pursuit of stronger long-term growth.
        However, higher-risk investing also increases the possibility of significant drawdowns.
        """