def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year!")
            else:
                print("This is not a leap year.")
        else:
            print("This is a leap year!")
    else:
        print("Not a leap year.")

print("This is a leap year checker program")
input_year = int(input("Input the year you would like to check: "))

is_leap_year(input_year)

