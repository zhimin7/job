import time


dates = ['2020-11-15 11:55:43','2020-11-14 22:11:31','2020-11-15 11:59:02',
'2020-11-15 11:38:20','2020-11-15 11:54:07']
format = '%Y-%m-%d %H:%M:%S'
ticks = time.time()
for date in dates:

    strftime = (time.mktime(time.strptime(date, format)))
    # print(type(strftime))
    print(int(ticks-strftime))
