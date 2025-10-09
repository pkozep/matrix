from main import Matrix

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 2]
])

B_reverse = B.reverse()

X = A * B
Y = B * A
Z = B * B_reverse

print( X, Y, Z )