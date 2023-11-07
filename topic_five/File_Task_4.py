file1 = open('C:\\Users\\xcali\\Documents\\Python\\topic_five\\topic_five.txt', 'r')
numb = [int(i) for i in file1.read() if i.isnumeric() == True]
file1.close()
def add_file():
    vavels = {'a', 'o', 'e', 'y', 'i', 'u', 'A', 'O', 'E', 'Y', 'I', 'U'}
    vavel = 0
    not_vavel = 0
    
    for word in numb:
        if word[0] in vavels:
            vavel += 1
        elif word[0] not in vavels:
            not_vavel += 1
    print(vavel, not_vavel)
print(add_file())
