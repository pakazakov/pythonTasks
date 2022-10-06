import numpy as np

list1 = list(map(int,input().split()))
vector1 = np.array(list1)
list2 = list(map(int,input().split()))
vector2 = np.array(list2)

print(vector1*vector2)