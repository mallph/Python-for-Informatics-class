def to_number(string):
    number = int(string)
    return number


def add_two(n1, n2):
    num_sum = n1 + n2
    return num_sum


def cube(n):
    cube_n = n * n * n
    return cube_n


print(cube(add_two(to_number('1'), to_number('2'))))
