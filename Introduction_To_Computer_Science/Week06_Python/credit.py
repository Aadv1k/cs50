def main():
    card_number = ""

    while not card_number or len(card_number) == 0:
        card_number = input("Number: ")

    sum = 0
    digit_count = 0

    for i in range(len(card_number) - 1, -1, -1):
        digit = int(card_number[i])

        if digit_count % 2 == 1:
            digit *= 2

            if digit > 9:
                digit = digit % 10 + 1

        sum += digit
        digit_count += 1

    if sum % 10 == 0:
        if (len(card_number) == 15 and (card_number.startswith("34") or card_number.startswith("37"))):
            print("AMEX")
        elif (len(card_number) == 16 and card_number.startswith(("51", "52", "53", "54", "55"))):
            print("MASTERCARD")
        elif (len(card_number) == 13 or len(card_number) == 16) and card_number.startswith("4"):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
