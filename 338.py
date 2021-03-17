# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 22:11
# @Author  : zxl
# @FileName: 338.py


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        import math
        if num == 0:
            return [0]

        ans = [0,1]
        for i in range(2,num+1):
            v = i - pow(2,int(math.log(i,2)))
            ans.append(1+ans[v])
        return ans

obj = Solution()
num = 32
ans = obj.countBits(num)
print(ans)