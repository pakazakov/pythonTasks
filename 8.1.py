dic = {'Иванов': 20, 'Сидоров': 68, 'Петров': 26, 'Смирнов': 68, 'Николаев': 53, 'Богомолов': 75, 'Шабаршина': 44}

medium = sum(dic.values())//len(dic)
minimum = min(dic.values())
maximum = max(dic.values())
print(f'Средний балл: {medium}. Список участников, балл которых выше среднего:')
for key, val in dic.items():
    if val > medium:
        print(f'{key} - {val} баллов')

print(f'Минимум: {minimum}, получил(а):')
for key, val in dic.items():
    if val == minimum:
        print(f'{key}')

print(f'Максимум: {maximum}, получил(а):')
for key, val in dic.items():
    if val == maximum:
        print(f'{key}')