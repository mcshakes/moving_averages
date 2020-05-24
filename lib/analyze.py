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

    def run(self):
        target_date = _fifty_days_prior()

        move_avg = SimpleMovingAverage()
        data = move_avg.import_data(self.ticker, target_date)
