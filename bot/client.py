from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

class BinanceClient:

    def __init__(self, api_key, api_secret):

        self.client = Client(api_key, api_secret)

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client