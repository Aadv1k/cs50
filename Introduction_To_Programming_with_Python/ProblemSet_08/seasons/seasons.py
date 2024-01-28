from datetime import datetime

import re
import inflect

import sys

infl_engine = inflect.engine()

def calculate_time_in_minutes_as_word(date1, date2) -> str:
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
    except ValueError:
        raise

    minutes = round(abs((d2 - d1).total_seconds()) / 60)

    word = re.sub(r"\b ?(and) ?\b", " ", infl_engine.number_to_words(minutes))
    return f"{word[0].upper() + word[1:]} minutes"

def main():
    inp = input("Date of Birth (YYYY-MM-DD): ")
    today = str(date.today())

    try:
        out = calculate_time_in_minutes_as_word(inp, today)
    except ValueError:
        print("Invalid date format")
        sys.exit(1)

    print(f"{out}")

if __name__ == "__main__":
    main()
