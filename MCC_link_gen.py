# This script provides the link to MCC for the top volume coins on Binance. No need to enter the markets manually anymore!

# 2 ways to get it running:
# Easy way: Go to https://repl.it, select Python3, copy the code below and click Run
# Pro way: Install Python 3.0, pip for python and the ccxt lib (recomended CMD --> pip install ccxt) the lib might also require the requests lib.

# If you feel like donating, give your money to the guys that created https://www.multicoincharts.com/

########################################### COPY FROM HERE TO THE END ###################################################

import ccxt
import operator

# Change this number to the number of charts you want to load
n_coins = 20

# This determines if the second link shows the biggest 24h pump or biggest dump;
# Change this to False to get the coins with the biggest 24h dump
pump = True

################################################################################################
bina = ccxt.binance()
markets_vol_dic = {}
markets_percent_dic = {}
tickers = bina.fetch_tickers()
link_vol = "https://www.multicoincharts.com/"
link_percentage = "https://www.multicoincharts.com/"
for ticker in tickers:
    if ticker.find("/BTC") != -1:
        #print(ticker, tickers[ticker]["percentage"])
        markets_vol_dic[ticker] = tickers[ticker]["quoteVolume"]
        markets_percent_dic[ticker] = tickers[ticker]["percentage"]
sorted_markets_vol = sorted(markets_vol_dic.items(), key= operator.itemgetter(1), reverse=True)
sorted_markets_percentage = sorted(markets_percent_dic.items(), key= operator.itemgetter(1), reverse=pump)
for market in range(n_coins):
    #print(sorted_markets[market][0])
    temp_str_vol = (sorted_markets_vol[market][0]).replace("/", "")
    temp_str_percentage = (sorted_markets_percentage[market][0]).replace("/", "")
    if market == 0:
        link_vol = link_vol + "?chart=BINANCE:" + temp_str_vol
        link_percentage = link_percentage + "?chart=BINANCE:" + temp_str_percentage
    else:
        link_vol = link_vol + "&chart=BINANCE:" + temp_str_vol
        link_percentage = link_percentage + "&chart=BINANCE:" + temp_str_percentage

print("Highest volume coins:")
print(link_vol)
print("")
if pump is True:
    print("Biggest 24h pump:")
else:
    print("Biggest 24h dump:")
print(link_percentage)