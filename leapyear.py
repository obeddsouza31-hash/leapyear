# date_utils.py

def is_leap(y):
    """Return True if year y is a leap year, False otherwise."""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def days_in_month(m, y):
    """Return the number of days in month m (1-12) of year y."""
    if m < 1 or m > 12:
        raise ValueError(f"Invalid month: {m}. Must be between 1 and 12.")
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif m in (4, 6, 9, 11):
        return 30
    else:
        return 29 if is_leap(y) else 28


def day_of_year(d, m, y):
    """Return the ordinal day number (1-366) for date (d, m, y)."""
    max_days = days_in_month(m, y)
    if d < 1 or d > max_days:
        raise ValueError(f"Invalid day {d} for month {m} in year {y}.")
    total_days = sum(days_in_month(month, y) for month in range(1, m)) + d
    return total_days


if __name__ == "__main__":
    print("is_leap(2024):", is_leap(2024))
    print("is_leap(1900):", is_leap(1900))
    print("days_in_month(2, 2024):", days_in_month(2, 2024))
    print("days_in_month(2, 2025):", days_in_month(2, 2025))
    print("day_of_year(15, 3, 2024):", day_of_year(15, 3, 2024))
    print("day_of_year(31, 12, 2024):", day_of_year(31, 12, 2024))
