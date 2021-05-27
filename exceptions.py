try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    print(x / y)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
    y = 1
    print(x / y)
finally:
    print("DONE")
    

# Asserting errors
x = 100
y = 20

assert(x < y)

# Raising exceptions 
def some_func():
    if True:
        raise Exception("Something went bad")
    

some_func()