class TheDateError(Exception):
    pass


class Data:
    """Конструктор принимает дату в формате дд-мм-гг"""

    def __init__(self, data):
        self.data = data

    @classmethod
    def cl_met(cls, data):
        value = [int(i) for i in data.split('-')]
        dic = {'day': value[0], 'month': value[1], 'year': value[2]}
        if Data.stat_met(value):
            return dic
        else:
            raise TheDateError()

    @staticmethod
    def stat_met(values):
        if 0 < values[0] < 32 and 0 < values[1] < 13:
            return True
        else:
            return False


dat = input('Input date in format dd-mm-yy: ')
d = Data(dat)
try:
    print(d.cl_met(dat))
except TheDateError:
    print('the date is incorrect!')
except ValueError:
    print('The date is incorrect!')
except IndexError:
    print('The date is incorrect!')
