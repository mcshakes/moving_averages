import sys
from lib.simple_moving_average import SimpleMovingAverage
import datetime


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

    def import_data(self):
        target_date = _fifty_days_prior()

        self.simple_move_avg = SimpleMovingAverage()
        return self.simple_move_avg.import_data(self.ticker, target_date)

    def crossover(self, financial_data):
        self.simple_move_avg.find_moving_crossover(financial_data)
