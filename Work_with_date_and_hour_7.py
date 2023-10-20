def spaniel(n , days):
    day_weeks = []
    day_number = 0
    number = 0
    pas = 0
    for day in range(0, n):
        if days[day] == 0:
            if days[day - 1] == 1:
                day_weeks.append(day_number)
                day_number = 0
            number += 1
        else:
           day_number += 1 
    print(len(day_weeks),(day_weeks))  
    return(len(day_weeks),(day_weeks))
print(spaniel(8, [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1]) == (1, [8]))
    