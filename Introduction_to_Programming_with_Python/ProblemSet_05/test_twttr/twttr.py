def main():
    pass


def shorten(word):
    return "".join([i for i in word
                   if i.lower() not in "aeiou"])


if __name__ == "__main__":
    main()
