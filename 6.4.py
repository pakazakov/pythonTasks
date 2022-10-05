words = input('Введите строку\n')
sumTitle = 0
sumSigns = 0
for word in words.split():
    word = ' '.join(word)
    if word.istitle()==True:
        sumTitle += 1
    if word.rfind('.',',','!','?',':',';'):
        sumSigns += 1

print(f'Количество слов начинающихся с заглавной буквы - {sumTitle}\n Количество слов заканчивающихся знаком препинания - {sumSigns}')
