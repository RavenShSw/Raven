# Task 1: Leap Year Checker

year = int(input("Enter any year past, present, or future: "))

if year % 4 == 0 and year % 400 == 0:
    print("Yay! Another February 29th for the century!")
elif year % 100 != 0 and year % 4 == 0:
    print("Cool! Another February 29th for the year!")
elif year % 400 != 0 or year % 4 != 0: 
    print("No leaps this year.")
