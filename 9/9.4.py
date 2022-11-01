with open("4.txt") as f:
    text = f.read().strip().split("Chapter")[1:]

r = []
for i in text:
    j = i.split()
    r.append(f"Chapter {j[0]}. {j[1]}")

with open("4_result.txt", "w") as f:
    print("\n".join(r), file=f)
