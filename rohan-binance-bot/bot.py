import argparse
import sys
from binance.enums import *

# Import all order logic modules
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.oco import place_oco_order
from advanced.twap import place_twap_order

# Setup logging
from utils import setup_logging
logger = setup_logging()

def main():
    """
    Parses arguments and runs the bot.
    """
    parser = argparse.ArgumentParser(description="Binance Futures CLI Trading Bot")
    parser.add_argument("--order_type", type=str, choices=["market", "limit", "oco", "twap"],
                        help="Type of order to place.")
    parser.add_argument("--symbol", type=str, help="Trading symbol (e.g., BTCUSDT).")
    parser.add_argument("--side", type=str, choices=["BUY", "SELL"], help="Order side (BUY or SELL).")

    # Arguments for various order types
    parser.add_argument("--quantity", type=float, help="Quantity of the asset to trade.")
    parser.add_argument("--price", type=float, help="Price for limit orders.")
    parser.add_argument("--stop-price", type=float, help="Stop price for oco orders.")
    parser.add_argument("--take-profit-price", type=float, help="Take-profit price for OCO orders.")
    parser.add_argument("--num-orders", type=int, help="Number of orders for TWAP strategy.")
    parser.add_argument("--interval", type=int, help="Interval in seconds for TWAP strategy.")
    
    args = parser.parse_args()
    
    if args.order_type == "market":
        if not all([args.symbol, args.side, args.quantity]):
            logger.error("Market order requires: symbol, side, quantity.")
            sys.exit(1)
        place_market_order(args.symbol, args.side, args.quantity)
    
    elif args.order_type == "limit":
        if not all([args.symbol, args.side, args.quantity, args.price]):
            logger.error("Limit order requires: symbol, side, quantity, price.")
            sys.exit(1)
        place_limit_order(args.symbol, args.side, args.quantity, args.price)

    elif args.order_type == "oco":
        if not all([args.symbol, args.side, args.quantity, args.take_profit_price, args.stop_price]):
            logger.error("OCO order requires: symbol, side, quantity, take-profit-price, stop-price.")
            sys.exit(1)
        place_oco_order(args.symbol, args.side, args.quantity, args.take_profit_price, args.stop_price)

    elif args.order_type == "twap":
        if not all([args.symbol, args.side, args.quantity, args.num_orders, args.interval]):
            logger.error("TWAP order requires: symbol, side, quantity, num-orders, interval.")
            sys.exit(1)
        place_twap_order(args.symbol, args.side, args.quantity, args.num_orders, args.interval)

if __name__ == '__main__':
    main()