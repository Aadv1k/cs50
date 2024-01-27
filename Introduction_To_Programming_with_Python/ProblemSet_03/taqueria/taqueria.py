menu_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.00

try:
    while True:
        print("Enter an item: ", end="")
        item = input()
        item = item.title()

        if item in menu_prices:
            total_cost += menu_prices[item]
            print(f"Total: ${total_cost:.2f}")
        elif not item:
            pass
        else:
            continue

except EOFError:
    pass
