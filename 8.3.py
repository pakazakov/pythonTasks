dic = {'привет': 'hello',
       'мир': 'world',
       'ты': 'you',
       'я': 'i',
       'сделал': 'made',
       'словарь': 'dictionary'}

text = input('Введите текст: ').split()

arr = []
try:
       for i in range(len(text)):
              word = ''.join(text[i])
              for key, val in dic.items():
                     arr.append(dic[word]+' ')
                     break
       print(''.join(arr))
except:
       print('К сожалению мы пока не можем перевести этот текст')