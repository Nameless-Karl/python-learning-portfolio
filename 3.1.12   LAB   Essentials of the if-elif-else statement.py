year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year%4 != 0:
        print("It is a common year")
    elif year % 100 != 0:
        print("It is a leap year")
    elif year % 400 != 0:
        print("It is a common year")
    else:
        print("It is a leap year")
# if flag = True:
#     print("It is a leap year")
# else:
#     print("It is a common year")