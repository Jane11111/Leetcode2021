# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 15:14
# @Author  : zxl
# @FileName: 455.py


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count


obj = Solution()
g = [1,2 ]
s = [1,2,3]
res = obj.findContentChildren(g,s)
print(res)

