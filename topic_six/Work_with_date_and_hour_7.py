def skahguel():
    n = int(input())
    weeks = 0
    day_weeks = []
    day_number = 0
    days =[int(i) for i in input().split()]
    for day in range(0, n):
        if days[day] == 0:
            if day != len(days):
                weeks += 1
                day_weeks.append(day_number)
                day_number = 0
        else:
           day_number += 1 
    
    print(len(day_weeks))
    print(day_weeks)
skahguel()
    