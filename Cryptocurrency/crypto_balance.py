#CCXT(CryptoCurrency eXchange Trading) 
import os
from dotenv import load_dotenv
import ccxt
import pandas as pd

load_dotenv()

api_key = os.environ['bn_apikey']
api_secret = os.environ['bn_secret']

bbb = ccxt.binance(config={'apiKey': api_key, 'secret': api_secret})

# spot 
balanceSpot = bbb.fetch_balance()['total']
spot = pd.DataFrame(list(balanceSpot.items()), columns=['name', 'balance'])
spot_usdt = balanceSpot['USDT']

# coin-m
balanceCoinm = bbb.fetch_balance(params={"type": 'delivery'})['total']
Coinm = pd.DataFrame(list(balanceCoinm.items()), columns=['name', 'balance'])

#futures usds
balanceUsds = bbb.fetch_balance(params={"type": "future"})
future_usd = balanceUsds['total']['USDT'] 

# spot and coin-m
total = pd.concat([spot, Coinm])
total = total[total['balance'] > 0]

print(future_usd)