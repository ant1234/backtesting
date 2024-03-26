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
    while True:

        data = client.get_historical_data(symbol, start_time=int(most_recent_ts + 60000))

        if data is None:
            time.sleep(4) # pause incase an error occurs during the request
            continue

        if len(data) < 2:
            break

        data = data[:-1] 

        if data[-1][0] > most_recent_ts:
            most_recent_ts = data[-1][0]
            
        logger.info("%s %s: collected %s recent data from %s to %s ", 
                        exchange, 
                        symbol, 
                        len(data),
                        ms_to_dt(data[0][0]),
                        ms_to_dt(data[-1][0]))
            
        time.sleep(1.1) # pause to overcome the rate limit

    # older data
    while True:

        data = client.get_historical_data(symbol, end_time=int(oldest_ts - 60000))

        if data is None:
            time.sleep(4) # pause incase an error occurs during the request
            continue

        if len(data) == 0:
            logger.info("%s %s: stopped older data collection because no data was found before %s", 
                        exchange, symbol, ms_to_dt(oldest_ts))
            break

        if data[0][0] < oldest_ts:
            oldest_ts = data[0][0]
            
        logger.info("%s %s: collected %s older data from %s to %s ", 
                        exchange, 
                        symbol, 
                        len(data),
                        ms_to_dt(data[0][0]),
                        ms_to_dt(data[-1][0]))
            
        time.sleep(1.1) # pause to overcome the rate limit

