# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 14:32
# @Author  : zxl
# @FileName: 119_2.py

class Solution:
    def getRow(self, rowIndex: int) :


        arr = [1 for i in range(rowIndex+1)]

        for i in range(1,rowIndex+1):
            for j in range(i-1,0,-1):
                arr[j] = arr[j]+arr[j-1]
        return arr
obj = Solution()
rowIndex = 4
ans = obj.getRow(rowIndex)
print(ans)

