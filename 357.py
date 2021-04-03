# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 22:35
# @Author  : zxl
# @FileName: 357.py


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        count = 0
        for i in range(1,n+1):

            if i == 1:
                base = 10
            else:
                base = 9
            for j in range(1,i):
                base *= (10-j)
            count += base
        return count

obj = Solution()
n = 1
ans = obj.countNumbersWithUniqueDigits(n)
print(ans)
