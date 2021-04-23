# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 11:13
# @Author  : zxl
# @FileName: Offer019.py



class Solution:
    def isMatch(self, s: str, p: str) -> bool:



        new_p = []
        i = 0
        while i<len(p):
            new_p+=p[i]
            i+=1
            if p[i-1] == '*' :
                if i<len(p) and len(new_p)>=2 and new_p[-2] == p[i]:
                    new_p.pop()
                    c = new_p.pop()
                    while i<len(p)  and c == p[i]:
                        new_p.append(p[i])
                        i+=1
                    new_p.append(c)
                    new_p.append('*')

        i = 0
        j = 0

        while i<len(s) and j<len(new_p):
            if s[i] == new_p[j] or new_p[j] == '.':

                i+=1
                if j+1>=len(new_p) or new_p[j+1] == '*':
                    j+=1
            elif s[i]!=new_p[j]:
                if j+1<len(new_p) and new_p[j+1] == '*':
                    j+=2


        if j<len(new_p):

            while j+1<len(new_p) and new_p[j+1] == '*':
                j+=2



        return i==len(s) and j>=len(new_p)

obj = Solution()
s= 'aaa'
p = 'ab*a*c*a'
ans = obj.isMatch(s,p)
print(ans)