# num = [1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j != k and i != k:
#                 print(num[i],num[j],num[k])
# from itertools import combinations
#


def comb(lst,n):
    if n == 0:
        return [[]]
    if len(lst) == 0:
        return []
    return ([[lst[0]] + c for c in comb(lst[1:],n-1)] + comb(lst[1:],n))

size = int(input("enter number of elements :"))

lst = []
for i in range(size):
    val = int(input(f"enter element {i+1}:"))
    lst.append(val)

n = int(input("enter number of elements in combination : "))
result = comb(lst,n)

for i in result:
    print(i)

#os model date and time