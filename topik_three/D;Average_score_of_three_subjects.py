student = int(input())
average = {}
count = 3

for _ in range(student):
    a = input().split()
    average[a[0]] = [int(i) for i in a[1:]]
    print('%s %.2f' % (a[0],
        sum(average[a[0]]) / count))
    
    # a = ivanov 5 10 3
    # {'ivanov' : [5, 10, 3]}