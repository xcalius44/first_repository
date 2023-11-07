file1 = open('C:\\Users\\xcali\\Documents\\Python\\topic_five\\topic_five.txt', 'r+')
numb = [int(i) for i in file1.readlines()if i != '\n']

def add_file():
    max_numb = max(numb)
    sum_numb = sum(numb)
    file1.write(str(sum_numb) + '\n')
    file1.write(str(max_numb) + '\n')  
add_file()
file1.close()
