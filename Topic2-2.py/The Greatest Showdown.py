#Task 1: Identify the Greatest

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
    
if num1 > num2 and num2 > num3:
    print("The first entered number is the largest.") 
elif num1 < num2 and num2 > num3:
    print("The second entered number is the largest.")
elif num1 < num3 and num2 < num3:
    print("The third entered number is the largest.") 
else:
    print("All numbers are of the same value.")

#Task 2: Identify the Smallest (too)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
    
if num1 > num2 and num2 > num3:
    print("The first entered number is the largest.") 
elif num1 < num2 and num2 > num3:
    print("The second entered number is the largest.")
elif num1 < num3 and num2 <num3:
    print("The third entered number is the largest.") 
if num1 < num2 and num2 < num3:
    print("The first entered number is the smallest.") 
elif num1 > num2 and num2 < num3:
    print("The second entered number is the smallest.")
elif num1 > num3 and num2 > num3:
    print("The third entered number is the smallest.") 
else:
    print("All numbers are of the same value.")