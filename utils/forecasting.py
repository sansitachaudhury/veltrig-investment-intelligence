from prophet import Prophet
import pandas as pd

def generate_forecast(data, days=30):

    df = data.reset_index()

    df = df.rename(columns={
        df.columns[0]: "ds",
        "Close": "y"
    })

    df = df[["ds", "y"]]

    model = Prophet()

    model.fit(df)

    future = model.make_future_dataframe(periods=days)

    forecast = model.predict(future)

    return forecast