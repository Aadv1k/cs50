import sys
import csv

def scourgify(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                full_name = row['name'].strip('"')
                last_name, first_name = map(str.strip, full_name.split(','))
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    except Exception as e:

        sys.exit(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    scourgify(input_file, output_file)
    print(f"Scourgification complete! Check {output_file} for the cleaned data.")

if __name__ == "__main__":
    main()
