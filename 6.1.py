from numpy import *

'''list1 = list(map(int,input().split('Введите первый массив: ')))
vector1 = array(list1)
list2 = list(map(int,input().split('Введите второй массив: ')))
vector2 = array(list2)

print(vector1*vector2)'''

print(array(list(map(int,input('Введите первый массив: ').split())))*array(list(map(int,input('Введите второй массив: ').split()))))