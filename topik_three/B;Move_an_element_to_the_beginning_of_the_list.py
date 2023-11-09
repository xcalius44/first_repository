len_list = int(input())
arrays = [int(s)for s in input().split()]
numb_on_start = int(input())
arrays.insert(0, arrays.pop(numb_on_start - 1))
print(' '.join([str(i) for i in arrays]))

