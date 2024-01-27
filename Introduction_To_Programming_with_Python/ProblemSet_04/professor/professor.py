import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        user_answer = prompt_for_answer(problem)

        if user_answer == x + y:
            print("Correct!")
            score += 1
        else:
            print("EEE")
            correct_answer = x + y
            for _ in range(2):  # Allowing up to three tries
                user_answer = prompt_for_answer(problem)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
            else:
                print(f"The correct answer is {correct_answer}")

    print(f"Your score is: {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

    return x, y


def prompt_for_answer(problem):
    while True:
        try:
            user_answer = int(input(problem))
            return user_answer
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
