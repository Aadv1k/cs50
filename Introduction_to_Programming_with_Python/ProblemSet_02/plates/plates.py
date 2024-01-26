def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or not s[:2].isalpha():
        return False

    if not 2 <= len(s) <= 6:
        return False

    if any(c.isdigit() for c in s[:-1]) or s[-1].isdigit():
        return False

    if s[-1] == '0':
        return False

    if any(not c.isalnum() for c in s):
        return False

    return True


if __name__ == "__main__":
    main()
