import sys
from lib.simple_moving_average import SimpleMovingAverage
import datetime
from lib.news_headlines import NewsHeadlines
from lib.vader_scores import VaderScore


def _fifty_days_prior():
    today = datetime.datetime.now()
    delta = datetime.timedelta(days=50)
    target = today - delta

    return target.strftime("%d %b %Y")


class Analyze:
    def __init__(self, ticker):
        self.ticker = ticker
        self.simple_move_avg = None

    def run(self):
        data = self.import_data()
        self.crossover(data)
        self.plot_graph(data)

        data_frame = self.news_data()
        self.vader_scores(data_frame)

    def import_data(self):
        target_date = _fifty_days_prior()

        self.simple_move_avg = SimpleMovingAverage()
        return self.simple_move_avg.import_data(self.ticker, target_date)

    def crossover(self, financial_data):
        self.simple_move_avg.find_moving_crossover(financial_data)

    def plot_graph(self, financial_data):
        self.simple_move_avg.plot_avgs_crossover(financial_data)

    def news_data(self):
        url = 'https://newsapi.org/v2/everything?'
        news = NewsHeadlines(url, self.ticker)
        api_resp = news.extract_data()
        data_frame = news.json_data_frame(api_resp)
        data = news.clean(data_frame)
        return data

    def vader_scores(self, json_df):
        vd_score = VaderScore()
        vd_score.compound_vader_scores(json_df)
