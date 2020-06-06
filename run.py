import traceback
import sys
from lib.analyze import Analyze
from dotenv import load_dotenv
load_dotenv()


def begin():

    while True:
        try:
            print("")
            choice = input("\nGive the stock ticker to look up: ")

            if choice == "done":
                break

            if not choice:
                raise ValueError("Can't look up an empty space. Give a ticker")
                continue

            if not choice.isalpha():
                raise ValueError("Can't take integer inputs")
                continue

            print("")
            print(f"We will analyze {choice} from 50 days prior")

            anal = Analyze(choice)
            anal.run()
            break
        except Exception:
            print("")
            traceback.print_exc()


print("")
print("Let's look up some Moving Averages for your favorite stock")
begin()
