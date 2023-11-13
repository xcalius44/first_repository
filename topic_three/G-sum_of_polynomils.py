# len1 = int(input())
# list1 = [int(x) for x in input().split()]
# len2 = int(input())
# list2 = [int(x) for x in input().split()]
# len_R = max(len1, len2) + 1
len1 = 2
list1 = [2, 3, 4]
len2 = 3
list2 = [3, 1, 5, 7]
len_R = max(len1, len2) + 1
R = [0] * len_R

for i in range(len_R):
    # R[i] = (list1[i] if i <= len1 else 0) + (list2[i] if i <= len2 else 0)
    res = 0
    if i <= len1:
        res += list1[i]
    else:
        res += 0 
    
    if i <= len2:
        res += list2[i]
    else:
        res += 0 
    R[i] = res
    
while len_R > 0 and R[len_R - 1] == 0:
    len_R -= 1
if len_R == 0:
    print(0)
else:
    print(R[:len_R])
