def isLeapYear(year):
    """Function to check if a year is a leap year."""
    if year % 4 == 0:  # If the year is divisible by 4
        if year % 100 == 0:  # But not divisible by 100
            if year % 400 == 0:  # Unless it's divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def countSundaysOnFirst():
    """Function to count the number of Sundays falling on the first of the month."""
    dayOfWeek = 2  # 1 Jan 1901 was a Tuesday (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
    sundayCount = 0

    # Loop through each year from 1901 to 2000
    for year in range(1901, 2001):
        # Loop through each month from January to December
        for month in range(1, 13):
            # Determine the number of days in the current month
            if month in [4, 6, 9, 11]:
                daysInMonth = 30
            elif month == 2:
                if isLeapYear(year):
                    daysInMonth = 29
                else:
                    daysInMonth = 28
            else:
                daysInMonth = 31

            # Check if the first day of the month is a Sunday
            if dayOfWeek == 6:
                sundayCount += 1

            # Update the day of the week for the next month
            dayOfWeek = (dayOfWeek + daysInMonth) % 7

    return sundayCount

# Call the function and print the result
print(countSundaysOnFirst())
