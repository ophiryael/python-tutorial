while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops! Not a valid number. Try again...")
    else:
        print(f"{x} is a valid number")
        break
    finally:
        print("Finally...")

try:
    raise Exception("foo", "bar")
except Exception as err:
    x, y = err.args
    print("x =", x)
    print("y =", y)

try:
    raise NameError("General Kenobi")
except NameError:
    print("Hello there")
    raise

