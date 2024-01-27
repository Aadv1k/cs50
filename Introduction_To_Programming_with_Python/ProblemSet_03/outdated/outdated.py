from datetime import datetime


def month_to_number(month):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return months.index(month) + 1


def convert_to_iso_date():
    while True:
        user_input = input(
            "Date: ")
        user_input = user_input.strip()

        try:
            date_obj = datetime.strptime(user_input, "%m/%d/%Y")

        except ValueError:
            try:
                date_obj = datetime.strptime(user_input, "%B %d, %Y")

            except ValueError:
                print("Invalid date. Please try again.")
                continue

        iso_date = date_obj.strftime("%Y-%m-%d")
        print(iso_date)
        break


if __name__ == "__main__":
    convert_to_iso_date()
