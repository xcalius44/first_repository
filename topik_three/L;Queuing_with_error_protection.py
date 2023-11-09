queue = []
N = True
while N:
    list = input().split()
    if list[0] == 'push':
        list.append(list[1])
        print('ok')
    if list[0] == 'pop':
        list.pop(0)
        if len(queue) == 0:
            print('error')
    if list[0] == 'front':
        print(queue[0])
        if len(queue) == 0:
            print('error')
    if list[0] == 'size':
        print(len(queue))
    if list[0] == 'clear':
        list.clear
        print('ok')
    if list[0] == 'exit':
        N = False
        print('bye')
