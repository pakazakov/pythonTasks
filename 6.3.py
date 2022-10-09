arr = list(map(str,input("Введите массив действительных чисел: ").split()))
sum_0 = 0
maximum = 0
for i in range(len(arr)):
    if arr[i] == '0':
        sum_0 += 1
        if maximum < sum_0:
            maximum = sum_0
            k = i-maximum+1
    else:
        sum_0 = 0

print(f'Длинa максимальной последовательности подряд идущих нулей {maximum}\nИндекс первого элемента этой последовательности {k}')




'''arr = list(map(str,input().split(' ')))
index_0 = 0
maximum = 0
for i in range(len(arr)):
    sum_0 = 0
    for j in range(i,len(arr)):
        if arr[j] == '0':
            sum_0 += 1
            if sum_0 > maximum:
                index_0 = i
                maximum = sum_0
        else:
            break

print(sum_0,index_0)'''
