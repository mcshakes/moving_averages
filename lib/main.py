# # from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# # analyzer = SentimentIntensityAnalyzer()
# import nltk

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.downloader.download('vader_lexicon')

# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# analyzer = SentimentIntensityAnalyzer()
# import nltk

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.downloader.download('vader_lexicon')

import sys


def begin():
    choice = None

    while choice != "quit":

        choice = input("\nGive the stock ticker to look up: ")

        # print("Your input was a ", type(choice))

        if choice == "text":
            print("Do something")
        elif choice == "quit":
            print("\nThanks for playing")
        else:
            print("\nI didn't understand that... ")


print("Let's look up some Moving Averages for your favorite stock")
begin()
