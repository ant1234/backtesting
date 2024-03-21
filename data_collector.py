from typing import *
import time
import logging
from exchanges.binance import BinanceClient
from utils import *
logger = logging.getLogger()

def collect_all(client: BinanceClient, exchange: str, symbol: str):

    oldest_ts, most_recent_ts = None, None

    # initial data
    if oldest_ts is None:

        data = client.get_historical_data(symbol, end_time=time.time() * 1000 - 60000)

        if len(data) == 0:
            logger.warning("%s %s: no initial data found", exchange, symbol)
            return
        else:
            logger.info("%s %s: collected %s initial data from %s to %s ", 
                        exchange, 
                        symbol, 
                        len(data),
                        ms_to_dt(data[0][0]),
                        ms_to_dt(data[-1][0]))
            
        oldest_ts = data[0][0]
        most_recent_ts = data[-1][0]
        
        #insert the data

    # most recent data

    # older data

