def calculator(x, func, y):
    opers = {'plus': x+y, 'minus': x-y, 'multiply': x*y, 'divide': x/y}
    return print(opers[func])
