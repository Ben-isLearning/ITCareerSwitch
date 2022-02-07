
a = 1

while a < 6:
    print(a)
    a += 1

print("----------------")

b = "hello world"
c = 1

while c <= 3:
    print(b)
    c += 1

print("----------------")

a = 0
while a < 6:
    a += 1
    if a == 4:
        continue
    print(a)

print("----------------")

a = 1
while a < 60:
    print(a)
    a += 1
    if a == 4:
        break
    a += 1

print("----------------")

# Create a While Loop and print "Great Job" atleast 3 times

cheer = "Great Job"
a = 0

while a < 4:
    print(cheer)
    a += 1

print("----------------")

# Create a While Loop and loop thrugh 1 to 10,
# But only print the first 6 on the screen utilizing the break statement

a = 0

while a < 10:
    print(a)
    if a == 6:
        break
    a += 1


print("----------------")
