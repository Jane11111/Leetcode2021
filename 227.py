# -*- coding: utf-8 -*-
# @Time    : 2021-04-04 17:03
# @Author  : zxl
# @FileName: 227.py


class Solution:
    def calculate(self, s: str) -> int:

        lst = []
        i = 0
        s = s.replace(' ','')
        while i<len(s):
            cur_s = s[i]
            i+=1
            while i<len(s) and (s[i] >='0' and s[i]<='9'):
                cur_s += s[i]
                i+=1

            if len(lst) == 0 or lst[-1] == '+' or lst[-1] == '-':
                lst.append(int(cur_s))
            else:
                if lst[-1] == '*' :
                    lst[-2] = int(lst[-2]*int(cur_s))
                    lst.pop()
                else :
                    lst[-2] = int(lst[-2]/int(cur_s))
                    lst.pop()
            if i<len(s):
                lst.append(s[i])
                i+=1

        ans = lst[0]
        for i in range(2,len(lst),2):
            if lst[i-1] == '+':
                ans += lst[i]
            else:
                ans -= lst[i]
        return ans

obj = Solution()
s = "1+1+1"
ans = obj.calculate(s)
print(ans)





