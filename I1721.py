# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 16:07
# @Author  : zxl
# @FileName: I1721.py


class Solution:
    def trap(self, height) :

        n = len(height)
        l = [0 for i in range(n)]
        r = [0 for i in range(n)]

        l_max = 0
        r_max = 0
        for i in range(n):

            l_max = max(l_max,height[i])
            r_max = max(r_max,height[n-i-1])

            l[i] = l_max
            r[n-i-1] = r_max

        ans = 0
        for i in range(n):
            h = min(l[i],r[i])
            if h>height[i]:
                ans += (h-height[i])
        return ans

obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = obj.trap(height)
print(ans)


