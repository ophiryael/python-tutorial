def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(2000)

# None return value
print(fib(0))


def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print(f100)


def mutableDefaultValue(a, L=[]):
    """Demonstrates mutable default value accumulation"""
    L.append(a)
    return L


print(mutableDefaultValue(1))
print(mutableDefaultValue(2))
print(mutableDefaultValue(3))


def immutableDefaultValue(a, L=None):
    """Demonstrates mutable default value without accumulation"""
    if L is None:
        L = []
    L.append(a)
    return L


print(immutableDefaultValue(1))
print(immutableDefaultValue(2))
print(immutableDefaultValue(3))


def keywordArguments(x=100, y=100, z=100):
    """Demonstrates use of keyword arguments"""
    print(x + y + z)


keywordArguments(z=20)

# Lambda expression example
def createIncrementor(n):
    return lambda x: x + n


f = createIncrementor(10)
print(f(5))
