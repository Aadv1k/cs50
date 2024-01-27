nutrition_data = {
    'Apple': {'Calories': 130},
    'Avocado': {'Calories': 50},
    'Banana': {'Calories': 110},
    'Cantaloupe': {'Calories': 50},
    'Grapefruit': {'Calories': 60},
    'Grapes': {'Calories': 90},
    'Honeydew Melon': {'Calories': 50},
    'Kiwifruit': {'Calories': 90},
    'Lemon': {'Calories': 15},
    'Lime': {'Calories': 20},
    'Nectarine': {'Calories': 60},
    'Orange': {'Calories': 80},
    'Peach': {'Calories': 60},
    'Pear': {'Calories': 100},
    'Pineapple': {'Calories': 50},
    'Plums': {'Calories': 70},
    'Strawberries': {'Calories': 50},
    'Sweet Cherries': {'Calories': 100},
    'Tangerine': {'Calories': 50},
    'Watermelon': {'Calories': 80},
}


def main():
    fruit = input("Enter a fruit: ")
    fruit = fruit.title()

    if fruit in nutrition_data:
        calories = nutrition_data[fruit]['Calories']
        print(f"Calories: {calories}")
    else:
        print("")


if __name__ == "__main__":
    main()
