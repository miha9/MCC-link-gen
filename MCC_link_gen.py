# Install Python 3.0, pip for python and the ccxt lib (recomended CMD --> pip install ccxt) the lib might also require the requests lib.

import ccxt
import operator

n_coins = 20
bina = ccxt.binance()
markets_dic = {}
tickers = bina.fetch_tickers()
link = "https://www.multicoincharts.com/"
for ticker in tickers:
    if ticker.find("/BTC") != -1:
        #print(ticker, tickers[ticker]["quoteVolume"])
        markets_dic[ticker] = tickers[ticker]["quoteVolume"]
sorted_markets = sorted(markets_dic.items(),  key= operator.itemgetter(1), reverse=True)
for market in range(n_coins):
    #print(sorted_markets[market][0])
    temp_str = (sorted_markets[market][0]).replace("/", "")
    if market == 0:
        link = link + "?chart=BINANCE:" + temp_str
    else:
        link = link + "&chart=BINANCE:" + temp_str

print(link)
