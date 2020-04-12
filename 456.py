class Sklad:
    tec = {}

    def new_org_tec(self, i):
        Sklad.tec[i] = self.firm

    def move_org_tec(self):
        pass


class OrgTec:
    def __init__(self, firm, cost, year_of_bought, typ='smth', place='main_office'):
        self.firm = firm
        self.cost = cost
        self.year_of_bought = year_of_bought
        self.typ = typ
        self.place = place


class Printer(OrgTec):
    def __init__(self, firm, cost, year_of_bought, color=True, laser=False, typ='Принтер', place='main_office'):
        super().__init__(firm, cost, year_of_bought, typ, place)
        self.color = color
        self.laser = laser


class Scan(OrgTec):
    def __init__(self, firm, cost, year_of_bought, frmt, typ='Сканер', place='main_office'):
        super().__init__(firm, cost, year_of_bought, typ, place)
        self.format = frmt


class Xerox(OrgTec):
    def __init__(self, firm, cost, year_of_bought, speed, typ='Ксерокс', place='main_office'):
        super().__init__(firm, cost, year_of_bought, typ, place)
        self.speed = speed

printers = []
scaners = []
xeroxes = []
i = 0
# try:
while True:
    print('Чтобы выйти из программы введите q!')
    num_of_tec = input('Какую оргтехнику Вы хотите создать? (1 - принтер, 2 - сканер, 3 - ксерокс) : ')
    if num_of_tec.lower() == 'q':
        choise = input('Желаете ли поместить какие-либо товары на склад? y/n : ')
        if choise.lower() == 'y':
            typ_og_tec = input(
                'Какое устройство Вы хотите поместить на склад? (1 - принтер, 2 - сканер, 3 - ксерокс) : ')
            if typ_og_tec == '1':
                for printer in printers:
                    print(f'{printers.index(printer) + 1}. {printer.firm}')
                while True:
                    i += 1
                    print('Для завершения введите q!')
                    num_of_printer = input('Введите номер принтера, который хотите сдать на склад: ')
                    if num_of_printer.lower() == 'q':
                        break
                    else:
                        Sklad.new_org_tec(printers[int(num_of_printer) - 1], i)
            if typ_og_tec == '2':
                for scaner in scaners:
                    print(f'{scaners.index(scaner) + 1}. {scaner.firm}')
                while True:
                    i += 1
                    print('Для завершения введите q!')
                    num_of_scaner = input('Введите номер сканера, который хотите сдать на склад: ')
                    if num_of_scaner.lower() == 'q':
                        break
                    else:
                        Sklad.new_org_tec(scaners[int(num_of_scaner) - 1], i)
            if typ_og_tec == '3':
                for xerox in xeroxes:
                    print(f'{xeroxes.index(xerox) + 1}. {xerox.firm}')
                while True:
                    i += 1
                    print('Для завершения введите q!')
                    num_of_xerox = input('Введите номер ксерокса, который хотите сдать на склад: ')
                    if num_of_xerox.lower() == 'q':
                        break
                    else:
                        Sklad.new_org_tec(xeroxes[int(num_of_xerox) - 1], i)

        elif choise.lower() == 'n':
            break
    elif num_of_tec == '1':
        printers.append(Printer(input('Введите фирму принтера: '), input('Введите стоимость принтера: '),
                                input('Введите текущий год: ')))
    elif num_of_tec == '2':
        scaners.append(Scan(input('Введите фирму сканера: '), input('Введите стоимость сканера: '),
                            input('Введите текущий год: '), input('Введите формат сканируемых листов сканера: ')))
    elif num_of_tec == '3':
        xeroxes.append(Xerox(input('Введите фирму ксерокса: '), input('Введите стоимость ксерокса: '),
                             input('Введите текущий год: '), input('Введите скорость копирования ( стр/мин ): ')))
    else:
        print('Повторите ввод: ')

# except:
#     print('Вводите указанные числа!!!')

print(i)
print(Sklad.tec)