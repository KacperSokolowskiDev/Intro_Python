
try:  # tries the code
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:  # prints errors
    print(err)
except ValueError:
    print("Invalid Input")
