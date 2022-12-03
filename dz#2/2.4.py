from math import pi
while True:
    try:
        radius = float(input('Введите радиус круга: '))
        break
    except ValueError:
        print('Некорректный ввод')
print(f'Площадь круга = {str(pi*radius**2)}')