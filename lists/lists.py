manga = ["Berserk", "Vagabond", "Beck", "Medaka", "FOTNS", "Kengan"]
print(manga[2])
manga[2] = "Bakemonogatari"
print(manga[0])
print(manga[-1])  # starts indexing from the back
print(manga[1:])  # shows everything every value after index 1 (included)
# shows value from index 1 up to index 2 (1 & 2 and 3 is not included)
print(manga[1:3])

# Basic List functions

lucky_numbers = [4, 8, 15, 16, 2, 42]
manga = ["Berserk", "Vagabond", "Beck", "Medaka", "FOTNS", "Kengan", "Kengan"]

manga2 = manga.copy()  # makes a copy of the list
print(manga2)

manga.append("Bakemonogatari")  # adds a new element at the end of the list
# insert a new value inside the list using the index
manga.insert(1, "Oyasumi")
manga.remove("Beck")  # removing a element
manga.pop()  # gets rid of the last element
manga.sort()  # sort the list in the ascending order
manga.reverse()  # sorts the list in descending order
lucky_numbers.sort()
lucky_numbers.reverse()

print(manga)
print(manga.index("Berserk"))
print(manga.count("Kengan"))  # shows how many times a element appears
print(lucky_numbers)

manga.clear()  # clears the list
manga.extend(lucky_numbers)  # adds an another list
