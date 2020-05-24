import sys
from lib.analyze import Analyze


def begin():
    choice = None

    # while choice != "quit":

    choice = input("\nGive the stock ticker to look up: ")

    if choice != "quit":
        print(f"You chose {choice}...")
        print(f"We will analyze {choice} from 50 days prior")

        anal = Analyze(choice)
        anal.run()
    else:
        print(f"Your input was a {choice}. Are you sure?")


print("Let's look up some Moving Averages for your favorite stock")
begin()
