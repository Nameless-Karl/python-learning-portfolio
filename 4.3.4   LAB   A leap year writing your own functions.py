def is_year_leap(year):
    # A year is a leap year if it meets the following conditions:
    #  It is evenly divisible by 4.
    # EXCEPTION 1: If it is also evenly divisible by 100, it is not a leap year.
    # EXCEPTION 2: Unless it is also evenly divisible by 400, in which case it is a leap year. 
    
    # Write your code here.
    while year % 4 == 0:
        leap_year = True
        if leap_year:
            if year % 100 != 0:
                leap_year = True
                return leap_year
            elif year % 400 == 0:
                leap_year = True
                return leap_year
            else:
                leap_year = False
                return leap_year
    else:
        leap_year = False
            
        return leap_year
            
    #
    

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
