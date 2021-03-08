def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))


say_hi("Kacper", 21)
say_hi("Jeff", 33)


print("-----")


def cube(num):
    return num*num*num  # no statement works after the return, breaks the function


result = cube(2)
print(result)


print("-----")


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))

print("-----")

# Detecting all vowels and replacing them with "g"


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aieou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
