numb_student = int(input())
average_score = {}
count = 3
marks = [0] * count

for _ in range(numb_student):
    a = input().split()
    average_score[a[0]] = [int(i) for i in a[1:]]
    for i in range(count):
        marks[i] += average_score[a[0]][i]

for i in range(count):
    print('%.2f' % (marks[i] / numb_student), end = ' ')
