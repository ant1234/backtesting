import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)

# on balance volume strategy

def backtest(df: pd.DataFrame, ma_period: int):
    
    # difference between each close row multiplied by the volume row
    df["obv"] = (np.sign(df["close"].diff()) * df["volume"]).fillna(0).cumsum()

    # rolling calculates the moving average
    df["obv_ma"] = round(df["obv"].rolling(window=ma_period).mean(), 2)

    # fill a new column with conditional values 
    df["signal"] = np.where(df["obv"] > df["obv_ma"], 1, -1)
    df["close_change"] = df["close"].pct_change()
    df["signal_shift"] = df["signal"].shift(1)

    # pct_change percent difference between each row, shift the row by one
    df["pnl"] = df["close"].pct_change() * df["signal"].shift(1)

    # cumulative drawdown over time 
    df["cum_pnl"] = df["pnl"].cumsum()
    df["max_cum_pnl"] = df["cum_pnl"].cummax()
    df["drawdown"] = df["max_cum_pnl"] - df["cum_pnl"]

    return df["pnl"].sum(), df["drawdown"].max()
