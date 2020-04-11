class ComplexDigit:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexDigit(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexDigit(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}i'


try:
    z = ComplexDigit(int(input('Введите действительную часть: ')), int(input('Введите мнимую часть: ')))
    k = ComplexDigit(int(input('Введите действительную часть: ')), int(input('Введите мнимую часть: ')))
    print(f'z = {z}')
    print(f'k = {k}')
    print(f'z + k = {z + k}')
    print(f'z * k = {z * k}')

except ValueError:
    print('Надо вводить числа!')
