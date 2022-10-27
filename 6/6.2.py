from random import *


matrix_A = []
matrix_B = []
# Программа запрашивает у пользователя размеры прямоугольных матриц 𝐴 и 𝐵, а также параметр k
a1, a2=list(map(int,input("Введите размер матрицы A (m x n): ").split()))
b1, b2=list(map(int,input("Введите размер матрицы B (n x p): ").split()))

k = int(input("Введите значение параметра k: "))

# Проверка условия, что m*n не превосходит 30*30
if a1 * a2 > 900:
    print("Матрица А имеет достаточно большой размер")
# Пpоверка уловия, что n*p не превосходит 30*30
if b1 * b2 > 900:
    print("Матрица В имеет достаточно большой размер")

else:
    # Получение матрицы А
    for i in range(a1):
        a = []
        matrix_A.append(a)
        for j in range(a2):
            a.append(randint(-9,9))
    # Получение матрицы В
    for i in range(b1):
        b = []
        matrix_B.append(b)
        for j in range(b2):
            b.append(randint(-9,9))

    print("Матрица А:\n",matrix_A)
    print("Матрица B:\n",matrix_B)
    # Ввывод дополнительных данных из имеющихся
    m, n, p = len(matrix_A), len(matrix_A[0]), len(matrix_B[0])

    # Получение матрицы С
    matrix_C = [[0 for i in range(p)] for j in range(m)]
    for i in range(m):
        for j in range(p):
            for g in range(n):
                matrix_C[i][j] += matrix_A[i][g] * matrix_B[g][j]
    print('Матрица С:\n',matrix_C)








