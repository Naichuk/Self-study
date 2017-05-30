

def largest_prime(data, i = 2):
    while i < data:
        if data%i != 0:
            i += 1
        else:
            data = data/i
    return i