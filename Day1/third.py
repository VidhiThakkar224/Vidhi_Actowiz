# m1 =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# m2 = [[8, 7, 6],[5, 4, 3],[2, 1, 0]]
#
# result=[]
#
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(m1[i][j] + m2[i][j])
#     result.append(row)
#
# print("matrix 1")
# for row in m1:
#     print(row)
#
# print("matrix 2")
# for row in m2:
#     print(row)
#
# print(sum)
# for row in result:
#     print(row)


#use class

class matrix:
    def __init__(self,m):
        self.m=m

    def __add__(self,other):
        res=[]
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(self.m[i][j]+other.m[i][j])
            res.append(row)

        return res

m1=matrix([[1,2,3],
    [4,5,6],
    [7,8,9]])

m2=matrix([[8,7,6],
    [5,4,3],
    [2,1,0]])

print(m1+m2)