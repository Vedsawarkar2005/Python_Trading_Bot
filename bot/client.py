from binance.client import Client
import os

class BinanceClient:

    def __init__(self, api_key, api_secret):

        self.client = Client(api_key, api_secret)

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client