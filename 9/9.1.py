with open("1.txt", "r") as f:
    text = f.read().split()

with open("1.txt", "w") as f:
    n = int(input())
    while n > len(text):
        n = int(input("Введите корректное значение n\n"))

    print(" ".join(list(text)[:-n]), file=f, end="")
