student = int(input())
average = []
count = 3

for _ in range(student):
    a = input().split()
    a[1:] = [int(i) for i in a[1:]]
    a.insert(0, -sum(a[1:]) / count)
    average.append(a)

average.sort()
for i in average:
    print('%s %s %.2f' % (i[1],' '.join([str(x) for x in i[2:]]),-i[0]))

# [
    # [-9 ,'Pupkin',7 ,8 ,12],
    # [-9, 'ivanov', 5, 10, 3 ]
# ]
