import pandas as pd
import numpy as np

import pandas_datareader as pandas_data_reader
import matplotlib.pyplot as plt


class SimpleMovingAverage:

    def import_data(self, ticker, date):
        data_acb = pandas_data_reader.get_data_yahoo(ticker, date)
        print(data_acb)
# SMA = Simple Moving Average


# data_acb['2_SMA'] = data_acb['Close'].rolling(window=2).mean()
# data_acb['5_SMA'] = data_acb['Close'].rolling(window=5).mean()

# data_acb = data_acb[data_acb['5_SMA'].notna()]

# Trade_Buy = []
# Trade_Sell = []

# for i in range(len(data_acb)-1):
#     if ((data_acb['2_SMA'].values[i] < data_acb['5_SMA'].values[i]) & (data_acb['2_SMA'].values[i+1] > data_acb['5_SMA'].values[i+1])):
#         print("Trade Call for {row} is Buy.".format(
#             row=data_acb.index[i].date()))
#         Trade_Buy.append(i)
#     elif ((data_acb['2_SMA'].values[i] > data_acb['5_SMA'].values[i]) & (data_acb['2_SMA'].values[i+1] < data_acb['5_SMA'].values[i+1])):
#         print("Trade Call for {row} is Sell.".format(
#             row=data_acb.index[i].date()))
#         Trade_Sell.append(i)

# plt.figure(figsize=(20, 10), dpi=80)
# plt.plot(data_acb.index, data_acb['Close'])
# plt.plot(data_acb.index, data_acb['2_SMA'], '-^',
#          markevery=Trade_Buy, ms=15, color='green')
# plt.plot(data_acb.index, data_acb['5_SMA'], '-v',
#          markevery=Trade_Sell, ms=15, color='red')
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Price in Dollars', fontsize=14)
# plt.xticks(rotation='60', fontsize=12)
# plt.yticks(fontsize=12)
# plt.title('Trade Calls - Moving Averages Crossover', fontsize=16)
# plt.legend(['Close', '2_SMA', '5_SMA'])
# plt.grid()
# plt.show()


# https://blog.quantinsti.com/moving-average-trading-strategies/
# Read Simple Moving Averages
