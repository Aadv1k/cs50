def main():
    time_str = input("What time is it? ")
    meal_time = check_meal_time(time_str)

    if meal_time:
        print(meal_time + " time")


def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def check_meal_time(time_str):
    time = convert(time_str)

    if 7 <= time < 8:
        return "Breakfast"
    elif 12 <= time <= 13:
        return "Lunch"
    elif 18 <= time < 19:
        return "Dinner"
    else:
        return None


if __name__ == "__main__":
    main()
