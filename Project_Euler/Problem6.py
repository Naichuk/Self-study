"""Find the difference between the sum of the squares of the first one hundred natural numbers
 and the square of the sum."""

def problem6():
    data = range(101)
    sum_square = (sum(data))**2
    each_square = sum([x**2 for x in data])
    return sum_square - each_square