def correctInput(text):
    while True:
        try:
            inputd = float(input('Введите ' + text + ' число: '))
            return inputd
        except ValueError:
            print('Некорректный ввод')

x = correctInput('первое')
y = correctInput('второе')

print('_' * 30)
print(f'Сумма: {x + y}')
print(f'Разность: {x - y} | {y - x}')
print(f'Произведение: {x * y}')
print(f'Деление: {x / y} | {y / x}')
print(f'Возведение в степень: {x ** y} | {y ** x}')
print(f'Деление по модулю: {x % y} | {y % x}')
print(f'Целочисленное деление: {x // y} | {y // x}')