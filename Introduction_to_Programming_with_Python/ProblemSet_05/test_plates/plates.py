def main():
    pass


def is_valid(s):
    if len(s) != 6:
        return False

    letters = s[:3]
    numbers = s[3:]

    if not letters.isalpha() or not numbers.isdigit():
        return False

    if letters.islower():
        return False

    if numbers.startswith("0"):
        return False

    return True


if __name__ == "__main__":
    main()
