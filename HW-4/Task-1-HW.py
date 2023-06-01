# Напишите функцию для транспонирования матрицы

def matrix_transpose(matrix: list) -> list:
    matrix_new = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_new[i][j] = matrix[j][i]
    return matrix_new


my_matrix_1 = [[1, 2, 3],
               [4, 5, 6],
               ]

my_matrix_2 = [[1, 2],
               [4, 5],
               [6, 7],
               ]

print('Было:', *my_matrix_1, 'Стало:', *matrix_transpose(my_matrix_1), sep='\n')
print('_' * 30)
print('Было:', *my_matrix_2, 'Стало:', *matrix_transpose(my_matrix_2), sep='\n')
