import pytest

from lib.analyze import Analyze


def test_analyze_accepts_string():
    a = Analyze("SPY")
    assert a.ticker == "SPY"


def test_analyze_does_not_accept_integers():
    a = Analyze(123)
    assert a.ticker != 123
