import requests
from typing import *
import logging

logger = logging.getLogger()


class BinanceClient:
    def __init__(self, furtures=False):

        self.furtures = furtures

        if self.furtures:
            self._base_url = "https://fapi.binance.com"
        else:
            self._base_url = "https://api.binance.com"
    
    def _make_requests(self, endpoint: str, query_parameters: Dict):

        try:
            response = requests.get(self._base_url + endpoint, params=query_parameters)
        except Exception as e:
            logger.error("Conection error while making request to %s: %s", endpoint, e)
            return None
        
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making request to %s: %s (status code = %s)", 
                         endpoint, response.json(), response.status_code)
            return None


        