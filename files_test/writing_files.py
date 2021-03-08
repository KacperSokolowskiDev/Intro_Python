
# Writing new files, overwriting files

# Can create new files if you write a new name using the "w"
manga_file = open("./files_test/index.html", "w")

# Using write, this .write will overwrite the whole file with only this new text using "w" !
# if using "a", then it will append the file with new text at the end !
manga_file.write("\n<h1>This is a Title</h1>")  # \n to add on new line
manga_file.write("<p>This is Paragraph</p>")

manga_file.close()
