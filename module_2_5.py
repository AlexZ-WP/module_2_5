def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0 or value <= 0:
        return []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)


    return matrix
matrix = get_matrix(2, 2, value=10)
print(matrix)
matrix = get_matrix(3, 5, value=42)
print(matrix)
matrix = get_matrix(4, 2, value=13)
print(matrix)


# def get_matrix(n, m, value):
#     matrix = []
#     i = n
#     j = m
#     for i in range(n):
#         row = []
#         for j in range(m):
#             row.append(value)
#             matrix.append(row)
#
#         return matrix
# matrix = get_matrix(2, 2, value=10)
# print(matrix)
# matrix = get_matrix(3, 5, value=42)
# print(matrix)
# matrix = get_matrix(4, 2, value=13)
# print(matrix)