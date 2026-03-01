#transpose of matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],[7,8,9]
]

# zip(*matrix) takes each sub list as a separate argument
# and groups the first elements together, then the second, etc.
transposed = [list(row) for row in zip(*matrix)]

print(transposed)
