def func1(*arg):
    minimal = min(arg)
    maximal = max(arg)
    return minimal, maximal
print(func1(1, 2, 3, 4, 5))

def func2(string = str(), case = True):
    if case:
        return string.upper()
    else:
        return string.casefold()
print(func2('downcase', True))
print(func2('UPPERCASE', False))

def func3(*strings, glue = ":"):
    output = str()
    for value in strings:
        if len(value) > 3:
            output += value + glue
    return output[0:-1]
print(func3('12', 'string', 'str', 'ssdjnsjdnjsn', 'dsdsdss'))