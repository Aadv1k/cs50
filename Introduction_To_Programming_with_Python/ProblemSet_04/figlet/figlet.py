import sys
import pyfiglet


def main():
    if len(sys.argv) not in [1, 3] or (len(sys.argv)
                                       == 3 and sys.argv[1] not in ['-f', '--font']):
        sys.exit("Invalid usage")

    font = None
    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font'] or not sys.argv[2]:
            sys.exit("Invalid usage")
        font = sys.argv[2]

    text = input("Enter text: ")

    if font:
        try:
            ascii_art = pyfiglet.figlet_format(text, font=font)
            print(ascii_art)
        except pyfiglet.FigletError:
            sys.exit("Invalid usage")
    else:
        ascii_art = pyfiglet.figlet_format(text)
        print(ascii_art)


if __name__ == "__main__":
    main()
