def main():
    while True:
        try:
            fraction_str = input("Enter a fraction (X/Y): ")
            numerator, denominator = map(int, fraction_str.split('/'))

            if not (isinstance(numerator, int) and isinstance(
                    denominator, int) and denominator != 0 and numerator <= denominator):
                raise ValueError

            percentage = round((numerator / denominator) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")


if __name__ == "__main__":
    main()
