def count_trailing_zeros(n):
    """
    Calculates the number of trailing zeros in the factorial of a given number n.
    """
    if n < 0:
        return 0
    count = 0
    i = 5
    while (n // i) >= 1:
        count += n // i
        i *= 5
    return count

num = 125
zeros = count_trailing_zeros(num)
print(f"The number of trailing zeros in {num}! is {zeros}")