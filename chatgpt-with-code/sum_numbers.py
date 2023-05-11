def add_two_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    :param a: The first number to be added
    :type a: int or float
    :param b: The second number to be added
    :type b: int or float
    :return: The sum of the two input numbers
    :rtype: int or float
    """
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    try:
        result = divide(3, 0)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

