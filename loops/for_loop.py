
mangas = ["Berserk", "Vagabond", "Beck", "Medaka", "FOTNS", "Kengan"]
for manga in mangas:
    print(manga)

print("-----")


for index in range(10):  # range specifies the max that we define, in this case 0-9
    print(index)

print("-----")

for index in range(3, 10):  # range from 3 to 9
    print(index)

print("-----")

for index in range(len(mangas)):  # range from 0 to num of mangas
    print(mangas[index])

print("-----")

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")
