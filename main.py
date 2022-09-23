# Printing out the numbers 1-100, but if the number is divisible by 3, it prints Fizz, if the number
# is divisible by 5, it prints Buzz, and if the number is divisible by both 3 and 5, it prints
# FizzBuzz.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
         
        