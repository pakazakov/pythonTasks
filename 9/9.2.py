import re

with open("2.txt", "r") as f:
    text = re.split(r"[.?!]+", f.read())

n = int(input())

text = map(lambda x: list(x.strip().split()), text)
text = filter(lambda x: len(x) > n, text)
text = map(lambda x: " ".join(x), text)

with open("2_result.txt", "w") as f:
    print("\n".join(text), file=f)