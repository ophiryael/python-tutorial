import json

year = 2020
name = "foo"

print(f"The year is {year}, and my name is {name}")

print("The year is {0}, and my name is {1}".format(year, name))

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))

with open("some-text.txt", "r+") as f:
    for line in f:
        print(line, end="")
    f.write("Some text...\n")

json_obj = json.dumps([1, "some text", 3])
print(repr(json_obj))

python_list = json.loads(json_obj)
print(repr(python_list))
