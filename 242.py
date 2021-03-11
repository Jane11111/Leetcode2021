# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 22:58
# @Author  : zxl
# @FileName: 242.py


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        l1= list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        return l1==l2

obj = Solution()
s = 'a'
t = 'b'
ans = obj.isAnagram(s,t)
print(ans)