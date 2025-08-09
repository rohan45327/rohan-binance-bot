import os
# Binance Futures Testnet API credentials
# NOTE: It's highly recommended to use environment variables instead of hardcoding keys.
# You can set them in your terminal with:
# export BINANCE_API_KEY="YOUR_API_KEY"
# export BINANCE_API_SECRET="YOUR_API_SECRET"
API_KEY = os.environ.get("BINANCE_API_KEY")
API_SECRET = os.environ.get("BINANCE_API_SECRET")
# Testnet Base URL for Binance Futures
FUTURES_TESTNET_URL = "https://testnet.binancefuture.com"
# Logging configuration
LOG_FILE = "bot.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"