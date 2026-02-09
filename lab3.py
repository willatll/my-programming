# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def identify_weekday_or_weekend(day_number):
    if day_number == 6:
        print("its a weekend")
    elif day_number == 7:
        print("its a weekend")
    elif 1<= day_number <= 5:
        print("its a weekday")
    else:
        print("invalid input. Please enter a number between 1 and 7")

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_of_week(day_number):
    if day_number == 1:
        print("It's a Monday")
    elif day_number == 2:
        print("its a tuesday")
    elif day_number == 3:
        print("its a wednesday")
    elif day_number == 4:
        print("its a thursday")
    elif day_number ==5:
        print("its a friday")
    elif day_number == 6:
        print("its a saturday")
    elif day_number == 7:
        print("its a sunday")
    else:
        print("invalid input. Please enter a number between 1 and 7")

if __name__ == '__main__' :
    num = int(input("weekend? or weekday?"))
    identify_weekday_or_weekend(num)
    num = int(input("name of the day of the week?"))
    get_day_of_week(num)