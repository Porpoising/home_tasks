import csv
from collections import Counter

with open('Crimes.csv') as crimes_data:
    reader = csv.DictReader(crimes_data)
    crime_list = Counter()
    for row in reader:
        if row['Date'][6:10] == '2015':
            crime_list[row['Primary Type']] += 1
    print(crime_list.most_common(3))
