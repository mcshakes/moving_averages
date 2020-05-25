import pandas as pd
import numpy as np

import pandas_datareader as pandas_data_reader
import matplotlib.pyplot as plt


class SimpleMovingAverage:

    def __init__(self):
        self.trade_buy = []
        self.trade_sell = []

    def import_data(self, ticker, date):
        data_returned = pandas_data_reader.get_data_yahoo(ticker, date)
        data_returned['2_SMA'] = data_returned['Close'].rolling(
            window=2).mean()

        data_returned['5_SMA'] = data_returned['Close'].rolling(
            window=5).mean()

        data_returned = data_returned[data_returned['5_SMA'].notna()]

        return data_returned

    def find_moving_crossover(self, data):

        for i in range(len(data)-1):
            if ((data['2_SMA'].values[i] < data['5_SMA'].values[i]) & (data['2_SMA'].values[i+1] > data['5_SMA'].values[i+1])):
                print("Trade Call for {row} is Buy.".format(
                    row=data.index[i].date()))
                self.trade_buy.append(i)
            elif ((data['2_SMA'].values[i] > data['5_SMA'].values[i]) & (data['2_SMA'].values[i+1] < data['5_SMA'].values[i+1])):
                print("Trade Call for {row} is Sell.".format(
                    row=data.index[i].date()))
                self.trade_sell.append(i)

        print(self.trade_buy)
        print(self.trade_sell)

        # plt.figure(figsize=(20, 10), dpi=80)
        # plt.plot(data_returned.index, data_returned['Close'])
        # plt.plot(data_returned.index, data_returned['2_SMA'], '-^',
        #          markevery=Trade_Buy, ms=15, color='green')
        # plt.plot(data_returned.index, data_returned['5_SMA'], '-v',
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
