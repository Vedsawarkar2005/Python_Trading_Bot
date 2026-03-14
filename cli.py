import argparse
import logging

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logger


API_KEY = "wZk7N4F1edQzaEFZWn9kOreH1M739ZWYuGukFrHuY4udsmZomNOp4OF4hgAGcff3 "
API_SECRET = "MMf2Pp9pItlqghI7zYC3GEzjdZaU3ZMQXEdVSxHyk4qqaGGt9PrH4mTVJCMCLQ9f"


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