# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 20:41
# @Author  : zxl
# @FileName: 003.py



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        dp = [1 for i in range(len(s))]
        dic = {}
        last_idx = -1

        for i in range(len(s)):
            if s[i] not in dic:
                dp[i] = i-last_idx
                dic[s[i]] = i
            else:
                dp[i] = i - max(dic[s[i]],last_idx)
                last_idx = max(last_idx,dic[s[i]])
                dic[s[i]] = i

        return max(dp)

obj = Solution()
s = "cdd"
ans = obj.lengthOfLongestSubstring(s)
print(ans)