import datetime
date_list = [int(i) for i in input().split()]
date1 = datetime.date(date_list[0], date_list[1], date_list[2])
days = datetime.timedelta(int(input()))
date2 = date1 + days
print(date2.year, date2.month, date2.day)
