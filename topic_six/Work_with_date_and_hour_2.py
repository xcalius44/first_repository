import time
from datetime import date
def times():
    a = time.ctime().split(" ")
    print(date.today(), a[3])
    
times()
