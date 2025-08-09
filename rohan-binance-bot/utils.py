"""
Utility functions for the trading bot, including logging and validation.
"""
import logging
import sys
from binance.client import Client
from config import API_KEY, API_SECRET, FUTURES_TESTNET_URL, LOG_FILE, LOG_FORMAT

# Global client instance
client = Client(API_KEY, API_SECRET, testnet=True)
client.API_URL = FUTURES_TESTNET_URL

def setup_logging():
    """
    Sets up the logging configuration to write to a file and the console.
    """
    # Create logger
    logger = logging.getLogger('binance_bot')
    logger.setLevel(logging.INFO)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.INFO)

    # Create console handler with a higher log level
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(LOG_FORMAT)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def validate_order_params(symbol, quantity, price=None, stop_price=None):
    """
    Validates the input parameters for an order.
    Returns True if valid, False otherwise.
    """
    logger = logging.getLogger('binance_bot')

    # Simple validation checks
    if not symbol or not isinstance(symbol, str):
        logger.error("Validation Error: Symbol must be a non-empty string.")
        return False
    
    try:
        quantity = float(quantity)
        if quantity <= 0:
            logger.error("Validation Error: Quantity must be a positive number.")
            return False
    except (ValueError, TypeError):
        logger.error("Validation Error: Quantity must be a valid number.")
        return False

    if price is not None:
        try:
            price = float(price)
            if price <= 0:
                logger.error("Validation Error: Price must be a positive number.")
                return False
        except (ValueError, TypeError):
            logger.error("Validation Error: Price must be a valid number.")
            return False
    
    if stop_price is not None:
        try:
            stop_price = float(stop_price)
            if stop_price <= 0:
                logger.error("Validation Error: Stop price must be a positive number.")
                return False
        except (ValueError, TypeError):
            logger.error("Validation Error: Stop price must be a valid number.")
            return False
            
    return True