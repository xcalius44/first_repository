len_list = int(input())
arrays = [int(s)for s in input().split()]
del_numb = int(input())
del arrays[del_numb - 1]
(key, value)= [int(s)for s in input().split()]
arrays.insert(key - 1, value)
print(' '.join([str(i)for i in arrays]))
