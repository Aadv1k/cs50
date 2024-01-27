def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if denominator == 0:
            raise ZeroDivisionError

        if not (isinstance(numerator, int) and isinstance(denominator,
                int) and denominator != 0 and numerator <= denominator):
            raise ValueError

        percentage = round((numerator / denominator) * 100)
        return percentage
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"
    except ValueError:
        raise
