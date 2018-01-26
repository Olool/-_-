#Ветвление
a = int(input('A: '))
b = int(input('B: '))
if a > b:
	print('a > b')
	if True:
		pass
elif a == b:
	print('a = b')
else:
	print('a < b')

#pass - можно использовать для реализации пустого блока кода

c = input('c: ')
c = c + c if isinstance(c, str) else 'bug' #пример тернального оператора
#Циклы

i = 5
while i:
	if i  == 10:
		break
	if i == 5:
		i += 1
		continue
	i += 1
'''while i < 10:
	print(i)
	i += 1'''

for i in range(10):
	print(i)

lst = list(range(10,42,2))
for i, v in enumerate(lst):# при использовании enumerate мы получаем словарь с ключами (номер элемента/значение элемента)
	print(i,v)
''' 
a = 1.1
b = 'kkk'
b, a = a, b
т.о. можно поменять значения двух переменных переменных местами без третьей
'''
#Срезы
'''
s = []
for c in range(s);
	s.append(chr'c')
s =''.join(s) 		лучше заменять строку списком
'''
s = 'Hello, world'
s[:5] #срез списка 
s[::2] #срез списка с шагом 2
s[::-1] #перевернуя строка (reverse)
'''
lst = list(range(10))
lst2 = lst[:] - копия списка lst, но при этом они ссылаются не на одну и ту же ячейку памяти


