import calendar

import datetime

a = input('Введите дату в формате DD.MM.YYYY:')

if len(a) == 10 and a[2] == "." and a[5] == '.':
    year = int(a[6:len(a)])  # вместо записи a[6:len(a)] можно использовать просто a[6:]
    month = int(a[3:5])
    day = int(a[0:2])
    d = calendar.weekday(year, month, day)

    # Это работает не так. Должно быть:
    # text_calendar = calendar.TextCalendar()
    # print(text_calendar.formatweekday(d, 9))
    # А можно было вместо использования классов просто использовать calendar.day_name:
    # print(calendar.day_name[d])
    self = calendar.TextCalendar.formatweekday
    print(calendar.TextCalendar.formatweekday(self, d, 9))
else:
    print('Дата введена в неверном формате ')
