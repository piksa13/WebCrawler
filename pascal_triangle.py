#  Blaise Pascal triangle
#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...


def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    elif n > 2:
        return triangle(n - 1) + [
            [1] + [triangle(n - 1)[-1][-i] + triangle(n - 1)[-1][-i - 1] for i in range(1, n - 1)] + [1]]
    else:
        print('Invalid parameter')


print(triangle(0))
# >>> []

print(triangle(1))
# >>> [[1]]

print(triangle(2))
# >> [[1], [1, 1]]

print(triangle(3))
# >>> [[1], [1, 1], [1, 2, 1]]

print(triangle(6))
# >>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]