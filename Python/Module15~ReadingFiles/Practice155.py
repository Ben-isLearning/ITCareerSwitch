with open("demo2.txt") as alpha:
    alphaContents = alpha.read()
    print(alphaContents)

beta = open("demo2.txt", "w")
beta.write("Are you sure?")
beta.close()

with open("demo2.txt") as alpha:
    alphaContents = alpha.read()
    print(alphaContents)


# yankee = open("BenText.txt", "x")


# Create a new file, write some text to the file, then print the text to screen.

oscar = open("demo3.txt", "x")
oscar.write("I smell like beef")
oscar.close()

oscar = open("demo3.txt", "r")
print(oscar.read())


# Create a new file, write some text to the file, then print the text to screen.
with open("demo4.txt", "x") as mike:
    mike.write("I like beef!")

with open("demo4.txt", "r") as mike:
    print(mike.read())


# Create a new file, write some text to the file using a While Loop. then print.
victor = open("demo5.txt", "x")

flavours = ["Beef", "Lamb", "Chicken", "Turkey"]
for flavour in flavours:
    victor.write(f"I smell like {flavour} \n")
victor.close()

victor = open("demo5.txt", "r")
print(victor.read())

# Whoops, thats not a While loop.

# Create a new file, write some text to the file using a While Loop. then print.
i = 0
with open("demo6.txt", "x") as kilo:
    while i < 4:
        kilo.write(f"I am line {i}. Take me to your leader! \n")
        i += 1

with open("demo6.txt", "r") as kilo:
    print(kilo.read())
