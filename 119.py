# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 14:11
# @Author  : zxl
# @FileName: 119.py


class Solution:
    def getRow(self, rowIndex: int) :

        arr = [1 for i in range(rowIndex+1)]

        for i in range(1,rowIndex+1):
            tmp = [1 for i in range(rowIndex+1)]
            for j in range(1,i):
                tmp[j] = arr[j-1]+arr[j]
            arr = tmp
        return arr

obj = Solution()
rowIndex = 4
ans = obj.getRow(rowIndex)
print(ans)



