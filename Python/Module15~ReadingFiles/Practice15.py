alpha = open("demo.txt", "r")
print(alpha.read())

print("-----------")

beta = open("demo.txt", "r")
print(beta.readline())
beta.close()

print("-----------")

alpha = open("demo.txt", "r")
print(alpha.read(24))

print("-----------")

with open("demo.txt") as charlie:
    contents = charlie.read()
    print(contents)

print("-----------")

delta = open("demo.txt", "r")
print(delta.read())
delta.close()
print("-----------")
delta = open("demo.txt", "a")
delta.write("\nIts almost Lunch Time!")
delta.close()
print("-----------")
delta = open("demo.txt", "r")
print(delta.read())
delta.close()

print("-----------")
print("-----------")
