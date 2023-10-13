file1 = open('C:\\Users\\xcali\\Documents\\Python\\topic_five\\topic_five.txt', 'r+')
lines = [int(i) for i in file1.read().split('\n') if i.isnumeric()]

def add_file():
    max_numb = max(lines)
    sum_numb = sum(lines)
 
    file1.write(str(max_numb) + '\n')
    file1.write(str(sum_numb) + '\n')
add_file()
file1.close()

