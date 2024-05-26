import os

f = open("hello.txt","x")
f.write("hello")
f.close()

f = open("hello.txt","r")
print(f.readlines())
f.close()

print(os.path.exists("hello.txt"))