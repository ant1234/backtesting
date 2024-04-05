import datetime
import pandas as pd

TF_EQUIV = {"1m": "1Min", 
            "5m": "5Min", 
            "15m": "15Min", 
            "30m": "30Min", 
            "1h": "1H", 
            "4h": "4H", 
            "12h": "12H",
            "1d": "D"}

STRAT_PARAMS = {
    "obv": {
        "ma_period": {"name": "moving average period", "type": int},
    },
    "ichimoku": {
        "kijun": {"name": "kijun period", "type": int},
        "tenkan": {"name": "tenkan period", "type": int},
    },
    "sup_res": {
        "min_points": {"name": "minimum points", "type": int},
        "min_diff_points": {"name": "min difference between points", "type": int},
        "rounding_nb": {"name": "rounding number", "type": float},
        "take_profit": {"name": "take profit %", "type": float},
        "stop_loss": {"name": "stop loss %", "type": float},
    },
}

#milliseconds to date time.
def ms_to_dt(ms: int):
    return datetime.datetime.utcfromtimestamp(ms / 1000)

def resample_timeframe(data: pd.DataFrame, tf: str) -> pd.DataFrame:
    return data.resample(TF_EQUIV[tf]).agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
    )