# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 12:01
# @Author  : zxl
# @FileName: 014_2.py


class Solution:
    def longestCommonPrefix(self, strs ) -> str:

        if len(strs) == 0:
            return ''

        ans = ""
        l = len(strs[0])
        s = strs[0]

        for i in range(1,len(strs)):
            if len(strs[i]) < l:
                l = len(strs[i])
                s = strs[i]

        for i in range(len(s)):
            c = s[i]
            f = True
            for j in range(0,len(strs)):
                if strs[j][i]!=c:
                    f = False
                    break
            if not f:
                break
            ans+=c
        return ans



