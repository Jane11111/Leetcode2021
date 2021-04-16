# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 09:14
# @Author  : zxl
# @FileName: 089.py

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,3,2]
        ans = [0,1,3,2]
        for i in range(3,n+1):
            base = 2**(i-1)

            j = len(ans)-1
            while j>=0:
                ans.append(base+ans[j])
                j-=1
        return ans
obj = Solution()
n = 3
ans = obj.grayCode(n)
print(ans)



