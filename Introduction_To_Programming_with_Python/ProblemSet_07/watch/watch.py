import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"https?://(www\.)?youtube\.com/embed/[\w-]+"
    found = re.search(pattern, s)
    return f"https://youtu.be/{found.group().split('/').pop()}" if found else None


if __name__ == "__main__":
    main()
