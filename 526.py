# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 10:26
# @Author  : zxl
# @FileName: 526.py

class Solution(object):

    def recursiveCount(self,s,n,dic):

        count = 0
        if s>n:
            return 1
        for i in range(1,n+1):
            if (i%s == 0 or s%i == 0) and dic[i]:
                dic[i] = False
                sub_count = self.recursiveCount(s+1,n,dic)
                count += sub_count

                dic[i] = True
        return count

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {i:True for i in range(1,1+n)}
        ans = self.recursiveCount(1,n,dic)
        return ans

obj = Solution()
n = 3
ans = obj.countArrangement(n)
print(ans)


