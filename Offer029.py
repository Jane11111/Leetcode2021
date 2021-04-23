# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 13:22
# @Author  : zxl
# @FileName: Offer029.py


class Solution:

    def circles(self,s,e1,e2,matrix,ans):


        if s == e2:
            for i in range(s,e1+1):
                ans.append(matrix[s][i])
            return
        if s == e1:
            for i in range(s,e2+1):
                ans.append(matrix[i][s])
            return
        for i in range(s,e1):
            ans.append(matrix[s][i])
        for i in range(s,e2):
            ans.append(matrix[i][e1])
        for i in range(e1,s,-1):
            ans.append(matrix[e2][i])
        for i in range(e2,s,-1):
            ans.append(matrix[i][s])



    def spiralOrder(self, matrix )  :

        ans = []
        m = len(matrix)
        if m == 0:
            return ans
        n = len(matrix[0])
        if n == 0:
            return ans
        i = 0
        e1 = n-1
        e2 = m-1
        while i<=e1 and i<=e2 :
            self.circles(i,e1,e2,matrix,ans)
            i+=1
            e1-=1
            e2-=1
        return ans
obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = obj.spiralOrder(matrix)
print(ans)



