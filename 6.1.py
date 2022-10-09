from numpy import *

list1 = list(map(int,input().split()))
vector1 = array(list1)
list2 = list(map(int,input().split()))
vector2 = array(list2)

print(vector1*vector2)