# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 17:54
# @Author  : zxl
# @FileName: 118.py



class Solution:
    def generate(self, numRows: int) :

        if numRows == 0:
            return []

        ans = [[1]]

        for i in range(1,numRows):
            l = i+1

            lst = [1]
            for j in range(1,l):

                if j == l-1:
                    lst.append(1)
                else:
                    lst.append(ans[i-1][j]+ans[i-1][j-1])
            ans.append(lst)
        return ans

obj = Solution()
numRows = 5
ans = obj.generate(numRows)
print(ans)

