import os

isExist = os.path.exists("hello.txt")

if isExist:
    my_file = open("hello.txt", "w")
    my_file.write("Updated version")
    my_file.close()
else:
    abcd = open("hello.txt", "x")
    abcd.write("Created version")
    abcd.close()