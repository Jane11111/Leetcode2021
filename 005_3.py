# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 11:13
# @Author  : zxl
# @FileName: 005_3.py




class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return s


        ans = 1
        cur_s = s[0]

        for i in range(len(s)):

            p = i-1
            q = i+1
            cnt = 1
            while p>=0 and q<len(s) and s[p] == s[q]:
                p-=1
                q+=1
                cnt+=2
            if cnt>ans:
                cur_s = s[p+1:q]
                ans = cnt

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                p = i-1
                q = i+2
                cnt = 2
                while p>=0 and q<len(s) and s[p] == s[q]:
                    cnt+=2
                    p-=1
                    q+=1
                if cnt>ans:
                    cur_s = s[p+1:q]
                    ans = cnt
        return cur_s