from binance.spot import Spot as Client

APIS = ['https://api.binance.com', 'https://api1.binance.com', 'https://api2.binance.com', 'https://api3.binance.com']
TEST = 'https://testnet.binance.vision'
KEY = 'Trr8kSXclstFqPPxqKNzvqhRZop1eHy5XbGZRJNBNKsl4pPfHY27dRbkmhmGxxad'
SECRET = 'UiN5mNznGf4pFwP6i1rEoyzNKUwkHMZAPSH7uUIzblbsxLQcIO1Bs5Bt2Df1s56U'

client = Client(key=KEY, secret=SECRET, base_url=TEST)
print(client.time())

# Get account information
print(client.account())

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': 0.002,
    'price': 9500
}

response = client.new_order(**params)
print(response)
