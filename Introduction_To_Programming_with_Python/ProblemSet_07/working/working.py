import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"[0-9]?[0-9](\:[0-5][0-9])? ([APap][Mm])?"
    elems = [elem.group() for elem in re.finditer(pattern, s.lower())]

    if len(elems) < 2:
        raise ValueError

    is_am = lambda e: "am" in e

    t = []

    for elem in elems:
        lhs, rhs = elem[:-3].split(":") if ":" in elem else (elem[:-3], None)

        lhs = int(lhs)

        if lhs > 12 or (rhs and int(rhs) >= 60):
            raise ValueError


        if not is_am(elem) and lhs == 12:
            hours = "00:00"
        else:
            hours = int(lhs) + 12 if not is_am(elem) else int(lhs)

        formatted_time = f"{hours:02d}:{rhs}" if rhs else f"{hours:02d}:00"
        t.append(formatted_time)

    return " to ".join(t)


if __name__ == "__main__":
    main()
