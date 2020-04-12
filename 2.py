class ZeroDivisionError1(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if b != 0:
        print(a / b)
    else:
        raise ZeroDivisionError1('Деление на ноль!')
except ZeroDivisionError1 as z:
    print(z)
except ValueError:
    print('Надо вводить числа!')
