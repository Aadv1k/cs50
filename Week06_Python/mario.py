def print_p(i, height):
    hc = i + 1
    sc = height - (i + 1)

    for j in range(sc):
        print(' ', end='')

    for j in range(hc):
        print('#', end='')

    print('  ', end='')

    for j in range(hc):
        print('#', end='')

def main():
    height = 0

    while height < 1 or height > 8:
        try:
            height = int(input("Height: "))
        except ValueError:
            continue

    for i in range(height):
        print_p(i, height)
        print()

if __name__ == "__main__":
    main()
