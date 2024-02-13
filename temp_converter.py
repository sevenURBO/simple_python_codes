# celsius2fahrenheit
def cel_to_far(c):
    return c * 9 / 5 + 32


# test
print(cel_to_far(30))
print(cel_to_far(40))


# fahrenheit2celsius
def far_to_cel(f):
    return round((f - 32) * 5 / 9, 1)


# test
print(far_to_cel(30))
print(far_to_cel(40))
