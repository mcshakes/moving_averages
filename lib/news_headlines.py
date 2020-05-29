import os

from pandas.tseries.offsets import BDay
import requests
import pandas as pd
import nltk
import pandas_datareader as pandas_data_reader
import matplotlib.pyplot as plt

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class NewsHeadlines:
    def __init__(self, url, ticker):
        self.url = url
        self.ticker = ticker

    def extract_data(self):

        parameters = {
            'q': self.ticker,  # query phrase
            'sortBy': 'popularity',  # articles from popular sources and publishers come first
            'language': 'en',
            'pageSize': 100,  # maximum is 100 for developer version
            'apiKey': os.getenv("NEWS_API_KEY")
        }

        return requests.get(self.url, params=parameters)

# Convert the response to JSON format and store it in dataframe
    def json_data_frame(self, response):
        data = pd.DataFrame(response.json())

        news_df = pd.concat([data['articles'].apply(pd.Series)], axis=1)

        final_news = news_df.loc[:, ['publishedAt', 'title']]
        final_news['publishedAt'] = pd.to_datetime(final_news['publishedAt'])
        final_news.sort_values(by='publishedAt', inplace=True)

        return final_news


# Import BDay to determine business day's dates

# to get the business day for which particular news headline should be used to make trade calls


# def get_trade_open(date):
#     curr_date_open = pd.to_datetime(date).floor(
#         'd').replace(hour=13, minute=30) - BDay(0)
#     curr_date_close = pd.to_datetime(date).floor(
#         'd').replace(hour=20, minute=0) - BDay(0)

#     prev_date_close = (curr_date_open - BDay()).replace(hour=20, minute=0)
#     next_date_open = (curr_date_close + BDay()).replace(hour=13, minute=30)

#     if ((pd.to_datetime(date) >= prev_date_close) & (pd.to_datetime(date) < curr_date_open)):
#         return curr_date_open
#     elif ((pd.to_datetime(date) >= curr_date_close) & (pd.to_datetime(date) < next_date_open)):
#         return next_date_open
#     else:
#         return None


#  # Apply the above function to get the trading time for each news headline
# final_news["trading_time"] = final_news["publishedAt"].apply(get_trade_open)

# final_news = final_news[pd.notnull(final_news['trading_time'])]
# final_news['Date'] = pd.to_datetime(
#     pd.to_datetime(final_news['trading_time']).dt.date)


# # ==================== Compound Vader Scores ======================

# analyzer = SentimentIntensityAnalyzer()

# cs = []
# for row in range(len(final_news)):
#     cs.append(analyzer.polarity_scores(
#         final_news['title'].iloc[row])['compound'])

# final_news['compound_vader_score'] = cs
# final_news = final_news[(final_news[['compound_vader_score']] != 0).all(
#     axis=1)].reset_index(drop=True)

# final_news.head()

# # ==================== Extreame values ======================


# unique_dates = final_news['Date'].unique()
# grouped_dates = final_news.groupby(['Date'])
# keys_dates = list(grouped_dates.groups.keys())

# max_cs = []
# min_cs = []

# for key in grouped_dates.groups.keys():
#     data = grouped_dates.get_group(key)
#     if data["compound_vader_score"].max() > 0:
#         max_cs.append(data["compound_vader_score"].max())
#     elif data["compound_vader_score"].max() < 0:
#         max_cs.append(0)

#     if data["compound_vader_score"].min() < 0:
#         min_cs.append(data["compound_vader_score"].min())
#     elif data["compound_vader_score"].min() > 0:
#         min_cs.append(0)

# extreme_scores_dict = {'Date': keys_dates,
#                        'max_scores': max_cs, 'min_scores': min_cs}
# extreme_scores_df = pd.DataFrame(extreme_scores_dict)


# # ==================== Final VADER scores ======================

# final_scores = []
# for i in range(len(extreme_scores_df)):
#     final_scores.append(
#         extreme_scores_df['max_scores'].values[i] + extreme_scores_df['min_scores'].values[i])

# extreme_scores_df['final_scores'] = final_scores

# # extreme_scores_df.head()


# # ==================== GERENATE Trade Calls ======================

# # Considering the volatile behavior of markets these days,
# # we'll use 0.20 as threshold value for making trade calls in our model.

# vader_Buy = []
# vader_Sell = []
# for i in range(len(extreme_scores_df)):
#     if extreme_scores_df['final_scores'].values[i] > 0.20:
#         print("Trade Call for {row} is Buy.".format(
#             row=extreme_scores_df['Date'].iloc[i].date()))
#         vader_Buy.append(extreme_scores_df['Date'].iloc[i].date())
#     elif extreme_scores_df['final_scores'].values[i] < -0.20:
#         print("Trade Call for {row} is Sell.".format(
#             row=extreme_scores_df['Date'].iloc[i].date()))
#         vader_Sell.append(extreme_scores_df['Date'].iloc[i].date())

# # ==================== PLOTTING ======================
# data_acb = pandas_data_reader.get_data_yahoo('ACB', '24-Feb-20')

# # vader_buy = []
# # for i in range(len(data_acb)):
# #     if data_acb.index[i].date() in vader_Buy:
# #         vader_buy.append(i)

# # vader_sell = []
# # for i in range(len(data_acb)):
# #     if data_acb.index[i].date() in vader_Sell:
# #         vader_sell.append(i)

# # plt.figure(figsize=(20, 10), dpi=80)
# # plt.plot(data_acb.index, data_acb['Close'], '-^',
# #          markevery=vader_buy, ms=15, color='green')
# # plt.plot(data_acb.index, data_acb['Close'], '-v',
# #          markevery=vader_sell, ms=15, color='red')
# # plt.plot(data_acb.index, data_acb['Close'])
# # plt.xlabel('Date', fontsize=14)
# # plt.ylabel('Price in Dollars', fontsize=14)
# # plt.xticks(rotation='60', fontsize=12)
# # plt.yticks(fontsize=12)
# # plt.title('Trade Calls - VADER', fontsize=16)
# # plt.legend(['Buy', 'Sell', 'Close'])
# # plt.grid()
# # plt.show()

# # prioritising SMA signals
