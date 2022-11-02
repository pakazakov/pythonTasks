"""Дан файл с текстом из нескольких глав. Каждая глава начинается со
слова «Глава» и её номера на одной строке, на следующей строке идёт
её название, текст главы идёт с новой строки. Между данными могут
находиться пустые строки. Выведите в отдельный файл оглавление."""
with open("4.txt") as f:
    text = f.read().strip().split("Chapter")[1:]

r = []
for i in text:
    j = i.split()
    r.append(f"Chapter {j[0]}. {j[1]}")

with open("4_result.txt", "w") as f:
    print("\n".join(r), file=f)
