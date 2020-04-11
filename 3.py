class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    print("Для завершения ввода введите q!")
    a = input('Введите число: ')
    if a.lower() == 'q':
        break
    elif a.isdigit():
        my_list.append(a)
    else:
        print(MyError('\nНАДО ВВОДИТЬ ЧИСЛА!\n'))

print(my_list)
