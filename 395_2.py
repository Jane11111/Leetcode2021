# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 10:53
# @Author  : zxl
# @FileName: 395_2.py



class Solution:

    def longestSubstring(self, s: str, k: int) -> int:

        ans = 0

        for t in range(1,27):


            dic = {}
            less = 0 # 比k少的字符数目
            l = 0
            r = 0
            tot = 0 # 当前窗口内字符数目
            while r<len(s):
                if s[r] not in dic or dic[s[r]] == 0:
                    dic[s[r]] = 1
                    tot+=1
                else:
                    dic[s[r]]+=1
                if dic[s[r]] == 1:
                    less += 1
                if dic[s[r]] == k:
                    less-=1
                while tot>t:

                    dic[s[l]] -=1

                    if dic[s[l]] == 0:
                        tot -=1
                        less-=1
                    if dic[s[l]] == k-1:
                        less+=1
                    l+=1

                if tot == t and less == 0:
                    ans = max(r-l+1,ans)
                r+=1
        return ans


s = "aaabbbcdefcdefgggggggggggggggcde"

k = 3
obj = Solution()
ans = obj.longestSubstring(s,k)
print(ans)


