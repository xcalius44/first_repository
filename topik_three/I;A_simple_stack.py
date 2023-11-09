stack = []
N = True
while N:
    list = input().split()
    if list[0] == 'push':
        stack.insirt(list[1],len(stack))
        print('ok')
    if list[0] == 'pop':
        list.pop(len(stack)- 1)
    if list[0] == 'back':
        print(stack[len(stack)- 1])
    if list[0] == 'size':
        print(len(stack))
    if list[0] == 'clear':
        list.clear
        print('ok')
    if list[0] == 'exit':
        N = False
        print('bye')
