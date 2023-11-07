from datetime import date
 
 
def numOfDays(date1, date2): 
        return (date2-date1).days
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)
print(numOfDays(date1, date2))