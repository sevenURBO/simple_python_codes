def generate_identity_matrix(size):
    identity_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        identity_matrix[i][i] = 1
    return identity_matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


m = generate_identity_matrix(4)
print_matrix(m)
