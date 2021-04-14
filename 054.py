# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 14:24
# @Author  : zxl
# @FileName: 054.py


class Solution:

    def getNext(self,i,j,m,n,d,matrix):

        d2 = (d+1)%4

        if d == 0:
            if j+1==n or matrix[i][j+1] == -101:
                return (i+1,j),d2
            return (i,j+1),d
        elif d == 1:
            if i+1==m or matrix[i+1][j] == -101:
                return (i,j-1),d2
            return (i+1,j),d
        elif d==2:
            if j-1<0 or matrix[i][j-1] == -101:
                return (i-1,j),d2
            return (i,j-1),d
        else:
            if i-1<0 or matrix[i-1][j] == -101:
                return (i,j+1),d2
            return (i-1,j),d





    def spiralOrder(self, matrix) :

        ans = []
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = 0
        d = 0
        while True:
            ans.append(matrix[i][j])
            matrix[i][j] = -101

            (i,j),d = self.getNext(i,j,m,n,d,matrix)
            if i<0 or i>=m or j<0 or j>=n or matrix[i][j]== -101:
                break
        return ans

obj = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
ans = obj.spiralOrder(matrix)
print(ans)


