def main():
    pass


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    else:
        return 20 if greeting[0].lower() == 'h' else 100


if __name__ == "__main__":
    main()
