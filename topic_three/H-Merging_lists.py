len_list1 = 2
list1 = [1,3]
len_list2 = 3
list2 = [2,6, 7]
# len_list1 = int(input())
# list1 = [int(x) for x in input().split()]
# len_list2 = int(input())
# list2 = [int(x) for x in input().split()]
len3 = len_list1 + len_list2
ind1 = 0
ind2 = 0
list3 = [0] * len3
for i in range(len3):
    if ind1 == len_list1:
        list3[len_list1 + 1:] = list2[1:]
    elif ind2 == len_list2:
        list3[len_list2 + 1:] = list1[ind1 - 1:]
    else:        
        if list1[ind1] <= list2[ind2]:
            list3[i] = list1[ind1]
            ind1 += 1
        else:
            list3[i] = list2[ind2]
            ind2 += 1

print(list3)
