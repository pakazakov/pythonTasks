from random import *


matrix_A=[]
matrix_B=[]
matrix_C=[]
#Программа запрашивает у пользователя размеры прямоугольных матриц 𝐴 и 𝐵, а также параметр k
a1,a2=list(map(int,input("Введите размер матрицы A (m x n): ").split()))
b1,b2=list(map(int,input("Введите размер матрицы B (n x p): ").split()))

k = int(input("Введите значение параметра k: "))

#Проверка условия, что m*n не превосходит 30*30
if a1*a2>900:
    print("Матрица А имеет достаточно большой размер\n")
#ПРоверка уловия, что n*p не превосходит 30*30
if b1*b2>900:
    print("Матрица В имеет достаточно большой размер\n")


#Умножение матриц
else:
    for i in range(a1):
        a = []
        matrix_A.append(a)
        for j in range(a2):
            a.append(randint(-9,9))

    for i in range(b1):
        b = []
        matrix_B.append(b)
        for j in range(b2):
            b.append(randint(-9,9))

    print("Матрица А:\n",matrix_A)
    print("Матрица B:\n",matrix_B)


    for i in range(a1):
        c = []
        matrix_C.append(c)
        for j in range(a2):
            for g in range(b2):
                c.append(matrix_A[i][j]*matrix_B[j][k])
    print('Матрица С:\n',matrix_C)








