import argparse
import logging
import os

from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logger

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

def main():

    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)
        validate_price(args.type, args.price)

        client = BinanceClient(API_KEY, API_SECRET).get_client()

        print("Order Request Summary")
        print("----------------------")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")
        confirmation = input("\nConfirm order? (yes/no): ")

        if confirmation.lower() != "yes":
           print("Order cancelled by user.")
           return
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Response")
        print("----------------------")

        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])

        if "avgPrice" in order:
            print("Average Price:", order["avgPrice"])

        print("\nOrder placed successfully!")

    except Exception as e:

        logging.error(e)
        print("Order failed:", e)


if __name__ == "__main__":
    main()