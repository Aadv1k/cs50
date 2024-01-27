def main():
    print("Valid" if is_valid(input("Input: ")) else "Invalid")


def is_valid(s):
    if not (len(s) >= 2 and len(s) <= 6):
        return False

    if any((i in s for i in [" ", ".", "?"])):
        return False

    nums = [i for i in s if i.isdigit()]
    if len(nums) and nums[0] == '0':
        return False

    if len(nums) and not (s[0].isdigit() or s[-1:].isdigit()):
        return False

    return True


if __name__ == "__main__":
    main()
