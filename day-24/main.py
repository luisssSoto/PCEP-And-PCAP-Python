"""with open("new_file.txt", mode="wt", encoding="utf-8") as file:
    file.write("new file".capitalize())"""

with open("/Users/AlexSoto/Desktop/new_file.txt", mode="rt", encoding="utf-8") as file:
    readed_file = file.read()
    print(readed_file)

with open("..\\..\\Desktop\\new_file.txt", mode="at", encoding="utf-8") as file:
    file.write("\n New Line".upper())
