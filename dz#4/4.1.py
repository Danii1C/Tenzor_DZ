from random import randint
arr = []
while True:
    try:
        l = input('Введите длину массива: ')
        l = int(l)
        break
    except ValueError:
        print('Ошибка ввода')

for i in range(l):
    arr.append(randint(-100, 100))
print(f'Исходный массив: {arr}')

for i in range(l - 1):
    for j in range(l - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f'Отсортированный массив: {arr}')