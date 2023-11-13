Dek = []
N = True
while N:
    list = input().split()
    if list[0] == 'push_front':
        Dek.insirt(list[1],len(Dek))
    if list[0] == 'push_back':
        Dek.append(list[1])
        print('ok')
    if list[0] == 'pop_front':
        list.pop(len(Dek)- 1)
    if list[0] == 'pop_back':
        list.pop(0)
    if list[0] == 'front':
        print(Dek[len(Dek)- 1])
    if list[0] == 'back':
        print(Dek[0])
    if list[0] == 'size':
        print(len(Dek))
    if list[0] == 'clear':
        list.clear
        print('ok')
    if list[0] == 'exit':
        N = False
        print('bye')
