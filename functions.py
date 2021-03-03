def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))


say_hi("Kacper", 21)
say_hi("Jeff", 33)


def cube(num):
    return num*num*num  # no statement works after the return, breaks the function


result = cube(2)
print(result)
