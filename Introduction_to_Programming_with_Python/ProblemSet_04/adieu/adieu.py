def bid_adieu(names):
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"
        print(farewell)


def main():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        bid_adieu(names)


if __name__ == "__main__":
    main()
