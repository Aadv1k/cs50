import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

    total_cost = bitcoins_to_buy * bitcoin_price
    print(
        f"The current cost of {bitcoins_to_buy:,.4f} Bitcoins is ${total_cost:,.4f}")


if __name__ == "__main__":
    main()
