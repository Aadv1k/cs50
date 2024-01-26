import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def guess_number():
    return random.randint(1, level)


def get_user_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            print("Please enter a valid integer.")


def main():
    global level
    level = get_level()
    secret_number = guess_number()

    while True:
        user_guess = get_user_guess()

        if user_guess < secret_number:
            print("Too small!")
        elif user_guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
