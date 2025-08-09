# rohan-binance-bot
# Project Overview
  This is a simple command-line Python bot designed to place various order types on the Binance Futures Testnet. It serves as a foundational script for learning      how to interact with the Binance API for futures trading. The bot supports placing market, limit, and OCO (One Cancels the Other) orders.

The project is structured into two files:

bot.py: The main script containing the bot's logic and command-line interface.

config.py: A separate file for securely managing API keys using environment variables.

# Prerequisites
Before running the bot, ensure you have the following installed:

Python 3.x

python-binance library: You can install this using pip:

pip install python-binance

Setup: API Key Configuration
For security, the bot uses environment variables to store your API keys. You will need a Binance Futures Testnet account to get your keys.

Get Testnet Keys:

Navigate to the Binance Futures Testnet website.

Log in or create an account.

Find and copy your Testnet API Key and Secret Key.

# Set Environment Variables:

Open your terminal and set the environment variables according to your operating system.

For macOS/Linux:

export BINANCE_API_KEY="YOUR_TESTNET_API_KEY"
export BINANCE_API_SECRET="YOUR_TESTNET_API_SECRET"

For Windows (Command Prompt):

set BINANCE_API_KEY="YOUR_TESTNET_API_KEY"
set BINANCE_API_SECRET="YOUR_TESTNET_API_SECRET"

Remember to replace "YOUR_TESTNET_API_KEY" and "YOUR_TESTNET_API_SECRET" with the keys you copied from the Testnet site.

# Running the Bot
The bot is executed from the command line and uses arguments to specify the order type and details.

1. Market Order
Places an order at the current market price.

Command:

  python bot.py --order_type market --symbol BTCUSDT --side BUY --quantity 0.002

--order_type market: Specifies a market order.

--symbol BTCUSDT: The trading pair.

--side BUY: The direction of the trade (can be BUY or SELL).

--quantity 0.002: The amount to trade.

2. Limit Order
Places an order that will only execute at a specified price or better.

Command:

  python bot.py --order_type limit --symbol BTCUSDT --side SELL --quantity 0.002 --price 60000.00

--order_type limit: Specifies a limit order.

--price 60000.00: The specific price at which to place the order.

3. OCO (One Cancels the Other) Order
Places two orders simultaneously: a take-profit order and a stop-loss order. If one is filled, the other is canceled.

Command:

  python bot.py --order_type oco --symbol BTCUSDT --side BUY --quantity 0.002 --take-profit-price 65000 --stop-price 55000

--order_type oco: Specifies an OCO order.

--take-profit-price 65000: The price for the take-profit (limit) order.

--stop-price 55000: The price for the stop-loss (stop-market) order.

# How the Code Works
config.py: This file simply imports the os library to retrieve the BINANCE_API_KEY and BINANCE_API_SECRET values from your system's environment variables. This is the recommended practice for keeping your credentials secure.

get_testnet_client(): This function initializes the UMFutures client from the python-binance library. It uses the API keys from config.py to establish a connection to the Testnet and includes a simple check to ensure the connection is successful.

Order Functions (place_market_order, place_limit_order, place_oco_order): Each of these functions is a dedicated wrapper for the client.new_order() method. They handle the specific parameters required for each order type and include a try...except block to catch and log any BinanceAPIException errors.

main(): This function uses the argparse library to process the command-line arguments you provide. Based on the --order_type argument, it calls the appropriate order placement function with the correct parameters. This makes the script flexible and easy to use.
