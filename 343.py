# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 22:22
# @Author  : zxl
# @FileName: 343.py

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        arr = [0,1,1]
        for i in range(3,n+1):
            max_val = 1
            for j in range(1,i):
                max_val = max(max_val,max(arr[j],j)*max(arr[i-j],i-j))
            arr.append(max_val)
        return arr[n]

obj = Solution()
n = 4
ans = obj.integerBreak(n)
print(ans)


