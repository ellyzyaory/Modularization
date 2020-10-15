import calendar

def text_calendar(yy, mm):
    return calendar.month(yy, mm, 0, 1)

if __name__ == "__main__":
    year = int(input("Enter the year  : "))
    month = int(input("Enter the month: "))
    print(text_calendar(year, month))


