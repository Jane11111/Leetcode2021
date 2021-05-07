# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 14:16
# @Author  : zxl
# @FileName: Offer048.py


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {}
        max_count = 0
        p = 0
        cur_val = 0
        for i in range(len(s)):
            c = s[i]
            if c not in dic or dic[c] == 0:
                if c not in dic:
                    dic[c] = 0
                dic[c]+=1
                cur_val+=1
                max_count = max(max_count,cur_val)
            else:
                while dic[c] > 0:
                    dic[s[p]]-=1
                    p+=1
                    cur_val-=1
                dic[c] =1
                cur_val+=1
        return max_count

obj = Solution()
s = "pwwkew"
ans = obj.lengthOfLongestSubstring(s)
print(ans)

