# -*- coding: utf-8 -*-
# @Time    : 2021-03-04 21:18
# @Author  : zxl
# @FileName: 014.py

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in range(1,len(strs),1):
            str = strs[i]
            j = 0
            while j < min(len(res),len(str)):
                if res[j] != str[j]:
                    break
                j += 1
            res = res[:j]
        return res
obj = Solution()
strs = ["flower","flow","flight"]
res = obj.longestCommonPrefix(strs)
print(res)