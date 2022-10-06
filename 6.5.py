from statistics import mode

arr = list(map(str,input('Введите массив через пробел:\n').split()))
first_len = len(arr)
moda1 = mode(arr)
while moda1 in arr:
    arr.remove(moda1)
second_len = len(arr)
moda2 = mode(arr)
while moda2 in arr:
    arr.remove(moda2)
third_len = len(arr)
if first_len - second_len == second_len - third_len:
    print("Массив не имеет моды")
else:
    print(f"Мода этого массива: {moda1}")