# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 10:01
# @Author  : zxl
# @FileName: 008.py


class Solution:
    def myAtoi(self, s: str) -> int:



        ns = ''
        for i in range(len(s)):
            c = s[i]
            if c == ' ' :
                continue

            if (s[i]>='0' and s[i]<='9') or  ((c=='+' or c=='-') and(i+1<len(s) and s[i+1]<='9' and s[i+1]>='0')) :
                ns+=c

                i+=1
                while i<len(s) and s[i]>='0' and s[i]<='9':
                    ns+=s[i]
                    i+=1

            break
        i=0
        if len(ns)>0 and (ns[i]=='+' or ns[i]=='-'):
            i=1
        new_s = ns[:i]
        while i<len(ns) and ns[i]=='0':
            i+=1

        if i<len(ns):
            new_s+=ns[i:]
        ns = new_s

        if ns=='+' or ns=='-':
            ns='0'


        if len(ns) == 0:
            return 0
        if len(ns)>=15:
            if ns[0] == '-':
                return -2**31
            return 2**31-1
        num = int(ns)
        if num>2**31-1:
            return 2**31-1
        if num<-2**31:
            return -2**31

        return int(ns)

obj = Solution()
s = '0000000000012345678'
ans = obj.myAtoi(s)
print(ans)