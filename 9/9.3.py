'''Прочитайте из файла матрицу. Транспонируйте её и выведите
результат в отдельный файл.'''
with open("3.txt", "r") as f:
    a = f.read().split("\n")
    a = list(map(lambda x: x.split(" "), a))

r = []

if a:
    r = [[None for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            r[j][i] = a[i][j]

r = map(lambda x: " ".join(x), r)
r = "\n".join(r)

with open("3_result.txt", "w") as f:
    print(r, file=f)
