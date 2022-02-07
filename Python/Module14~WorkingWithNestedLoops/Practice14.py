outer = ["outer1", "outer2", "outer3"]
nest = ["nest1", "nest2", "nest3"]

for x in outer:
    for y in nest:
        print(x, y)

print("----------------")

teams = ["Football City", "Football United", "Football Fever"]
jobs = ["Manager", "Striker", "Defender"]

for team in teams:
    for job in jobs:
        print(team, job)


print("----------------")

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for alpha in numbers:
    print(alpha)
    for beta in letters:
        print(beta)
    print("\n")


print("----------------")


# Create a Nested for loop - Outerloop should have 3 elements.
# Innerloop should have 5 elements.
# Print in groups  header/body style.

lads = ["John", "Jacob", "Jingleheimer"]
foods = ["Bacon", "Eggs", "Beans", "Sausage", "Spam"]

for lad in lads:
    print(f"{lad} Absolutely loves...")
    for food in foods:
        print(food)
    print("\n")
