import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = re.compile(r"\b(um)\b")
    return len(re.findall(pattern, s.strip().lower()))


if __name__ == "__main__":
    main()
