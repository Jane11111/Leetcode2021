# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 21:18
# @Author  : zxl
# @FileName: 003_2.py




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        dic = {}
        max_length = 0
        last_idx = -1
        for i in range(len(s)):
            if s[i] not in dic:
                max_length = max(max_length,i-last_idx)
                dic[s[i]] = i
            else:

                max_length = max(max_length,i-max(last_idx,dic[s[i]]))
                last_idx = max(last_idx,dic[s[i]])
                dic[s[i]] = i
        return max_length



obj = Solution()
s = "abcabcbb"
ans = obj.lengthOfLongestSubstring(s)
print(ans)