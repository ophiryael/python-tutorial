def average(values):
    """Computes list average

        >>> print(average([10, 20, 60]))
        30.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()
