salary = 27
txt = "You make {} pennies a year"
print(txt.format(salary))


salary = 27
txt = "You make {0:f} pennies a year"
print(txt.format(salary))


spring = "Ben likes {} and {}."
print(spring.format("Pizza", "Python"))


string = "Ben likes {} and {} and rides {} {}."
print(string.format("Pizza", "Python", "Monarch Butterflies", "Red"))


string = "Ben likes {0} and {1} and rides {3} {2}."
print(string.format("Pizza", "Python", "Monarch Butterflies", "Red"))


strong = "Bob likes to eat {act} and take {1} {0}."
print(strong.format("Baths", "Hot", act="Pizza"))

print("Bob likes to eat {act} and take {1} {0}.".format(
    "Baths", "Hot", act="Pizza"))


stronk = "{user}, Beware there are {enemy}'s nearby, atleast {encounter_size} of them!"
print(stronk.format(user="Ben", enemy="Orc", encounter_size=7))
