def get_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def format_output(data):
    return str(data)


def validate_input(data):
    if not isinstance(data, list):
        raise TypeError("Expected a list")
    return True


def is_positive(n):
    """Check if a number is positive."""
    return n > 0
