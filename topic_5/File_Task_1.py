file1 = open('C:\\Users\\xcali\\Documents\\Python\\topic_five\\topic_five.txt', 'w')
numb = [str(i) for i in input().split()]
def add_file():
    for i in numb:
        file1.write(i + '\n')

add_file()
file1.close()
