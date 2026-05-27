import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from utils.forecasting import generate_forecast
from utils.riskanalysis import calculate_risk
from utils.beginner_insights import generate_beginner_insight
from utils.investor_profile import get_investor_guidance
from utils.portfolio_engine import generate_portfolio
from utils.confidence_score import calculate_confidence
from utils.ai_insights import generate_ai_insight

@st.cache_data
def load_data(stock, period):
    return yf.download(stock, period=period)
#page configuration
st.set_page_config(
    page_title="Veltrig",
    page_icon="📈",
    layout="wide"
)
#header and desc
st.title("Veltrig")

st.markdown("""
### Smarter Market Insights for New Investors

Veltrig simplifies stock analysis using forecasting, portfolio intelligence,
risk interpretation and beginner friendly financial guidance.

Built to help new investors understand market behavior with clarity instead of hype.
""")
#sidebar info
st.sidebar.info("""
Veltrig helps beginner investors:
- Analyze stocks
- Understand risk
- Explore forecasting
- Learn diversification
- Build smarter investment habits
""")

st.sidebar.header("Stock Selection")

stock = st.sidebar.selectbox(
    "Choose an NSE Stock",
    [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS"
    ]
)

period = st.sidebar.selectbox(
    "Select Time Period",
    [
        "6mo",
        "1y",
        "2y",
        "5y"
    ]
)
investor_profile = st.sidebar.selectbox(
    "Investment Style",
    [
        "Conservative",
        "Moderate",
        "Aggressive"
    ]
)
investment_amount = st.sidebar.number_input(
    "Investment Amount (₹)",
    min_value=1000,
    value=50000,
    step=1000
)

# fetching the data

with st.spinner("Fetching live market data..."):

    data = load_data(stock, period)

try:

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

except Exception:
    pass

if data.empty or "Close" not in data.columns:

    st.error("Unable to fetch stock market data currently.")
    st.stop()

data = data.dropna()

if data.empty:

    st.error("No valid stock data available.")
    st.stop()

price_change = (
    (data["Close"].iloc[-1] - data["Close"].iloc[0])
    / data["Close"].iloc[0]
) * 100

#overview metrics of the stocks
display_stock = stock.replace(".NS", "")
st.write(f"## {display_stock} Stock Overview")
latest_close = float(data["Close"].iloc[-1])
highest_price = float(data["High"].max())
lowest_price = float(data["Low"].min())

col1, col2, col3, col4 = st.columns(4)

price_change_display = round(price_change, 2)
col1.metric("Latest Closing Price", f"₹ {latest_close:.2f}")
col2.metric("Highest Price", f"₹ {highest_price:.2f}")
col3.metric("Lowest Price", f"₹ {lowest_price:.2f}")
col4.metric("Price Change", f"{price_change_display}%")

st.divider()

#price chart
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["Close"],
        mode="lines",
        name="Closing Price"
    )
)

fig.update_layout(
    title=f"{display_stock} Closing Price Trend",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

#forecast section
st.write("## AI-Based Trend Forecast")

try:
    forecast = generate_forecast(data)

    forecast_data = forecast[
        ["ds", "yhat", "yhat_lower", "yhat_upper"]
    ].tail(30)

except Exception as e:

    st.error("Forecast generation failed for the selected stock.")
    st.stop()

forecast_fig = go.Figure()

forecast_fig.add_trace(
    go.Scatter(
        x=forecast_data["ds"],
        y=forecast_data["yhat"],
        mode="lines",
        name="Forecasted Price"
    )
)

forecast_fig.add_trace(
    go.Scatter(
        x=forecast_data["ds"],
        y=forecast_data["yhat_upper"],
        mode="lines",
        line=dict(width=0),
        showlegend=False
    )
)

forecast_fig.add_trace(
    go.Scatter(
        x=forecast_data["ds"],
        y=forecast_data["yhat_lower"],
        mode="lines",
        fill='tonexty',
        line=dict(width=0),
        name="Confidence Range"
    )
)

forecast_fig.update_layout(
    title="30-Day Forecast",
    xaxis_title="Date",
    yaxis_title="Predicted Price",
    template="plotly_white",
    height=500
)

st.plotly_chart(forecast_fig, use_container_width=True)
st.divider()

#risk analysis(understanding this is important)
st.write("## Investment Risk Analysis")

risk_data = calculate_risk(data)

if risk_data["color"] == "green":
    st.success(f"### {risk_data['risk_level']}")

elif risk_data["color"] == "orange":
    st.warning(f"### {risk_data['risk_level']}")

else:
    st.error(f"### {risk_data['risk_level']}")

st.write(risk_data["explanation"])

st.metric(
    "Annualized Volatility",
    f"{risk_data['volatility']:.2%}"
)
st.divider()
#forecast confidence
st.write("## Forecast Confidence")

confidence, confidence_explanation, confidence_color = calculate_confidence(
    risk_data["volatility"]
)

if confidence_color == "green":

    st.success(f"### {confidence}")

elif confidence_color == "orange":

    st.warning(f"### {confidence}")

else:

    st.error(f"### {confidence}")

st.write(confidence_explanation)
st.divider()
#ai market insights in form of cards
st.write("## AI Market Insights")

with st.spinner("Generating market insights..."):

    ai_text = generate_ai_insight(
        stock,
        risk_data["risk_level"],
        confidence,
        price_change
    )

st.info(ai_text)
st.divider()
#educating the investor probably 
st.write("## Before You Invest")

beginner_text = generate_beginner_insight(
    stock,
    risk_data["risk_level"],
    price_change
)

st.info(beginner_text)
st.divider()
#investor profile 
st.write("## Personalized Investor Guidance")

profile_guidance = get_investor_guidance(
    investor_profile,
    risk_data["risk_level"]
)

st.info(profile_guidance)
st.divider()
#portfolio in investments
st.write("## Suggested Portfolio Allocation")

allocation, investment_split, portfolio_explanation = generate_portfolio(
    investor_profile,
    investment_amount
)

st.write(portfolio_explanation)

portfolio_df = {
    "Stock": [],
    "Allocation %": [],
    "Investment Amount": []
}

for stock_name in allocation:

    portfolio_df["Stock"].append(stock_name)
    portfolio_df["Allocation %"].append(f"{allocation[stock_name]}%")
    portfolio_df["Investment Amount"].append(
        f"₹ {investment_split[stock_name]}"
    )

portfolio_df = pd.DataFrame(portfolio_df)

st.table(portfolio_df)
st.divider()
#again educational stuff
with st.expander("Learn About Volatility"):
    st.write("""
    Volatility measures how much a stock price changes over time.
    
    - Higher volatility = Higher risk and larger price swings
    - Lower volatility = More stable price movement
    
    New investors should avoid judging stocks only by short-term growth.
    """)
st.divider()

st.write("## Beginner Investment Tips")

tips = [
    "Diversification helps reduce concentrated market risk.",
    "Short-term momentum does not guarantee long-term growth.",
    "High returns often come with higher volatility.",
    "Avoid emotional investing during sudden market swings.",
    "Historical data helps analysis but the future markets remain uncertain."
]

for tip in tips:
    st.success(tip)

st.divider()
#recent market data
st.write("## Recent Market Data")

st.dataframe(data.tail())
st.divider()

#the end ig, future enhancements definitely there 
st.caption("""
Disclaimer: Veltrig is an educational investment intelligence platform.
Forecasts and insights are based on historical market behavior and should not be treated as financial advice.
""")

st.markdown("---")

st.markdown("""
<center>
Built with Python, Streamlit, Forecasting Models and Financial Intelligence Logic
</center>
""", unsafe_allow_html=True)
