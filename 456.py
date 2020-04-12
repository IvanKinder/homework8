from abc import ABC


class InputError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Sklad:
    tec = {}

    def new_org_tec(self, i):
        Sklad.tec[i] = self.__dict__

    def change_place(self, i):
        place = input(
            'Введите номер нового подразделения (1 - Главный офис, 2 - Склад, 3 - Отдел логистики, 4 - Маркетинговый отдел) : ')
        places = ['Главный офис', 'Склад', 'Отдел логистики', 'Маркетинговый отдел']
        if 0 < int(place) < 4:
            Sklad.tec[i]['place'] = places[int(place) - 1]
        else:
            print(InputError('Вводите корректные значения!'))


class OrgTec(ABC):
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
try:
    while True:
        print('Чтобы выйти из программы введите q!')
        num_of_tec = input('Какую оргтехнику Вы хотите создать? (1 - принтер, 2 - сканер, 3 - ксерокс) : ')
        if num_of_tec.lower() == 'q':
            choise = input('Желаете ли поместить какие-либо товары на склад? y/n : ')
            if choise.lower() == 'y':
                typ_og_tec = input(
                    'Какое устройство Вы хотите поместить на склад? (1 - принтер, 2 - сканер, 3 - ксерокс) : ')
                if typ_og_tec == '1':
                    if printers:
                        for printer in printers:
                            print(f'{printers.index(printer) + 1}. {printer.firm}')
                        while True:
                            print('Для завершения введите q!')
                            num_of_printer = input('Введите номер принтера, который хотите сдать на склад: ')
                            if num_of_printer.lower() == 'q':
                                break
                            elif int(num_of_printer) in range(len(printers) + 1):
                                i += 1
                                Sklad.new_org_tec(printers[int(num_of_printer) - 1], i)
                            else:
                                print('Такого принтера здесь нет...')
                    else:
                        print('К сожалению принтеры ещё не поступали...')
                if typ_og_tec == '2':
                    if scaners:
                        for scaner in scaners:
                            print(f'{scaners.index(scaner) + 1}. {scaner.firm}')
                        while True:
                            print('Для завершения введите q!')
                            num_of_scaner = input('Введите номер сканера, который хотите сдать на склад: ')
                            if num_of_scaner.lower() == 'q':
                                break
                            elif int(num_of_scaner) in range(len(scaners) + 1):
                                i += 1
                                Sklad.new_org_tec(scaners[int(num_of_scaner) - 1], i)
                            else:
                                print('Такого сканера здесь нет...')
                    else:
                        print('К сожалению сканеры ещё не поступали...')
                if typ_og_tec == '3':
                    if xeroxes:
                        for xerox in xeroxes:
                            print(f'{xeroxes.index(xerox) + 1}. {xerox.firm}')
                        while True:
                            print('Для завершения введите q!')
                            num_of_xerox = input('Введите номер ксерокса, который хотите сдать на склад: ')
                            if num_of_xerox.lower() == 'q':
                                break
                            elif int(num_of_xerox) in range(len(xeroxes) + 1):
                                i += 1
                                Sklad.new_org_tec(xeroxes[int(num_of_xerox) - 1], i)
                            else:
                                print('Такого ксерокса здесь нет...')
                    else:
                        print('К сожалению ксероксы ещё не поступали...')
                elif typ_og_tec.isalpha():
                    print(InputError('Вводите цифры!'))
                else:
                    print('Повторите ввод: ')
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
        elif num_of_tec.isalpha():
            print(InputError('Вводите цифры!'))
        else:
            print('Повторите ввод: ')

    print(f'На складе имеются следующие товары:\n{Sklad.tec}')

    while True:
        print('Для выхода из программы введите q!')
        choise_1 = input('Хотите ли Вы отправить товары со склада в какое-нибудь подразделение? ( y/n ): ')
        if choise_1.lower() == 'y':
            num_of_ed = input('Введите номер товара со склада, который необходимо передать в другое подразделение: ')
            if num_of_ed.lower() == 'q':
                break
            else:
                if int(num_of_ed) in Sklad.tec.keys():
                    Sklad.change_place(Sklad.tec[int(num_of_ed)], int(num_of_ed))
                else:
                    print('Такого товара на складе нет!')
        elif choise_1.lower() == 'n':
            break

    print(f'На складе имеются следующие товары:\n{Sklad.tec}')
except:
    print('Вводите корректные значения!!!!!!!!')
