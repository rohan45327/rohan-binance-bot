import logging
from binance.enums import *
from utils import client, setup_logging, validate_order_params

logger = setup_logging()

def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price):
    """
    Places an OCO order. Note that Binance Futures API does not have a direct OCO order type.
    It's implemented as a combination of a take-profit order and a stop-market order.
    Both are conditional orders and will be canceled if one is triggered.
    :param symbol: The trading pair, e.g., 'BTCUSDT'
    :param side: 'BUY' or 'SELL'
    :param quantity: The amount of base asset to trade
    :param take_profit_price: The price for the take-profit limit order
    :param stop_loss_price: The stop price for the stop-market order
    """
    # Validation for both prices
    if not validate_order_params(symbol, quantity, price=take_profit_price) or \
       not validate_order_params(symbol, quantity, price=stop_loss_price):
        logger.error("OCO order validation failed.")
        return

    try:
        # Place a take-profit order
        take_profit_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='TAKE_PROFIT_MARKET',
            closePosition=True, # This is crucial for OCO logic on Binance
            stopPrice=take_profit_price
        )
        
        # Place a stop-loss order
        stop_loss_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP_MARKET',
            closePosition=True, # This is crucial for OCO logic on Binance
            stopPrice=stop_loss_price
        )

        logger.info(f"OCO orders placed successfully. Take-profit: {take_profit_order}, Stop-loss: {stop_loss_order}")
        return take_profit_order, stop_loss_order
    except Exception as e:
        logger.error(f"Failed to place OCO orders: {e}")
        return None

if __name__ == '__main__':
    # Example usage for testing
    from utils import setup_logging
    setup_logging()
    logger.info("Attempting to place an OCO order for BTCUSDT...")
    place_oco_order('BTCUSDT', SIDE_SELL, 0.001, 28000, 25000)