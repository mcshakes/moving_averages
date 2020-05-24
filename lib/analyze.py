import sys
from lib.moving_average import MovingAverage


class Analyze:
    def __init__(self, ticker):
        self.ticker = ticker

    def run(self):
        move_avg = MovingAverage()
        data = move_avg.import_data(self.ticker)
