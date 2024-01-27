import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    s = [i.isdigit() and int(i) <= 255 for i in ip.strip().split(".")]
    return all(s) and len(s) == 4

if __name__ == "__main__":
    main()
