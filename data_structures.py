# List comprehension
values = [-2, 2, -3, 4, -5]

doubled = [x * 2 for x in values]
print(doubled)

absolutes = [abs(x) for x in values]
print(absolutes)

# Set
colors = {"black", "blue", "green", "blue", "green"}
print(colors)

# Dictionary
tel = {"foo": 123, "bar": 456, "baz": 789}
print(tel, list(tel))

for name, num in tel.items():
    print(name, num)

# Sequence looping
names = ["foo", "bar", "baz"]
for i, name in enumerate(names):
    print(i, name)

