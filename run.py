import sys
from lib.analyze import Analyze
from dotenv import load_dotenv
load_dotenv()


def begin():

    while True:
        try:
            print("")
            choice = input("\nGive the stock ticker to look up: ")

            if not choice:
                raise ValueError("Can't look up an empty space. Give a ticker")

            if not choice.isalpha():
                raise ValueError("Can't take integer inputs")

            print("")
            print(f"We will analyze {choice} from 50 days prior")

            anal = Analyze(choice)
            anal.run()
            break
        except Exception as e:
            print("A problem => ", e)


print("")
print("Let's look up some Moving Averages for your favorite stock")
begin()
