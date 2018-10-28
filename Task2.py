import calendar

import datetime

a = input('Введите дату в формате DD.MM.YYYY:')

if len(a) == 10 and a[2] == "." and a[5] == '.':
    year = int(a[6:len(a)])
    month = int(a[3:5])
    day = int(a[0:2])
    d = calendar.weekday(year, month, day)

    self = calendar.TextCalendar.formatweekday
    print(calendar.TextCalendar.formatweekday(self, d, 9))
else:
    print('Дата введена в неверном формате ')