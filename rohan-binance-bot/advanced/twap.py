import logging
import time
from binance.enums import *
from utils import client, validate_order_params

logger = logging.getLogger('binance_bot')

def place_twap_order(symbol, side, total_quantity, num_orders, interval_seconds):
    """
    Splits a large order into smaller market orders placed over time.
    :param symbol: The trading pair, e.g., 'BTCUSDT'
    :param side: 'BUY' or 'SELL'
    :param total_quantity: The total amount of base asset to trade
    :param num_orders: The number of smaller orders to place
    :param interval_seconds: The time interval between orders in seconds
    """
    if not validate_order_params(symbol, total_quantity):
        logger.error("TWAP order validation failed.")
        return

    try:
        per_order_quantity = total_quantity / num_orders
        for i in range(num_orders):
            logger.info(f"TWAP order {i+1}/{num_orders} for {symbol} with quantity {per_order_quantity} is being placed.")
            client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=per_order_quantity
            )
            logger.info(f"TWAP order {i+1} placed. Waiting for {interval_seconds} seconds.")
            time.sleep(interval_seconds)
        
        logger.info(f"TWAP strategy for {symbol} completed successfully.")
    except Exception as e:
        logger.error(f"Failed to execute TWAP strategy: {e}")
        return None

if __name__ == '__main__':
    # Example usage for testing
    from utils import setup_logging
    setup_logging()
    logger.info("Attempting to place a TWAP order for BTCUSDT...")
    place_twap_order('BTCUSDT', SIDE_BUY, 0.01, 5, 2) # Total 0.01 BTC in 5 orders with 2s interval