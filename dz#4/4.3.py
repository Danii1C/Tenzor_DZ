from random import randint
arrayF = []
arrayS = []
while True:
    try:
        l = input('Введите длину массивов: ')
        l = int(l)
        break
    except ValueError:
        print('Ошибка ввода')
for i in range(l):
    arrayF.append(randint(-50, 50))
    arrayS.append(randint(-50, 50))
print(f'Первый массив: {arrayF}')
print(f'Первый массив: {arrayS}')
set1=set(arrayF)
set2=set(arrayS)

print(f'Пересечение: {str(set1.intersection(set2))}')
print(f'Все элементы первого множества за исключением тех,что во втором: {str(set1.difference(set2))}')
print(f'Все элементы второго множества за исключением тех,что в первом: {str(set2.difference(set1))}')
print(f'Элементы, входящие не в оба множества одновременно: {str(set1.symmetric_difference(set2))}')