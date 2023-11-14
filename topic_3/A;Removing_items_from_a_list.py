list_len = int(input())
arrays = [int(s)for s in input().split()]
del_number = int(input())
print(' '.join(str(i)for i in arrays if i != del_number))
