import logging
from binance.enums import *
from utils import client, validate_order_params

logger = logging.getLogger('binance_bot')

def place_market_order(symbol, side, quantity):
    """
    Places a market order.
    :param symbol: The trading pair, e.g., 'BTCUSDT'
    :param side: 'BUY' or 'SELL'
    :param quantity: The amount of base asset to trade
    """
    if not validate_order_params(symbol, quantity):
        logger.error("Market order validation failed.")
        return

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logger.info(f"Market order placed successfully: {order}")
        return order
    except Exception as e:
        logger.error(f"Failed to place market order: {e}")
        return None

if __name__ == '__main__':
    # Example usage for testing
    from utils import setup_logging
    setup_logging()
    logger.info("Attempting to place a market buy order for BTCUSDT...")
    place_market_order('BTCUSDT', SIDE_BUY, 0.001)