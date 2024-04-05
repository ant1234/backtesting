#!/usr/bin/env python3

import logging 
from exchanges.binance import BinanceClient
from data_collector import collect_all
import backtester
from utils import TF_EQUIV
import datetime

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == "__main__":
    mode = input("choose the program mode (data / backtest / optimize): ").lower()

    exchange = "binance"

    if exchange == "binance":
        client = BinanceClient(True)

    while True:
        symbol = input("choose a crytocurrency: ").upper()
        if symbol in client.symbols:
            break

    if mode == "data":
        collect_all(client, exchange, symbol)

    elif mode == "backtest":

        # strategy

        available_strategies = ["obv", "ichimoku", "sup_res"]

        while True:
            strategy = input(f"choose a strategy ({', '.join(available_strategies)}): ").lower()
            if strategy in available_strategies:
                break

        # from 

        while True:
            tf = input(f"choose a timeframe ({', '.join(TF_EQUIV.keys())}): ").lower()
            if tf in TF_EQUIV.keys():
                break

        while True:
            from_time = input("backtest from (yyyy-mm-dd or press enter to use all data): ").lower()
            if from_time == "":
                from_time = 0
                break

            try: 
                from_time = int(datetime.datetime.strptime(from_time, "%Y-%m-%d").timestamp() * 1000)
                break
            except ValueError:
                continue

        while True:
            to_time = input("backtest to (yyyy-mm-dd or press enter to use current time): ").lower()
            if to_time == "":
                to_time = int(datetime.datetime.now().timestamp() * 1000)
                break

            try: 
                to_time = int(datetime.datetime.strptime(to_time, "%Y-%m-%d").timestamp() * 1000)
                break
            except ValueError:
                continue

        print(backtester.run(exchange, symbol, strategy, tf, from_time, to_time))