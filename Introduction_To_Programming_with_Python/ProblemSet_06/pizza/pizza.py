import sys
import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def print_pizza_table(file_path):
    pizza_data = read_csv(file_path)

    headers = pizza_data[0].keys()
    max_col_widths = {header: max(len(str(row[header])) for row in pizza_data) for header in headers}
    total_width = sum(max_col_widths.values()) + len(headers) * 3 - 1

    print(f"+{'-' * total_width}+")
    print(f"| {' | '.join(header.ljust(max_col_widths[header]) for header in headers)} |")
    print(f"+{'-' * total_width}+")

    for row in pizza_data:
        print(f"| {' | '.join(str(row[header]).ljust(max_col_widths[header]) for header in headers)} |")

    print(f"+{'-' * total_width}+")

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith('.csv'):
        sys.exit("Not a CSV file")

    print_pizza_table(file_path)

if __name__ == "__main__":
    main()
