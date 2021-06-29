# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 14:34
# @Author  : zxl
# @FileName: 119_3.py


class Solution:
    def getRow(self, rowIndex: int) :

        arr = [1 for i in range(rowIndex+1)]

        i = 1
        j = rowIndex-1

        n1 = rowIndex
        n2 = 1

        while i<=j:
            num = int(n1/n2)

            n1*=(rowIndex-i)
            n2 *= (i+1)
            arr[i] = num
            arr[j] = num
            i+=1
            j-=1
        return arr

obj = Solution()
rowIndex = 4
ans = obj.getRow(rowIndex)
print(ans)



