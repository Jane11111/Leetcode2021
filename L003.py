# -*- coding: utf-8 -*-
# @Time    : 2021-02-14 15:51
# @Author  : zxl
# @FileName: L003.py

import numpy as np
def lengthOfLongestSubstring(  s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    for i in range(len(s)):
        cs = s[i]
        dic = {cs:True}
        j = i + 1
        while j < len(s):
            ce = s[j]
            if ce in dic:
                break
            dic[ce] = True
            j+=1
        res = max(res,j-i)
    return res



s = 'pwwkew'
res = lengthOfLongestSubstring(s)
print(res)



