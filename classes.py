class Greeter:
    def __init__(self, title, name):
        self.title = title
        self.name = name

    def greet(self):
        return f"Hello there, {self.title} {self.name}"


x = Greeter("General", "Kenobi")
print(x.greet())

# Generators
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse("Hello"):
    print(char)
