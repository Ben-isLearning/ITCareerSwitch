

x = 10
y = 15

print(y > x and x < 20)
# is True ~ 15 > 10 AND 10 < 20.

print(y > x or x >= 20)
# is True ~ 15 > 10 OR X >= 20  (1st condition is True / 2nd is False)

print(not(y > x and x < 20))
# Earlier we found out that (y > x and x < 20) returns True.
# is False ~ the not operator reveses the Boolean value (T becomes F / F becomes T )


# and     True if both statements are true        10 < 100 and 10 > 1
# or      True if a single statmenet is true      10 < 100 or 10 = 100
# not     Reverses the Boolean of the operand     not(10 < 100 and 10 > 1)
