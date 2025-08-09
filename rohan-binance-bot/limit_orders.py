import logging
from binance.enums import *
from utils import client, validate_order_params

logger = logging.getLogger('binance_bot')

def place_limit_order(symbol, side, quantity, price):
    """
    Places a limit order.
    :param symbol: The trading pair, e.g., 'BTCUSDT'
    :param side: 'BUY' or 'SELL'
    :param quantity: The amount of base asset to trade
    :param price: The price at which to place the order
    """
    if not validate_order_params(symbol, quantity, price=price):
        logger.error("Limit order validation failed.")
        return

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC, # Good 'Til Cancel
            quantity=quantity,
            price=price
        )
        logger.info(f"Limit order placed successfully: {order}")
        return order
    except Exception as e:
        logger.error(f"Failed to place limit order: {e}")
        return None
if __name__ == '__main__':
    # Example usage for testing
    from utils import setup_logging
    setup_logging()
    logger.info("Attempting to place a limit buy order for BTCUSDT...")
    place_limit_order('BTCUSDT', SIDE_BUY, 0.001, 25000)