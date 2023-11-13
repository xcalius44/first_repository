import random
coking_metods = ['Latin', 'Peruvian', 'Argentenian', 'Mexican', 'Jamaican', 'Cuban', 'French', 'Italian', 'Greek', 'Irish', 'Spanish', 'Ukrain', 'Southern', 'American', 'Fast Food', 'Pizza', 'Pub Food', 'Chinese', 'Japanese', 'Thai', 'Indian']
N = True
while N:
    print(coking_metods)
    list = input().split()
    if list[0] == 'push':
        coking_metods.insirt(list[1],len(coking_metods))
        print('ok')
    if list[0] == 'pop':
        coking_metods.pop(list[1])
    if list[0] == 'print':
        print(coking_metods)
    if list[0] == 'size':
        print(len(coking_metods))
    if list[0] == 'clear':
        list.clear
        print('ok')
    if list[0] == 'role_dise':
        print(random.choice(coking_metods))
    if list[0] == 'exit':
        N = False
        print('bye')
