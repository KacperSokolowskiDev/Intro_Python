
# Reading a file
manga_file = open("./files_test/manga.txt", "r")

# check if file is readable, returns boolean
print(manga_file.readable())

# shows all info from file
# print(manga_file.read())

# reads 1 line from the file and puts itself on the next line
# print(manga_file.readline())

# reads the 2nd line bcs we used it a 2nd time
# print(manga_file.readline())

# reads all line in form of a list and using an index
# we can access a specific line in this list
# print(manga_file.readlines()[1])

# .readlines can be used with a for loop to see all values
for manga in manga_file.readlines():
    print(manga)

# closing a file (always)
manga_file.close()

# writing in a file, modify a file
# open("manga.txt", "w")
# Append a file, add new information
# open("manga.txt", "a")
# Reading & write a file
# open("manga.txt", "r+")
