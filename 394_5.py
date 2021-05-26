# -*- coding: utf-8 -*-
# @Time    : 2021-05-11 20:03
# @Author  : zxl
# @FileName: 394_5.py


class Solution:
    def decodeString(self, s: str) -> str:


        cur_s = ''
        num = 0

        lst = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i].isalpha():
                cur_s+=s[i]
            elif s[i] == '[':
                lst.append([cur_s,num])
                num = 0
                cur_s = ''
            else:

                ss,n = lst.pop()
                ss+=n*cur_s
                cur_s = ss
        return cur_s
obj = Solution()
s = "2[abc]3[cd]ef"
ans = obj.decodeString(s)
print(ans)








