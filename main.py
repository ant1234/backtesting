#!/usr/bin/env python3

import logging 
from exchanges.binance import BinanceClient
from data_collector import collect_all

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
    mode = input("choose the program mode (data / backtest / optimize)").lower()

    exchange = "binance"

    if exchange == "binance":
        client = BinanceClient(True)

    while True:
        symbol = input("choose a crytocurrency: ").upper()
        if symbol in client.symbols:
            break

    if mode == "data":
        collect_all(client, exchange, symbol)