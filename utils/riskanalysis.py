import numpy as np

def calculate_risk(data):

    returns = data["Close"].pct_change().dropna()

    volatility = returns.std() * np.sqrt(252)

    if volatility < 0.2:
        risk_level = "Low Risk"
        explanation = "This stock has shown relatively stable price movement over time."
        color = "green"

    elif volatility < 0.35:
        risk_level = "Moderate Risk"
        explanation = "This stock experiences moderate fluctuations and may suit medium-risk investors."
        color = "orange"

    else:
        risk_level = "High Risk"
        explanation = "This stock shows strong price fluctuations and may be risky for beginner investors."
        color = "red"

    return {
        "volatility": volatility,
        "risk_level": risk_level,
        "explanation": explanation,
        "color": color
    }