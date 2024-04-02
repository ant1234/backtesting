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

#milliseconds to date time.
def ms_to_dt(ms: int):
    return datetime.datetime.utcfromtimestamp(ms / 1000)

def resample_timeframe(data: pd.DataFrame, tf: str) -> pd.DataFrame:
    return data.resample(TF_EQUIV[tf]).agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
    )