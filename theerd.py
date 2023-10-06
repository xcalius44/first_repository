# A
# n = int(input())
# a = [int(s)for s in input().split()]
# p = int(input())
# print(' '.join(str(i)for i in a if i != p))





# B
# n = int(input())
# a = [int(s)for s in input().split()]
# p = int(input())
# a.insert(0, a.pop(p - 1))
# print(' '.join([str(i) for i in a]))




# C
# n = int(input())
# a = [int(s)for s in input().split()]
# p = int(input())
# del a[p - 1]
# (q, k)= [int(s)for s in input().split()]
# a.insert(q - 1, k)
# print(' '.join([str(i)for i in a]))





# D
# n = int(input())
# b = {}
# count = 3

# for _ in range(n):
#     a = input().split()
#     b[a[0]] = [int(i) for i in a[1:]]
#     print('%s %.2f' % (a[0],
#         sum(b[a[0]]) / count))





# E
# n = int(input())
# b = {}
# count = 3
# marks = [0] * count

# for _ in range(n):
#     a = input().split()
#     b[a[0]] = [int(i) for i in a[1:]]
#     for i in range(count):
#         marks[i] += b[a[0]][i]

# for i in range(count):
#     print('%.2f' % (marks[i] / n), end = ' ')





# F
# n = int(input())
# b = []
# count = 3

# for _ in range(n):
#     a = input().split()
#     a[1:] = [int(i) for i in a[1:]]
#     a.insert(0, -sum(a[1:]) / count)
#     b.append(a)

# b.sort()
# for i in b:
#     print('%s %s %.2f' %
#         (i[1],
#          ' '.join([str(x) for x in i[2:]]),
#         -i[0]
#         ))





# G
# N = int(input())
# P = [int(x) for x in input.split()]
# M = int(input())
# Q = [int(x) for x in input.split()]
# len_R = max(N, M) + 1
# R = [0] * len_R
# for  i in range(len_R):
#     R[i] = (P[i] if i <= N else 0) + (Q[i] if i <= M else 0)
# while len_R > 0 and R[len_R - 1] == 0:
#     len_R -= 1
# if len_R == 0:
#     print(0)
# else:
#     print(*R[:len_R])





# H
# N = int(input())
# P = [int(x) for x in input.split()]
# M = int(input())
# Q = [int(x) for x in input.split()]
# C = Q + P
# print(*sorted(C))





# I
# stak = []
# N = True
# while N:
#     A = input().split()
#     if A[0] == 'push':
#         stak.insirt(A[1],len(stak))
#         print('ok')
#     if A[0] == 'pop':
#         A.pop(len(stak)- 1)
#     if A[0] == 'back':
#         print(stak[len(stak)- 1])
#     if A[0] == 'size':
#         print(len(stak))
#     if A[0] == 'clear':
#         A.clear
#         print('ok')
#     if A[0] == 'exit':
#         N = False
#         print('bye')





# K
# stak = []
# N = True
# while N:
#     A = input().split()
#     if A[0] == 'push':
#         A.append(A[1])
#         print('ok')
#     if A[0] == 'pop':
#         A.pop(0)
#     if A[0] == 'front':
#         print(stak[0])
#     if A[0] == 'size':
#         print(len(stak))
#     if A[0] == 'clear':
#         A.clear
#         print('ok')
#     if A[0] == 'exit':
#         N = False
#         print('bye')





# L
# stak = []
# N = True
# while N:
#     A = input().split()
#     if A[0] == 'push':
#         A.append(A[1])
#         print('ok')
#     if A[0] == 'pop':
#         A.pop(0)
#         if len(stak) == 0:
#             print('error')
#     if A[0] == 'front':
#         print(stak[0])
#         if len(stak) == 0:
#             print('error')
#     if A[0] == 'size':
#         print(len(stak))
#     if A[0] == 'clear':
#         A.clear
#         print('ok')
#     if A[0] == 'exit':
#         N = False
#         print('bye')





# M
# stak = []
# N = True
# while N:
#     A = input().split()
#     if A[0] == 'push_front':
#         stak.insirt(A[1],len(stak))
#     if A[0] == 'push_back':
#         stak.append(A[1])
#         print('ok')
#     if A[0] == 'pop_front':
#         A.pop(len(stak)- 1)
#     if A[0] == 'pop_back':
#         A.pop(0)
#     if A[0] == 'front':
#         print(stak[len(stak)- 1])
#     if A[0] == 'back':
#         print(stak[0])
#     if A[0] == 'size':
#         print(len(stak))
#     if A[0] == 'clear':
#         A.clear
#         print('ok')
#     if A[0] == 'exit':
#         N = False
#         print('bye')
