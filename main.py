from typing import List

# AI
# Return list of investment opportunities - To make profit
def should_invest(?) -> List[?]:
    pass

# Return list of investments to pull out of - Avoid loss
def should_pull_out(?) -> List[?]:
    pass

# If possible - do shorting
def should_short(?) -> List[?]:
    pass

# If possible - do longing
def should_long(?) -> List[?]:
    pass

# Take into account all opportunities and prepare list of decisions to be made with the exact amounts
def decide(?) -> List[?]:
    pass


# Transaction handler
# Give command for binance API to sell certain coin at a given amount and price
def set_sell(symbol: str, amount: float, price: float) -> None:
    pass

#Give command to binance API to buy certain coin at a given amount and price
def set_buy(symbol: str, amount: float, price: float) -> None:
    pass


# Get information
# Get information about certain coin(s) - min/max buy, price, etc.
def get_coin_info():
    pass

# Get our account information - Usable money, etc.
def get_account_info():
    pass


# Database
# Use this function for AI to make decisions based on past candles
def get_coin_history():
    pass

# Add new candles to the database for future usage
def append_coin_history():
    pass


# Main loop

def main():
    # connect the API and WEBSOCKET
    connect()
    while True:
        # Make decisions
        sell, buy = decide()

        # Act based on decisions
        for i in sell:
            set_sell()

        for i in buy:
            set_buy()